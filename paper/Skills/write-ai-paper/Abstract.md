# ABSTRACT WRITING SKILL

## 1. Objective

When writing or rewriting an abstract for a scientific paper, produce a concise, self-contained summary of the entire study.

The abstract must allow the reader to understand:

1. why the research topic is important;
2. what problem or research gap remains unresolved;
3. what method is proposed;
4. how the method is experimentally validated;
5. what the principal quantitative results are;
6. what these results demonstrate.

The abstract must summarize the complete research rather than function as a shortened Introduction.

---

## 2. Default Length

The default abstract length is:

**200–250 words.**

Target approximately **220–240 words** unless the journal or user specifies another word limit.

Do not make the abstract artificially short when sufficient methodological and quantitative information is available.

Do not exceed 250 words by adding unnecessary background, implementation details, or generic statements.

---

## 3. Required Logical Structure

Unless the target journal requires another format, construct the abstract according to the following sequence:

**Context → Challenge/Research Gap → Proposed Method → Experimental Validation → Quantitative Results → Interpretation/Conclusion**

The transitions between these components must be natural. The abstract should normally remain a **single coherent paragraph**.

---

# 4. Context and Importance

Begin with one sentence establishing the research topic and its significance.

The opening sentence should communicate that the research problem is relevant, important, increasingly studied, or practically necessary.

Appropriate opening patterns include, but are not limited to:

* `In recent years, ... has received increasing attention because ...`
* `In recent years, increasing attention has been devoted to ...`
* `Over the past decade, ... has emerged as an important research topic in ...`
* `Over the last decade, significant progress has been made in ...`
* `Recent advances in ... have stimulated increasing interest in ...`
* `With the rapid development of ..., ... has become increasingly important for ...`
* `The increasing demand for ... has motivated substantial research on ...`
* `... plays an important role in ...`
* `... is a fundamental task in ...`

Do not mechanically use `In recent years` for every paper.

Vary the opening according to the context, maturity, and development history of the research topic.

Use temporal expressions such as:

* `In recent years`
* `Over the past decade`
* `Over the last several years`
* `Recent advances in`
* `With the rapid development of`

only when such wording is logically appropriate.

The opening should normally occupy **one sentence only**.

Do not spend several sentences providing general background.

---

# 5. Research Challenge or Gap

Immediately after establishing the topic, identify the unresolved problem.

A preferred transition is:

`However, ...`

The challenge must be **specific**, rather than generic.

Avoid weak statements such as:

`However, this task remains challenging.`

Instead, state why it remains challenging:

`However, accurate pixel-level segmentation remains challenging under limited annotated data because of weak boundaries, severe class imbalance, and complex structural connectivity.`

Whenever possible, identify approximately **two to four major technical difficulties**.

The stated challenges must be directly relevant to the proposed method.

There should be a logical correspondence:

**identified problem → proposed design → intended improvement**

Do not introduce a challenge that is never addressed by the methodology.

---

# 6. Proposed Method

Introduce the proposed method immediately after the research gap.

Preferred transitions include:

* `To address these challenges, we propose ...`
* `To overcome these limitations, we propose ...`
* `To tackle these issues, we develop ...`
* `Accordingly, we introduce ...`
* `To this end, we propose ...`

At first occurrence, provide:

**full method name (acronym)**

For example:

`Edge-guided Strip-context Global-Attention Network (ESGA-Net)`

Afterward, use only the acronym or shortened method name.

The method description should answer:

* What type of model or framework is proposed?
* What are its principal innovations?
* What technical purpose does each major innovation serve?

Prefer functional descriptions over module enumeration.

Weak:

`The model contains Modules A, B, C, and D.`

Preferred:

`The framework integrates multi-scale strip-context modeling, semantic edge-guided feature gating, global self-attention, and topology-aware learning to enhance boundary localization and structural connectivity.`

Only include architectural components that constitute important contributions.

Do not include minor implementation details in the abstract.

---

# 7. Relationship Between Challenges and Method Design

The abstract should preferably exhibit an implicit or explicit mapping between the identified challenges and the proposed technical components.

For example:

* thin or elongated structures → strip/context modeling;
* weak boundaries → edge-guided learning;
* long-range dependencies → global attention;
* discontinuity or fragmentation → topology-aware learning;
* limited data → transfer learning, regularization, or data-efficient design.

