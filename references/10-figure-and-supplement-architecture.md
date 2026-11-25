# Figure & Subpanel Distribution and Main-vs-Supplement Content Architecture (`n = 1,215` CNS Manuscripts)

Empirically distilled from **1,215** high-impact tumor-omics manuscripts (2023–2026, spanning 22 journals), **50,030** Main-Figure-only vs **22,709** Supplement/Extended-Data-only Results sentences, and **3,965** Main vs **2,771** Extended Data full captions.

---

## 1. Journal-Specific Main Figure, Extended Data / Supp Figure & Subpanel Budgets

### 1.1 Overall High-IF Benchmarks
- **Main Figures / paper**: **`5–7`** (strictly journal-dependent: *Nature/Nat Med* = **`5`**, *Science/Nat Methods/Nat Genet* = **`6`**, *Cell/Cancer Cell/Immunity/Nat Cancer/Nat Immunol/Nat Commun* = **`7`**).
- **Panels per Main Figure**: Median **`8` panels** (IQR **`6–11`**, P10–P90 `4–14` — typically `a–h` / `A–I`). Total main panels per paper: **~40–63 panels**.
- **Extended Data / Supplementary Figures / paper**: Median **`7–10`** peer-reviewed ED/S-Figs (Cell Press strictly enforces **1:1 pairing `Fig. 1–7 ↔ Fig. S1–S7`**; Nature Portfolio allows up to **`10` Extended Data Figs** plus additional Supplementary Figs).
- **Panels per Extended Data / Supp Figure**: Median **`6–8` panels** (IQR `4–11`; full-page ED/Cell S-Figs hold **`8` panels**!).

### 1.2 Exact 20-Journal Budget Matrix (Verified 2023–2026)

| Target Journal | Main Figs Median (IQR) | Extended Data Figs (IQR) | Supplementary Figs (IQR) | Panels / Main Fig | Panels / Supp/ED Fig | Architectural Signature |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Nature** | **`5`** (`5–5`, P10–P90 `4–5`) | **`9`** (`8–10`, cap `10`) | `3` (`2–9`) | **`8`** | **`8`** | Ultra-tight 4–5 Main Figs + heavy peer-reviewed Extended Data (`8–10` full plates) |
| **Nat Med** | **`5`** (`4–6`) | **`7`** (`6–10`, cap `10`) | `9.5` (`5–17`) | **`6`** | **`5`** | Cleaner clinical curves/swimmer plots in 5 Main Figs; deep trial safety/subgroups in ED+Supp |
| **Science** | **`6`** (`5–6`) | — | **`13`** (`9–14`) | **`10`** | **`6`** | Dense 10-panel Main Figs + large Supplementary PDF |
| **Cell / Cancer Cell / Immunity / Mol Cell** | **`7`** (`6–7`; *Immunity* `7–7`) | — | **`7`** (`7–8`, **exact 1:1**) | **`9–10`** | **`8`** | **Strict 1:1 pairing** (`Fig. 1 ↔ Fig. S1` ... `Fig. 7 ↔ Fig. S7`, same `8–9` panel density!) |
| **Nat Cancer / Nat Immunol / Nat Cell Biol** | **`7`** (`6–7`) | **`8–9`** (`6–10`) | `1–6` | **`8–10`** | **`6–8`** | 6–7 Main Figs backed by 8–9 Extended Data plates |
| **Nat Genet / Nat Methods / Nat Biotechnol** | **`6`** (`5–6`) | **`8–9`** (`5–10`) | `3–12.5` | **`7–9`** | **`5–6`** | 6 Main Figs; *Nat Methods/Biotechnol* offload extensive benchmarks/ablations to `11–12` Supp Figs |
| **Nat Commun** | **`7`** (`6–8`) | — | **`12`** (`7–20`) | **`8`** | **`5`** | 6–8 Main Figs + generous Supplementary Info (`12+` Figs) |
| **Cell Rep Med** | **`6.5`** (`6–7`) | — | **`7`** (`6–11`) | **`8`** | **`6`** | Cell Press 1:1 style (`6–7` Main + `7` S-Figs) |
| **Sci Adv / Sci Transl Med / Sci Immunol** | **`6–7`** (`5–7`) | — | **`7–10`** (`4–15`) | **`7–9`** | **`4–5`** | 6–7 Main Figs + `7–10` focused Supp Figs |
| **Cancer Discov / Cancer Res / J Clin Invest** | **`6–7`** (`6–7`) | — | **`8–10.5`** (`7–19`) | **`8–9`** | **`4–6`** | Classic 6–7 oncology Main Figs + `8–11` Supp Figs |
| **Clin Cancer Res** | **`5`** (`4–6`) | — | **`7`** (`6–14`) | **`5`** | **`3`** | Compact clinical-translational layout (`5` Main × `5` panels) |

---

## 2. What Goes into Main Figures vs Extended Data / Supplementary Figures? (Empirical Decision Matrix)

Derived from **`50,030`** Main-only vs **`22,709`** Supp-only Results sentences AND **`3,965`** Main vs **`2,771`** Extended Data captions:

> **The 3-Second Triage Law**:
> - **MAIN Figure** = Any panel whose removal **breaks the core logical causal chain** (the headline discovery, schematic/working model, representative spatial/mIF proof, decisive *in vivo* KO/rescue, or primary clinical validation).
> - **EXTENDED DATA / SUPPLEMENTARY Figure** = Any panel that answers a **reviewer's rigor, QC, control, validation-repeat, or granular breakdown question** without advancing a brand-new plot twist.

| Content Category | Empirical Signal (Main vs Supp/ED) | Verdict | Exact Split Rule (What Stays in Main vs Moves to Supp/ED) |
| :--- | :--- | :---: | :--- |
| **1. Study Design Schematic & Final Working Model** | **`7.44×`** in text / **`2.23×`** in caps (`35.8%` Main vs `16.0%` ED) | **MUST BE MAIN** | Put cohort/experiment workflow in **`Fig. 1a`** and final mechanistic synthesis diagram in the **last panel of final Main Fig** (or Cell Graphical Abstract). |
| **2. Decisive *In Vivo* Efficacy, KO/Depletion Rescue & ICB Synergy** | **`1.69×`** in caps (`20.8%` vs `12.3%`) / **`1.27×`** in text | **STRONG MAIN** | Put primary tumor growth curves, endpoint burden, survival, and anti-PD-1 synergy in **Main (`Fig. 5–7`)**; put secondary mouse models, dosing pilot curves, and individual spider plots in **Supp/ED**. |
| **3. Core Single-Cell / Spatial Discovery UMAP & Cell-State Shift** | **`1.59×`** in text / **`1.19×`** in caps (`24.1%` Main) | **STRONG MAIN** | Put the headline atlas UMAP + key compositional shift bar/boxplot in **Main (`Fig. 1–2`)**; put UMAP split by sample/batch/donor and secondary subclusters in **Supp/ED**. |
| **4. Headline Cell–Cell Communication / Niche Hub** | **`1.67×`** in caps (`1.19×` in text) | **MAIN (Headline)** | Put the focal ligand–receptor circuit/circle or niche heatmap in **Main**; put full all-pair CellChat/CellPhoneDB interaction matrices in **Supp/ED**. |
| **5. Clinical Survival (KM), Multivariable Cox & Predictive ROC/AUC** | **`1.41×`** in caps (`17.8%` vs `12.6%`) | **MAIN (Primary)** | Put primary discovery + lead external validation KM/AUC/forest plot in **Main (`Fig. 6–7`)**; put extra validation cohorts, cutoff sensitivity, and sex/stage subgroup KMs in **Supp/ED**. |
| **6. Spatial Map, Multiplex IF / IHC / CODEX Histology** | **`1.24×`** in text / **`1.22×`** in caps | **DUAL (Split!)** | Put **1 representative high-impact ROI + cohort quantification** in **Main**; put uncropped fields, single-channel grayscale splits, antibody controls, and extra patient slides in **Supp/ED**. |
| **7. Pathway / GSEA / TF Regulon & Trajectory / CNV** | **`1.41×`** (Pathway) / `0.94–1.14×` (Trajectory) | **DUAL (Curated)** | Keep ONLY the **1–2 causal pathways / key trajectories** in **Main**; move exhaustive GO/KEGG tables, alternate trajectory tools (Slingshot vs Monocle), and per-sample inferCNV heatmaps to **Supp/ED**. |
| **8. Exhaustive Marker-Gene Annotation Dotplots / FeaturePlots** | **`0.96×`** in caps (nearly 1:1 ED vs Main) | **MOSTLY SUPP/ED** | Keep a **compact 3–6 key-marker feature/dotplot** in Main only when defining a novel cell state; move the full 30-gene lineage annotation dotplot & top-DEG heatmap to **`Fig. S1 / ED Fig. 1–2`**. |
| **9. Method Benchmarks, Hyperparameter Ablations & Runtime** | **`0.88×`** in caps (for biology papers) | **SUPP/ED** *(Main only in *Nat Methods*)* | In biological papers, move clustering resolution sweeps, integration benchmarks, and tool comparisons to **Supp/ED**. In *Nat Methods*, lead benchmark goes to Main; stress tests & ablations go to Supp. |
| **10. Per-Patient / Per-Sex / Per-Cancer Subgroup Breakdowns** | `1.06×` caps (space-heavy) | **SUPP/ED** | Move individual donor stacked bars, patient-level heatmaps, replicate correlation scatters, and clinical covariate tables to **Supp/ED**. |
| **11. scRNA-seq / Spatial QC, Filtering, Batch & Depth Metrics** | **`0.55×` (`1.82×` enriched in ED caps!)** | **STRICTLY SUPP/ED** | **NEVER put QC violin plots (nFeature, nCount, %MT), doublet rates, Harmony pre/post-integration UMAPs, or sequencing depth in Main Figures!** Always `ED Fig. 1–2` / `Fig. S1`. |
| **12. Negative Controls, Vehicle/Isotype & Null Findings** | **`0.62×` (`1.61×` enriched in Supp text!)** | **STRICTLY SUPP/ED** | Move `"did not significantly differ"` controls, sham/isotype controls, baseline sanity checks, and unperturbed normal-organ readouts to **Supp/ED**. |
| **13. Flow Gating Strategy, KO/KD Efficiency, Indels & Mouse Toxicity** | **`0.51×` (`1.96×` enriched in Supp!)** / **`0.58×`** ED caps | **STRICTLY SUPP/ED** | **ALWAYS put in Supp/ED**: FACS sequential gating trees, CRISPR indel/WB/qPCR knockdown efficiency verification, mouse body-weight curves, serum ALT/AST/BUN, and normal-organ H&E safety panels! |

