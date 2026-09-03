# TAWs-Transformer General Academic Writing Rules

## 1. Scope

These rules apply to all manuscript sections unless a section-specific skill explicitly overrides them.

They govern:

- academic language;
- scientific tone;
- sentence and paragraph construction;
- terminology;
- repetition control;
- claim discipline;
- LaTeX-aware writing;
- cross-section consistency;
- handling of missing information;
- reduction of formulaic or machine-generated writing patterns.

The objective is to produce writing that reads as if it were prepared and carefully revised by a domain expert.

---

# 2. Default Language

Write in formal academic English unless the user explicitly requests another language.

Use the variety of English required by the target journal. If no journal style is specified, default to consistent American English.

Do not mix American and British spelling within the same manuscript.

Examples:

- American: `modeling`, `optimization`, `behavior`
- British: `modelling`, `optimisation`, `behaviour`

Once a spelling convention is selected, preserve it throughout the manuscript.

---

# 3. Scientific Tone

Use a professional, precise, restrained, and evidence-based tone.

Prefer language that states:

- what was observed;
- what was measured;
- what was proposed;
- what the evidence supports;
- what remains uncertain.

Avoid promotional, emotional, exaggerated, or conversational language.

Do not use expressions such as:

- `remarkable`;
- `revolutionary`;
- `groundbreaking`;
- `outstanding`;
- `exceptional`;
- `highly impressive`;
- `game-changing`;
- `unprecedented`;

unless such wording is part of a direct quotation, which is rarely appropriate in a scientific manuscript.

---

# 4. Reduce AI-Like Writing Patterns

The manuscript must not read like generic AI-generated prose.

Avoid repeated use of formulaic expressions such as:

- `It is worth noting that ...`
- `It should be noted that ...`
- `This highlights the importance of ...`
- `This underscores the significance of ...`
- `This demonstrates the effectiveness of ...`
- `These findings provide valuable insights into ...`
- `In today's rapidly evolving ...`
- `In the ever-growing field of ...`
- `A comprehensive analysis reveals ...`
- `plays a pivotal role`
- `holds great promise`
- `offers a powerful solution`
- `serves as a cornerstone`
- `paves the way for`
- `opens new avenues for`

These expressions are not absolutely forbidden when scientifically justified, but they should be used rarely and never as generic filler.

Prefer direct technical statements.

Weak:

`These findings provide valuable insights into the effectiveness of the proposed framework.`

Preferred:

`The improvement is concentrated in clDice and Recall, indicating that the main benefit lies in preserving connected crack structures.`

---

# 5. No Em Dash

Do not use the em dash character:

`—`

in manuscript prose.

Use one of the following instead, depending on sentence structure:

- comma;
- semicolon;
- colon;
- parentheses;
- separate sentence.

Avoid replacing every em dash mechanically with another punctuation mark. Rewrite the sentence when necessary.

Preferred:

`The model improves connectivity, particularly for thin crack branches.`

or:

`The model improves connectivity; this effect is most evident for thin crack branches.`

---

# 6. Avoid Excessive En-Dash Usage in Prose

Use an en dash only where typographically appropriate, such as:

- numerical ranges;
- paired concepts;
- compound relations where required by the journal style.

Examples:

`20--30 epochs`

`encoder--decoder architecture`

`accuracy--complexity trade-off`

Do not use en dashes as substitutes for sentence punctuation.

---

# 7. Sentence Construction

Write complete, grammatically controlled sentences.

Prefer sentences with one clear principal claim.

Avoid excessively long sentences containing multiple unrelated claims.

A sentence may be technically complex, but its logical structure must remain traceable.

When a sentence exceeds approximately 35--40 words, check whether it should be divided.

Do not shorten sentences mechanically if division would damage scientific coherence.

---

# 8. Sentence-Length Variation

Avoid producing paragraphs in which every sentence has nearly the same length or syntactic structure.

Use natural variation:

- short sentence for a central conclusion;
- medium-length sentence for evidence;
- longer sentence when technical qualification is necessary.

Avoid repetitive patterns such as:

`Method A does X. Method B does Y. Method C does Z.`

Synthesize related information whenever possible.

---

# 9. Avoid Repetitive Sentence Openings

Do not begin consecutive sentences repeatedly with the same subject or transition.

