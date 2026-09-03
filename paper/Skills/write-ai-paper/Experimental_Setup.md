# EXPERIMENTAL SETUP WRITING AND VALIDATION SKILL

## 1. Objective

When writing or rewriting the Experimental Setup of a scientific paper, provide enough methodological detail for another researcher to understand, reproduce, and critically evaluate the experiments.

The section must answer:

1. What data are used?
2. How are the data partitioned?
3. How are models trained?
4. Which settings are shared across competing methods?
5. Which settings differ and why?
6. How are checkpoints selected?
7. On which data are final results calculated?
8. Which metrics are used?
9. How are computational costs measured?
10. How is statistical uncertainty quantified?
11. How are statistical comparisons performed?
12. What safeguards are used against data leakage, unfair comparison, and selective reporting?

The section must describe what was **actually done**, not what would be methodologically ideal.

---

# 2. Core Structure

Unless the target journal requires another structure, organize the Experimental Setup approximately as:

## 2.1 Datasets

* dataset origin;
* dataset characteristics;
* annotation type;
* sample count;
* spatial resolution;
* train/validation/test partitions;
* preprocessing;
* data cleaning;
* duplicate handling;
* dataset-specific modifications;
* data leakage safeguards.

## 2.2 Implementation Details

* hardware;
* software/framework versions;
* input resolution;
* pretrained weights;
* optimizer;
* learning rate;
* scheduler;
* batch size;
* epochs;
* early stopping;
* model-selection rule;
* augmentation;
* random seeds;
* mixed precision;
* gradient clipping;
* other relevant optimization details.

## 2.3 Evaluation Metrics

* primary metric;
* secondary metrics;
* metric definitions;
* aggregation procedure;
* thresholding;
* topology/boundary metrics when applicable;
* computational metrics.

## 2.4 Statistical Analysis

When repeated experiments are available:

* number of independent runs;
* summary statistics;
* confidence intervals;
* statistical tests;
* paired/unpaired design;
* effect size;
* multiple-comparison correction;
* significance threshold.

Additional subsections may be created when necessary.

---

# 3. Absolute Non-Fabrication Rule

Never invent experimental information.

Do not fabricate:

* dataset sizes;
* train/test splits;
* image resolutions;
* random seeds;
* optimizer settings;
* learning rates;
* hardware;
* framework versions;
* number of epochs;
* augmentation probabilities;
* evaluation thresholds;
* number of runs;
* statistical tests;
* confidence intervals;
* FLOPs/MACs;
* parameter counts.

When information is unavailable, use a precise placeholder.

Examples:

`[TRAINING_SPLIT]`

`[VALIDATION_SPLIT]`

`[TEST_SPLIT]`

`[LEARNING_RATE]`

`[BATCH_SIZE]`

`[NUMBER_OF_SEEDS]`

`[MODEL_SELECTION_CRITERION]`

`[GPU_MODEL]`

Do not infer values from “common practice.”

---

# 4. Describe the Actual Experiment

The Experimental Setup is a factual record of the experiment.

Do not silently improve the protocol while writing.

If the supplied implementation used:

`batch size = 4`

the manuscript must not state:

`batch size = 8`

unless gradient accumulation explicitly produces an effective batch size of 8 and both quantities are distinguished.

Preferred:

`A physical batch size of 4 with two-step gradient accumulation was used, yielding an effective batch size of 8.`

---

# 5. Dataset Source Verification

Every external dataset must be traceable to a real source.

For each dataset, verify:

* official dataset name;
* original publication or repository;
* sample count;
* image modality;
* native resolution or resolution range;
* annotation type;
* original partition, if one exists.

Cite the original dataset source whenever possible.

Never fabricate a dataset citation.

If the dataset is derived from another dataset, explain the relationship precisely.

---

# 6. Dataset Naming

Use the official dataset name whenever known.

Prefer:

`DeepCrack`

rather than:

`Dataset 2`

in scientific discussion.

Labels such as:

`Dataset 1`, `Dataset 2`, `Dataset 3`

may be used as compact aliases only after the corresponding official names have been introduced.

If the dataset does not have a formal name, use a descriptive identifier such as:

`[DATASET_NAME/IDENTIFIER]`

rather than inventing one.

---

# 7. Dataset Summary Table

When multiple datasets are used, provide a compact table containing relevant properties.

Recommended fields include:

* dataset name;
* number of samples;
* native resolution;
* training samples;
* validation samples;
* test samples;
* modality;
* annotation type.

Do not include columns that contain no useful information.

All values in the table must agree exactly with the prose.

---

# 8. Dataset Description

For each dataset, describe only properties relevant to the experiment.

Possible properties include:

* crack width;
* morphology;
* illumination;
* texture;
* acquisition environment;
* material;
* modality;
* resolution;
* noise;
* class imbalance.

Avoid unsupported subjective descriptions such as:

`This dataset is extremely difficult.`

Prefer measurable or observable characteristics.

---

# 9. Dataset Claims Require Evidence

When describing properties inherited from the original dataset publication, cite the source.

When describing properties observed during the present study, make that distinction clear.

For example:

`The dataset was reported to contain ... \cite{...}`

versus:

`During dataset inspection, ten duplicated identifiers were identified ...`

Do not attribute your own preprocessing observation to the original dataset paper.

---

# 10. Data Cleaning Must Be Disclosed

Report any operation that changes the original dataset.

Examples:

* duplicate removal;
* corrupted-image removal;
* label correction;
* filename normalization;
* image resizing;
* mask thresholding;
* removal of samples;
* merging original folders;
* recomputing train/test partitions.

State:

1. what was changed;
2. why it was changed;
3. how many samples were affected;
4. the resulting dataset size.

---

# 11. Original Partition Versus Custom Partition

If the original dataset provides an official train/test split, state whether it is preserved.

If it is changed, explicitly disclose this.

Example:

`The original train/test partition was not used. Instead, [SPLITTING METHOD] was applied ...`

When using a custom split, results must not be presented as directly comparable to papers evaluated using the original split unless equivalent evaluation is additionally performed.

---

# 12. Split Terminology Must Be Exact

Use:

**training set**

for model fitting.

Use:

**validation set**

for:

* checkpoint selection;
* hyperparameter selection;
* early stopping;
* architecture selection;
* threshold selection.

Use:

**test set**

only when the data are not used for any model-selection decision.

Never call a set:

`test set`

or:

`held-out evaluation set`

if its performance is used to select the checkpoint.

---

# 13. Validation–Test Leakage Rule

If the same split is used to:

1. choose the best checkpoint; and
2. report final performance,

then it is a **validation evaluation**, not an independent test evaluation.

Do not describe such results as unbiased test performance.

Preferred terminology:

`held-out validation set`

or:

`evaluation/validation split`

depending on the protocol.

If an independent test set exists, final claims should preferably be based on that test set.

---

# 14. Hyperparameter Leakage

Do not select:

* learning rates;
* loss weights;
* augmentation policies;
* thresholds;
* architecture parameters;
* early-stopping patience;

using test-set performance.

If the supplied methodology does so, disclose it rather than hiding it.

---

# 15. Split Reproducibility

When custom partitions are used, report enough information to reproduce them.

Include where relevant:

* split ratio;
* stratification criterion;
* random seed;
* grouping constraints;
* duplicate handling;
* patient/specimen/structure-level grouping;
* resulting sample counts.

Example:

`An 80/20 split was generated using [STRATIFICATION PROCEDURE] with random seed 42.`

---

# 16. Custom Stratification Must Be Defined

If a non-standard split criterion is introduced, define it precisely.

For example, if splitting uses:

`crack-area ratio`

and:

`boundary-complexity ratio`

the manuscript must explain how both quantities are computed.

Do not introduce a custom term such as:

`boundary-complexity ratio`

without a mathematical definition or reproducible algorithm.

If the exact formula is not available, insert:

`[DEFINE BOUNDARY-COMPLEXITY RATIO]`

rather than inventing one.

---

# 17. Data Leakage Audit

Before finalizing the Experimental Setup, check for possible leakage through:

* duplicate images;
* near-duplicate frames;
* image crops from the same original image;
* data from the same specimen;
* video frames;
* augmented copies;
* subject identity;
* acquisition sequence;
* filename collisions.

If leakage checks were performed, report them.

Do not claim:

`no overlap exists`

unless it has actually been verified.

---

# 18. Independent Dataset Evaluation

If multiple datasets are trained and evaluated independently, state this clearly.

Example:

`No image from one dataset was used to train, pretrain, fine-tune, or select models evaluated on another dataset.`

Use this statement only if true.

Do not call the experiment:

`cross-dataset generalization`

unless a model trained on one dataset is actually evaluated on another without target-dataset retraining.

Independent within-dataset experiments and cross-dataset generalization are different protocols.

---

# 19. Dataset Figures

Representative dataset figures should:

* show actual input samples;
* show corresponding ground truth when relevant;
* use clearly readable captions;
* identify datasets consistently.

The text should reference the complete figure when discussing all datasets:

```latex
Fig.~\ref{fig:dataset_samples}
```

and individual subfigures when discussing a specific dataset if necessary.

Avoid repeatedly referring to three separate labels when one combined figure is sufficient.

