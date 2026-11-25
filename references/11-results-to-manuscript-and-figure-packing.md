# End-to-End Pipeline: Data/Results Notes → Millimeter-Bounded Figure Storyboard → Full Manuscript Expansion (`sci-paper-writing` × `sci-plot` Linkage)

> **Purpose**: Transform raw experimental/omics analysis notes, result tables, and candidate plots into a **physically valid, journal-calibrated Main + Extended Data/Supplementary Figure Storyboard** (zero page-size overflow!), and expand the approved storyboard into a **complete, synchronized CNS manuscript** with zero fabricated numbers.

---

## 1. The 5-Stage End-to-End Expansion Pipeline (Mode D)

When the user provides **data files, analysis summaries, or a Results description document** (`.md`, `.docx`, `.csv`/`.tsv`, or free-form notes) and asks to plan figures and write the manuscript, execute these 5 stages in strict order:

### Stage 1 — Atomic Evidence Extraction & Grounding Audit
- Parse the user's data/results document into an **Atomic Finding Table**:
  - `Finding ID` | `Biological Claim` | `Assay / Modality` | `Sample Size n (biological unit)` | `Key Quantitative Stats (fold/HR/AUC/r/P/FDR)` | `Causal Evidence Tier (Tier 1–4)` | `Candidate Chart Type`
- **Strict Anti-Fabrication Rule**: NEVER invent unverified `P` values, sample sizes `n`, fold changes, gene rankings, or ethical protocol numbers. Whenever a critical stat or reagent detail is missing from the source document, insert an explicit `[TODO: confirm exact n / P / catalog no.]` placeholder and list all TODOs at the end.

### Stage 2 — Study Archetype Lock & Initial Main/Supp Triage
- Classify the work into one of the **5 Study Archetypes** ([00-strategic-narrative-design.md](./00-strategic-narrative-design.md)) and lock the **Target Journal** (`nature`, `nat_med`, `cell`, `cancer_cell`, `science`, `nat_cancer`, `nat_commun`, `clin_cancer_res`).
- Triage every atomic finding into **Main Figure (`Fig. 1–N`)** vs **Extended Data / Supplementary (`ED Fig. 1–M` / `Fig. S1–SN`)** using the empirical 3-Second Triage Law ([10-figure-and-supplement-architecture.md](./10-figure-and-supplement-architecture.md)):
  - **Main**: Schematic/working model, headline UMAP/spatial discovery, core crosstalk/pathway, decisive *in vivo* KO/rescue/ICB synergy, primary clinical validation.
  - **Supp/ED**: QC/batch metrics, flow gating, KO/KD efficiency, toxicity/body weight, negative/null controls, exhaustive marker dotplots, per-patient/subgroup splits, secondary model repeats, algorithm ablations.

### Stage 3 — Physical Millimeter Page-Budget Check & Overflow Rebalancing (`sci-plot` Linkage!)
**CRITICAL**: Journals enforce strict full-page physical width and height ceilings. Cramming 12–15 complex panels into one Main Figure destroys typography (`< 5 pt` unreadable labels) and triggers editorial revision.

Run the built-in millimeter shelf-packing checker BEFORE drafting prose or rendering final figures:
```bash
python scripts/audit_manuscript.py plan-figures --journal nature --input draft_storyboard.json --rebalance --out final_storyboard.json
```

#### 3.1 Journal Physical Full-Page Canvas & Figure Count Limits (Synced with `sci-plot`)

| Target Journal | Full-Page Width (`W_max`) | Usable Plate Height (`H_max`, excl. caption/margins) | Max Main Figs (Ideal) | Max Panels / Main Fig (Ideal) | Paired Supp / ED Limit |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Nature** | **`180 mm`** | **`220 mm`** *(full page 247 mm)* | **`5–6`** *(ideal `5`)* | **`8–10`** *(ideal `8`)* | Up to **`10` Extended Data Figs** (`180×220 mm` each) |
| **Nat Med** | **`180 mm`** | **`215 mm`** | **`5–6`** *(ideal `5`)* | **`6–8`** *(ideal `6`)* | Up to **`10` ED Figs** + Supp Figs |
| **Nat Cancer / Genet / Immunol / Methods / Commun** | **`180 mm`** | **`220 mm`** | **`6–7`** *(ideal `6–7`)* | **`8–10`** *(ideal `8`)* | Up to `10` ED Figs (*Nat Commun*: unlimited Supp) |
| **Cell / Cancer Cell / Immunity / Cell Rep Med** | **`174 mm`** | **`215 mm`** *(full page 230 mm)* | **`7`** *(strict ceiling `7`)* | **`9–11`** *(ideal `9`)* | **Exact `1:1` pairing** (`Fig. S1–S7`, `174×215 mm` each) |
| **Science / Sci Transl Med / Sci Adv** | **`184 mm`** | **`218 mm`** *(full page 235 mm)* | **`6–7`** *(ideal `6`)* | **`8–10`** *(ideal `9–10`)* | Generous Supplementary PDF (`8–14` Figs) |
| **Clin Cancer Res** | **`178 mm`** | **`210 mm`** | **`5–6`** *(ideal `5`)* | **`5–7`** *(ideal `5`)* | `6–10` Supp Figs |

