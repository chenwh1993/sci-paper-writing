# Comprehensive Empirical Phrasebank, Verb Precision Matrices & Micro-Scenario Corpus (`n = 1,960` CNS Full Texts, 2020–2026)

> **Purpose**: Eliminate invented phrasing, Chinglish templates, and random verb swapping. Every verb ranking, 4-gram opener, and `[Slot]` sentence frame below is empirically mined from **1,960 full-text CNS & high-impact tumor-omics manuscripts** (`1,464` from 2025–2026 + `496` held-out validation papers from 2020–2024).

---

## Part 1 — Five Precision Verb Confusion Matrices (Choose the Exact Verb Every Time)

Never treat academic verbs as interchangeable synonyms. Match **verb precision** to **experimental truth** (counts = total occurrences across `1,960` CNS Results + Discussion sections):

### 1.1 Evidence & Claim Strength Matrix
| Verb / Phrase | Results Hits | Discussion Hits | Exact Semantic Scope & Permitted Use |
| :--- | :---: | :---: | :--- |
| **`showed`** | `12,476` | `1,588` | Neutral empirical workhorse for any direct experimental/data readout. |
| **`associated with`** | `8,985` | `2,658` | **Mandatory** for clinical/cohort correlations, survival, and non-perturbed omics links. |
| **`revealed`** | `8,241` | `1,233` | Uncovering a previously hidden structure, pattern, niche, or molecular axis. |
| **`confirmed`** | `4,060` | `374` | Orthogonal validation (e.g., mIF/IHC confirming scRNA-seq; independent cohort confirming discovery). |
| **`demonstrated`** | `3,949` | `1,767` | High-confidence functional or multi-assay evidence (genetic/pharmacological perturbation). |
| **`indicated`** | `3,099` | `439` | Moderate-strong logical inference connecting an observation to a mechanistic takeaway. |
| **`correlated with`** | `2,315` | `384` | Quantitative continuous covariance (Pearson/Spearman `r` or `ρ`). |
| **`established`** | `2,166` | `715` | Definitive causal proof (KO + rescue, *in vivo* necessity + sufficiency) or foundational model creation. |
| **`suggested`** | `1,356` | `448` | Cautious inference for trajectory/CellChat predictions, indirect evidence, or Discussion hypotheses. |
| **`supported`** | `822` | `343` | Secondary evidence reinforcing a prior claim or model (`consistent with / supported the notion that`). |
| **`proved`** | `72` *(Avoid!)* | `53` *(Avoid!)* | Virtually taboo in biomedical manuscripts — replace with `demonstrated` or `established`. |

### 1.2 Positive Causation & Activation Matrix
| Verb | Results + Disc Hits | Exact Biological Nuance |
| :--- | :---: | :--- |
| **`induced`** | `7,751` | Directly elicited a downstream state, gene program, or cell death (`RT induced cuproptosis`). |
| **`mediated`** | `5,370` | Acted as the intermediate causal bridge (`CEACAM1 mediated immune evasion through TIM-3`). |
| **`enhanced`** | `4,129` | Elevated an existing biological response or therapeutic efficacy (`enhanced CD8+ T cell infiltration`). |
| **`promoted`** | `831` | Actively pushed progression, differentiation, or tumorigenesis (`promoted bone colonization`). |
| **`amplified`** | `576` | Magnified a signaling cascade or transcriptional program (`further amplified in dual-KO cells`). |
| **`triggered`** | `375` | Initiated an acute cascade or switch (`triggered emergency granulopoiesis`). |
| **`accelerated`** | `317` | Sped up kinetics/time-to-event (`accelerated tumor progression / aging`). |
| **`sensitized`** | `177` | Rendered resistant cells/tumors responsive to a therapy (`sensitized resistant tumors to anti-PD-1`). |
| **`drove`** | `156` | Dominant, primary causal force (reserve for genetic/causal proof: `drove clonal dominance`). |
| **`potentiated` / `boosted`** | `193` | Synergistically strengthened a second agent/immunity (`potentiated ICB efficacy`). |
| **`orchestrated`** | `54` | Coordinated a complex multi-cell or multicellular niche program (`orchestrated myeloid suppression`). |

### 1.3 Negative Causation & Inhibition Matrix (Degree of Effect!)
| Degree | Verbs (Total Hits) | Exact Biological Nuance |
| :--- | :--- | :--- |
| **Complete Elimination (90–100%)** | **`abolished`** (`454`), **`abrogated`** (`408`), **`eliminated`** (`184`) | Use ONLY when genetic KO/blockade completely wipes out the phenotype or rescues it back to baseline. |
| **Direct Pathway / Functional Block** | **`suppressed`** (`1,085`), **`inhibited`** (`1,088`), **`prevented`** (`269`), **`antagonized`** (`10`) | Active suppression of immunity/growth (`suppressed T cell cytotoxicity`), enzymatic/receptor blockade (`inhibited PI3K`), or prophylactic prevention (`prevented metastasis`). |
| **Partial / Graded Reduction** | **`impaired`** (`1,059`), **`attenuated`** (`419`), **`disrupted`** (`291`), **`blunted`** (`82`), **`impeded`** (`61`), **`restrained`** (`39`), **`curtailed`** (`12`) | Partial loss of function (`impaired erythropoiesis`), quantitative dampening (`attenuated/blunted tumor growth`), structural breakdown (`disrupted TLS maturation`), or slowing (`impeded colonization`). |