---

# 20. Implementation Details Must Be Reproducible

Report all settings that materially affect training.

At minimum, when relevant:

* framework;
* framework version;
* hardware;
* input dimensions;
* initialization/pretraining;
* optimizer;
* optimizer parameters;
* learning rate;
* learning-rate schedule;
* weight decay;
* batch size;
* epoch limit;
* early stopping;
* augmentation;
* random seeds;
* checkpoint selection.

Do not bury important differences between methods.

---

# 21. Hardware Description

Report hardware factually.

Example:

`Experiments were conducted on NVIDIA RTX 6000 Ada Generation GPUs with 48 GB memory, with each training run confined to a single GPU.`

Avoid wording that implies multi-GPU training when each run actually used only one GPU.

Hardware information should support reproducibility, not marketing.

---

# 22. Software Environment

Report the primary computational environment when available.

Examples:

* Python version;
* PyTorch/TensorFlow version;
* CUDA version when relevant;
* important evaluation libraries.

Do not list every installed package unless necessary.

If exact versions are unavailable:

`Python [VERSION] and PyTorch [VERSION]`

---

# 23. Shared Training Protocol

For controlled comparisons, explicitly identify settings shared across all methods.

Example:

`All methods were trained using the same optimizer, augmentation strategy, data split, evaluation threshold, and checkpoint-selection criterion.`

Only claim a setting is identical if it is genuinely identical.

---

# 24. Fair-Comparison Rule

Never write:

`under identical training conditions`

when any relevant training condition differs.

Instead write:

`under a controlled protocol with shared [A, B, C], except for [DIFFERENCE].`

Any method-specific difference must be disclosed.

Examples:

* different patience;
* different learning rate;
* different optimizer;
* different input resolution;
* different pretraining;
* method-specific loss;
* method-specific crop size.

---

# 25. Method-Specific Training Differences

If a proposed method receives a more favorable training setting than baselines, the manuscript must:

1. disclose the difference;
2. justify it;
3. evaluate whether it materially changes the comparison when possible.

For example:

`Baselines use patience 20, whereas ESGA-Net uses patience 50.`

This is not an “identical model-selection protocol.”

Do not simultaneously make both claims in different sections.

---

# 26. Cross-Section Consistency

Experimental Setup statements must agree with:

* Abstract;
* Introduction;
* Methodology;
* Results;
* tables;
* algorithms;
* figure captions.

The AI must check for contradictions such as:

`50 epochs` in Algorithm,

but:

`100 epochs` in Experimental Setup.

or:

`identical model-selection criteria` in Introduction,

but:

different early-stopping patience in Experimental Setup.

When a conflict is detected, flag it rather than deciding silently which value is correct.

---

# 27. Pretraining

If pretrained weights are used, specify:

* source;
* affected model component;
* whether all compared models receive comparable pretraining where applicable.

Example:

`ImageNet-pretrained encoder weights were used.`

Do not write simply:

`pretrained`

without identifying the pretraining source when relevant.

---

# 28. Optimizer Notation

Use mathematically consistent notation.

Example:

```latex
AdamW with $\beta_1=0.9$, $\beta_2=0.999$, and a weight decay of $10^{-2}$.
```

Use:

```latex
\eta_0 = 3\times10^{-4}
```

or:

`learning rate of $3\times10^{-4}$`

rather than switching unnecessarily between `lr`, `LR`, and `\eta`.

Follow the notation conventions of the Methodology and Algorithm sections.

---

# 29. Effective Batch Size

When gradient accumulation is used, distinguish:

* physical mini-batch size;
* accumulation steps;
* effective batch size.

Example:

`A mini-batch size of 4 with two-step gradient accumulation yielded an effective batch size of 8.`

Do not call 8 the batch size without explaining accumulation.

---

# 30. Learning-Rate Schedule

Specify:

* initial/base learning rate;
* scheduler type;
* warm-up if used;
* final/minimum learning rate where relevant.

Do not state:

`cosine schedule`

if the actual implementation uses cosine annealing with warm restarts or another variant.

Use implementation-accurate terminology.

---

# 31. Augmentation

Describe augmentations applied during training.

For stochastic augmentations, report probabilities when known.

Example:

`Horizontal and vertical flips were applied with probability 0.5.`

Do not imply augmentations were used during validation/test unless that was actually part of test-time augmentation.

---

# 32. Augmentation Fairness

If comparison methods are evaluated under a controlled protocol, apply the same augmentation pipeline unless a method intrinsically requires a different procedure.

Disclose exceptions.

Do not tune augmentation independently for the proposed method while claiming universal identical augmentation.

---

# 33. Random Seeds

When repeated runs are used, specify:

* number of seeds;
* exact seed values or generation rule;
* whether data splits remain fixed;
* which stochastic processes the seed controls when known.

Example:

`Thirty independent runs were performed using seeds 100–129 while the dataset partition remained fixed.`

Do not imply that different seeds create independent datasets if only optimization randomness changes.

---

# 34. Independent Runs

Use the term:

`independent training runs`

carefully.

A repeated run generally means independently initialized/stochastic training under the same fixed dataset split.

Do not call samples statistically independent solely because they use different numerical seed values.

The statistical design must determine the appropriate interpretation.

---

# 35. Checkpoint Selection

State the exact criterion.

Example:

`The checkpoint with the highest validation crack-class IoU was retained.`

Do not write:

`the best model was selected`

without defining “best.”

If ties occur and a deterministic tie-breaking rule matters, describe it.

---

# 36. Never Select Checkpoints Using Test Performance

Test metrics must not determine:

* checkpoint;
* threshold;
* hyperparameters;
* architecture.

If they do, do not label the evaluation an independent test.

---

# 37. Metric Selection

The metric set must reflect the scientific claims of the study.

For segmentation, region-based metrics may include:

* Precision;
* Recall;
* F1/Dice;
* IoU.

If the proposed method claims improved topology:

include a topology-sensitive metric.

If it claims boundary improvement:

include a boundary metric.

If it claims efficiency:

include computational metrics.

The evaluation design must test the actual contributions.

---

# 38. Primary Metric Must Be Identified

Specify the primary metric used for:

* model selection;
* principal ranking;
* primary statistical hypothesis.

Example:

`\(\operatorname{IoU}_{\mathrm{crack}}\) is used as the primary region-overlap metric.`

Do not treat every metric as equally primary.

This reduces selective metric interpretation.

---

# 39. Metric Definitions

For non-trivial or central metrics, define them mathematically.

Follow the project's Equation Skill:

```latex
\begin{equation}
...
\label{eq:...}
\end{equation}
```

Every equation subsequently discussed must be referenced using:

```latex
Eq.~\eqref{eq:...}
```

Every newly introduced symbol must be defined immediately after the equation.

---

# 40. Standard Metrics Still Require Clarity

Even for common metrics, specify:

* positive class;
* aggregation scheme;
* threshold;
* whether metrics are class-specific;
* whether averaging is macro or micro.

For highly imbalanced binary segmentation, this information materially affects interpretation.

---

# 41. Confusion-Matrix Definitions

When defining:

* TP;
* FP;
* FN;
* TN;

identify the foreground/positive class explicitly.

For crack segmentation:

`crack pixels constitute the positive class.`

Avoid ambiguity about whether IoU refers to:

* crack IoU;
* background IoU;
* mean IoU.

---

# 42. IoU Naming

If only crack-class IoU is reported, write:

```latex
\operatorname{IoU}_{\mathrm{crack}}
```

or explicitly define:

`\(\operatorname{IoU}\) denotes crack-class IoU throughout this study.`

Do not call a binary foreground IoU `mIoU` unless an actual mean over classes is computed.

---

# 43. Micro Versus Macro Averaging

Always disclose metric aggregation.

## Micro aggregation

Accumulate sufficient statistics over all images, then calculate the metric.

## Macro aggregation

Calculate the metric per image, then average.

These may produce materially different values.

Do not use `dataset-level` without specifying the procedure.

---

# 44. Metric Aggregation Must Match the Equation

If:

TP, FP, FN

are accumulated globally before computing IoU, describe the result as:

`micro-averaged pixel-level IoU`.

If metrics are averaged per image, describe them accordingly.

Do not mix the two procedures across methods.

---

# 45. Thresholding

For probability-based binary segmentation, report the threshold.

Example:

`A fixed threshold of 0.5 was applied to all methods.`

If the threshold is optimized, explain:

* on which set;
* by which metric;
* whether it is method-specific.

Never optimize thresholds on the test set without disclosure.

---

# 46. Specialized Metrics Require Primary Citations

When using a metric such as:

* clDice;
* Hausdorff distance;
* boundary F1;
* topology loss;
* SSIM;
* LPIPS;

cite the original or authoritative methodological source where appropriate.

The citation must refer to a real verified publication.

If the implementation differs from the original metric definition, state the difference.

---

# 47. clDice Evaluation

When hard-mask clDice is used, distinguish it from differentiable soft-clDice used for training.

Clearly define:

* predicted mask;
* ground-truth mask;
* skeletonization method;
* topological precision;
* topological sensitivity;
* aggregation procedure.

Do not imply that evaluation clDice and training soft-clDice are identical if their implementations differ.

---

