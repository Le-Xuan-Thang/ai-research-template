# RESULTS AND DISCUSSION WRITING SKILL

## 1. Objective

When writing or rewriting the Results and Discussion section of a scientific paper, transform experimental evidence into a rigorous scientific argument.

The section must answer:

1. What are the principal experimental findings?
2. How does the proposed method compare with relevant baselines?
3. Are the observed differences consistent across repeated experiments?
4. Are the differences statistically and practically meaningful?
5. Which aspects of the proposed method appear to explain the observed behavior?
6. Which contributions are supported by which experiments?
7. What trade-offs are revealed?
8. Under which datasets, conditions, or competing architectures does the proposed method perform less favorably?
9. How do the findings relate to previous literature?
10. What limitations remain?

The section must not simply repeat numerical values already contained in tables.

The required reasoning pattern is:

**Evidence → Comparison → Statistical support → Interpretation → Mechanistic explanation → Broader implication → Limitation**

---

# 2. Results and Discussion Are Evidence-Driven

Every statement about performance must be grounded in:

* a table;
* a figure;
* a statistical analysis;
* an ablation study;
* a qualitative result;
* or a verified external source when discussing previous literature.

Do not write conclusions first and search for supporting numbers afterward.

The experimental evidence must determine the narrative.

---

# 3. Never Fabricate Results

Never invent:

* metric values;
* rankings;
* confidence intervals;
* standard deviations;
* $p$-values;
* effect sizes;
* FPS;
* MACs/FLOPs;
* parameter counts;
* memory usage;
* ablation results;
* qualitative observations.

If information is unavailable, use precise placeholders such as:

`[MAIN_RESULT]`

`[ABLATION_RESULT]`

`[EFFECT_SIZE]`

`[EFFICIENCY_RESULT]`

`[QUALITATIVE_OBSERVATION]`

Do not infer missing results from trends elsewhere in the manuscript.

---

# 4. Recommended Section Architecture

For a comprehensive AI/engineering study, organize Results and Discussion approximately as:

## 4.1 Overview and Training Behavior

* experimental scope;
* number of methods;
* number of datasets;
* number of repeated runs;
* convergence behavior when relevant.

## 4.2 Main Quantitative Segmentation Results

* primary metric;
* principal ranking;
* dataset-specific patterns;
* strongest competitors;
* important trade-offs.

## 4.3 Statistical Robustness

* pairwise differences;
* confidence intervals;
* effect sizes;
* adjusted significance tests;
* interpretation of practical versus statistical magnitude.

## 4.4 Topology / Boundary / Contribution-Specific Results

* metrics directly corresponding to claimed methodological contributions.

## 4.5 Computational Efficiency

* parameters;
* MACs/FLOPs;
* runtime;
* memory;
* accuracy–complexity trade-off.

## 4.6 Qualitative Analysis

* representative successes;
* characteristic failure modes;
* relation to quantitative metrics.

## 4.7 Ablation Studies

* contribution of each component;
* interaction among components if examined;
* cost versus benefit.

## 4.8 Integrated Discussion

* why the method performs as observed;
* relation to proposed design;
* relation to prior studies;
* dataset dependence;
* limitations;
* practical implications.

The exact subsection arrangement may vary, but all major claims should be supported.

---

# 5. Begin with Experimental Scope

At the beginning of Results, summarize the evaluation scope briefly.

Example structure:

`[METHOD] is compared with [NUMBER] representative methods on [NUMBER] datasets under the protocol described in Section~\ref{...}. Each method--dataset combination is repeated over [NUMBER_OF_RUNS] random seeds, yielding [TOTAL_RUNS] completed runs.`

Check arithmetic before writing the total.

For example:

[
11\times3\times30=990.
]

Do not report a run count without verifying it.

---

# 6. Do Not Repeat the Experimental Setup

Results may remind the reader of the evaluation scope, but should not restate:

* optimizer;
* augmentation;
* learning rate;
* batch size;
* split procedure;

unless directly needed to interpret a finding.

Refer to the Experimental Setup instead.

---

# 7. Learning-Curve Analysis

When learning curves are available, discuss only meaningful behaviors such as:

* convergence speed;
* stability;
* train–validation gap;
* variability across seeds;
* late-epoch behavior.

Do not simply describe every curve geometrically.

Preferred reasoning:

**observed trajectory → interpretation**

Example:

`The validation IoU saturates after approximately [EPOCH RANGE], while the train–validation gap remains small, indicating limited evidence of severe overfitting under the adopted split.`

Avoid stronger claims such as:

`the model generalizes well`

when no independent test/generalization experiment exists.

---

# 8. Generalization Language Must Match the Evaluation Design

If performance is measured on a validation split used for checkpoint selection, avoid language implying unbiased test generalization.

Prefer:

* `validation performance`;
* `held-out split performance`;
* `train–validation gap`.

Use:

`generalization`

only with appropriate qualification.

Do not write:

`excellent generalization`

from training and validation curves alone.

---

# 9. Main Results Should Focus on the Primary Metric

The discussion of comparative performance should be anchored by the predefined primary metric.

For example:

`\(\operatorname{IoU}_{\mathrm{crack}}\)`.

Secondary metrics such as:

* Precision;
* Recall;
* F1;
* clDice;
* BF1;

should support specific interpretations.

Do not change the primary metric after seeing which metric favors the proposed method.

---

# 10. Avoid Table Narration

Do not convert every row and column into prose.

Weak:

`Method A achieves X, Y, Z, and W. Method B achieves ... Method C achieves ...`

Preferred:

`ESGA-Net achieves the highest IoU on Dataset~1, improving over the strongest baseline, Swin-UNet, by 0.54 percentage points, while SegFormer retains a slightly higher Recall.`

The table contains complete values.

The prose should identify:

* best result;
* second-best/strongest competitor;
* meaningful margin;
* trade-off;
* unusual behavior.

---

# 11. Select Numbers for a Scientific Purpose

Include a number in prose only when it establishes one of the following:

* ranking;
* improvement;
* degradation;
* trade-off;
* stability;
* practical magnitude;
* statistical effect;
* computational difference.

Do not repeat numbers solely because they are available.

---

# 12. Use Absolute Differences Clearly

For metrics reported in percent, distinguish:

**percentage points**

from:

**relative percent improvement**.

If IoU increases from 77.33% to 77.87%, write:

`an improvement of 0.54 percentage points`

not:

`an improvement of 0.54%`

unless a relative percentage improvement has actually been calculated.

---

# 13. Dataset-by-Dataset Results Must Be Synthesized

When several datasets are evaluated, do not discuss each one as an isolated benchmark only.

After dataset-specific analysis, synthesize the pattern.

Example:

`Across the three datasets, ESGA-Net ranks first on Datasets~1 and~3 and second on Dataset~2, indicating strong but not universal superiority.`

This cross-dataset interpretation is more informative than three separate rankings.

---

# 14. Never Hide an Unfavorable Result

If another method performs better on a dataset or metric, state it clearly.

Example:

`Swin-UNet achieves a higher IoU on Dataset~2 by 0.78 percentage points.`

Do not omit or downplay such findings.

A scientifically credible Discussion should explain where the proposed method does **not** dominate.

---

# 15. Avoid Universal Superiority Claims

Do not write:

`The proposed method is superior to all existing methods.`

when any dataset or metric contradicts the statement.

Prefer:

* `achieves the best performance on two of the three datasets`;
* `outperforms nine of ten baselines on Dataset~2`;
* `provides consistently competitive performance`;
* `shows strong overall performance while remaining second to [METHOD] under [CONDITION]`.

---

# 16. Ranking Must Be Metric-Specific

Do not write:

`ESGA-Net is the best method`

when it is only best in IoU/F1 but second in Precision or Recall.

Specify:

`ESGA-Net achieves the highest IoU and F1.`

Similarly:

`Swin-UNet achieves the highest Recall.`

---

# 17. Statistical Significance Is Not Practical Significance

When repeated-run statistical analysis is available, distinguish:

**statistical evidence**

from:

**effect magnitude**.

A difference of 0.2–0.5 IoU points can be statistically significant with low variability while still being practically modest.

Discuss both.

Preferred:

`Although the difference is statistically supported, the absolute margin is modest.`

Do not equate small $p$-values with large scientific importance.

---

# 18. Statistical Analysis Must Match Experimental Design

Before interpreting paired tests, verify that the Experimental Setup establishes valid pairing.

Do not assume that using the same numerical random seed automatically creates matched observations.

If pairing is uncertain, flag the statistical interpretation.

Results must not overstate a questionable inferential design.

---

# 19. Confidence Intervals