### 1.4 State-Change, Phenocopy & Rescue Matrix
| Verb (Total Hits) | Exact Usage |
| :--- | :--- |
| **`reversed`** (`578`) / **`restored`** (`479`) / **`rescued`** (`527`) | `reversed` = flipped direction back (`reversed radioresistance`); `restored` = returned a depleted parameter to normal (`restored CD8+ infiltration`); `rescued` = functionally salvaged a defective genetic/survival phenotype (`rescued defective hematopoiesis`). |
| **`recapitulated`** (`394`) / **`mirrored`** (`178`) / **`phenocopied`** (`45`) | `recapitulated` = model/cohort reproduced human/reference biology (`mouse model recapitulated human ccRCC`); `mirrored` = parallel pattern across cohorts/assays; `phenocopied` = drug or second gene KO produced the exact same phenotype as gene A KO (`PI3K inhibition phenocopied CD74 blockade`). |
| **`reprogrammed`** (`201`) / **`polarized`** (`175`) / **`skewed`** (`177`) / **`remodeled`** (`75`) / **`rewired`** (`21`) | `reprogrammed` = durable transcriptional/epigenetic identity shift (macrophages/microglia); `polarized` = directional immune fate; `skewed` = shifted relative cell-state balance (`skewed T cells toward effectors`); `remodeled` = reshaped tissue/ECM/TME architecture; `rewired` = reconnected metabolic/chromatin circuitry. |

### 1.5 Spatial & Compartmental Localization Matrix
| Verb (Total Hits) | Exact Spatial Meaning |
| :--- | :--- |
| **`enriched`** (`9,448`) | Higher relative proportion/abundance in a niche, stage, or cluster. |
| **`restricted`** (`1,048`) / **`confined`** (`187`) | Strictly localized to a specific compartment/boundary (`restricted to hypoxic tumor borders`). |
| **`excluded`** (`624`) | Physically kept out of the tumor core (`CD8+ T cells were spatially excluded from serpin-high niches`). |
| **`infiltrated`** (`440`) / **`accumulated`** (`236`) | Active migration into tumor parenchyma vs progressive local buildup over time. |
| **`colocalized / co-localized`** (`294`) / **`juxtaposed`** (`23`) | Occupying the same micro-region (`colocalized with necrotic zones`) vs direct cell-to-cell adjacency (`juxtaposed with tumor cells at the invasive margin`). |
| **`segregated`** (`170`) | Spatially separated into mutually exclusive tissue domains (`spatially segregated into tumor- and stroma-rich niches`). |

---

## Part 2 — Top Empirically Ranked 4-Gram Discourse Openers (`n = 1,960`)

| Section | Top Authentic CNS Sentence Openers (Empirical Frequency) |
| :--- | :--- |
| **Introduction** | `In this study, we...` (`324`), `Here, we show that...` (`72`), `In this work, we...` (`64`), `In the present study...` (`45`), `To this end, we...` (`35`), `In the context of...` (`28`), `However, the role of...` (`28`), `Here, we report/demonstrate...` (`71`), `We and others have...` (`22`), `To address this [gap/challenge/question], we...` (`79`), `However, it remains unclear...` (`17`), `Here, we sought to...` (`15`), `To overcome these limitations...` (`11`) |
| **Results** | `These results/findings/data suggest that...` (`1,127`), `These results/data/findings indicate that...` (`611`), `Taken together, these data/results/findings...` (`480`), `To this end, we...` (`370`), `We found/observed that the...` (`369`), `To further investigate/explore/validate/characterize/assess...` (`683`), `To test this [hypothesis], we...` (`425`), `We next sought to / investigated / assessed / examined / asked whether...` (`756`), `Together, these data/results/findings suggest/indicate/demonstrate...` (`511`), `In line with this/our/these...` (`415`), `These results/data demonstrate that...` (`195`), `To determine whether the...` (`145`), `We did not observe...` (`111`), `In contrast to the...` (`83`), `Consistent with these findings...` (`69`) |
| **Discussion** | `In this study, we...` (`607`), `These/Our findings/results/data suggest that...` (`391`), `In our/the present/the current study...` (`187`), `In summary/conclusion, our/this study...` (`184`), `Our findings/data/results indicate that...` (`84`), `Here, we show/demonstrate/found that...` (`140`), `In line with this/these...` (`72`), `In the context of...` (`49`), `Our study has several [limitations]...` (`38`), `These findings highlight/underscore the...` (`60`), `In support of this...` (`30`), `In contrast to the...` (`25`), `To our knowledge, this...` (`25`), `Our study demonstrates that...` (`24`) |