This mapping strengthens the scientific logic of the abstract.

Avoid presenting the method as an arbitrary collection of modules.

---

# 8. Experimental Validation

After introducing the method, summarize the experimental design.

State the most important validation information, such as:

* number or names of datasets;
* number/type of competing methods;
* major model families used for comparison;
* fair training/evaluation protocol;
* repeated experiments or random seeds;
* statistical validation, when relevant.

Example:

`ESGA-Net is evaluated on three public crack datasets and compared with ten representative CNN- and Transformer-based segmentation methods under identical training, augmentation, model-selection, and evaluation protocols.`

If rigorous repeated experiments are an important strength, mention them:

`Each method–dataset pair is evaluated over 30 independent random seeds to ensure statistically reliable comparisons.`

Do not normally report:

* batch size;
* optimizer;
* learning rate;
* number of epochs;
* GPU model;
* detailed augmentation parameters;

unless one of these is itself a methodological contribution.

---

# 9. Baseline Description

Do not overload the abstract with a long list of baseline names.

Prefer:

`ten representative CNN- and Transformer-based segmentation methods`

over listing every competing architecture.

A small number of particularly important baselines may be named if doing so strengthens the comparison.

Avoid excessive use of `SOTA`.

Prefer formal expressions such as:

* `representative state-of-the-art methods`;
* `competitive segmentation methods`;
* `representative CNN- and Transformer-based approaches`.

---

# 10. Quantitative Results Are Mandatory

Whenever numerical results are available, report the principal quantitative findings.

Do not write only:

`The proposed method outperforms existing approaches.`

Provide concrete evidence.

For example:

`ESGA-Net achieves IoU scores of 77.87%, 81.84%, and 80.72% on the three datasets, respectively.`

Select metrics that directly support the paper's principal contributions.

Normally report approximately **one to three key metrics**, not every metric contained in the Results section.

For example:

* IoU/Dice for segmentation accuracy;
* clDice for topology preservation;
* MAE/RMSE for regression;
* Accuracy/F1 for classification;
* FLOPs/parameters/FPS when computational efficiency is a contribution.

---

# 11. Dataset–Result Correspondence

When reporting results for multiple datasets, the relationship between dataset and score must be unambiguous.

Preferred:

`The proposed method achieves IoU scores of X%, Y%, and Z% on Dataset A, Dataset B, and Dataset C, respectively.`

Do not use unclear expressions such as:

* `dataset 1`;
* `dataset 2`;
* `datasets (1,3)`;
* `the second dataset`

unless the datasets have already been explicitly ordered and no ambiguity exists.

When individual dataset names would make the abstract too long, summarize the ranking instead:

`The proposed method achieves the best IoU on two of the three datasets and ranks second on the remaining dataset.`

---

# 12. Interpret the Numerical Results

Important numerical results should be followed by a short technical interpretation.

Use the pattern:

**metric → result → scientific meaning**

Example:

`It further obtains the highest clDice scores across all three datasets, demonstrating improved preservation of crack connectivity and reduced segmentation fragmentation.`

Do not merely list numbers without explaining what they demonstrate.

---

# 13. Final Conclusion

End the abstract with one concise sentence describing the principal implication of the results.

Preferred patterns include:

* `These results demonstrate that ...`
* `The results indicate that ...`
* `Overall, the proposed method provides ...`
* `These findings demonstrate the effectiveness of ...`

The final statement must be supported by the presented experiments.

Do not introduce a new contribution in the final sentence.

Do not claim properties that have not been experimentally demonstrated.

For example, do not write:

`computationally efficient`

unless computational complexity, inference speed, FLOPs, parameters, memory, or equivalent evidence has been evaluated.

Similarly, use claims such as:

* `robust`;
* `generalizable`;
* `statistically significant`;
* `superior`;
* `efficient`;

only when experimental evidence supports them.

---

# 14. Scientific Claim Discipline

Every major claim in the abstract must correspond to evidence in the paper.

Maintain consistency among:

**Abstract claims ↔ Introduction contributions ↔ Methodology ↔ Experimental results ↔ Conclusion**

Do not exaggerate novelty or performance.

