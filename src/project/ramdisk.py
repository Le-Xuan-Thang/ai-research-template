"""Ramdisk-first scratch space with verified promotion of kept results (skill: Skills/ramdisk-workspace/SKILL.md).

Heavy, regenerable intermediates (caches, per-epoch checkpoints, temporary arrays, verbose logs) live on a RAM-backed
tmpfs when one is available; files that are evidence are copied to the persistent experiment directory as soon as a run
finishes, verified by SHA-256, and only then may the RAM copy be deleted. A reboot therefore loses at most the run in
progress, which must be resumable.

Configuration (environment):
  RESEARCH_RAMROOT          directory on a tmpfs mount, set per machine; unset or "off" disables the ramdisk.
  RESEARCH_RAM_RESERVE_GB   free RAM and free tmpfs space that must remain after the request (default 64).

CLI:
  python -m project.ramdisk status
  python -m project.ramdisk scratch <persistent_run_dir> [need_gb]      prints the scratch dir to use
  python -m project.ramdisk promote <scratch_dir> <persistent_run_dir> [glob ...]
"""
import fnmatch
import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path

GB = 1024 ** 3


def _root():
    return os.environ.get("RESEARCH_RAMROOT", "off") or "off"


def _reserve_gb():
    return float(os.environ.get("RESEARCH_RAM_RESERVE_GB", "64"))


def mem_available_gb():
    with open("/proc/meminfo") as f:
        for line in f:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) / 1024 ** 2
    return 0.0


def is_tmpfs(path):
    path = os.path.realpath(path)
    best, fstype = "", None
    with open("/proc/mounts") as f:
        for line in f:
            _, mnt, typ = line.split()[:3]
            if (path == mnt or path.startswith(mnt.rstrip("/") + "/")) and len(mnt) > len(best):
                best, fstype = mnt, typ
    return fstype in ("tmpfs", "ramfs")


def ram_status(need_gb=0.0):
    """Return (usable, reason). Usable only if the root is a writable tmpfs with room for need_gb plus the reserve."""
    root = _root()
    if root == "off":
        return False, "disabled (RESEARCH_RAMROOT unset or off)"
    try:
        Path(root).mkdir(parents=True, exist_ok=True)
    except OSError as e:
        return False, f"cannot create {root}: {e}"
    if not os.access(root, os.W_OK):
        return False, f"{root} not writable"
    if not is_tmpfs(root):
        return False, f"{root} is not on tmpfs"
    free_fs = shutil.disk_usage(root).free / GB
    free_mem = mem_available_gb()
    need = need_gb + _reserve_gb()
    if free_fs < need or free_mem < need:
        return False, f"insufficient room: tmpfs free {free_fs:.0f} GB, MemAvailable {free_mem:.0f} GB, need {need:.0f} GB"
    return True, f"tmpfs free {free_fs:.0f} GB, MemAvailable {free_mem:.0f} GB"


def scratch_dir(persistent_run_dir, need_gb=0.0, project=None):
    """Scratch directory for a run: on the ramdisk when usable, else <persistent_run_dir>/scratch.

    The choice is recorded in <persistent_run_dir>/scratch.json so the run record says where intermediates lived.
    """
    run = Path(persistent_run_dir).resolve()
    run.mkdir(parents=True, exist_ok=True)
    ok, reason = ram_status(need_gb)
    project = project or Path.cwd().name
    if ok:
        cwd = Path.cwd().resolve()
        rel = run.relative_to(cwd) if run.is_relative_to(cwd) else Path(*run.parts[1:])   # full path keeps runs distinct
        path = Path(_root()) / project / rel
    else:
        path = run / "scratch"
    path.mkdir(parents=True, exist_ok=True)
    (run / "scratch.json").write_text(json.dumps(dict(scratch=str(path), on_ramdisk=ok, reason=reason,
                                                      created=time.strftime("%Y-%m-%dT%H:%M:%S")), indent=1))
    return path


def sha256(path, chunk=1 << 22):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while b := f.read(chunk):
            h.update(b)
    return h.hexdigest()


def promote(scratch, persistent_run_dir, patterns=("*",)):
    """Copy files matching patterns from scratch to the persistent run dir, verify SHA-256, never overwrite.

    An existing destination with identical content is accepted; a different one raises (results are never overwritten).
    Writes promoted.json (relative path -> sha256). Returns that mapping.
    """
    src, dst = Path(scratch), Path(persistent_run_dir)
    dst.mkdir(parents=True, exist_ok=True)
    done = {}
    for f in sorted(p for p in src.rglob("*") if p.is_file()):
        rel = f.relative_to(src)
        if not any(fnmatch.fnmatch(str(rel), pat) or fnmatch.fnmatch(f.name, pat) for pat in patterns):
            continue
        h = sha256(f)
        out = dst / rel
        if out.exists():
            if sha256(out) != h:
                raise FileExistsError(f"{out} exists with different content; not overwriting")
            done[str(rel)] = h
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_name(out.name + ".partial")
        with open(f, "rb") as a, open(tmp, "wb") as b:
            shutil.copyfileobj(a, b, 1 << 22)
            b.flush()
            os.fsync(b.fileno())
        if sha256(tmp) != h:
            tmp.unlink()
            raise IOError(f"checksum mismatch while promoting {f}")
        os.replace(tmp, out)
        done[str(rel)] = h
    manifest = dst / "promoted.json"
    old = json.loads(manifest.read_text()) if manifest.exists() else {}
    manifest.write_text(json.dumps(old | done, indent=1))
    return done


def release(scratch, persistent_run_dir, promoted):
    """Delete a ramdisk scratch dir only after every promoted file is re-verified at its destination.

    Never deletes a scratch dir that is not on tmpfs (the persistent fallback) and returns False on any mismatch.
    """
    scratch, dst = Path(scratch), Path(persistent_run_dir)
    if not promoted or not is_tmpfs(scratch):
        return False
    if any(not (dst / rel).is_file() or sha256(dst / rel) != h for rel, h in promoted.items()):
        return False
    shutil.rmtree(scratch)
    return True


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        print(*ram_status(), sep=": ")
    elif cmd == "scratch":
        print(scratch_dir(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.0))
    elif cmd == "promote":
        print(json.dumps(promote(sys.argv[2], sys.argv[3], sys.argv[4:] or ("*",)), indent=1))
    else:
        print(__doc__)
        sys.exit(2)