---

## Part 3 — Twelve Micro-Scenario Sentence Frame Banks (Ready-to-Migrate Slots + Real CNS Examples)

### Scenario 1 — Introduction Gap Frames
- **Slot 1**: `However, whether and how [process A] controls [cell identity/plasticity/resistance] in human [cancer] remains [poorly understood / to be charted / elusive].`
- **Slot 2**: `Despite significant advances in characterizing [X], the molecular cues within the TME that dictate [Y] remain largely unknown.`
- **Slot 3**: `Although [therapy/profiling] has improved [outcome], clinical benefit remains limited to a small subset of patients, and the mechanisms underlying [resistance] remain unclear.`
- *CNS Verbatim*: `"However, whether and how spatial patterning controls cell identity and plasticity of tumor cells in human cancer remains to be charted."` (*Cancer Cell*, 2025)

### Scenario 2 — Results: Cohort, Omics Profiling & Clustering
- **Slot 1**: `To systematically chart [biological process], we profiled [N] [specimens] from [M] patients using [scRNA-seq and spatial transcriptomics], yielding [K] high-quality cells after quality control (Fig. 1a).`
- **Slot 2**: `Unsupervised clustering and dimensionality reduction segregated [cells] into [k] transcriptionally distinct compartments annotated by canonical lineage markers (Fig. 1b).`
- **Slot 3**: `To validate generalizability, we integrated [N] independent external cohorts spanning [M] patients across [C] cancer types (Extended Data Fig. 1a).`
- *CNS Verbatim*: `"Unsupervised clustering and principal-component analysis (PCA) revealed distinct transcriptional profiles by treatment conditions (Figure S3A)."` (*Cancer Cell*, 2025)

### Scenario 3 — Results: Differential Abundance & Expression
- **Slot 1**: `[Cell subset / Gene X] was markedly enriched/expanded in [condition A] compared with [condition B] ([fold]-fold, P = [val]; Fig. 2a), accompanied by a concomitant decrease in [subset B] (Fig. 2b).`
- **Slot 2**: `[Group A] exhibited significantly elevated levels of [cytokine/metabolite/gene] relative to [Group B] (Fig. 2c).`
- *CNS Verbatim*: `"...significantly enriched in ccRCC (clusters 6, 8, 12, 17, 18, 19, and 22) compared to three in sRCC (clusters 14, 16, and 20; Figures 1E–G and S1B)."` (*Cancer Cell*, 2025)

### Scenario 4 — Results: Pathway Enrichment, GSEA & Transcription Factors
- **Slot 1**: `Gene set enrichment analysis (GSEA) indicated that [group/cluster] was strongly enriched for [pathway A, pathway B] gene programs (NES = [val], FDR = [val]; Fig. 2d).`
- **Slot 2**: `Regulon inference [SCENIC / pySCENIC] identified [TF1] and [TF2] as top candidate transcriptional regulators driving the [state] program (Fig. 2e).`
- *CNS Verbatim*: `"Gene set enrichment analysis (GSEA) indicated that pTR-2 patients in the Nivo+Ipi cohort had an enrichment of effector CD8+ T cell (TEFF) gene programs (Figure 2E)."` (*Cancer Cell*, 2025)

### Scenario 5 — Results: Pseudotime Trajectory, Velocity & Plasticity
- **Slot 1**: `Pseudotime trajectory inference [Slingshot / Monocle] predicted that [cell type] progressed along a continuum from [state A] through [intermediate state] to [terminal state B] (Fig. 3a).`
- **Slot 2**: `RNA velocity and lineage-tracing analyses suggested that [subset B] predominantly arose from [progenitor A] rather than [alternative lineage], mirroring the [clinical/aging] trajectory (Fig. 3b).`
- *CNS Verbatim*: `"RNA velocity analysis suggested this was unlikely, as the C1 and C2 subpopulations displayed distinct differentiation trajectories with separate origins (Fig. 2D)."` (*Cancer Cell*, 2025)