# 48. Skeletonization Algorithm

If a named skeletonization algorithm is used, such as Zhang–Suen thinning:

* cite the appropriate source when necessary;
* state implementation details that materially affect the metric.

Do not name an algorithm unless that algorithm is actually used.

---

# 49. Boundary Metrics

For boundary evaluation, define:

* boundary extraction procedure;
* tolerance;
* distance metric;
* structuring element;
* matching rule;
* aggregation.

A statement such as:

`BF1 with tolerance 2`

is insufficient for strict reproducibility.

---

# 50. Pixel Tolerance Depends on Resolution

When boundary tolerance is measured in pixels, note that its physical interpretation depends on image resolution.

If datasets use different spatial resolutions, use the same pixel tolerance only if this is the intended protocol.

Do not imply physical equivalence unless pixel size or spatial calibration supports it.

---

# 51. Custom Metrics

Any non-standard metric introduced by the study must include:

1. mathematical definition;
2. symbol definitions;
3. aggregation procedure;
4. direction of improvement;
5. edge-case handling.

For example:

`Smaller \(E_{\mathrm{CC}}\) indicates better agreement.`

---

# 52. Metric Edge Cases

Explicitly define behavior when denominators can be zero.

Examples:

* no ground-truth crack;
* no predicted crack;
* no skeleton pixels;
* no boundary pixels.

Do not leave evaluation software behavior implicit if it can affect reported scores.

---

# 53. Computational Efficiency

When claiming computational efficiency, report measurable evidence.

Possible metrics:

* trainable parameters;
* MACs;
* FLOPs;
* inference latency;
* FPS;
* peak memory.

Do not use:

`efficient`

solely because a model has fewer parameters.

---

# 54. MACs Versus FLOPs

Do not use MACs and FLOPs interchangeably without defining the convention.

Report:

`GMACs`

when counting multiply–accumulate operations.

If converting MACs to FLOPs, state the convention.

Do not compare GMAC values to another paper's GFLOPs as if they were necessarily equivalent.

---

# 55. Complexity Input Resolution

Always report the input size used for complexity measurement.

Computational cost depends strongly on spatial resolution.

Example:

`GMACs were measured at each dataset's evaluation resolution.`

For direct architecture comparison, also consider a common canonical resolution if needed.

---

# 56. Runtime Comparison

When reporting FPS or inference time, specify:

* GPU/CPU;
* batch size;
* input resolution;
* precision mode;
* warm-up procedure where relevant.

Do not compare runtime numbers measured on different hardware as a controlled ranking.

---

# 57. Repeated-Seed Reporting

When multiple seeds are used, report at minimum:

* mean;
* standard deviation.

When appropriate, also report:

* confidence interval;
* median;
* interquartile range.

Do not report only the best seed.

Do not select a representative seed post hoc because it looks visually favorable.

---

# 58. Confidence Intervals

State:

* confidence level;
* quantity receiving the interval;
* method used to calculate it where non-obvious.

Example:

`Mean IoU and its 95% confidence interval were calculated across 30 training runs.`

Do not confuse:

confidence interval of the mean

with:

empirical spread of individual runs.

---

# 59. Statistical Design Must Match the Experiment

Before choosing a statistical test, determine whether observations are:

* paired;
* independent;
* repeated measures;
* hierarchical;
* cross-validated;
* seed-replicated.

Do not choose a paired test merely because runs share numerical seed labels.

---

# 60. Same Seed Does Not Automatically Establish Pairing

Running Method A and Method B with:

`seed = 100`

does not automatically guarantee a statistically meaningful paired observation.

Pairing is strongest when the design deliberately couples stochastic conditions or uses a common experimental unit.

Before using a paired test, justify what constitutes the matched experimental unit.

Possible matched units include:

* identical folds;
* identical subject partitions;
* identical resampling replicates;
* deliberately shared stochastic perturbations.

If pairing cannot be justified, use an appropriate alternative or describe the analysis cautiously.

---

# 61. Paired-Difference Definition

When a genuinely paired design is used, define the difference explicitly.

Example:

```latex
\begin{equation}
\Delta_i
=
M_i^{(A)}-M_i^{(B)},
\label{eq:paired_difference}
\end{equation}
```

where (M_i^{(A)}) and (M_i^{(B)}) correspond to the same experimental unit (i).

State which sign favors which method.

---

# 62. Statistical Hypothesis

For inferential tests, state the hypothesis when useful.

Example:

[
H_0:\mathbb{E}[\Delta]=0.
]

Do not use significance testing without identifying the comparison quantity.

---

# 63. Parametric Assumptions

When using a paired (t)-test, the relevant normality assumption concerns the **paired differences**, not necessarily the raw metrics.