#### 3.2 Minimum Readable Panel Footprints (`w_mm × h_mm`, Synced 1:1 with `sci-plot`)

| Chart Type (`chart_type` key) | Minimum Readable `(W × H mm)` | Typical Row Slot (`180 mm` wide) | Space-Saving `sci-plot` Upgrade When Tight |
| :--- | :---: | :---: | :--- |
| `schematic` / `working_model` | **`88 × 46 mm`** *(or full-width `176 × 42`)* | 1/2 or Full row | Compress timeline horizontally; keep crisp icon labels |
| `umap` / `spatial_map` | **`58 × 55 mm`** | 1/3 row | Use `add_umap_corner_axes()` (recovers ~12 mm!) + inline labels |
| `spatial_zoom_mif` / `histology` | **`62 × 52 mm`** | 1/3–1/2 row | Move single-channel splits & extra patient slides to Supp |
| `heatmap` / `pseudotime_cascade` | **`86 × 60 mm`** | 1/2 row | Show top 20–30 genes; put full gene matrix in Supp |
| `dotplot` (grouped markers) | **`88 × 55 mm`** | 1/2 row | Use `+90°` tilted italic genes; full 40-gene panel → `Fig. S1` |
| `oncoprint` / `km_risk_table` | **`86 × 68 mm`** | 1/2 row | Merge clinical tracks cleanly; secondary cohorts → Supp |
| `forest_plot` / `swimmer` | **`86 × 54 mm`** | 1/2 row | Trim non-significant covariates into Supplementary Table |
| `chord` / `alluvial` / `upset` | **`64 × 56 mm`** | 1/3 row | Limit to top 6–8 interactions/sets |
| `bar` / `box` / `violin` / `raincloud` / `paired_slope` | **`43 × 42 mm`** | **1/4 row** (4 per row!) | Use `smart_rotate_xticklabels()` (`+45°`); combine 2 conditions via `plot_split_violin()` |
| `lollipop` / `diverging_enrichment` | **`62 × 46 mm`** | 1/3 row | Use **`plot_diverging_enrichment()`** (opposite-embedded labels save **40% width**!) |
| `volcano` / `scatter` / `roc` / `boundary_gradient` / `ripley` | **`46 × 46 mm`** | **1/4 row** (1:1 square) | Merge 4–8 cluster volcanoes into **1 `plot_multi_cluster_volcano()` (`88 × 48 mm`)**! |
| `roe_matrix` / `corr_matrix` / `neighborhood_matrix` | **`54 × 52 mm`** | 1/3 row | Merge upper/lower correlations into **1 `plot_split_corr_matrix()`** |
| `waterfall` / `spider` / `milo` / `shap` | **`58 × 46 mm`** | 1/3 row | Compact ticks (3–5) & zero background gridlines |

#### 3.3 The 4-Tier CNS Overflow Rebalancing Protocol (Apply in Strict Priority Order!)

Whenever a Main Figure exceeds `H_max` (e.g., packed height `> 220 mm` in *Nature* or `> 215 mm` in *Cell*) OR total panels exceed the journal cap OR total Main Figures exceed the journal cap (`> 5` in *Nature*, `> 7` in *Cell*):

1. **Tier 1 — Priority Demotion to Paired `ED Fig. X` / `Fig. S_X` (First Resort!)**:
   - Demote panels strictly in reverse causal priority: `QC/Batch` (`0.55×`) → `Gating/KO Efficiency/Toxicity` (`0.51×`) → `Negative/Null Controls` (`0.62×`) → `Per-Patient/Subgroup Splits` → `Exhaustive Marker Dotplots` → `Secondary Model / Extra Validation Cohort`.
   - Maintain **1:1 logical pairing** (`Fig. 3` overflow moves to `Fig. S3` or `ED Fig. 5–6`, NEVER dumped randomly into an unrelated supplement!).