### Scenario 6 — Results: Spatial Architecture, Niches & Cell–Cell Crosstalk
- **Slot 1**: `Cellular neighborhood (CN) analysis based on the [k] nearest spatial neighbors partitioned tissues into [m] recurrent spatial niches, including [vasculature-, lymphocyte-, stroma-, and tumor-enriched] domains (Fig. 4a).`
- **Slot 2**: `[Cell A] was preferentially localized at the invasive margin (defined as [35–50] μm inside and outside the tumor border) and spatially segregated from [Cell B] (Fig. 4b).`
- **Slot 3**: `Ligand–receptor communication analysis [CellChat / CellPhoneDB / NicheNet] predicted enhanced [Ligand–Receptor] signaling between [Sender] and [Receiver] within [Niche X], which we orthogonally confirmed by multiplex immunofluorescence (Fig. 4c,d).`
- *CNS Verbatim*: `"...cellular neighborhoods (CNs) based on the ten nearest spatial neighbors for each cell (Figure 2B) to further depict the multicellular TME architecture of LUAD precursors."` (*Cancer Cell*, 2025)

### Scenario 7 — Results: Genetic / Pharmacological Perturbation, Rescue & Synergy
- **Slot 1**: `To test whether [X] is causally required for [Y] in vivo, we generated [conditional knockout / CRISPR-KO] models (Fig. 5a). Genetic ablation of [X] markedly impaired [tumor growth / metastasis] and restored [CD8+ T cell infiltration] (Fig. 5b,c).`
- **Slot 2**: `Pharmacological blockade of [target] phenocopied genetic deletion of [X] and synergized with anti-PD-1 therapy to extend survival without overt toxicity (Fig. 5d,e).`
- **Slot 3**: `Conversely, [ectopic expression / agonist treatment] reversed [phenotype], demonstrating that [X] is both necessary and sufficient to drive [Y] (Fig. 5f).`
- *CNS Verbatim*: `"Depletion of MT1E or MT1X in radioresistant cells restored intracellular copper levels and decreased the levels of protein lipoylation and Fe-S cluster proteins (Fig. 5C)."` (*Cancer Cell*, 2025)

### Scenario 8 — Results: Clinical Prognosis, Multivariable Cox & Predictive Models
- **Slot 1**: `High [signature / cell-state abundance] was significantly associated with shortened [overall / progression-free] survival across [N] independent patient cohorts (HR = [val], 95% CI [low–high], P = [val]; Fig. 6a).`
- **Slot 2**: `Multivariable Cox regression confirmed that [signature] retained independent prognostic value after adjusting for age, stage, and treatment regimen (Fig. 6b).`
- **Slot 3**: `In external validation cohorts, [ModelName] outperformed established [PD-L1 / TMB / single-modality] benchmarks in predicting [response] (AUC = [val] vs [val], P = [val]; Fig. 6c).`
- *CNS Verbatim*: `"Multivariable Cox regression further supported the signature as an independent predictor of both DFS (P = 0.002) and OS."` (*Cancer Cell*, 2026)

### Scenario 9 — Results: Negative Controls, Null Differences & Contrast Clauses
- **Slot 1**: `[Intervention] did not significantly alter [baseline cell number / body weight / short-term viability] (P = [val]; Extended Data Fig. X), excluding the possibility that [observed effect] was secondary to [confounder].`
- **Slot 2**: `In contrast to [Group A], [Group B] exhibited no significant change in [metric], indicating that [effect] is specific to [context].`
- *CNS Verbatim*: `"...did not affect MSM numbers, confirming changes in phagocytosis were not due to MSM reduction (Fig. S1D)."` (*Cancer Cell*, 2025)

### Scenario 10 — Discussion: Literature Concordance & Paradox Reconciliation
- **Slot 1 (Concordance)**: `Consistent with prior clinical reports in [cancer B] showing that [X], our data reveal that [Y] extends across [cohort].`
- **Slot 2 (Contrast & Synthesis)**: `Unlike previous studies that classified [cell type] solely by bulk transcriptomics, our spatially resolved profiling demonstrates that [niche context] dictates [functional polarity].`
- **Slot 3 (Paradox Resolution)**: `At first glance, [Finding A] appears paradoxical alongside [Prior Finding B]. This discrepancy may be reconciled by a context-dependent dual role across [disease stage / anatomical compartment / treatment timing].`
- *CNS Verbatim*: `"Unlike previous studies that classified CAF subtypes based on transcriptomic or biomarker data, this approach does not rely on the expression of specific marker genes or proteins."` (*Cancer Cell*, 2025)

### Scenario 11 — Discussion: Calibrated Speculation & Hypothesis Hedging
- **Slot 1**: `These findings raise the intriguing possibility that [upstream cue] epigenetically pre-conditions [cell type] prior to tissue infiltration.`
- **Slot 2**: `This pattern may reflect [mechanism A] rather than [alternative explanation B]; we speculate that [testable hypothesis] governs this switch.`
- *CNS Verbatim*: `"This may reflect limited recruitment or retention within this compartment, rather than active exclusion at the junction itself."` (*Cancer Cell*, 2026)