Weak:

`ESGA-Net achieves ...`
`ESGA-Net also obtains ...`
`ESGA-Net further shows ...`
`ESGA-Net demonstrates ...`

Preferred:

`ESGA-Net achieves the highest IoU on Dataset~1. Its advantage is smaller for Recall, where SegFormer ranks first. On Dataset~3, the proposed model again leads in IoU and F1.`

---

# 10. Avoid Repetitive Transitions

Do not repeatedly use:

- `Moreover`;
- `Furthermore`;
- `Additionally`;
- `In addition`;
- `However`;
- `Therefore`;
- `Consequently`;
- `Taken together`;
- `Overall`;

in neighboring sentences or paragraphs.

Use transitions only when they represent a real logical relationship.

Sometimes no explicit transition is needed.

---

# 11. Avoid Repetitive Conclusions

Do not end every paragraph with:

`These results demonstrate ...`

or:

`These findings indicate ...`

Vary paragraph endings according to the scientific purpose:

- limitation;
- comparison;
- implication;
- transition;
- unresolved issue;
- design requirement.

---

# 12. Paragraph Structure

Each paragraph should normally contain:

1. one principal idea;
2. evidence or explanation;
3. synthesis or transition where needed.

Do not combine unrelated topics into one paragraph merely to reduce paragraph count.

Do not create very short one-sentence paragraphs in the manuscript unless required by a specific style.

---

# 13. Paragraph Connectivity

Adjacent paragraphs must form a logical progression.

A paragraph should prepare the reader for the next one.

Preferred progression:

`problem importance`
→ `technical challenge`
→ `existing solutions`
→ `remaining limitation`
→ `proposed response`

Avoid abrupt topic changes.

---

# 14. Use Domain-Specific Language

Use terminology appropriate to the scientific field.

For structural health monitoring, crack segmentation, machine learning, signal processing, and computer vision, prefer established technical vocabulary rather than generic language.

Examples:

Prefer:

- `pixel-level segmentation`;
- `foreground crack pixels`;
- `long-range contextual modeling`;
- `boundary localization`;
- `topological continuity`;
- `class imbalance`;
- `anisotropic structure`;
- `feature aggregation`;
- `held-out validation set`;
- `paired effect size`;

over vague expressions such as:

- `better image understanding`;
- `more powerful features`;
- `better learning ability`;
- `stronger results`;
- `good performance`.

---

# 15. Do Not Use Jargon Without Purpose

Technical terminology must improve precision.

Do not use complex terms merely to make the manuscript sound sophisticated.

Every specialized term should correspond to a recognized concept or be clearly defined.

---

# 16. Terminology Consistency

Once a term is selected, use it consistently.

Do not alternate unnecessarily between:

- `proposed model`;
- `proposed framework`;
- `proposed network`;
- `proposed architecture`;
- `proposed approach`;

if all refer to exactly the same object.

Variation for style is less important than scientific consistency.

A limited amount of controlled variation is acceptable when the referent remains unambiguous.

---

# 17. Method Name Consistency

Use the exact method name and acronym throughout the manuscript.

For example:

`Edge-guided Strip-context Global-Attention Network (ESGA-Net)`

After definition, use:

`ESGA-Net`

Do not later introduce variants such as:

`ESGA Net`

`ESGANet`

`ESGA-network`

unless required by a figure or code identifier.

---

# 18. Acronym Discipline

Define non-standard acronyms at first occurrence.

Example:

`structural health monitoring (SHM)`

Use the acronym consistently afterward.

Do not redefine the same acronym in every section unless the target journal requires sections to be independently readable.

Avoid excessive acronym density.

If an acronym appears only once or twice, consider writing the term in full instead.

---

# 19. Avoid Ambiguous Pronouns

Use `it`, `this`, `these`, `they`, and `which` only when the referent is obvious.

Weak:

`This improves the representation.`

Preferred:

`The edge-guided gate improves boundary-selective feature transfer.`

Avoid beginning multiple sentences with `This` when each refers to a different concept.

---

# 20. Control the Word “This”

The construction:

`This + verb`

is often overused in AI-generated prose.

Prefer a specific noun phrase when ambiguity exists.

Weak:

`This indicates that the model is robust.`

Preferred:

`The low seed-to-seed variance indicates stable optimization under the tested protocol.`