---

## 3. The `Fig. 1 → Fig. 7` Main Storyboard & 1:1 `Main ↔ Supp/ED` Pairing Blueprint

Empirically, Main Figures follow a strict **Discovery → Mechanism → Causal In Vivo Rescue → Clinical Translation** arc (notice *In Vivo Efficacy/Rescue* climbs monotonically from `21.2%` in `Fig. 1` → `26.5%` in `Fig. 5` → `34.0%` in `Fig. 6` → **`39.3%` in `Fig. 7`**, while *Clinical Survival/ROC* surges to **`13.8%` in `Fig. 7`**!):

| Main Figure Slot | Median Panels | Main Figure Narrative Mission | Paired Companion `Fig. S_X` / `ED Fig. X` Mission (Real CNS Pairing!) |
| :--- | :---: | :--- | :--- |
| **`Fig. 1`** | **8** (`6–11`) | **Cohort / Experimental Design (`1a`) + Core Landscape Discovery**: Study schematic, scRNA-seq/spatial UMAP atlas, primary abundance/phenotype shift across clinical groups. | **`Fig. S1 / ED Fig. 1–2`**: QC violins (UMI/gene/%MT), batch-correction check, full canonical marker dotplot/heatmap, per-patient cellular composition breakdown, cohort clinical baseline. |
| **`Fig. 2`** | **8** (`6–11`) | **Zoom-In on Lead Subpopulation / Trajectory / Spatial Niche**: Subclustering of focal myeloid/T/malignant compartment, pseudotime trajectory, signature scoring, spatial localization. | **`Fig. S2 / ED Fig. 3–4`**: Subcluster marker FeaturePlots, alternate trajectory/velocity validation, full spatial ROI gallery, per-sample reproducibility & negative subsets. |
| **`Fig. 3`** | **9** (`6–11`) | **Intercellular Crosstalk & Microenvironmental Architecture**: Spatial neighborhood/colocalization quantification, representative mIF/CODEX/Visium images, focal ligand–receptor circuit. | **`Fig. S3 / ED Fig. 5`**: Single-channel mIF splits, antibody/isotype controls, full CellChat/NicheNet interaction matrices, spatial distance sensitivity thresholds. |
| **`Fig. 4`** | **9** (`6–12`) | **Molecular Mechanism & Downstream Pathway Dissection**: GSEA/TF regulon, *in vitro* co-culture / biochemical proof (WB, ChIP, metabolomics, phosphorylation, reporter assays) defining the causal axis. | **`Fig. S4 / ED Fig. 6–7`**: Full uncropped/auxiliary blots, qPCR primers/KD efficiency checks, dose–response/time-course pilots, off-target/alternative pathway exclusion controls. |
| **`Fig. 5`** | **9** (`6–12`) | **Causal Genetic Perturbation *In Vivo***: Conditional KO / CRISPR deletion / lineage depletion showing necessity & rescue on tumor growth, immune infiltration, and survival. | **`Fig. S5 / ED Fig. 8`**: Flow cytometry gating trees, genetic KO/depletion validation in mice, unchanged baseline immune compartments (negative controls), second cell-line/model repeat. |
| **`Fig. 6` *(or `Fig. 5` in Nature)*** | **9** (`6–12`) | **Pharmacological Targeting & Combination Therapy Synergy**: Drug/antibody blockade alone and combined with anti-PD-1 / chemo / RT across orthotopic/PDX/syngeneic models. | **`Fig. S6 / ED Fig. 9`**: Mouse body-weight monitoring, liver/kidney H&E & blood chemistry toxicity panels, individual tumor spider curves, pharmacokinetic/dosing schedules. |
| **`Fig. 7` *(optional in 6–7 Fig journals)*** | **8** (`6–11`) | **Human Clinical Validation, Biomarker Prognosis & Working Model**: Multi-cohort KM survival, multivariable Cox, ICB responder ROC/AUC, human mIF confirmation + **final graphical working model (`last panel`)**. | **`Fig. S7 / ED Fig. 10`**: Additional independent cohorts (TCGA/GEO), subgroup/stage/sex stratification, biomarker cutpoint sensitivity, comparison against PD-L1/TMB. |

> **Compression Rule for 5-Figure *Nature / Nat Med* Papers**: Merge `Fig. 2+3` (Subpopulation + Spatial Niche) and `Fig. 5+6` (Genetic KO + Therapeutic Blockade), and lean heavily on **`8–10` full-page Extended Data Figures** to house orthogonal mechanistic assays, second models, and human cohort validations!