### Scenario 12 — Discussion: Constructive 3-Part Limitations (`Boundary → Mitigation → Next Step`)
- **Slot 1**: `Our study has several limitations that should be considered when interpreting these findings. First, [scope boundary: e.g., cohort size / retrospective design / targeted spatial panel]; we addressed this limitation by [validation across external multi-center cohorts / orthogonal scRNA-seq].`
- **Slot 2**: `Second, while our preclinical models establish causal necessity for [X], future studies employing [genetic lineage tracing / prospective trials with paired on-treatment biopsies] will be essential to definitively validate [mechanism/translation] in patients.`
- *CNS Verbatim*: `"Future studies employing robust genetic lineage tracing systems, potentially utilizing split-Cre technology, will be essential to definitively validate F-apCAF developmental trajectories and function."` (*Cancer Cell*, 2025)

---

## Part 4 — Anti-AI → Authentic Human CNS Replacement Corpus (`Scenarios 13–18`, Distilled from `550` Flagship 2025–2026 CNS Papers)

> **Median-Bullseye Rule**: Do **NOT** merely aim to slip inside the "safe ceiling" (`65%` grounding or `CV = 0.38` or `5 P/1kw`). Actively use the verbatim human CNS frames, short burstiness sentences, high-grounding Discussion openers, and compound-stack unpackings below to land squarely around the **real human CNS median** (`76.0%` 2-gram grounding, `46.5%` 3-gram grounding, `73.8%` opener grounding, `CV = 0.49` with `23.1% <= 18w` sentences, `0.6 P/1kw` in Results, `0` alien words or invented hyphen stacks).

### Scenario 13 — Crisp Short Human Burstiness Sentences (`8–17w`, Driving `CV` to the `0.45–0.55` Human Median)
LLMs flatten every Results sentence to `25–30` words (`CV ≈ 0.32`), creating an unmistakable "metronome cadence." Real CNS authors interleave **1 punchy `8–17w` sentence every 3–4 sentences** (targeting **`20–28% <= 18w`**) to establish topic shifts, crisp empirical readouts, or decisive null controls:
- **Slot 1 (Crisp Discovery)**: `We identified a subpopulation of [cells] that was transcriptionally distinct from [control cells] (Fig. Xa).`
- **Slot 2 (Crisp Perturbation Readout)**: `[Drug / Deletion] impaired tumour growth but did not induce complete regression (Fig. Xb).`
- **Slot 3 (Crisp Negative Control)**: `The frequency of [other immune subsets], including [cell B], did not change (Extended Data Fig. Xc).`
- **Slot 4 (Crisp Confirmation)**: `First, we confirmed that [model/cells] expressed [Marker A] but lacked [Marker B] (Fig. Xd).`
- **Slot 5 (Crisp Contrast)**: `Unlike [Model A], [Model B] did not exhibit improved response to combined therapy (Fig. Xe).`
- *CNS Verbatim (`10–17w`, 2025–2026 Flagship Papers)*:
  - `"We identified a subpopulation of LPT-MET fibroblasts that were transcriptionally distinct from LPT-WT fibroblasts (Fig. 4a)."` (*Nat Cell Biol*, 2025 — `16w`)
  - `"The frequency of other resident macrophages, including alveolar macrophages, did not change (Figure S5F)."` (*Cell*, 2025 — `14w`)
  - `"Paclitaxel hampered tumor growth, but did not lead to any complete tumor regression (Fig. 1A)."` (*Immunity*, 2025 — `15w`)
  - `"First, we confirmed that CP-A cells expressed TP53 but did not express CDKN2A (Fig. 2d)."` (*Nat Cancer*, 2025 — `15w`)
  - `"Unlike 2208L, EMT6 did not exhibit improved response to the combined therapy (Fig. 1B)."` (*Immunity*, 2025 — `14w`)
  - `"Finally, we confirmed that NRG1 treatment triggered downstream signaling pathways, including AKT, MAPK and FAK (Fig. 1j)."` (*Nat Cancer*, 2025 — `17w`)