Interpret confidence intervals in terms of the estimated comparison.

For a paired difference:

* CI entirely above zero → positive mean difference supported;
* CI entirely below zero → negative mean difference supported;
* CI overlapping zero → evidence does not establish a non-zero mean difference at the corresponding confidence level.

Do not interpret CI width as performance variability unless that is what the interval represents.

---

# 20. Effect Size Interpretation

Effect sizes should be interpreted together with absolute performance differences.

Do not write:

`Cohen's $d_z=5.40$ proves an enormous practical improvement`

without considering the actual IoU difference.

Extremely large standardized effects can arise when run-to-run variability of paired differences is very small.

Use cautious language:

`The standardized effect is large because the paired differences exhibit low variability.`

---

# 21. $p$-Value Discipline

Do not write:

`$p=0.000$`.

Use:

`$p<0.001$`

when appropriate.

When multiple comparisons are corrected, discuss **adjusted $p$-values**, not unadjusted values.

Always maintain consistency with the predefined primary statistical test.

---

# 22. No Significance Fishing

If multiple statistical tests are reported, do not emphasize whichever yields the most favorable conclusion.

Use the primary analysis specified in Experimental Setup.

Secondary tests should be presented as robustness/sensitivity evidence.

---

# 23. Statistical Claims Must Not Exceed the Test

A statistically significant difference between two methods on one dataset does not prove:

* general superiority;
* universal robustness;
* better real-world performance;
* causal benefit of a module.

Keep inference within the scope of the tested comparison.

---

# 24. Link Metrics to Contributions

Every major contribution should have corresponding evidence.

Example:

**directional/global modeling**
→ region accuracy and possibly challenging long-range structures;

**edge-guided gating**
→ BF1 / boundary localization;

**topology-aware objective**
→ clDice / fragmentation;

**efficient low-resolution attention**
→ parameters, GMACs, FPS, memory;

**individual modules**
→ ablation studies.

Discussion should explicitly connect these.

---

# 25. Do Not Claim Causality from Full-Model Comparisons Alone

If ESGA-Net has higher clDice than baselines, this supports the performance of the **overall framework**.

It does not by itself prove that the topology-aware loss caused the improvement.

Causal statements about individual components require ablation evidence.

Prefer:

`The full model exhibits higher clDice...`

until ablation results isolate the contribution.

---

# 26. Ablation Is Required for Component Claims

If the paper claims that:

* Module A improves long-range context;
* Module B improves boundaries;
* Loss C improves connectivity;

the Results should include controlled ablations wherever feasible.

Without ablation evidence, weaken the contribution language.

If ablation results are not yet available, use:

`[ABLATION RESULTS FOR MODULE A]`

rather than inventing them.

---

# 27. Ablation Writing Pattern

For each component, discuss:

**baseline configuration → added component → metric change → computational cost change → interpretation**

Example:

`Adding [MODULE] increases IoU from [X] to [Y] while increasing GMACs by [Z], indicating [INTERPRETATION].`

Do not analyze only accuracy.

Include cost when efficiency is part of the design rationale.

---

# 28. Combined Ablations

When modules interact, evaluate whether combined improvements are:

* additive;
* complementary;
* redundant;
* antagonistic.

Do not assume that a full-model gain equals the sum of independent module gains.

---

# 29. Topology Results

When topology preservation is a major contribution, discuss:

* ranking in clDice;
* consistency across datasets;
* size of improvements;
* relation to qualitative continuity;
* relation to ablation results.

Do not interpret clDice as a direct measure of all geometric properties.

State what the metric actually captures.

---

# 30. Boundary Results

Boundary F1 should be interpreted separately from region overlap and topology.

A model can have:

* high IoU;
* moderate BF1;
* high clDice.

Discuss these as distinct dimensions.

This prevents collapsing all metrics into one generic notion of “accuracy.”

---

# 31. Fragmentation Metrics

If connected-component error or another fragmentation metric is defined in Experimental Setup, report and discuss it when relevant.

Do not define a metric in the methodology and then omit it from Results without explanation.

If results are not yet available:

`[CONNECTED-COMPONENT RESULTS]`

---

# 32. Every Defined Evaluation Metric Should Have a Result

Before finalizing, compare the Results section with the Evaluation Metrics subsection.

If Experimental Setup defines:

* Precision;
* Recall;
* F1;
* IoU;
* clDice;
* BF1;
* connected-component error;
* parameters;
* GMACs;
* statistical comparisons;