Use `statistically significant` only if an appropriate statistical significance test was conducted.

Multiple random seeds alone demonstrate evaluation robustness but do not automatically establish statistical significance.

---

# 15. Acronyms

Define an acronym at its first occurrence:

`structural health monitoring (SHM)`

not:

`structural health monitoring(SHM)`

Define the proposed method using:

`Full Method Name (ACRONYM)`

Avoid excessive abbreviations because they reduce abstract readability.

Common technical metrics or terms may remain abbreviated when standard for the target research community, but clarity takes priority.

---

# 16. Mathematical Content

Do not use numbered equations in an abstract unless explicitly required.

Inline mathematical notation is acceptable when necessary:

`an IoU of $81.84\%$`

However, prefer readable prose for ordinary numerical results.

The abstract should remain accessible without requiring the reader to interpret complex mathematical notation.

---

# 17. Citations

Do not normally include references or `\cite{}` commands in the abstract.

The abstract should be understandable independently of the reference list.

---

# 18. Language Style

Use formal scientific English.

The writing should be:

* concise;
* technically precise;
* evidence-based;
* logically connected;
* free from unnecessary rhetorical language.

Prefer active constructions when they improve clarity:

`We propose ESGA-Net...`

`We evaluate the method...`

rather than unnecessarily passive and indirect constructions.

Avoid promotional language such as:

* `remarkable`;
* `revolutionary`;
* `groundbreaking`;
* `extremely powerful`;
* `excellent`.

Use technically defensible expressions instead.

---

# 19. Sentence Distribution

For a standard 200–250-word abstract, use approximately **6–9 sentences**.

Recommended distribution:

**Sentence 1:** research context and importance.

**Sentence 2:** specific research challenge/gap.

**Sentence 3–4:** proposed method and principal innovations.

**Sentence 4–5:** experimental setup and comparison protocol.

**Sentence 5–7:** principal quantitative results.

**Sentence 7–8:** interpretation and final implication.

This is a guideline rather than a rigid sentence-count requirement.

Logical completeness has priority over exact sentence count.

---

# 20. Preferred Abstract Reasoning Pattern

Internally construct the abstract according to:

**WHY → WHAT IS MISSING → WHAT WE PROPOSE → HOW WE VERIFY IT → WHAT WE OBTAIN → WHAT IT MEANS**

Before generating the final abstract, verify that all six components are present.

---

# 21. Avoid Formulaic Repetition Across Papers

When generating abstracts for multiple manuscripts, vary sentence construction while preserving the same scientific logic.

Do not repeatedly produce:

`In recent years ... However ... To address this problem ... Experimental results demonstrate ...`

with identical syntax for every manuscript.

Vary expressions naturally according to the research context.

Possible context openings:

`In recent years, ...`

`Over the past decade, ...`

`Recent advances in ...`

`With the increasing deployment of ...`

`The growing demand for ...`

`Accurate ... is essential for ...`

Possible gap transitions:

`However, ...`

`Despite these advances, ...`

`Nevertheless, ...`

`Existing approaches remain limited by ...`

Possible method transitions:

`To address these limitations, ...`

`To this end, ...`

`Accordingly, ...`

`Motivated by these challenges, ...`

Possible conclusion transitions:

`These results demonstrate ...`

`The findings indicate ...`

`Overall, the results suggest ...`

Variation must not come at the cost of scientific precision.

---

# 22. Final Abstract Validation

Before returning an abstract, verify all of the following:

* The length is approximately 200–250 words unless otherwise specified.
* The topic importance is established.
* A concrete research challenge or gap is identified.
* The challenge is logically connected to the proposed method.
* The proposed method is clearly named and defined.
* Only major methodological innovations are included.
* Experimental validation is summarized.
* Important comparison conditions are stated when relevant.
* At least one principal quantitative result is provided when results are available.
* Numerical results are unambiguous.
* The major results are interpreted.
* The conclusion does not exceed the experimental evidence.
* Acronyms are defined at first occurrence.
* No unnecessary citations are included.
* No unnecessary implementation details are included.
* No unsupported claims are made.
* Terminology and numerical values are consistent with the rest of the manuscript.
* The abstract can be understood independently of the full paper.

# Core Rule