### Scenario 14 — Spatial Niches, Distance Gradients & Unsupervised Clustering (Replacing Tech-Blog Metaphors)
Replace AI metaphors (`locked atlas`, `habitats`, `portals`, `cleanly`, `cross-cohort robustness`, `target-to-vascular geometry`) with plain spatial-biology CNS phrasing:
- **Slot 1 (Adjacency & Proportion)**: `In [tumour] sections, [Cell A] localized predominantly adjacent to [Cell B], with [X]% of their nearest neighbours being [Cell B] (Fig. Xa,b).`
- **Slot 2 (Niche Organization)**: `These results reveal a conserved spatial organization of [Cell A] within [perivascular / stromal / invasive-margin] niches across [human and mouse] tumours (Fig. Xc).`
- **Slot 3 (Barrier / Gradient)**: `We next investigated whether the boundary formed by [Cell A] acts as a physical barrier that restricts [Cell B] infiltration into the tumour core (Fig. Xd).`
- **Slot 4 (Orthogonal Multiplex Confirmation)**: `This spatial proximity was confirmed by multiplexed immunofluorescence imaging, which identified [Cell A] in the direct cellular neighbourhood of [Cell B] (Fig. Xe).`
- *CNS Verbatim (2025–2026 Flagship Papers)*:
  - `"These results reveal a conserved spatial organization of CCR7+ DCs in perivascular and lymphatic niches in both human and mouse tumors."` (*Immunity*, 2025)
  - `"We then investigated whether the boundary formed by eFibro_CTHRC1 could serve as a physical barrier that may affect the infiltration of immune cells into the tumor core."` (*Nat Cancer*, 2025)
  - `"No significant correlations were observed in the inner tumor-invasive margin and the central tumor regions (Figure S3C)."` (*Cancer Cell*, 2025)
  - `"This was confirmed by multiplexed immunofluorescence imaging using codetection by indexing (CODEX), which identified IFNG-producing T cells in the direct cellular neighborhood to small DCC clusters and micrometastases (Fig. 4e)."` (*Nat Cancer*, 2025)
  - `"Single disseminated cells localized to interstitial and luminal sites in the lungs (Extended Data Fig. 1d) and in perivascular niches in the brain parenchyma (Fig. 1a)."` (*Nat Cancer*, 2025)

### Scenario 15 — Prognostic Models, Cross-Validation & Independent External Validation
Replace Kaggle/ML-blog wording (`quarantined cohort`, `out-of-fold`, `parsimonious`, `upgraded stratification`, `two-feature composite`, `outcome-blind`) with plain clinical-genomics CNS prose:
- **Slot 1 (Cross-Validation & Feature Selection)**: `We trained [classifier/regression] models using repeated cross-validation to minimize overfitting and evaluate predictive performance across cohorts (Fig. Xa).`
- **Slot 2 (Independent Validation Cohort)**: `To validate [Signature/Model] in an independent patient cohort, we evaluated [N] tumours from [M] patients without overlap with the discovery set (Fig. Xb).`
- **Slot 3 (Multivariable Confounder Control)**: `To account for potential clinical confounders, we included [stage, age, sex, and baseline marker] in a multivariable analysis of [DFS/OS] (Fig. Xc).`
- **Slot 4 (Treatment-Specific vs Prognostic Distinction)**: `To distinguish prognostic from treatment-specific predictive effects, we evaluated [biomarker] in relation to outcomes in the [control/monotherapy] arm (Fig. Xd).`
- *CNS Verbatim (2025–2026 Flagship Papers)*:
  - `"We constructed subtype-balanced repeated cross-validation folds for all cohorts, and set these as training and test sets (Figure 2A)."` (*Cancer Cell*, 2025)
  - `"For the validation of ORACLE in an independent patient cohort, we exclude patients profiled in our previous study to yield the TRACERx validation cohort, consisting of 369 tumor regions from 158 patients."` (*Nat Cancer*, 2025)
  - `"To account for any confounding effect, we included ITH, age, sex, race, IMDC risk score, and CNL in our multivariable analysis."` (*Nat Cancer*, 2025)
  - `"To account for possible bias and distinguish between prognostic and predictive factors, we also studied tumor-intrinsic biomarkers in relation to response to tyrosine kinase inhibitor (TKI) monotherapy in the control arm of these trials."` (*Nat Cancer*, 2025)
  - `"Samples are stratified by American Joint Committee on Cancer (AJCC) 8th edition pathological stage (stage I, n = 23; stage III–IV, n = 163)."` (*Nat Cell Biol*, 2025)

### Scenario 16 — Computational Pathology, H&E Histology & Multimodal Integration
Replace AI hype/metaphors (`honest optical blind spot`, `decodes macro-architectural`, `capitalising on division of labour`, `unanchored end-to-end`, `crosswalk`) with restrained, concrete CNS phrasing:
- **Slot 1 (Histology Limitation — Plain & Factual)**: `Haematoxylin and eosin (H&E) staining alone was not sufficient to distinguish [state A from state B], as [molecular feature] is not clearly visible morphologically (Extended Data Fig. Xa).`
- **Slot 2 (Multimodal Integration)**: `We integrated [spatial transcriptomics / multiplex imaging] with routine H&E histology to jointly capture [macroscopic tissue architecture] and [molecular states] (Fig. Xb).`
- **Slot 3 (Unimodal vs Multimodal Comparison)**: `Using cross-validation with both [imaging] and [molecular] features, we compared combined multimodal models against each unimodal baseline (Fig. Xc).`
- **Slot 4 (Deep-Learning Mapping)**: `We next applied [ToolName], a deep-learning framework, to map [modality A] profiles onto matched [modality B] slides and infer [cellular composition / score] (Fig. Xd).`
- *CNS Verbatim (2025–2026 Flagship Papers)*:
  - `"Hematoxylin and eosin (H&E) staining is not sufficient to identify CRATERs, as the gap is not clearly visible (Figure S5J)."` (*Cell*, 2025)
  - `"Using cross-validation with both MIBI and RNA features, we found that multimodal models did not outperform unimodal ones; in fact, combined models showed reduced performance (Extended Data Fig. 9i)."` (*Nat Cancer*, 2025)
  - `"Next, we used Tangram, a deep learning framework, to map tumor-matched scRNA-seq profiles to the corresponding ST data and generate a probabilistic measure of the cellular composition for each spatial measurement (Fig. 1g)."` (*Nat Cancer*, 2025)
  - `"Histological analysis of haematoxylin and eosin (H&E)-stained tumour sections confirmed larger tumour sizes in the HOXB3-WT group compared with the notably smaller tumours in the SN5I group (Fig. 8d)."` (*Nat Cell Biol*, 2025)
  - `"Pathological response rates were assessed according to microscopic examination of H&E slides of the resected tumor as part of routine clinical practice (Figures 1A and S1A–S1C; STAR Methods)."` (*Cell*, 2025)

