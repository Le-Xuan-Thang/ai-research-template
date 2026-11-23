---
name: ramdisk-workspace
description: Place heavy, regenerable intermediates of simulations and training runs on a RAM-backed tmpfs when the machine has one, and copy the results worth keeping to the persistent experiment directory with checksum verification as soon as each run finishes. Use before launching any long or file-heavy run (dataset generation, training sweeps, many small cache files).
---

# Ramdisk-first workspace

Code: `src/project/ramdisk.py` (standard library only). Principle: RAM holds what a rerun recreates, persistent
storage holds everything else.

## Why

Simulation and training runs create many temporary files (per-sample caches, per-epoch checkpoints, verbose logs).
Writing them to persistent storage costs time, wears the disk and, on a nearly full or slow file system, can stall
every process that creates files. A tmpfs ramdisk avoids those writes. Its contents are lost on reboot, so nothing that
is the only copy of evidence may stay there.

## Rules

1. **Check, then choose.** `python -m project.ramdisk status`. Each machine opts in by setting `RESEARCH_RAMROOT`
   to a directory on a tmpfs mount; when it is unset the ramdisk is not used. The ramdisk is used only when that
   root is a writable tmpfs and both free tmpfs space and
   `MemAvailable` exceed the request plus a reserve (`RESEARCH_RAM_RESERVE_GB`, default 64). Otherwise the run falls
   back to `<run_dir>/scratch/` on persistent storage. Unset `RESEARCH_RAMROOT` (or set it to `off`) to disable it.
2. **RAM:** caches, intermediate arrays, per-epoch checkpoints, temporary plots, verbose logs, scratch folders.
3. **Persistent, always:** source code, configs, `data/*/raw/` (immutable), protocols, reports, `.agent/` files,
   and every final run artefact: `config.json`, metrics, predictions used in tables, the selected checkpoint,
   the run log, figures that enter the paper.
4. **Promote per run, not per sweep.** When a run finishes, call `promote(scratch, run_dir, patterns)`: files are
   copied with fsync, verified by SHA-256, never overwrite different existing results, and are listed in
   `run_dir/promoted.json`. A reboot then loses at most the run in progress.
5. **Release only after verification.** `release(scratch, run_dir, promoted)` deletes the RAM copy only when every
   promoted file matches at its destination, and never deletes a persistent fallback directory.
6. **Runs must be resumable.** Skip runs whose final artefact exists in the persistent run directory, so a reboot
   costs a rerun, not a lost result.
7. **Record where intermediates lived.** `scratch_dir()` writes `run_dir/scratch.json` (path, ramdisk or not, reason).
8. **Shared machines.** The ramdisk consumes RAM. Size requests honestly (`need_gb`), keep the reserve, clean up
   released scratch, and do not mirror the whole ramdisk to persistent storage with a bulk `rsync`; promote only
   the files that are kept.
9. **After a reboot** the RAM root is empty: rerun unfinished runs; never assume a RAM path still exists.

## Minimal use

```python
from project.ramdisk import scratch_dir, promote, release

run = Path("experiments/exp012_model/dataset_a/seed0")
if (run / "metrics.json").exists():          # resumable
    return
work = scratch_dir(run, need_gb=20)          # RAM if usable, else run/scratch
train(out=work)                              # writes checkpoints, logs, metrics.json into work
kept = promote(work, run, ("config.json", "metrics.json", "best.pt", "test_predictions.npz", "*.log"))
release(work, run, kept)
```