A high-quality abstract should form a complete scientific argument within approximately 200–250 words:

**importance → unresolved problem → technical solution → rigorous validation → quantitative evidence → defensible conclusion.**


# Handling Missing or Incomplete Information

The abstract may be requested before all information about the study is available. The AI must therefore be able to generate a structurally complete abstract without fabricating missing scientific information.

## 1. Never Invent Missing Scientific Information

If required information is unavailable, uncertain, or has not yet been provided, **do not infer, fabricate, or assume it**.

Instead, insert a clear placeholder at the exact location where the missing information is required.

For example:

`The proposed method is evaluated on [DATASET(S)] and compared with [NUMBER] representative baseline methods.`

or:

`The proposed method achieves an IoU of [XX.XX%], outperforming [BASELINE/COMPARISON] by [XX.XX%].`

The goal is to preserve the complete logical structure of the abstract while clearly identifying information that must be supplied later.

---

## 2. Standard Placeholder Format

Use square brackets with concise uppercase labels:

* `[METHOD_NAME]`
* `[FULL_METHOD_NAME]`
* `[APPLICATION]`
* `[RESEARCH_PROBLEM]`
* `[RESEARCH_GAP]`
* `[CHALLENGE_1]`
* `[CHALLENGE_2]`
* `[DATASET_NAME]`
* `[DATASET_NAMES]`
* `[NUMBER_OF_DATASETS]`
* `[NUMBER_OF_BASELINES]`
* `[BASELINE_METHODS]`
* `[METRIC]`
* `[RESULT]`
* `[RESULT_1]`
* `[RESULT_2]`
* `[IMPROVEMENT]`
* `[NUMBER_OF_SEEDS]`
* `[STATISTICAL_TEST]`
* `[COMPUTATIONAL_COST]`
* `[FINAL_CONCLUSION]`

Placeholders should describe exactly what information is missing.

Avoid vague placeholders such as:

`[something]`

`[information]`

`[add here]`

---

## 3. Preserve All Available Information

Only replace genuinely missing information with placeholders.

If part of a sentence is known, preserve it.

For example, if the method and datasets are known but numerical results are not yet available:

`ESGA-Net is evaluated on Crack500, DeepCrack, and CFD against ten representative CNN- and Transformer-based segmentation methods. ESGA-Net achieves an IoU of [RESULT_1], [RESULT_2], and [RESULT_3] on the three datasets, respectively.`

Do not replace known information with unnecessary placeholders.

---

## 4. Maintain a Complete Abstract Structure

Even when information is incomplete, retain the standard abstract organization:

**Context → Challenge/Gap → Proposed Method → Experimental Validation → Quantitative Results → Interpretation → Conclusion**

Missing information must not cause the AI to omit an entire logical component if that component is expected to exist later.

For example, if experimental results are not yet available, write:

`Experimental results show that [MAIN_QUANTITATIVE_RESULT]. In addition, [SECONDARY_RESULT], indicating [TECHNICAL_INTERPRETATION].`

rather than removing the result section completely.

---

## 5. Maintain Grammatical Sentences Around Placeholders

Placeholders must be embedded naturally into complete academic sentences.

Preferred:

`The proposed framework is evaluated on [NUMBER_OF_DATASETS] benchmark datasets and compared with [NUMBER_OF_BASELINES] representative methods.`

Avoid fragmented drafting such as:

`Datasets: [DATASETS]. Baselines: [BASELINES]. Results: [RESULTS].`

The abstract should remain readable as a near-final manuscript draft.

---

## 6. Missing Numerical Results

When numerical results are not available, use explicit metric-specific placeholders.

For example:

`The proposed method achieves IoU scores of [IOU_DATASET_1], [IOU_DATASET_2], and [IOU_DATASET_3], respectively.`

For comparative improvements:

`This represents an improvement of [IOU_IMPROVEMENT] over the strongest competing method.`

For statistical information:

`The improvement is statistically significant according to [STATISTICAL_TEST] with $p=[P_VALUE]$.`

Do not invent plausible numerical values.

---

## 7. Missing Dataset Information

If datasets have not yet been finalized, write:

`The proposed method is evaluated on [NUMBER_OF_DATASETS] [PUBLIC/PRIVATE] datasets, including [DATASET_NAMES].`