the Results section should report the metrics relevant to the paper's claims.

Missing predefined metrics must be either:

* added;
* intentionally omitted with justification;
* or removed from Experimental Setup.

---

# 33. Efficiency Discussion Must Be Multi-Dimensional

Do not equate efficiency with one metric.

Discuss separately:

* model size;
* computational operations;
* throughput;
* memory.

A method may have:

* more parameters;
* fewer MACs;
* higher FPS;
* higher memory.

Efficiency is a trade-off, not a single ranking.

---

# 34. Accuracy–Efficiency Trade-Off

Prefer Pareto-style reasoning.

Example:

`Although ESGA-Net is not the smallest model, it achieves higher IoU than several lighter alternatives while remaining substantially less computationally expensive than U-Net.`

Do not write:

`computationally efficient`

without context.

---

# 35. Runtime Must Be Interpreted Under the Measurement Protocol

FPS comparisons are valid only under comparable:

* hardware;
* batch size;
* precision;
* input resolution;
* implementation environment.

Reference the Experimental Setup measurement protocol.

Do not compare your measured FPS directly with FPS values from unrelated papers using different hardware.

---

# 36. Complexity Terminology Must Be Consistent

Do not use:

`mIoU`

when the reported metric is crack-class IoU.

Do not use:

`GFLOPs`

when the experiment measured GMACs.

Do not use:

`parameters`

as a synonym for computational cost.

Maintain terminology across:

* tables;
* figures;
* captions;
* prose.

---

# 37. Accuracy–Complexity Figures

When discussing an accuracy–complexity plot, identify:

* which accuracy metric is used;
* which complexity measure is used;
* whether input resolution differs across datasets;
* whether bubble size has another encoding.

The caption and prose must match the actual data.

---

# 38. Qualitative Results Need a Defined Purpose

Qualitative figures should illustrate phenomena not fully captured by scalar metrics.

Examples:

* thin branches;
* discontinuities;
* false positives from texture;
* weak boundaries;
* junction recovery;
* fragmentation.

Do not include qualitative images merely for visual decoration.

---

# 39. Qualitative Claims Must Be Visible

Only claim a visual advantage if it can actually be seen in the presented figure.

Do not write:

`ESGA-Net clearly preserves more branches`

unless the figure supports this.

When working from text without access to the actual figure content, use:

`[VERIFY QUALITATIVE CLAIM AGAINST FIGURE]`

instead of fabricating visual observations.

---

# 40. Avoid Cherry-Picked Qualitative Samples

Whenever possible, define how qualitative samples were selected.

Prefer:

* predefined representative cases;
* median-performing cases;
* difficult cases selected by a fixed criterion;
* a mixture of successes and failures.

Avoid selecting only examples where the proposed method wins dramatically.

If selection procedure is unknown, do not claim representativeness.

---

# 41. Show Failure Cases

A credible Results and Discussion section should include or discuss cases where the proposed method fails.

Possible failure conditions include:

* severe background texture;
* extremely weak boundaries;
* very thin structures;
* illumination artifacts;
* domain shift.

Do not portray only success cases.

---

# 42. Qualitative and Quantitative Evidence Should Agree

Use qualitative results to explain quantitative patterns.

Example:

`The improved clDice is consistent with the visually reduced fragmentation observed along thin branches.`

Do not claim consistency when the figures do not visibly support it.

---

# 43. Discussion Must Go Beyond Ranking

After reporting performance, explain why the observed pattern may occur.

Possible explanations should connect to:

* architecture;
* inductive bias;
* data characteristics;
* loss design;
* resolution;
* receptive field;
* attention mechanism;
* class imbalance;
* preprocessing.

Avoid unsupported causal certainty.

Prefer:

`This behavior may be attributable to...`

unless ablation or mechanistic evidence establishes the cause.

---

# 44. Dataset-Specific Interpretation

Use known dataset characteristics to interpret results.

Example structure:

`Dataset~3 contains [CHARACTERISTIC]. ESGA-Net's stronger Recall but slightly lower Precision relative to [METHOD] suggests [CAUTIOUS INTERPRETATION].`

Do not invent dataset properties during Discussion.

Use only characteristics established in the Dataset subsection or verified literature.

---

# 45. Cross-Dataset Consistency

Distinguish between:

* consistent ranking;
* consistent absolute performance;
* consistent metric behavior.