Do not state incorrect assumptions.

When sample size is modest or distributional concerns exist, a non-parametric sensitivity analysis may be appropriate.

---

# 64. Wilcoxon Signed-Rank Test

Use the Wilcoxon signed-rank test only for genuinely paired observations.

Do not use it as a generic alternative whenever the paired (t)-test is questionable due to lack of pairing.

Statistical test selection must follow the experimental design.

---

# 65. Effect Size

Statistical significance alone is insufficient.

When inferential comparisons are central, report an appropriate effect size.

For paired observations, one possible measure is:

```latex
d_z=\frac{\overline{\Delta}}{s_{\Delta}}.
```

Use this only when its assumptions and interpretation are appropriate.

Define:

* numerator;
* denominator;
* direction.

---

# 66. Multiple Comparisons

When many baselines or datasets are tested, address multiplicity.

Possible procedures include:

* Holm;
* Bonferroni;
* Benjamini–Hochberg;

depending on the inferential objective.

State:

* correction method;
* correction family;
* significance level.

Do not apply one correction family arbitrarily across unrelated hypotheses without defining the rationale.

---

# 67. Primary Versus Secondary Statistical Analysis

Identify which analysis is primary.

Example:

`Holm-adjusted paired \(t\)-test results constitute the primary inferential analysis, whereas Wilcoxon results are treated as robustness evidence.`

Do not search among multiple tests and report only whichever yields significance.

---

# 68. P-Value Reporting

Use:

```latex
$p$
```

with correct spacing and formatting.

Do not write:

`p=0.000`

when software rounding caused the value.

Prefer:

`$p<0.001$`

when appropriate.

Do not equate statistical significance with practical importance.

---

# 69. Statistical Significance Language

Only write:

`statistically significant`

when:

1. a valid inferential test has been conducted;
2. multiplicity has been handled when required;
3. the adjusted (p)-value satisfies the predefined threshold.

Multiple random seeds alone do not establish significance.

---

# 70. Avoid Pseudoreplication

Do not treat every pixel in a segmentation dataset as an independent experimental replicate for model-level significance testing.

The unit of replication must correspond to the experimental design.

For repeated training experiments, seed-level/fold-level/model-run summaries may be relevant, subject to the design.

---

# 71. Reproducibility Versus Robustness

Distinguish:

**reproducibility across random seeds**

from:

**generalization across datasets**

from:

**robustness to perturbations**

from:

**statistical significance**

These terms are not interchangeable.

---

# 72. Experiment Objectives Must Match Metrics

For each principal contribution, identify its corresponding experiment.

Example:

**region segmentation**
→ IoU/F1

**connectivity preservation**
→ clDice/fragmentation metric

**boundary localization**
→ BF1

**efficiency**
→ parameters/MACs/runtime

**component effectiveness**
→ ablation study

If a contribution has no corresponding evaluation, the experimental design is incomplete.

---

# 73. Ablation Protocol

When ablation studies are performed:

* define a common base model;
* change one component at a time where possible;
* keep training/evaluation protocol controlled;
* report repeated-run variability when feasible.

Do not compare ablations trained under materially different conditions without explanation.

---

# 74. Baseline Integrity

Each external baseline must correspond to a real published method.

Verify:

* original publication;
* implementation source;
* architecture version;
* pretrained weights;
* modifications made for the current task.

Do not silently alter baseline architecture.

---

# 75. Baseline Implementation Source

When relevant, report whether each baseline uses:

* official implementation;
* established library implementation;
* independent reimplementation.

If implementation differences may affect fairness, disclose them.

---

# 76. Baseline Adaptation

If the output head, input channels, or number of classes is modified, explain this.

Example:

`The final classifier was replaced with a two-class segmentation head while preserving the original encoder–decoder architecture.`

Do not imply the original baseline was evaluated unchanged if adaptations were required.

---

# 77. Baseline Hyperparameters

A controlled benchmark does not necessarily require identical hyperparameters when architectures have fundamentally different optimization requirements.

However, the comparison protocol must be transparent.

Choose and state one approach:

**Protocol A:** identical training hyperparameters for all methods.

**Protocol B:** method-specific recommended hyperparameters.

**Protocol C:** controlled tuning under the same search budget.

Do not mix approaches without explanation.

---

# 78. Fairness Is More Important Than Superficial Uniformity

Identical settings do not automatically mean fair settings.

For example, forcing the same learning rate on every architecture may disadvantage some methods.

The manuscript should describe the comparison philosophy clearly.

If a single unified protocol is deliberately adopted to isolate architectural effects, state that rationale.

---

# 79. No Selective Reporting