### Scenario 17 — Clean `P4` Specificity, Confounder Exclusion & Stat-Light Results (`Median 0.6 P/1kw`)
Never write defensive audit prose (`without outcome-label leakage`, `guarding against batch`, `adversarial removal`) or inline `P`-value dumps. State the biological independence cleanly and anchor exact `P`/`n` on the figure with *Nature* parenthetical semicolon syntax `(n = X; Fig. Ya)`:
- **Slot 1 (Independence From Confounder)**: `These observations were independent of [tumour viability / baseline expression / clinical stage], which were unaffected by [perturbation / cohort strata] (Extended Data Fig. Xa).`
- **Slot 2 (Ruling Out Alternative Mechanism)**: `[Treatment/Perturbation] did not alter [cell counts / baseline proliferation], confirming that changes in [phenotype] were not due to [confounder] (Extended Data Fig. Xb).`
- **Slot 3 (Stat-Light Magnitude + Clean Nature Semicolon)**: `[Blockade/Regimen] markedly reduced [endpoint] by [X]% (n = [M]; Fig. Xc) and prolonged survival (Fig. Xd).`
- **Slot 4 (Consistent Across Subgroups)**: `[Effect] persisted across [both cohorts / all genotypes], regardless of [mutation status / prior regimen] (Extended Data Fig. Xe).`
- *CNS Verbatim (2025–2026 Flagship Papers)*:
  - `"These observations are independent of tumour cell viability, initial drug response or persister cell formation, which were each found to be unaffected by DFFB deficiency (Extended Data Fig. 4)."` (*Nat Cell Biol*, 2025)
  - `"Chemotherapy did not affect MSM numbers, confirming changes in phagocytosis were not due to MSM reduction (Fig S1D)."` (*Cancer Cell*, 2025)
  - `"CCR7 levels remain unchanged (Figure S7E), suggesting that CCR7 expression is independent of other DC activation markers."` (*Immunity*, 2025)
  - `"Strikingly, b2 blockade also significantly reduced metastatic burden by 50%, measured as number and size of lung nodules (Figures 3L and 3M), and prolonged mouse survival (Figure 3N)."` (*Cell*, 2025)
  - `"In accordance with these findings, FLASH RT enhanced the infiltration of CD3+ T cells into the tumors (Fig. 1l)."` (*Nat Cancer*, 2025)
  - `"In agreement with previous studies29,32,41, CDKN2A was the second most frequently damaged EAC driver, with LoF in 25% of samples (Fig. 1b)."` (*Nat Cancer*, 2025)

### Scenario 18 — High-Grounding Human Discussion Openers (`550` Flagship Papers) & Hyphen-Stack Unpacking Bank

#### 18.1 Top 20 Real Human Discussion 3-Word Openers (Raises Discussion Opener Grounding From `~35%` to the `74%` Human Median!)
| Rank | Authentic Flagship Discussion Opener (`n = 550` Papers) | Hits | Best Discussion Function |
| :---: | :--- | :---: | :--- |
| 1 | **`In this study, we...`** | `121` | P1 conceptual summary |
| 2 | **`We found that...`** / **`We show that...`** / **`We demonstrate that...`** | `132` | Core takeaway & synthesis |
| 3 | **`In addition to...`** | `53` | Extending to a second axis/cohort |
| 4 | **`Consistent with this, ...`** / **`This is consistent with...`** | `64` | Literature concordance |
| 5 | **`In our study, ...`** | `40` | Anchoring scope or cohort design |
| 6 | **`In line with...`** | `40` | Reconciling with prior reports |
| 7 | **`This suggests that...`** / **`These findings suggest...`** | `76` | Mechanistic interpretation |
| 8 | **`In summary, our/we...`** / **`In conclusion, our...`** | `100` | Closing synthesis paragraph |
| 9 | **`Together, these findings...`** | `27` | Multi-evidence convergence |
| 10 | **`Our data suggest/indicate...`** / **`Our findings suggest...`** | `60` | Calibrated inference |
| 11 | **`Future studies should...`** / **`Future work will...`** | `23+` | Constructive limitations & roadmap |
| 12 | **`Previous studies have...`** / **`A recent study...`** | `42` | Setting up literature contrast |
| 13 | **`These findings highlight...`** | `20` | Broader conceptual significance |
| 14 | **`However, it is...`** / **`It is important...`** | `38` | Nuance, caveat, or clinical context |
| 15 | **`In contrast to...`** | `18` | Sharp paradigm contrast (`X, rather than Y`) |
| 16 | **`We speculate that...`** / **`This may be...`** | `36` | Explicit calibrated speculation |