A model can rank highly across datasets while absolute scores vary substantially.

Discuss both when relevant.

---

# 46. Generalization Claims

Evaluation on three independently trained datasets demonstrates:

`consistency across heterogeneous within-dataset evaluations`

more directly than:

`cross-dataset generalization`.

Do not use the latter unless models trained on one dataset are evaluated on another.

---

# 47. Discussion Should Acknowledge Dataset Dependence

If the method wins on some datasets but not others, investigate plausible dataset characteristics.

Possible explanation pattern:

**dataset property → architecture interaction → observed ranking**

Keep explanations conditional unless directly demonstrated.

---

# 48. Compare with Prior Literature When Useful

Discussion may relate current findings to prior studies.

This requires actual literature research.

Prefer recent high-quality literature, with high priority given to:

* recent Q1 SCIE papers;
* original peer-reviewed sources;
* relevant landmark conference papers.

All citations must follow the Reference Integrity Skill.

Never fabricate a reference.

---

# 49. Purpose of Literature in Discussion

Use previous studies to:

* explain why a result is plausible;
* identify agreement/disagreement with prior findings;
* contextualize architectural behavior;
* discuss trade-offs;
* identify remaining limitations.

Do not add citations merely to make Discussion appear scholarly.

---

# 50. Do Not Perform Invalid Cross-Paper Benchmark Ranking

Avoid statements such as:

`Our IoU of 81.84% exceeds the 80.2% reported by X, therefore our method is better.`

unless:

* dataset;
* split;
* preprocessing;
* metric;
* evaluation protocol;

are directly comparable.

Prefer:

`The observed trend is consistent with prior studies showing that [TECHNICAL FINDING].`

---

# 51. Controlled Baselines Have Priority

Performance superiority claims should primarily rely on baselines evaluated under the current controlled protocol.

External literature should provide context, not substitute for controlled comparison.

---

# 52. Discuss Unexpected Results

Do not ignore results that contradict the design hypothesis.

For example:

* proposed method loses to Swin-UNet on one dataset;
* edge metric does not improve;
* efficiency is lower than expected;
* one ablation reduces performance.

Unexpected findings often provide the strongest Discussion.

---

# 53. Separate Observation from Interpretation

Use a two-step structure.

**Observation:**

`Swin-UNet exceeds ESGA-Net by 0.78 IoU points on Dataset~2.`

**Interpretation:**

`This suggests that [CAUTIOUS EXPLANATION].`

Do not present interpretations as raw facts.

---

# 54. Avoid Unsupported Mechanistic Claims

Do not write:

`The global attention module enables the network to capture long-range dependencies, resulting in the observed improvement.`

unless ablation or analysis supports that causal link.

Prefer:

`The result is consistent with the intended role of global attention in capturing long-range context.`

This distinction is important.

---

# 55. Discussion of Precision–Recall Trade-Off

When Precision and Recall move differently, analyze the trade-off.

Example:

`The higher Recall but slightly lower Precision suggests a tendency to recover more crack pixels at the cost of a small increase in false-positive responses.`

This interpretation follows directly from metric definitions.

---

# 56. Connect Statistical and Practical Evidence

A strong discussion should integrate:

* mean difference;
* CI;
* effect size;
* absolute metric improvement.

Example:

`The 0.54-point IoU gain over Swin-UNet on Dataset~1 is modest in absolute magnitude but consistent across repeated runs, with the confidence interval remaining above zero.`

This is more informative than citing only a $p$-value.

---

# 57. Avoid Words Such as “Robust” Without Qualification

Use:

`robust across random seeds`

only when repeated-seed evidence supports it.

Use:

`robust across datasets`

only when multiple datasets support it.

Use:

`robust to noise`

only when noise experiments support it.

Do not use one kind of robustness to imply another.

---

# 58. Do Not Call Small Standard Deviation “Generalization”

Low seed-to-seed variability indicates:

`optimization/retraining stability under the tested protocol`.

It does not by itself establish:

* cross-domain generalization;
* real-world robustness;
* out-of-distribution performance.

Use precise terminology.

---

# 59. Discussion Must Include Trade-Offs

If ESGA-Net achieves stronger accuracy but:

* has more parameters;
* lower FPS;
* higher memory;
* worse performance on one dataset;

state these trade-offs.

Scientific Discussion must not function as marketing.

---

