# sci-paper-writing

An empirically distilled **Agent Skill** for architecting, drafting, polishing, and auditing **publication-grade biomedical & oncology manuscripts** (*Nature*, *Cell*, *Science*, *Cancer Cell*, *Nature Medicine*, *Immunity*, *Nature Methods* standard) across **all 9 manuscript sections + journal companion micro-texts**.

Distilled and out-of-time cross-validated across **2020–2026**:
- **6,665** high-impact tumor-omics titles (`2,725` 2025–2026 + `3,940` 2020–2024) & **1,960** full-text manuscripts (`1,464` 2025–2026 derivation + `496` 2020–2024 hold-out validation)
- **1,223** full-text Results chaining & citation-architecture audits (`562` HTML subheading trees / `3,955` subheadings; `1,009` total-ref budgets; `1,016` per-section citation splits; `65,117` dated references)
- **1,215** manuscript figure/subpanel architecture & Main-vs-Supplement content triage audits (`50,030` Main-only vs `22,709` Supp-only Results sentences; `3,965` Main vs `2,771` Extended Data captions)
- **2,990** CNS Figure Captions & **307** complete CNS Methods / STAR★METHODS sections
- Benchmarked against *Nature* Summary Paragraph, MIT/Harvard CommKit *Discussion*, *Science* *Introduction/Results*, and Elsevier Editor *Cover Letter* standards.

---

## Three Operating Modes

1. **Storyline Architect Mode (Reverse-Engineering from Results)**:
   - Given a set of Results / figures, classifies the paper into one of **5 empirical Study Archetypes** (*Mechanistic Axis + Perturbation*, *Clinical Biomarker / Immunotherapy*, *Single-Cell / Spatial Atlas Resource*, *Clonal Evolution / Metastasis*, *Computational / AI Method*), locks target journal constraints, and reverse-engineers:
     - **3 ranked Title options** calibrated to journal norms (*Nature* `9w / 0% colons`, *Nat Med* `46% clinical colon / 2.4% declarative`, *Immunity/Cancer Cell* `58–79% causal clause`, *Nat Methods* `38% ToolName: ...`)
     - **Abstract framing** (anti-methods-bloat `≤150w` / `200w`, ~50% findings, ≤1s methods)
     - **Reverse-pruned Introduction funnel** (`P1 10% → P2–P3 37% → Final 28%` entity back-propagation law; zero `"few studies"` weak gaps)
     - **6–7 Results Subheading Domino Chain** + `Fig. 1 → Fig. 7` Main-vs-Supplement Storyboard (`1:1` pairing)
     - **4-Layer Elevated Discussion** (99.6% zero raw-stat P1, paradox reconciliation, translational roadmap, constructive 3-part Limitations)
     - **30-Second Editor-Focused Cover Letter** (`300–500w`, 1 page)
2. **Section Drafting & Idiomatic Polishing Mode**:
   - Enforces authentic CNS grammar, tense discipline (`4.93:1` Results past tense; `5:1` `-ing` figure captions; `9.89:1` past-passive Methods), inline parenthetical figure citations (`765.3:1` `(Fig. 1a)` vs `"Fig. 1a shows"`), the **4-Tier Certainty Verb Ladder**, **5 Precision Verb Confusion Matrices**, and **12 micro-scenario ready-to-migrate sentence banks**.
3. **Automated Pre-Submission Audit & Scaffolding CLI (`scripts/audit_manuscript.py`)**:
   - Zero-dependency Python linter auditing any single section or full Markdown manuscript (`title`, `abstract`, `highlights`, `in_brief`, `intro`, `results`, `subheadings`, `discussion`, `cover_letter`, `caption`, `methods`, `all`) plus an interactive archetype scaffolder.

```bash
# Audit an entire Markdown manuscript against Cancer Cell / Nature / Science rules
python scripts/audit_manuscript.py audit --section all --journal cancer_cell --file manuscript.md

# Audit a single section (e.g., Abstract, Highlights, Cover Letter)
python scripts/audit_manuscript.py audit --section abstract --journal nature --file abstract.txt
python scripts/audit_manuscript.py audit --section highlights --journal cell --file highlights.txt

# Generate a journal-calibrated storyline scaffold from Study Archetype
python scripts/audit_manuscript.py scaffold --archetype mechanistic --journal nature
```

---

## Repository Structure

```text
sci-paper-writing/
├── SKILL.md                                                    # Unified master skill specification & routing
├── README.md
├── LICENSE
├── references/
│   ├── 00-strategic-narrative-design.md                        # Higher-order storyline design: 5 Archetypes × 6 sections + 5 CNS blueprints
│   ├── 01-title-and-abstract.md                                # Title norms, Abstract formulas & Companion Micro-Texts (Highlights/In brief/Significance)
│   ├── 02-introduction.md                                      # Reverse-engineered 4-para funnel, 5 strong Gap types, 3-tense rules & 10-pt check
│   ├── 03-results-and-subheadings.md                           # Journal subheadings, 765:1 inline fig citations, 4-tier verb ladder & 6 chaining patterns
│   ├── 04-discussion.md                                        # MIT/Harvard 5-block elevation, 99.6% stat-free P1, paradox resolution & 3-part Limitations
│   ├── 05-cover-letter.md                                      # Elsevier/CNS 5-step 1-page rules, 4 compliance statements & 4 journal templates
│   ├── 06-figure-captions.md                                   # 2,990-caption corpus: journal specs, 5:1 -ing syntax, 13 chart templates & stats disclosures
│   ├── 07-methods-and-star.md                                  # 307-Methods corpus: Nature/Cell STAR+KRT/Science schemas, 9.89:1 past-passive & reproducibility
│   ├── 08-comprehensive-phrasebank-and-collocations.md         # 1,960-paper corpus: 5 verb confusion matrices, top 4-gram openers & 12 micro-scenario banks
│   ├── 09-citation-and-reference-architecture.md               # 20-journal reference budgets, Intro/Results/Discussion/Methods split, 95% 1–3 anti-stuffing & recency
│   └── 10-figure-and-supplement-architecture.md                # 20-journal Main/ED/Supp figure & subpanel budgets, Main-vs-Supp triage matrix & Fig 1–7 pairing
└── scripts/
    └── audit_manuscript.py                                     # Zero-dependency full-manuscript linter & storyline scaffolder
```

---

## Installation as an Agent Skill

### Option 1: Direct Clone (Antigravity / Claude Code / Cursor / Codex)
```bash
# Global install for Antigravity
git clone https://github.com/chenwh1993/sci-paper-writing.git ~/.gemini/config/skills/sci-paper-writing

# Or project-level install inside any workspace
git clone https://github.com/chenwh1993/sci-paper-writing.git .agents/skills/sci-paper-writing
```

### Option 2: External Directory Mount (`skills.json`, Antigravity)
Keep the cloned folder anywhere (e.g., `D:/skills/sci-paper-writing`) and register its parent folder in `~/.gemini/config/skills.json`:

```json
{
  "entries": [
    { "path": "D:/skills" }
  ]
}
```

---

## Companion Skill

Pairs seamlessly with [**`sci-plot`**](https://github.com/chenwh1993/sci-plot) for end-to-end CNS figure design, 1:1 millimeter vector/raster plotting, and publication-grade manuscript writing.

## License

MIT License — see [LICENSE](./LICENSE).