---

# 21. Avoid Vague Evaluative Adjectives

Avoid:

- `good`;
- `bad`;
- `strong`;
- `weak`;
- `large`;
- `small`;
- `significant`;

when a more precise description is available.

Preferred:

`The IoU gain is 0.54 percentage points.`

instead of:

`The model achieves a significant improvement.`

Use `statistically significant` only when supported by inferential testing.

---

# 22. Avoid Unnecessary Intensifiers

Minimize words such as:

- `very`;
- `highly`;
- `extremely`;
- `substantially`;
- `significantly`;
- `considerably`;
- `remarkably`;

unless the magnitude is quantified or scientifically justified.

---

# 23. Claim Strength Must Match Evidence

Use claim strength proportional to the evidence.

Possible hierarchy:

`is`
→ direct factual statement.

`shows`
→ observed experimental result.

`indicates`
→ evidence-supported interpretation.

`suggests`
→ cautious interpretation.

`may reflect`
→ plausible but unconfirmed mechanism.

`is consistent with`
→ evidence agrees with a hypothesis but does not establish causality.

Do not use strong causal language when only association or comparative performance has been observed.

---

# 24. Avoid Unsupported Causal Language

Do not write:

`Module A improves IoU because it captures long-range dependencies.`

unless a controlled experiment supports this causal explanation.

Prefer:

`The observed IoU improvement is consistent with the intended role of Module A in capturing long-range dependencies.`

---

# 25. Non-Fabrication Applies Everywhere

Never fabricate scientific information.

This includes:

- citations;
- datasets;
- experimental settings;
- equations;
- results;
- numerical values;
- hyperparameters;
- statistical tests;
- model properties;
- journal rankings;
- prior-study findings.

If information is missing, use a precise placeholder.

---

# 26. Placeholder Rule

Use uppercase square-bracket placeholders for missing scientific information.

Examples:

`[DATASET_NAME]`

`[NUMBER_OF_SEEDS]`

`[IOU_RESULT]`

`[CITATION NEEDED: limited-data crack segmentation]`

`[ABLATION RESULT]`

Use the smallest reasonable placeholder.

Do not invent content to avoid placeholders.

---

# 27. Do Not Overuse Placeholders

Preserve all known information.

Only unresolved information should become a placeholder.

Weak:

`[RESULT PARAGRAPH]`

Preferred:

`ESGA-Net achieves an IoU of [IOU_RESULT] on [DATASET_NAME].`

---

# 28. Avoid Redundant Information

Do not repeat the same scientific point in:

- consecutive sentences;
- neighboring paragraphs;
- text immediately after a table;
- several manuscript sections.

Repetition is acceptable only when the information serves a different purpose.

Example:

- Abstract: concise main result.
- Results: detailed evidence.
- Conclusion: high-level implication.

The wording should not be copied verbatim across sections.

---

# 29. Do Not Narrate Tables

Tables contain detailed numerical information.

The prose should extract:

- main ranking;
- strongest comparison;
- important exception;
- trade-off;
- scientific implication.

Do not reproduce every value from the table.

---

# 30. Do Not Narrate Figures Mechanically

Avoid descriptions such as:

`The blue line increases and the red line decreases.`

Instead explain what the figure reveals scientifically.

---

# 31. Numerical Consistency

Every repeated numerical value must be identical across:

- Abstract;
- Results;
- Conclusion;
- tables;
- figures;
- captions.

If two values conflict, flag the inconsistency.

Do not decide silently which one is correct.

---

# 32. Numerical Precision

Use consistent decimal precision for comparable results.

For example, if IoU is reported to two decimal places, preserve two decimals for all methods in the same table.

Do not imply more precision than the experiment supports.

---

# 33. Percentage Versus Percentage Points

Distinguish carefully.

From 77.33% to 77.87%:

`+0.54 percentage points`

is the absolute difference.

Do not call it:

`+0.54% improvement`

unless relative improvement was calculated.

---

# 34. Mathematical Notation

Follow the project's Equation Skill for all equations.

Scalar, vector, matrix, tensor, index, and set notation must remain consistent throughout the manuscript.

Do not change symbols solely for stylistic variation.

---

# 35. Equation Integration

Equations are part of sentences.