# 60. Limitations Are Mandatory

A mature Results and Discussion section should identify limitations supported by the evidence.

Possible categories:

* dataset size;
* custom split;
* absence of independent test data;
* limited domain diversity;
* computational overhead;
* sensitivity to weak boundaries;
* lack of cross-dataset testing;
* comparison protocol limitations;
* statistical design limitations;
* reliance on pretrained encoders.

Do not invent limitations unrelated to the actual study.

---

# 61. Limitations Should Follow from Evidence

Preferred:

`Dataset~3 qualitative results show residual errors around weak boundaries, indicating that ambiguous crack-like texture remains challenging.`

Less useful:

`Future work should improve the model further.`

Limitations should be concrete and technically meaningful.

---

# 62. Threats to Validity

When relevant, distinguish:

## Internal validity

* training fairness;
* hyperparameter differences;
* checkpoint selection;
* leakage.

## External validity

* number of datasets;
* materials;
* imaging conditions;
* cross-domain generalization.

## Statistical validity

* number of runs;
* pairing assumptions;
* multiplicity;
* unit of analysis.

Do not hide threats that materially affect interpretation.

---

# 63. Discussion Should Not Repeat the Introduction

Do not restate all research gaps or literature.

The Discussion should answer:

`What did we learn from the experiments?`

rather than repeating:

`Why was the study needed?`

---

# 64. Discussion Should Not Become a Second Methodology

Do not re-explain module architecture in full.

Refer to relevant modules only when interpreting their apparent experimental effects.

---

# 65. Use Cautious Scientific Language

Preferred:

* `suggests`;
* `indicates`;
* `is consistent with`;
* `may reflect`;
* `provides evidence that`;
* `supports the hypothesis that`.

Use stronger causal language only when experiments justify it.

---

# 66. Avoid Promotional Language

Do not use:

* `remarkable`;
* `outstanding`;
* `revolutionary`;
* `unprecedented`;
* `exceptional`;

unless quoting a source, which is rarely appropriate.

Let the evidence establish performance.

---

# 67. Avoid Repetitive “These Results Demonstrate”

Vary logical transitions.

Possible alternatives:

* `This pattern indicates ...`
* `Taken together, ...`
* `The comparison suggests ...`
* `The observed trend is consistent with ...`
* `A different pattern emerges ...`
* `In contrast, ...`
* `Collectively, ...`

Variation must preserve precision.

---

# 68. Best/Second-Best Formatting Must Match the Data

If tables mark best and second-best results:

* verify ranking numerically;
* account for direction of the metric;
* do not mark ties incorrectly;
* ensure prose agrees with formatting.

Never trust manually inserted `\best{}` or `\second{}` without checking the values.

---

# 69. Table Arithmetic and Ranking Audit

For every comparison table:

1. identify best value;
2. identify second-best value;
3. verify reported difference;
4. verify prose ranking;
5. verify sign of improvement.

If the table and prose conflict, flag it.

Do not silently choose one.

---

# 70. Cross-Table Consistency

Values repeated across:

* main result tables;
* statistical tables;
* abstract;
* conclusion;
* figures;

must agree.

Example:

If Dataset~1 IoU is:

`77.87%`

every section must use the same mean unless another statistic is explicitly identified.

---

# 71. Statistical Difference Audit

If:

[
\Delta =
\operatorname{IoU}_{\mathrm{ESGA}}
----------------------------------

\operatorname{IoU}_{\mathrm{baseline}},
]

verify that the displayed difference approximately agrees with the reported means.

Minor differences can occur if differences are calculated seed-wise and averaged, but any discrepancy should be mathematically explainable.

---

# 72. Figure–Text Consistency

Check that:

* figure axes;
* metric labels;
* units;
* legends;
* caption;
* prose;

describe the same quantities.

For example, do not label an axis `mIoU` if the manuscript reports crack-class IoU.

---

# 73. Efficiency Table Consistency

When memory is reported at only one resolution, state this clearly.

Do not imply memory values apply equally to all datasets.

Similarly, FPS values measured at different resolutions should not be interpreted as dataset-independent model throughput.

---

# 74. Missing Complexity Values

If a baseline has:

`GMACs = --`

do not include it in quantitative GMAC ranking or bubble-size comparison without explaining how the missing value is handled.

Never invent the missing complexity.

---

# 75. Qualitative Figure Referencing

Use:

```latex id="k9ygu1"
Fig.~\ref{fig:qual_d1}
```

or the journal's preferred form consistently.

Do not alternate randomly between:

`Fig.`

and:

`Figure`

unless required by sentence position/style.

---

# 76. Main Result Paragraph Pattern

For each dataset, a concise high-quality paragraph can follow:

**ranking → strongest comparison → important secondary metric → trade-off → interpretation**

Example:

`On Dataset~[X], ESGA-Net achieves the highest IoU of [VALUE], exceeding the strongest competing method, [BASELINE], by [DIFFERENCE] percentage points. It also ranks [RANK] in [SECONDARY_METRIC], while [OTHER_METHOD] retains the highest [TRADEOFF_METRIC]. This pattern indicates [INTERPRETATION].`

Do not list all baseline values.

---

# 77. Statistical Paragraph Pattern

Use:

**mean difference → CI → adjusted significance → effect size → practical interpretation**

Example:

`Relative to [BASELINE], ESGA-Net improves IoU by [DELTA] points (95% CI [LOWER, UPPER]). The Holm-adjusted [TEST] yields [P_VALUE], while the effect size is [D]. Although statistically supported, the absolute margin is [small/moderate/large in context].`

---

# 78. Efficiency Paragraph Pattern

Use:

**accuracy position → compute position → Pareto/trade-off interpretation**

Example:

`ESGA-Net is not the lightest architecture, but it achieves [ACCURACY RESULT] with [GMACS] GMACs. [LIGHTER METHOD] requires fewer operations but attains [LOWER/HIGHER] IoU, whereas [HEAVIER METHOD] incurs substantially higher computation. Thus, ESGA-Net occupies [TRADE-OFF DESCRIPTION].`

---

# 79. Qualitative Paragraph Pattern

Use:

**visual challenge → competing behavior → proposed behavior → failure case → relation to quantitative evidence**

Avoid declaring visual superiority in every sample.

---

# 80. Integrated Discussion Paragraph

After individual results, synthesize:

1. where ESGA-Net is consistently strong;
2. where another method is stronger;
3. which contribution-specific metrics support the design;
4. whether efficiency claims are justified;
5. how dataset characteristics affect behavior;
6. what remains unresolved.

This paragraph should provide the main scientific takeaway.

---

# 81. Results Should Support the Abstract

Every quantitative claim in the Abstract must be traceable to Results.

Before finalizing, verify:

* IoU values;
* rankings;
* clDice values;
* efficiency claims;
* statistical claims.

If the Abstract states something not demonstrated in Results, revise the Abstract.

---

# 82. Results Should Support the Contributions

For every contribution listed in Introduction:

`Contribution 1 → [RESULT/TABLE/FIGURE]`

`Contribution 2 → [ABLATION/METRIC]`

`Contribution 3 → [RESULT/TABLE/FIGURE]`

If no evidence exists, the contribution is unsupported.

---

# 83. Results Must Align with Conclusion

The Conclusion may summarize only findings established in Results.

Do not introduce new quantitative claims in Conclusion.

---

# 84. Literature Research in Discussion

When scientific interpretation requires comparison with prior work, conduct a fresh literature search rather than relying solely on references already used in Introduction.

Prioritize:

1. recent Q1 SCIE studies from the latest five-year window;
2. original method papers;
3. authoritative reviews;
4. leading peer-reviewed conference papers where appropriate.

Every external claim must follow:

**search → verify paper → verify claim → verify metadata → cite**

Never fabricate.

---

# 85. Recent Contradictory Literature Must Not Be Ignored

If recent studies report findings that differ from the current interpretation, acknowledge them where relevant.

Discussion should not selectively cite only papers that support the proposed mechanism.

---

# 86. External Performance Numbers

Use external benchmark numbers sparingly.

If reported:

* verify them from the original paper;
* identify dataset;
* split;
* metric;
* protocol.

Do not imply direct superiority unless protocols are genuinely comparable.

---

# 87. No Citation Needed for Own Experimental Findings

Do not attach literature citations to statements that merely report your own table.

Example:

`ESGA-Net achieves 80.72% IoU on Dataset~3.`

does not require an external citation.

Cite literature only when making an external scientific comparison or interpretation.

---

# 88. Placeholder Rule

When a result is missing, preserve the logical structure.

Example:

`The ablation results in Table~\ref{tab:ablation} show that [ABLATION_MAIN_FINDING].`