- *CNS Verbatim Discussion Sentences (2025–2026 Flagship Papers)*:
  - `"In this study, we identified GUK1 activation as a metabolic liability in oncogene-driven lung cancers."` (*Cell*, 2025 — crisp `15w` P1 opener!)
  - `"Consistent with our findings, a recent report showed that FLASH RT increases antitumor Mϕs and reduces protumor Mϕs in lung cancer."` (*Nat Cancer*, 2025)
  - `"In line with this, AML cells and HSCs under other pathological conditions such as BM failure have been shown to be particularly sensitive to ferroptosis induction."` (*Nat Cell Biol*, 2025)
  - `"We have shown that, rather than recruiting monocytes, tumor cells induce expansion of resident IMs in the lung PTN, reprogramming them toward a CD163+/CD206+ M2-like phenotype."` (*Cell*, 2025)
  - `"A key limitation of our method is the focus on a targeted set of genes for transcriptomic readout, which limits the potential for de novo discovery."` (*Cell*, 2025)
  - `"Although this study integrates data for 42 RCC tumor samples across three independent cohorts, dataset size remains a notable limitation."` (*Immunity*, 2025)

#### 18.2 Compound Hyphen-Stack Unpacking Dictionary (3-Part & AI-Tell 2-Part Pre-Modifiers → Plain CNS Prepositional English)
Invented compound stacks drop de-lexicalized 2-gram grounding by `~25%` because real human CNS writers unpack them into natural nouns + prepositions (`of`, `by`, `for`, `across`, `within`):

| AI-Tell Compound Modifier Stack (`~0%` in `1,312` CNS Papers) | Authentic Human CNS Replacement |
| :--- | :--- |
| `marker-stability-tiered spatial features` | `spatial features filtered for staining stability` |
| `copy-number-confirmed malignant cells` | `malignant cells confirmed by copy-number inference` |
| `outcome-blind tile-level scores` | `unsupervised tile-level scores` *(or `scores derived without clinical labels`)* |
| `out-of-fold predictions` / `out-of-fold AUC` | `cross-validated predictions` / `cross-validated AUC` |
| `leave-one-patient-out validation` | `leave-one-patient-out cross-validation` *(define once in Methods; write `cross-validation` in Results)* |
| `cross-regimen signed-Z synthesis` | `meta-analysis across independent treatment regimens` |
| `target-to-vascular geometry` | `spatial proximity between target-expressing cells and vessels` |
| `two-feature composite` / `three-feature model` | `a two-feature spatial score` / `a model combining [Feature A] and [Feature B]` |
| `same-section histology` / `same-section mIHC` | `matched H&E sections` / `serial sections` / `within the same tissue section` |
| `single-marker quantification` / `single-metric scoring` | `quantification of [Marker] alone` / `conventional single-marker scoring` |
| `batch-matched controls` / `within-batch normalization` | `controls matched for batch` / `normalization within each batch` |
| `multi-compartment atlas` | `atlas spanning epithelial, stromal and immune compartments` |
| `macro-architectural features` | `macroscopic tissue architecture` / `histological architecture` |
| `ambient-RNA-filtered` / `ambient-RNA contamination` | `after removing ambient RNA` / `ambient RNA contamination` *(no hyphen as noun!)* |
| `zero-shot foundation-model embeddings` | `pretrained pathology foundation model embeddings` |
| `per-slide summary` / `per-patient median` | `slide-level summary` / `patient-level median` |
| `dendritic-cell infiltration` / `bladder-wall invasion` | `dendritic cell infiltration` / `bladder wall invasion` *(unhyphenated noun adjuncts!)* |
| `dose-dense regimen` / `treatment-specific interaction` | `standard chemotherapy` / `biomarker-by-treatment interaction` |
| `strictly quarantined validation cohort` | `independent external validation cohort` |
| `honest optical blind spot` | `limited ability of H&E morphology alone to resolve [X]` |
| `capitalising on this division of labour` | `combining these complementary modalities` |
| `upgraded clinical stratification` | `improved clinical stratification` / `enhanced risk stratification` |