Use correct punctuation before and after displayed equations.

Define new symbols immediately after first use.

Reference equations using the established LaTeX convention.

---

# 36. LaTeX-Aware Prose

When writing LaTeX manuscript text:

Use:

`Section~\ref{...}`

`Table~\ref{...}`

`Fig.~\ref{...}`

`Eq.~\eqref{...}`

according to the manuscript's chosen convention.

Use non-breaking spaces where needed to prevent awkward line breaks.

---

# 37. LaTeX Typography

Preferred forms include:

`30 random seeds`

`48\,GB`

`95\%`

`$512\times512$`

`$3\times10^{-4}$`

Avoid source-code style in prose unless discussing actual code.

---

# 38. Avoid Raw Variable Names in Prose

Prefer:

`Dataset~2`

instead of:

`Dataset_2`

Prefer:

`learning rate`

instead of:

`lr`

unless the variable has been explicitly defined mathematically.

---

# 39. Citation Placement

Place citations where their supporting relationship is clear.

Do not place one citation at the end of a long paragraph containing several unrelated claims.

A reviewer should be able to determine which claim each citation supports.

---

# 40. Citation Clusters

Avoid unnecessarily large citation clusters.

Prefer a small number of highly relevant sources over citation dumping.

When several citations support the same broad statement, order them consistently according to the target journal or bibliography style.

---

# 41. Primary Source Preference

Cite original sources for:

- methods;
- datasets;
- metrics;
- algorithms;
- foundational architectures.

Use review papers for synthesis and broad context.

---

# 42. Recent Literature Preference

For claims about the current state of the field, prioritize recent high-quality literature according to the project's Research and Reference Integrity skills.

Do not force recent citations into statements where a seminal original source is more appropriate.

---

# 43. Avoid Citation Padding

Do not add citations merely to make a paragraph appear academically dense.

Every citation must have a clear evidential purpose.

---

# 44. Do Not Cite Own Results

Do not attach external citations to statements reporting results generated by the current study.

Reference the appropriate table, figure, or section instead.

---

# 45. Avoid Excessive Parentheses

Parentheses should clarify, not interrupt every sentence.

If a sentence contains several parenthetical remarks, rewrite it.

---

# 46. Avoid Excessive Colons and Semicolons

Use punctuation according to syntax, not as a style device.

Do not replace every em dash with a colon or semicolon.

---

# 47. Avoid Slash-Heavy Writing

Prefer:

`training and validation`

over:

`training/validation`

unless the slash expresses a recognized compact relation.

Excessive slash use makes academic prose look compressed and informal.

---

# 48. Avoid Repetitive “and” Chains

Do not create long lists connected entirely by `and`.

Use controlled enumeration or split the sentence.

---

# 49. Avoid Excessive “not only ... but also ...”

This construction is common in formulaic AI writing.

Use it only when the contrast genuinely matters.

Often a direct statement is clearer.

Weak:

`The model not only improves accuracy but also enhances connectivity.`

Preferred:

`The model improves both segmentation accuracy and connectivity.`

---

# 50. Avoid Empty Contrast

Do not use `however`, `although`, or `whereas` unless a real contrast exists.

Weak:

`However, the model also achieves high Recall.`

Preferred:

`Although ESGA-Net ranks second in Precision, it achieves the highest Recall.`

---

# 51. Avoid Excessive Hedging

Scientific caution is necessary, but do not overload sentences with:

`may possibly suggest that...`

Prefer one calibrated hedge.

Example:

`This pattern may reflect the stronger sensitivity of the model to weak crack responses.`

---

# 52. Avoid Excessive Certainty

Do not write:

`clearly proves`

`definitively demonstrates`

`undoubtedly shows`

in ordinary experimental research.

Use evidence-proportional language.

---

# 53. Avoid Anthropomorphic Model Language

Prefer:

`The model identifies...`

`The network assigns...`

`The architecture captures...`

when technically meaningful.

Avoid:

`The model understands...`

`The network knows...`

`The method realizes...`

unless the target discipline commonly uses such terminology in a precise sense.

---

# 54. Avoid Informal First-Person Commentary

Use `we` when appropriate for describing actions:

`We evaluate ESGA-Net on three datasets.`

Avoid conversational first-person statements:

`We can clearly see...`

`We believe...`