Define evaluation protocol before inspecting final results whenever possible.

Do not:

* choose metrics because the proposed method performs well;
* remove unfavorable seeds;
* change threshold after test inspection;
* selectively exclude baselines.

If exclusions occur, state the predefined reason.

---

# 80. Experimental Setup Should Not Report Results

Keep actual performance results primarily in the Results section.

Experimental Setup may state:

* design;
* evaluation objectives;
* metrics;
* protocols.

Avoid:

`Preliminary experiments showed that ESGA-Net was superior...`

unless such preliminary experimentation is essential to justify a methodological decision and is transparently disclosed.

---

# 81. Preliminary Tuning Must Be Treated Carefully

If a setting differs because:

`preliminary runs showed late improvements`

state:

* which data were used for those preliminary runs;
* whether equivalent tuning opportunities were offered to baselines;
* whether this could introduce tuning advantage.

Do not use undisclosed preliminary experiments to optimize only the proposed method.

---

# 82. Avoid Causal Language Without Experimental Support

Do not write:

`This augmentation improves generalization`

inside Experimental Setup unless an experiment demonstrates it.

Prefer:

`This augmentation was applied to increase training variability.`

Methodological intention and empirical effect are different claims.

---

# 83. Citation Requirements

External citations are appropriate for:

* datasets;
* optimizers;
* specialized metrics;
* skeletonization algorithms;
* statistical methodology when non-standard;
* benchmark methods.

Do not cite common implementation facts unnecessarily.

Every citation introduced must follow the Reference Integrity Skill:

**real source → verified metadata → verified relevance → BibTeX entry → citation**

---

# 84. Primary Sources for Metrics

Prefer original methodological references.

Examples:

* AdamW → original AdamW source;
* clDice → original clDice source;
* Zhang–Suen thinning → original algorithm source if cited;
* Holm correction → authoritative statistical source where needed.

Do not cite a later application paper merely because it uses the same method.

---

# 85. Equation Discipline

All displayed mathematical definitions must follow the project's Equation Skill.

Use:

```latex
\begin{equation}
...
\label{eq:metric_name}
\end{equation}
```

Immediately define any newly introduced symbols.

Reference the equation in prose.

Example:

`The F1-score is calculated using Eq.~\eqref{eq:f1}.`

---

# 86. Punctuation Around Equations

Treat equations as part of the sentence.

If prose continues with:

`where ...`

end the displayed expression with a comma.

If the sentence terminates at the equation, use a period where appropriate.

Maintain this consistently throughout the metrics subsection.

---

# 87. Symbol Consistency

Do not alternate between:

`\operatorname{IoU}`

`\mathrm{IoU}`

`IoU`

or:

`F1`

`\operatorname{F1}`

without a style decision.

Likewise keep consistent:

* (P): predicted mask;
* (G): ground truth;
* (S(P)): skeleton;
* (B_P): predicted boundary;
* (N_{\mathrm{pred}}): connected components.

Once defined, preserve the notation.

---

# 88. Metric Direction

For every uncommon metric, state whether:

* higher is better;
* lower is better.

Example:

`Higher clDice values indicate stronger topological agreement.`

`Smaller \(E_{\mathrm{CC}}\) values indicate closer component-count agreement.`

---

# 89. Units and Typography

Use non-breaking or thin spacing appropriately.

Examples:

```latex
48\,GB
```

```latex
95\%
```

```latex
$512\times512$
```

Use consistent typography for:

* pixels;
* FPS;
* GMACs;
* parameters;
* epochs.

---

# 90. Avoid Implementation-Style Variable Names in Prose

Prefer:

`Dataset~2`

rather than:

`Dataset_2`

unless referring to an actual code variable.

Prefer:

`learning rate`

rather than:

`lr`

in prose unless `lr` has been explicitly defined mathematically.

The manuscript should not look like source code documentation.

---

# 91. Grammar and Mechanical Quality Audit

Before returning the section, check for accidental concatenations such as:

`predictedbinary`

`respectively.Topological`

`aremeasured`

`duringi nference`

`the$i$th`

`zero forimages`

These errors commonly arise after LaTeX editing and must be removed.

---

# 92. Table–Text Consistency Audit

Verify every numerical value appearing both in a table and in prose.

Examples:

* total images;
* training images;
* validation images;
* test images;
* resolutions.

The AI must detect inconsistencies rather than silently select one value.

---

# 93. Arithmetic Audit

Check simple partition arithmetic.

For example:

[
303+76=379.
]

[
430+107=537.
]

[
358+90=448.
]

If counts do not sum correctly, flag the discrepancy.

Do not correct study data by guessing.

---

# 94. Percentage Audit