Do not invent values.

Use the smallest possible placeholder.

---

# 89. Do Not Ask for Every Missing Number

If enough evidence is available to draft most of the section:

* write the available analysis;
* insert placeholders for missing results;
* flag unresolved methodological issues.

Only ask for clarification when a missing fact changes the interpretation fundamentally.

---

# 90. Mechanical LaTeX Audit

Check for:

* missing spaces before `\cite`;
* inconsistent `Fig.`/`Table`;
* malformed `%`;
* bad math spacing;
* missing `~`;
* duplicated punctuation;
* incorrect percentage-point wording;
* accidental line-break artifacts.

Results tables are highly vulnerable to copy-editing errors.

---

# 91. Table Caption Rules

Captions should identify:

* dataset;
* metric context;
* repeated-run reporting when necessary.

Notes should define:

* mean ± SD;
* best/second-best formatting;
* special symbols;
* missing values.

Do not overload captions with interpretation.

---

# 92. Significant Digits

Use consistent decimal precision across comparable methods.

If mean IoU is reported to two decimals, report all methods to two decimals.

Standard deviation precision should be consistent.

Do not imply measurement precision beyond what the experiment supports.

---

# 93. Ordering of Methods

Keep baseline order consistent across tables where possible.

This makes cross-dataset comparison easier.

If methods are grouped by architecture family, apply the grouping consistently.

---

# 94. Statistical Table Reporting

Statistical tables should include enough information to interpret each comparison:

* baseline;
* mean difference;
* confidence interval;
* effect size;
* adjusted $p$-value.

Do not report only $p$-values.

---

# 95. Extreme Effect Sizes Require Inspection

If standardized effects are unusually large, verify:

* calculation;
* denominator;
* paired differences;
* unit scaling;
* data extraction.

Do not assume extremely large values are correct merely because software produced them.

Flag suspicious values for audit.

---

# 96. Wilcoxon Repeated Identical $p$-Values

If many comparisons yield identical Wilcoxon $p$-values, verify whether this results from:

* discrete exact-test limits;
* correction;
* software behavior;
* tied/rank structure.

Do not treat repeated identical values as automatically erroneous, but audit them before publication.

---

# 97. Results Audit — Numerical Integrity

Before returning Results:

* `[ ]` Every value is sourced from actual experiment output.
* `[ ]` Means agree with tables.
* `[ ]` SDs agree with tables.
* `[ ]` Rankings are correct.
* `[ ]` Percentage-point differences are correct.
* `[ ]` CIs agree with statistical analysis.
* `[ ]` $p$-values are correctly adjusted.
* `[ ]` Effect sizes are correctly signed.
* `[ ]` FPS/GMAC/parameter values are consistent.
* `[ ]` Missing values have not been invented.

---

# 98. Results Audit — Scientific Interpretation

Check:

* `[ ]` The primary metric anchors the main comparison.
* `[ ]` Unfavorable findings are acknowledged.
* `[ ]` Statistical significance is distinguished from effect magnitude.
* `[ ]` Causal module claims are supported by ablation.
* `[ ]` Efficiency claims use appropriate evidence.
* `[ ]` Qualitative claims are visible in figures.
* `[ ]` Dataset-specific interpretations use known dataset characteristics.
* `[ ]` No cross-dataset generalization claim is made without cross-dataset testing.
* `[ ]` Limitations are discussed.
* `[ ]` Discussion does not overstate the evidence.

---

# 99. Results Audit — Cross-Section Consistency

Compare Results against:

### Abstract

* main scores;
* rankings;
* topology claims;
* efficiency claims.

### Introduction

* contributions;
* promised experimental objectives.

### Experimental Setup

* primary metric;
* evaluation split;
* number of seeds;
* statistical design;
* metrics.

### Methodology

* component claims.

### Conclusion

* final claims.

Flag all contradictions.

---

# 100. Research Integrity Rule

Results and Discussion must never be written as advocacy for the proposed model.

The role of the AI is to explain the evidence faithfully, including:

* strengths;
* weaknesses;
* uncertainty;
* exceptions;
* trade-offs;
* limitations.

# CORE RULE

**Do not narrate tables. Identify the scientifically important findings, quantify the relevant differences, establish their statistical and practical meaning, explain them cautiously in relation to the method and prior literature, acknowledge unfavorable results and limitations, and never claim more than the experiments demonstrate.**