`We would like to emphasize...`

Prefer evidence-based formulations.

---

# 55. Active Versus Passive Voice

Use active voice when it improves clarity.

Preferred:

`We evaluate ESGA-Net on three datasets.`

Passive voice is acceptable when the action or process matters more than the actor:

`All models were trained using the same data partition.`

Do not force either voice mechanically.

---

# 56. Avoid “The authors”

When writing the current manuscript, do not refer to the current research team as:

`the authors`

unless required by a journal style.

Use:

`we`

or an impersonal construction.

Use `the authors` only when referring to authors of another study.

---

# 57. Subject–Verb Precision

Technical nouns often create agreement errors.

Check carefully:

- `data are` or journal-preferred usage;
- `results indicate`;
- `model performance is`;
- `metrics are`;
- `number of parameters is`.

Maintain the grammar convention selected by the manuscript.

---

# 58. Comparison Grammar

Use explicit comparison targets.

Weak:

`ESGA-Net performs better.`

Preferred:

`ESGA-Net achieves a higher IoU than Swin-UNet on Dataset~1.`

Do not use comparative adjectives without identifying the reference point.

---

# 59. Parallel Structure

When listing comparable contributions or objectives, maintain grammatical parallelism.

Example:

`to improve boundary localization, preserve connectivity, and reduce computational cost`

not:

`to improve boundary localization, connectivity preservation, and reducing computational cost`.

---

# 60. Lists in Manuscripts

Use lists only when they improve readability, such as:

- contributions;
- objectives;
- algorithm steps.

Do not convert ordinary prose into excessive bullet lists.

---

# 61. Section-Specific Style Has Priority

If a section-specific skill defines a stronger rule, follow it.

Examples:

- Abstract may require 200--250 words.
- Introduction may require literature research.
- Experimental Setup may require exact reproducibility detail.
- Results may require evidence-first interpretation.

`general.md` supplies the common baseline, not a replacement for specialized section skills.

---

# 62. Cross-Section Terminology

The same concepts must use the same names across sections.

Examples:

If Experimental Setup defines:

`held-out validation set`

Results must not call it:

`test set`.

If Methodology defines:

`Global Attention Refinement (GAR)`

Results must not call it:

`global attention module`

when referring specifically to GAR unless the context is unambiguous.

---

# 63. Cross-Section Claim Consistency

Claims made in:

- Abstract;
- Introduction;
- Results;
- Conclusion;

must be mutually consistent.

Do not call a method:

`computationally efficient`

in the Abstract if Results show only moderate efficiency and no supporting comparison.

---

# 64. Cross-Section Numerical Audit

Before finalizing any manuscript section, compare reused values against the source of truth.

Typical high-risk values include:

- number of datasets;
- number of baselines;
- number of seeds;
- learning rate;
- epoch count;
- patience;
- IoU;
- F1;
- clDice;
- model parameters;
- GMACs.

---

# 65. Avoid Duplicating Entire Sentences Across Sections

Do not copy the same sentence verbatim from Abstract to Introduction or Conclusion.

Reformulate according to the role of each section.

The scientific content may recur; the rhetorical function should differ.

---

# 66. Preserve Authorial Style Across Revisions

When revising an existing manuscript, preserve:

- terminology;
- level of technical detail;
- preferred sentence rhythm;
- citation style;
- notation;
- section structure;

unless one of these creates a scientific or grammatical problem.

Do not rewrite the manuscript into a generic assistant voice.

---

# 67. Minimal Necessary Rewriting

When asked to improve an existing section, change only what improves:

- correctness;
- clarity;
- logic;
- academic tone;
- consistency;
- concision.

Do not rewrite satisfactory sentences merely to make them stylistically different.

Unnecessary rewriting increases inconsistency across the manuscript.

---

# 68. Preserve Technical Meaning

Never alter the scientific meaning for stylistic elegance.

If a sentence is awkward but scientifically exact, revise its grammar while preserving the technical claim.

Do not simplify away:

- conditions;
- assumptions;
- metric definitions;
- uncertainty;
- dataset restrictions.

---

# 69. Use Concrete Nouns

Prefer specific nouns over vague placeholders in finished prose.

Weak:

`This method improves the result.`

Preferred:

`The topology-aware objective improves clDice while leaving boundary F1 largely unchanged.`