When an 80/20 split produces integer counts, small rounding deviations are normal.

Do not state exact:

`80.00%`

unless mathematically exact.

The phrase:

`an 80/20 split`

is sufficient when counts arise from integer rounding.

---

# 95. Cross-Dataset Resolution Consistency

When resolutions differ, distinguish clearly between:

* native resolution;
* training resolution;
* evaluation resolution;
* resized resolution.

Do not call a resized image size “native resolution.”

---

# 96. Reproducibility Audit

Before finalizing the Experimental Setup, ask:

Could another competent researcher reconstruct:

* dataset composition;
* splits;
* preprocessing;
* training settings;
* checkpoint selection;
* evaluation threshold;
* metrics;
* statistical analysis?

If a necessary detail is missing, insert a precise placeholder rather than inventing it.

---

# 97. Methodological Validity Audit

Separately from reproducibility, check:

* Was test data used for model selection?
* Were baselines given comparable tuning opportunities?
* Are repeated observations genuinely paired?
* Is multiplicity controlled?
* Are metrics aligned with claims?
* Are computational comparisons measured under comparable conditions?
* Are custom metrics defined?
* Are all exclusions disclosed?

If a potential validity issue is identified, flag it.

Do not conceal it through polished writing.

---

# 98. Cross-Section Audit

Before finalizing, compare Experimental Setup against claims elsewhere.

Check for consistency in:

* number of epochs;
* patience;
* learning rate;
* weight decay;
* number of seeds;
* number of datasets;
* number of baselines;
* model-selection criterion;
* augmentation;
* pretrained initialization;
* input resolution.

Do not allow the paper to contain two different experimental protocols.

---

# 99. Missing Information

Use narrow placeholders.

Preferred:

`Training was performed for up to [MAX_EPOCHS] epochs.`

rather than:

`[IMPLEMENTATION DETAILS]`

Preferred:

`A fixed probability threshold of [THRESHOLD] was used.`

rather than:

`[METRIC DETAILS]`

Keep all known information unchanged.

---

# 100. Do Not Ask Unnecessarily

If most Experimental Setup information is known, produce the section with placeholders.

Only ask the user when a missing decision fundamentally changes the experimental interpretation and cannot safely be represented with a placeholder.

---

# 101. Final Experimental Setup Checklist

Before returning the section, verify:

* `[ ]` Every dataset is real and properly cited.
* `[ ]` Official dataset names are correct.
* `[ ]` Sample counts agree throughout.
* `[ ]` Resolutions agree throughout.
* `[ ]` Dataset modifications are disclosed.
* `[ ]` Duplicate handling is described where relevant.
* `[ ]` Split procedure is reproducible.
* `[ ]` Custom stratification variables are defined.
* `[ ]` Validation and test terminology is correct.
* `[ ]` No test-set leakage is hidden.
* `[ ]` Hardware information is accurate.
* `[ ]` Software versions are accurate.
* `[ ]` Pretraining source is stated.
* `[ ]` Optimizer settings are complete.
* `[ ]` Learning-rate schedule is complete.
* `[ ]` Physical and effective batch sizes are distinguished.
* `[ ]` Augmentation is fully described.
* `[ ]` Seed protocol is explicit.
* `[ ]` Early stopping is explicit.
* `[ ]` Method-specific differences are disclosed.
* `[ ]` Model-selection criterion is defined.
* `[ ]` Primary metric is identified.
* `[ ]` Metric threshold is specified.
* `[ ]` Micro/macro aggregation is specified.
* `[ ]` Specialized metrics are properly defined and cited.
* `[ ]` Metric edge cases are handled.
* `[ ]` Computational metrics include input resolution.
* `[ ]` Statistical unit of analysis is identified.
* `[ ]` Pairing is justified when paired tests are used.
* `[ ]` Effect size is reported when appropriate.
* `[ ]` Multiple testing is handled where necessary.
* `[ ]` Equations follow the Equation Skill.
* `[ ]` Symbols remain consistent.
* `[ ]` No numerical information has been fabricated.
* `[ ]` No contradictions exist with the rest of the manuscript.
* `[ ]` No accidental LaTeX spacing/concatenation errors remain.

---

# 102. Core Experimental Rule

The Experimental Setup must provide a complete chain:

**Data**
→ **Partitioning**
→ **Training**
→ **Model selection**
→ **Evaluation**
→ **Statistical inference**

Every step must be sufficiently precise to reproduce the experiment and sufficiently transparent to evaluate its validity.

# CORE RULE

**Describe exactly what was done, distinguish validation from testing, disclose every meaningful difference between methods, define every metric and statistical procedure precisely, and never fabricate missing experimental information.**