If even the number of datasets is unknown:

`The proposed method is evaluated on [DATASET_NAMES/NUMBER_OF_DATASETS] and compared with [BASELINE_INFORMATION].`

Do not assume commonly used datasets simply because they are typical for the research topic.

---

## 8. Missing Baseline Information

If comparison methods have not yet been selected:

`The proposed method is compared with [NUMBER_OF_BASELINES] representative [METHOD_FAMILIES] approaches.`

Examples of `[METHOD_FAMILIES]` include:

* CNN-based methods;
* Transformer-based methods;
* conventional machine-learning methods;
* physics-based methods;
* signal-processing approaches.

Only specify a family when that information is known.

---

## 9. Missing Method Details

If the proposed method has been named but some components remain undecided:

`We propose [METHOD_NAME], which integrates [COMPONENT_1], [COMPONENT_2], and [COMPONENT_3] to address [TECHNICAL_OBJECTIVE].`

If the method name itself is not finalized:

`To address these challenges, we propose [METHOD_NAME], a [MODEL_TYPE] designed to [PRIMARY_OBJECTIVE].`

Do not invent a method acronym.

---

## 10. Missing Research Gap

If the research topic is known but the exact gap has not yet been established, retain a placeholder rather than creating an unsupported limitation:

`However, existing approaches remain limited by [RESEARCH_GAP], particularly under [TARGET_CONDITION].`

A research gap is a scientific claim and therefore must not be fabricated.

---

## 11. Missing Final Conclusion

The conclusion must not exceed the available evidence.

If experimental results are unavailable, do not write:

`These results demonstrate the superior performance of the proposed method.`

Instead, use:

`These results are expected to clarify [FINAL_INTERPRETATION].`

or, preferably for a manuscript draft awaiting results:

`[FINAL_CONCLUSION_BASED_ON_RESULTS].`

When there is insufficient evidence to formulate the conclusion safely, use a placeholder rather than predicting successful results.

---

## 12. Unsupported Claims Must Become Placeholders

If a claim requires evidence that has not yet been supplied, convert the unsupported part into a placeholder.

For example, do not write:

`The proposed method is computationally efficient.`

when computational evaluation is unavailable.

Write:

`The proposed method achieves [COMPUTATIONAL_EFFICIENCY_RESULT], indicating [EFFICIENCY_INTERPRETATION].`

Similarly:

`[STATISTICAL_SIGNIFICANCE_CLAIM]`

`[GENERALIZATION_CLAIM]`

`[ROBUSTNESS_CLAIM]`

should remain placeholders until supported by evidence.

---

## 13. Do Not Stop Writing Because Information Is Missing

When enough information exists to understand the intended research, generate the abstract directly.

Do not unnecessarily ask the user to provide every missing detail before drafting.

Instead:

1. use all information currently available;
2. construct the full abstract;
3. insert placeholders for unavailable elements;
4. allow the placeholders to be replaced when additional results become available.

Ask for clarification only when the missing information prevents identification of the fundamental research topic or intended contribution.

---

## 14. Placeholder Granularity

Use the smallest reasonable placeholder.

Preferred:

`ESGA-Net achieves an IoU of [IOU_SCORE] on Crack500.`

Less preferred:

`[RESULT_SENTENCE]`

Use an entire-sentence placeholder only when almost no information about that sentence is available.

This makes later revision easier and preserves as much finished manuscript text as possible.

---

## 15. Placeholder Consistency

The same missing quantity must use the same placeholder throughout the abstract.

For example, if the method name is unknown, consistently use:

`[METHOD_NAME]`

Do not alternate between:

`[MODEL_NAME]`

`[NETWORK_NAME]`

`[METHOD]`

for the same missing item.

---

## 16. Placeholder Replacement

When the user later provides missing information:

* replace the corresponding placeholders;
* revise surrounding grammar as needed;
* verify numerical and logical consistency;
* remove obsolete placeholders;
* do not rewrite already satisfactory sections unnecessarily.

After all required information is available, the final abstract should contain **no placeholders**.

---

# Core Missing-Information Rule

**Use known information exactly as provided. Never fabricate unknown scientific content. Preserve the complete abstract structure and represent every unresolved element with a precise, easily replaceable placeholder.**