---

# 70. Avoid Generic Nouns

Minimize vague words such as:

- `aspect`;
- `factor`;
- `thing`;
- `issue`;
- `approach`;
- `performance`;

when a more specific term is available.

---

# 71. Avoid Excessive Nominalization

Do not turn every verb into a noun.

Weak:

`The utilization of the module enables the enhancement of connectivity.`

Preferred:

`The module improves connectivity.`

Use nominalization when it is standard technical terminology.

---

# 72. Prefer Direct Verbs

Prefer:

- `uses`;
- `combines`;
- `measures`;
- `evaluates`;
- `increases`;
- `reduces`;
- `preserves`;
- `captures`;

over unnecessarily inflated alternatives:

- `utilizes`;
- `leverages`;
- `facilitates`;
- `enables the achievement of`;

unless the nuanced meaning is needed.

---

# 73. Limit “Leverage”

The verb `leverage` is heavily overused in AI-generated technical writing.

Prefer:

- `uses`;
- `exploits`;
- `incorporates`;
- `builds on`;

according to the intended meaning.

---

# 74. Limit “Robust”

Do not use `robust` as a generic positive adjective.

Specify the dimension:

- `stable across random seeds`;
- `consistent across datasets`;
- `resistant to noise`;
- `insensitive to initialization`.

Use `robust` only when the relevant robustness has been evaluated.

---

# 75. Limit “Effective”

Do not repeatedly describe the proposed method as:

`effective`.

State the measured advantage instead.

Weak:

`The method is effective for crack segmentation.`

Preferred:

`The method achieves the highest IoU on two datasets and the highest clDice on all three.`

---

# 76. Limit “Efficient”

Use `efficient` only with measurable support such as:

- parameters;
- MACs/FLOPs;
- runtime;
- memory;
- energy.

Always identify the relevant trade-off when necessary.

---

# 77. Avoid “State-of-the-Art” as Filler

Use `state-of-the-art` only when:

- comparison scope is sufficiently broad;
- the claim is current;
- evidence supports it.

Prefer:

`representative recent methods`

when the benchmark does not establish a comprehensive state-of-the-art claim.

---

# 78. Avoid Excessive Superlatives

Use:

`highest`, `lowest`, `best`, `second-best`

only when verified against the complete comparison set being discussed.

Do not use:

`superior`

when the proposed method loses on relevant metrics without qualification.

---

# 79. Time-Sensitive Phrases

Use:

`In recent years`

`Over the past decade`

`Recent advances in`

only when temporally meaningful.

Do not repeat the same opening across multiple manuscripts or sections.

Section-specific skills may define preferred opening strategies.

---

# 80. Avoid Generic Importance Claims

Weak:

`Crack segmentation is an important research topic.`

Preferred:

`Pixel-level crack segmentation supports geometric measurements of crack width, length, and connectivity that cannot be obtained directly from image-level classification.`

Whenever possible, explain **why** something is important.

---

# 81. Explain Technical Relevance

Do not list properties without connecting them to the research problem.

Weak:

`Cracks are thin, elongated, and sparse.`

Preferred:

`Their thin and spatially sparse morphology increases sensitivity to downsampling and class imbalance, while elongated structures require context beyond local receptive fields.`

---

# 82. Avoid Decorative Complexity

Do not make sentences more complex merely to sound academic.

Scientific writing should be sophisticated because the ideas are precise, not because the syntax is ornate.

---

# 83. Avoid Excessive Synonym Substitution

Do not replace the same technical term with several synonyms merely to avoid repetition.

In scientific writing, controlled repetition of exact terminology is often preferable to ambiguity.

For example, repeat:

`crack segmentation`

when necessary rather than alternating with:

`fracture delineation`

`defect parsing`

`surface discontinuity extraction`

unless those terms have distinct meanings.

---

# 84. Repetition Audit

Before finalizing a paragraph, inspect repeated:

- nouns;
- verbs;
- transition phrases;
- sentence openings;
- conclusions.

Revise only repetitions that make the prose mechanical.

Do not remove necessary technical repetition.

---

# 85. Vocabulary Distribution

Avoid overusing common AI-associated academic verbs within a short span:

- `demonstrate`;
- `highlight`;
- `underscore`;
- `showcase`;
- `reveal`;
- `illustrate`.