2. **Tier 2 — `sci-plot` High-Density Chart Consolidation (Recover 35–60% Area Without Losing Information!)**:
   - `≥ 3` per-cluster Volcano plots (`3 × 46×46 mm`) ⟹ **1 `plot_multi_cluster_volcano()`** (`88 × 48 mm`).
   - `≥ 2` side-by-side group Violins (`2 × 43×42 mm`) ⟹ **1 `plot_split_violin()`** (`56 × 42 mm`).
   - Long-label GSEA Bar + separate NES bar (`110 mm` wide) ⟹ **1 `plot_diverging_enrichment()`** with opposite-embedded labels (`68 × 48 mm`).
   - Separate abundance bars + statistical heatmap ⟹ **1 `plot_roe_bubble_heatmap()`** (`56 × 52 mm`).
   - Separate UMAP + separate lineage bar + separate legend ⟹ **1 `plot_atlas_umap_composite()`** (`88 × 60 mm`).
3. **Tier 3 — Split Dense Main Module into 2 Consecutive Main Figures (Only When `Current Main Figs < Journal Cap`)**:
   - Example: A 5-figure *Cancer Cell* draft (cap `7`) has an overflowing 14-panel `Fig. 3` (Spatial Niche + L–R Mechanism + In Vitro Co-culture). Split cleanly into **`Fig. 3` (Spatial Niche Architecture, 7 panels)** + **`Fig. 4` (L–R Mechanism & Co-culture, 7 panels)**, and shift `Fig. 4–5` → `Fig. 5–6`!
4. **Tier 4 — Cross-Journal Main-Figure Compression (When `Current Main Figs > Journal Cap`, e.g., 7-Fig Draft → 5-Fig *Nature*)**:
   - Merge adjacent discovery figures (`Fig. 1 + Fig. 2` → condensed `Fig. 1`; `Fig. 5 + Fig. 6` → combined Genetic + Pharmacological `Fig. 4`) and promote orthogonal assays into *Nature*'s generous **`8–10` Extended Data Figures**!

### Stage 4 — Lock Shared `storyboard.json` (Single Source of Truth!)
Present the rebalanced Storyboard Table to the user for 1-turn confirmation before full-text expansion:
- Exact Main Figure count (`Fig. 1..N`), exact packed height (`e.g., 196 / 220 mm — OK`), exact panel letters (`a–h` / `A–I`), chart types & `(w_mm, h_mm)` specs for `sci-plot`, and exact paired `ED Fig. / Fig. S` allocation.

### Stage 5 — Synchronized Full-Manuscript Expansion
Once the Storyboard is locked (`0 OVERFLOW`), expand **every section in synchronized sequence** using the exact finalized panel IDs:
1. **Results Subheadings (`H1..Hk`) & Full Results Prose** ([03-results-and-subheadings.md](./03-results-and-subheadings.md) + [08-comprehensive-phrasebank-and-collocations.md](./08-comprehensive-phrasebank-and-collocations.md)) — every `(Fig. Xa)` and `(Extended Data Fig. Yb / Fig. SYB)` matches `final_storyboard.json` 1:1; strict 4-tier certainty verbs & tail-to-head chaining.
2. **Figure Captions (Main + Extended Data/Supp)** ([06-figure-captions.md](./06-figure-captions.md)) — exact 1:1 panel letter alignment (`a–h` vs `(A)–(I)`), `5:1` `-ing` syntax, stats & scale-bar disclosures.
3. **Reverse-Engineered Introduction** ([00-strategic-narrative-design.md](./00-strategic-narrative-design.md) + [02-introduction.md](./02-introduction.md)) — seeded ONLY with the 2–3 core entities paid off in Results (`P1 10% → P2–P3 37% → Final 28%`).
4. **4-Layer Elevated Discussion & Limitations** ([04-discussion.md](./04-discussion.md)) — zero raw stats in P1, paradox reconciliation, translational roadmap, journal-matched Limitations.
5. **Title (3 ranked options), Abstract & Companion Micro-Texts (`Highlights` / `In brief` / `Significance`)** ([01-title-and-abstract.md](./01-title-and-abstract.md)).
6. **Methods / STAR★METHODS + Key Resources Table** ([07-methods-and-star.md](./07-methods-and-star.md)) + **Reference Budget Check** ([09-citation-and-reference-architecture.md](./09-citation-and-reference-architecture.md)) + **Cover Letter** ([05-cover-letter.md](./05-cover-letter.md)).
7. **Automated Gate**: Run `python scripts/audit_manuscript.py audit --section all --journal <target> --file full_manuscript.md` until `0 FAIL`.