Prefer the verb that matches the evidence:

- `shows`;
- `indicates`;
- `reports`;
- `measures`;
- `achieves`;
- `increases`;
- `decreases`.

---

# 86. Avoid “Comprehensive” Without Scope

Do not call an evaluation:

`comprehensive`

unless its breadth is explicitly justified.

Prefer:

`an evaluation across three datasets and ten baselines`.

Concrete scope is stronger than an adjective.

---

# 87. Avoid “Novel” Without Need

Do not repeatedly call components:

`novel`.

Describe what is new.

Use `novel` only when novelty has been established by literature research.

---

# 88. Avoid “Unique”

Do not call a design:

`unique`

unless exclusivity has been verified.

Prefer a factual description of the design.

---

# 89. Avoid “First”

Use:

`the first`

only after a dedicated novelty search supports the claim.

Otherwise use narrower formulations such as:

`comparatively few studies have jointly considered...`

---

# 90. Avoid Overclaiming Generalization

Do not infer:

- real-world generalization;
- cross-domain robustness;
- deployment readiness;

from ordinary within-dataset validation.

Use terminology matched to the experimental design.

---

# 91. Avoid Overclaiming Practical Applicability

Do not write:

`ready for real-world deployment`

without evidence from deployment-oriented evaluation.

Prefer:

`the measured throughput suggests that real-time deployment may be feasible under the tested hardware configuration`

when supported.

---

# 92. Failure and Limitation Language

Discuss limitations directly and technically.

Avoid apologetic language.

Preferred:

`Performance decreases in highly textured regions with weak crack contrast.`

not:

`Unfortunately, the model still has some limitations.`

---

# 93. Future Work Language

Future work should follow from identified limitations.

Avoid generic endings such as:

`Future work will explore more advanced deep-learning methods.`

Prefer:

`Future work should evaluate cross-dataset transfer without target-domain fine-tuning and examine whether topology-aware supervision remains beneficial under domain shift.`

---

# 94. No Meta-Writing in Manuscript Prose

Do not write:

`In this paragraph...`

`The following text discusses...`

`As requested...`

`It can be seen that...`

unless required by a specific rhetorical context.

Write the scientific content directly.

---

# 95. No Assistant-Like Commentary

Never include in the manuscript:

- drafting notes;
- apologies;
- suggestions to the user;
- explanations of why wording was selected;
- reminders that information is missing,

except explicit placeholders during drafting.

---

# 96. Remove Mechanical Draft Artifacts

Audit for:

- duplicated words;
- missing spaces;
- accidental concatenation;
- broken LaTeX commands;
- inconsistent capitalization;
- incorrect punctuation;
- copied comments;
- placeholder fragments.

Examples of errors to detect:

`predictedbinary`

`respectively.Topological`

`the$i$th`

`duringi nference`

---

# 97. Journal Style Compliance

When a target journal template or author guide is provided, its rules override general preferences for:

- headings;
- abbreviations;
- figure references;
- citation style;
- table formatting;
- word limits;
- spelling;
- section organization.

Do not impose a generic style over explicit journal requirements.

---

# 98. Manuscript-Wide Consistency Audit

Before finalizing a section, check consistency with the rest of the manuscript for:

- terminology;
- acronyms;
- method names;
- symbols;
- datasets;
- metrics;
- numerical results;
- capitalization;
- citation keys;
- section references.

---

# 99. Final Language Audit

Before returning manuscript text, verify:

- no em dashes;
- no unnecessary AI-like filler;
- no repetitive sentence templates;
- no excessive transition words;
- no vague unsupported adjectives;
- no promotional language;
- no unnecessary synonym substitution;
- no inconsistent terminology;
- no fabricated information;
- no unsupported causal claim;
- no cross-section contradiction.

---

# 100. Core General Writing Rule

Scientific writing should sound like the work of a careful domain researcher, not a generic language generator.

The default writing principle is:

**technical precision + evidence discipline + natural sentence variation + terminology consistency + restrained academic tone**

# CORE RULE

**Write directly, precisely, and in domain-appropriate academic English. Minimize formulaic AI-style phrasing, avoid em dashes, control repetition, preserve terminology and scientific meaning, and never trade evidential accuracy for stylistic fluency.**
