#!/usr/bin/env python3
"""
audit_manuscript.py — Unified Zero-Dependency CNS Scientific Manuscript Linter & Scaffolder.

Covers ALL 9 manuscript components:
  title | abstract | intro | results | subheadings | discussion | cover_letter | caption | methods | all

Usage:
  python audit_manuscript.py audit --section abstract --journal nature --file draft.txt
  python audit_manuscript.py audit --section all --journal cell --file full_manuscript.md
  python audit_manuscript.py scaffold --archetype mechanistic --journal cancer_cell
"""
import argparse
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

JOURNAL_SPECS = {
    "general": {
        "style_family": "general",
        "title_max_w": 15, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 150, "abs_num_warn": 7,
        "intro_min_w": 450, "intro_med_w": 620, "intro_max_w": 820,
        "res_min_w": 3600, "res_med_w": 4200, "res_max_w": 5000, "res_pure_min": 3150, "res_pure_med": 3650,
        "disc_min_w": 850, "disc_med_w": 1100, "disc_max_w": 1500,
        "main_target_w": 6000, "main_min_w": 5200, "main_max_w": 6800, "main_pure_min": 4600,
        "sub_max_w": 13, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK/US",
        "main_ref_min": 48, "main_ref_target": "55-68 (+~18 Methods)", "intro_ref_min": 14, "res_ref_min": 18, "disc_ref_min": 11,
        "nonp_med": 1.5, "nonp_bull": 10.0, "nonp_warn": 15.0,
        "paren_tot_med": 37.4, "paren_tot_warn": 48.0, "paren_nfnum_med": 4.0, "paren_nfnum_warn": 12.0,
        "paren_share_med": 13.2, "paren_share_warn": 18.0, "ge3p_med": 7.5, "ge3p_warn": 16.0,
    },
    "nature": {
        "style_family": "nature",
        "title_max_w": 12, "title_colon_ok": False,
        "abs_min_w": 130, "abs_max_w": 215, "abs_num_warn": 6,
        "intro_min_w": 260, "intro_med_w": 401, "intro_max_w": 550,
        "res_min_w": 3400, "res_med_w": 4293, "res_max_w": 5000, "res_pure_min": 3000, "res_pure_med": 3581,
        "disc_min_w": 500, "disc_med_w": 645, "disc_max_w": 950,
        "main_target_w": 5430, "main_min_w": 4500, "main_max_w": 6200, "main_pure_min": 3950,
        "sub_max_w": 9, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK",
        "main_ref_min": 46, "main_ref_target": "50-58 (+~27 Methods)", "intro_ref_min": 14, "res_ref_min": 16, "disc_ref_min": 10,
        "nonp_med": 3.0, "nonp_bull": 10.0, "nonp_warn": 15.0,
        "paren_tot_med": 40.3, "paren_tot_warn": 50.0, "paren_nfnum_med": 3.5, "paren_nfnum_warn": 10.0,
        "paren_share_med": 16.8, "paren_share_warn": 21.0, "ge3p_med": 8.8, "ge3p_warn": 16.0,
    },
    "nat_cell_biol": {
        "style_family": "nature",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 150, "abs_num_warn": 6,
        "intro_min_w": 340, "intro_med_w": 511, "intro_max_w": 680,
        "res_min_w": 3400, "res_med_w": 4278, "res_max_w": 5100, "res_pure_min": 3000, "res_pure_med": 3471,
        "disc_min_w": 620, "disc_med_w": 930, "disc_max_w": 1300,
        "main_target_w": 5710, "main_min_w": 4700, "main_max_w": 6600, "main_pure_min": 4150,
        "sub_max_w": 13, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK",
        "main_ref_min": 46, "main_ref_target": "52-65 (+~18 Methods)", "intro_ref_min": 14, "res_ref_min": 16, "disc_ref_min": 10,
        "nonp_med": 2.9, "nonp_bull": 10.0, "nonp_warn": 15.0,
        "paren_tot_med": 40.9, "paren_tot_warn": 52.0, "paren_nfnum_med": 4.1, "paren_nfnum_warn": 11.0,
        "paren_share_med": 14.5, "paren_share_warn": 20.0, "ge3p_med": 7.9, "ge3p_warn": 16.0,
    },
    "nat_commun": {
        "style_family": "nature",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 150, "abs_num_warn": 7,
        "intro_min_w": 480, "intro_med_w": 723, "intro_max_w": 950,
        "res_min_w": 3500, "res_med_w": 4299, "res_max_w": 5400, "res_pure_min": 2990, "res_pure_med": 3698,
        "disc_min_w": 880, "disc_med_w": 1283, "disc_max_w": 1800,
        "main_target_w": 6110, "main_min_w": 5100, "main_max_w": 7300, "main_pure_min": 4550,
        "sub_max_w": 14, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK/US",
        "main_ref_min": 48, "main_ref_target": "54-68 (+~18 Methods)", "intro_ref_min": 15, "res_ref_min": 18, "disc_ref_min": 11,
        "nonp_med": 2.3, "nonp_bull": 10.0, "nonp_warn": 15.0,
        "paren_tot_med": 35.8, "paren_tot_warn": 46.0, "paren_nfnum_med": 4.2, "paren_nfnum_warn": 12.0,
        "paren_share_med": 12.4, "paren_share_warn": 18.0, "ge3p_med": 7.1, "ge3p_warn": 16.0,
    },
    "nat_cancer": {
        "style_family": "nature",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 150, "abs_num_warn": 7,
        "intro_min_w": 320, "intro_med_w": 516, "intro_max_w": 700,
        "res_min_w": 3200, "res_med_w": 4152, "res_max_w": 5000, "res_pure_min": 2650, "res_pure_med": 3483,
        "disc_min_w": 650, "disc_med_w": 943, "disc_max_w": 1350,
        "main_target_w": 5610, "main_min_w": 4600, "main_max_w": 6600, "main_pure_min": 4000,
        "sub_max_w": 13, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK/US",
        "main_ref_min": 46, "main_ref_target": "52-62 (+~18 Methods)", "intro_ref_min": 14, "res_ref_min": 16, "disc_ref_min": 10,
        "nonp_med": 4.6, "nonp_bull": 12.0, "nonp_warn": 18.0,
        "paren_tot_med": 39.6, "paren_tot_warn": 52.0, "paren_nfnum_med": 5.6, "paren_nfnum_warn": 16.0,
        "paren_share_med": 15.2, "paren_share_warn": 21.0, "ge3p_med": 8.8, "ge3p_warn": 18.0,
    },
    "nature_sister": {
        "style_family": "nature",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 150, "abs_num_warn": 7,
        "intro_min_w": 340, "intro_med_w": 520, "intro_max_w": 750,
        "res_min_w": 3300, "res_med_w": 4200, "res_max_w": 5000, "res_pure_min": 2900, "res_pure_med": 3480,
        "disc_min_w": 680, "disc_med_w": 935, "disc_max_w": 1350,
        "main_target_w": 5650, "main_min_w": 4700, "main_max_w": 6600, "main_pure_min": 4100,
        "sub_max_w": 13, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK",
        "main_ref_min": 46, "main_ref_target": "52-65 (+~18 Methods)", "intro_ref_min": 14, "res_ref_min": 16, "disc_ref_min": 10,
        "nonp_med": 2.9, "nonp_bull": 10.0, "nonp_warn": 15.0,
        "paren_tot_med": 40.0, "paren_tot_warn": 50.0, "paren_nfnum_med": 4.5, "paren_nfnum_warn": 12.0,
        "paren_share_med": 14.5, "paren_share_warn": 20.0, "ge3p_med": 8.0, "ge3p_warn": 16.0,
    },
    "nat_med": {
        "style_family": "nature",
        "title_max_w": 18, "title_colon_ok": True,
        "abs_min_w": 140, "abs_max_w": 225, "abs_num_warn": 10,
        "intro_min_w": 250, "intro_med_w": 475, "intro_max_w": 650,
        "res_min_w": 2600, "res_med_w": 3523, "res_max_w": 4400, "res_pure_min": 2100, "res_pure_med": 2820,
        "disc_min_w": 900, "disc_med_w": 1255, "disc_max_w": 1750,
        "main_target_w": 5260, "main_min_w": 4100, "main_max_w": 6400, "main_pure_min": 3550,
        "sub_max_w": 13, "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
        "main_ref_min": 42, "main_ref_target": "48-58 (+~17 Methods)", "intro_ref_min": 12, "res_ref_min": 14, "disc_ref_min": 10,
        "nonp_med": 2.7, "nonp_bull": 12.0, "nonp_warn": 18.0,
        "paren_tot_med": 47.1, "paren_tot_warn": 56.0, "paren_nfnum_med": 11.8, "paren_nfnum_warn": 22.0,
        "paren_share_med": 19.5, "paren_share_warn": 25.0, "ge3p_med": 14.9, "ge3p_warn": 22.0,
    },
    "nat_methods": {
        "style_family": "nature",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 150, "abs_num_warn": 7,
        "intro_min_w": 380, "intro_med_w": 656, "intro_max_w": 900,
        "res_min_w": 3100, "res_med_w": 3752, "res_max_w": 4600, "res_pure_min": 2900, "res_pure_med": 3340,
        "disc_min_w": 450, "disc_med_w": 590, "disc_max_w": 1050,
        "main_target_w": 5280, "main_min_w": 4300, "main_max_w": 6300, "main_pure_min": 4000,
        "sub_max_w": 12, "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "US/UK",
        "main_ref_min": 44, "main_ref_target": "50-60 (+~20 Methods)", "intro_ref_min": 14, "res_ref_min": 16, "disc_ref_min": 9,
        "nonp_med": 0.3, "nonp_bull": 8.0, "nonp_warn": 13.0,
        "paren_tot_med": 31.0, "paren_tot_warn": 42.0, "paren_nfnum_med": 2.2, "paren_nfnum_warn": 8.0,
        "paren_share_med": 11.0, "paren_share_warn": 16.0, "ge3p_med": 4.8, "ge3p_warn": 12.0,
    },
    "cell": {
        "style_family": "cell",
        "title_max_w": 15, "title_colon_ok": True,
        "abs_min_w": 100, "abs_max_w": 150, "abs_num_warn": 6,
        "intro_min_w": 340, "intro_med_w": 533, "intro_max_w": 700,
        "res_min_w": 3100, "res_med_w": 3852, "res_max_w": 4600, "res_pure_min": 2850, "res_pure_med": 3420,
        "disc_min_w": 680, "disc_med_w": 984, "disc_max_w": 1350,
        "main_target_w": 5400, "main_min_w": 4500, "main_max_w": 6400, "main_pure_min": 4150,
        "sub_max_w": 16, "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
        "main_ref_min": 52, "main_ref_target": "62-84 (+~16 STAR)", "intro_ref_min": 15, "res_ref_min": 22, "disc_ref_min": 12,
        "nonp_med": 0.0, "nonp_bull": 6.0, "nonp_warn": 10.0,
        "paren_tot_med": 39.2, "paren_tot_warn": 48.0, "paren_nfnum_med": 1.8, "paren_nfnum_warn": 7.0,
        "paren_share_med": 11.9, "paren_share_warn": 17.0, "ge3p_med": 8.5, "ge3p_warn": 17.0,
    },
    "cancer_cell": {
        "style_family": "cell",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 100, "abs_max_w": 150, "abs_num_warn": 6,
        "intro_min_w": 320, "intro_med_w": 458, "intro_max_w": 650,
        "res_min_w": 2900, "res_med_w": 3627, "res_max_w": 4400, "res_pure_min": 2650, "res_pure_med": 3160,
        "disc_min_w": 680, "disc_med_w": 866, "disc_max_w": 1250,
        "main_target_w": 4950, "main_min_w": 4100, "main_max_w": 5900, "main_pure_min": 3850,
        "sub_max_w": 16, "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
        "main_ref_min": 52, "main_ref_target": "60-80 (+~16 STAR)", "intro_ref_min": 15, "res_ref_min": 20, "disc_ref_min": 12,
        "nonp_med": 0.6, "nonp_bull": 7.0, "nonp_warn": 11.0,
        "paren_tot_med": 40.1, "paren_tot_warn": 50.0, "paren_nfnum_med": 2.7, "paren_nfnum_warn": 9.0,
        "paren_share_med": 12.3, "paren_share_warn": 18.0, "ge3p_med": 10.3, "ge3p_warn": 17.0,
    },
    "immunity": {
        "style_family": "cell",
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 100, "abs_max_w": 150, "abs_num_warn": 6,
        "intro_min_w": 340, "intro_med_w": 494, "intro_max_w": 660,
        "res_min_w": 3000, "res_med_w": 3724, "res_max_w": 4500, "res_pure_min": 2750, "res_pure_med": 3224,
        "disc_min_w": 700, "disc_med_w": 943, "disc_max_w": 1300,
        "main_target_w": 5020, "main_min_w": 4200, "main_max_w": 6000, "main_pure_min": 3950,
        "sub_max_w": 16, "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
        "main_ref_min": 52, "main_ref_target": "60-80 (+~16 STAR)", "intro_ref_min": 15, "res_ref_min": 20, "disc_ref_min": 12,
        "nonp_med": 0.0, "nonp_bull": 6.0, "nonp_warn": 10.0,
        "paren_tot_med": 36.4, "paren_tot_warn": 48.0, "paren_nfnum_med": 1.6, "paren_nfnum_warn": 7.0,
        "paren_share_med": 10.1, "paren_share_warn": 16.0, "ge3p_med": 6.9, "ge3p_warn": 17.0,
    },
    "science": {
        "style_family": "science",
        "title_max_w": 13, "title_colon_ok": False,
        "abs_min_w": 85, "abs_max_w": 125, "abs_num_warn": 5,
        "intro_min_w": 280, "intro_med_w": 456, "intro_max_w": 650,
        "res_min_w": 3600, "res_med_w": 4874, "res_max_w": 5600, "res_pure_min": 3400, "res_pure_med": 4322,
        "disc_min_w": 500, "disc_med_w": 786, "disc_max_w": 1150,
        "main_target_w": 6090, "main_min_w": 4700, "main_max_w": 6900, "main_pure_min": 4500,
        "sub_max_w": 14, "disc_lim_mandatory": False, "cap_max_w": 300, "spelling": "US",
        "main_ref_min": 50, "main_ref_target": "58-78 (+~16 Supp)", "intro_ref_min": 15, "res_ref_min": 20, "disc_ref_min": 12,
        "nonp_med": 0.0, "nonp_bull": 6.0, "nonp_warn": 10.0,
        "paren_tot_med": 37.6, "paren_tot_warn": 50.0, "paren_nfnum_med": 1.9, "paren_nfnum_warn": 7.0,
        "paren_share_med": 12.6, "paren_share_warn": 18.0, "ge3p_med": 6.3, "ge3p_warn": 14.0,
    },
}

CHINGLISH_PATTERNS = [
    (r"\bwith the rapid development of\b", "Macro-era throat-clearing cliché ('with the rapid development of'); open directly with the biological or clinical phenomenon."),
    (r"\bfew studies have (investigated|explored|studied|focused on)\b", "Weak 'few studies' gap (only 1.1% in 2025-2026 CNS); replace with a mechanistic, spatial, clinical, or technical contradiction."),
    (r"\blittle attention has been paid\b", "Weak 'little attention' gap; state the concrete scientific barrier instead."),
    (r"\bmore and more\b", "Informal ('more and more'); replace with 'increasingly' or 'a growing number of'."),
    (r"\bobviously\b|\bvery significantly\b|\bremarkably significant\b", "Subjective/redundant intensifier ('obviously' / 'very significantly'); use 'markedly' or report exact fold change and P value."),
    (r"\bin order to\b", "Wordy ('in order to'); tighten to concise 'To [verb]...'."),
    (r"\bas can be seen from (fig|figure)\b", "Chinglish figure reference ('As can be seen from Fig.'); state the biological result as subject and cite '(Fig. Xa)' parenthetically."),
    (r"\bproved that\b|\bproves that\b", "Overclaiming verb ('proved'); biological data rarely 'prove'—use 'demonstrated', 'established', or 'indicated' per the 4-tier certainty ladder."),
    (r"\bplay(s)? a very important role\b|\bhas (great|important) clinical significance\b", "Empty significance cliché; name the concrete biological function or translational utility."),
    (r"\bnovel\b.*\bfirst\b|\bfor the first time\b", "Editorial red flag ('for the first time' / 'novel...first', only 0.1-1.0% in Tier-1 CNS vs 2.7x higher in lower tiers); prove conceptual delta via 'X, rather than Y' instead of self-praise."),
    (r"\b(first (?:study|report|investigation) to|to the best of our knowledge|never been (?:studied|reported|explored))\b", "Empty priority/novelty claim ('first study to / never been studied' is 2.8-5.0x more common in lower tiers and triggers 'no novelty' scrutiny); replace with explicit prior-art contrast ('Whereas prior studies..., our data show...')."),
]

# Journal-calibrated Results P/q density targets: (published_median, bullseye_hi, warn_hi, fail_hi) per 1,000 words
CNS_JOURNAL_P_TARGETS = {
    "general":       (0.6, 2.0, 5.5, 10.0),
    "cell":          (0.0, 1.0, 3.5, 10.0),
    "immunity":      (0.0, 0.8, 2.5, 10.0),
    "cancer_cell":   (0.3, 1.5, 6.0, 10.0),
    "nat_cell_biol": (0.4, 1.5, 4.0, 10.0),
    "nat_commun":    (0.8, 2.0, 6.0, 10.0),
    "nat_cancer":    (1.0, 2.5, 8.0, 12.0),
    "nat_methods":   (0.3, 1.5, 4.0, 10.0),
    "nature_sister": (0.4, 1.8, 5.0, 10.0),
    "nature":        (1.0, 2.0, 5.5, 10.0),
    "science":       (0.0, 1.5, 4.5, 10.0),
    "nat_med":       (2.8, 4.5, 9.0, 14.0),
}

# Authentic CNS replacement dictionaries (distilled from 1,312 + 550 flagship 2025-2026 papers)
CNS_LEXICON_REPLACEMENTS = {
    "audited": "evaluated / assessed",
    "rigorous audit": "systematic evaluation",
    "quarantined": "held-out / independent validation",
    "obliterates": "disrupts / eliminates / abolishes",
    "obliterate": "disrupt / eliminate / abolish",
    "crosswalk": "comparison / mapping",
    "capitalising": "combining / integrating",
    "capitalised": "combined / integrated",
    "capitalizing": "combining / integrating",
    "capitalized": "combined / integrated",
    "over-optimistic": "prevailing / unverified",
    "honest optical blind spot": "limited ability of H&E morphology alone to resolve",
    "honest blind spot": "limited ability to distinguish",
    "upgraded clinical": "improved clinical",
    "phase cliff": "sharp decline / threshold shift",
    "division of labour": "complementary roles",
    "division of labor": "complementary roles",
    "triage cascade": "two-step stratification",
    "parsimonious": "compact / minimal",
    "habitats": "niches / compartments",
    "descriptors": "features / metrics",
    "portals": "compartments / interfaces",
    "cleanly": "distinctly / clearly",
    "decodes": "predicts / infers",
    "decode": "predict / infer",
}

CNS_DEFENSIVE_REPLACEMENTS = {
    "without outcome-label leakage": "unsupervised (move leakage controls to Methods)",
    "without outcome label leakage": "unsupervised (move leakage controls to Methods)",
    "outcome-blind": "unsupervised / derived without clinical labels",
    "outcome blind": "unsupervised / derived without clinical labels",
    "zero-outcome-peeking": "unsupervised (describe cross-validation in Methods)",
    "adversarial removal": "sensitivity analysis excluding extreme samples (Methods)",
    "sensitivity audit": "sensitivity analysis (Extended Data)",
    "sensitivity audits": "sensitivity analyses (Extended Data)",
    "quarantined": "independent external validation",
    "bidirectional rescue disabled": "move scoring constraints to Methods",
    "conflict-free": "consistent / concordant",
    "guarding against technical batch": "independent of batch effects (Methods)",
    "zero batch confounding": "no batch-associated bias (Extended Data)",
    "negative penalty": "move scoring penalty details to Methods",
    "fragile antibodies": "markers failing staining QC (Methods)",
    "strictly isolated": "independent held-out",
    "overfitted": "evaluated via cross-validation to minimize overfitting",
}

CNS_2PART_STACK_REPLACEMENTS = {
    "two-feature": "a model combining [A] and [B] / two-variable",
    "three-feature": "a model combining [A], [B] and [C]",
    "same-section": "matched / serial sections / within the same section",
    "single-marker": "quantification of [Marker] alone",
    "single-metric": "single-marker / univariate scoring",
    "batch-matched": "controls matched for batch",
    "multi-compartment": "spanning epithelial, stromal and immune compartments",
    "macro-architectural": "macroscopic tissue architecture",
    "ambient-rna": "ambient RNA (unhyphenated noun)",
    "zero-shot": "pretrained (specify zero-shot once in Methods)",
    "out-of-fold": "cross-validated",
    "within-batch": "within each batch",
    "per-slide": "slide-level",
    "bladder-wall": "bladder wall (unhyphenated noun adjunct)",
    "dendritic-cell": "dendritic cell (unhyphenated noun adjunct)",
    "signed-z": "standardized z-score",
}

CNS_HYPHEN_UNPACK = {
    "antibody-stability-tiered": "filtered for antibody staining stability",
    "marker-stability-tiered": "filtered for marker staining stability",
    "copy-number-confirmed": "confirmed by copy-number inference",
    "copy-number-gated": "filtered by copy-number inference",
    "near-versus-distal": "proximal versus distal",
    "out-of-sample": "held-out / independent validation",
    "leave-one-patient-out": "leave-one-patient-out cross-validation (define in Methods; use 'cross-validation' in Results)",
    "out-of-fold": "cross-validated",
    "target-to-vascular": "spatial proximity between target-expressing cells and vessels",
    "immune-checkpoint-blockade": "immune checkpoint blockade (unhyphenated noun)",
    "single-cell-resolution": "at single-cell resolution",
    "zero-outcome-peeking": "unsupervised",
    "outcome-label-free": "unsupervised",
}

CNS_SHORT_BURST_MODELS = [
    "We identified a subpopulation of [cells] transcriptionally distinct from controls (Fig. 2a).",
    "The frequency of other resident immune subsets did not change (Extended Data Fig. 2b).",
    "Unlike [Model A], [Model B] did not improve response to combined therapy (Fig. 3b).",
]

CNS_DISC_OPENER_MODELS = [
    "In this study, we...",
    "Consistent with this, ...",
    "In line with previous reports, ...",
    "These findings suggest that...",
    "In contrast to prior studies, ...",
    "Our data indicate that...",
    "Future studies should...",
    "We speculate that...",
]


def suggest_lexicon_fixes(hits: list, mapping: dict, max_items: int = 6) -> str:
    seen = []
    for raw in hits:
        k = raw.lower().strip()
        if k in seen:
            continue
        seen.append(k)
        if len(seen) >= max_items:
            break
    pairs = []
    for k in seen:
        repl = mapping.get(k)
        if not repl:
            for mk, mv in mapping.items():
                if mk in k or k in mk:
                    repl = mv
                    break
        if not repl and k.startswith("locked "):
            repl = "consensus atlas"
        pairs.append(f"'{k}' -> '{repl or 'plain CNS wording'}'")
    return "; ".join(pairs)


def suggest_hyphen_unpacks(hits: list, max_items: int = 6) -> str:
    seen = []
    for h in hits:
        kl = h.lower()
        if kl not in seen:
            seen.append(kl)
        if len(seen) >= max_items:
            break
    pairs = []
    for kl in seen:
        repl = CNS_HYPHEN_UNPACK.get(kl, "unpack into plain prepositional phrase (avoid 3-part hyphen stack)")
        pairs.append(f"'{kl}' -> '{repl}'")
    return "; ".join(pairs)


def count_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def strip_parens(text: str) -> str:
    """Remove all parenthetical blocks (...) to measure pure narrative prose length."""
    prev = None
    cur = text or ""
    while prev != cur:
        prev = cur
        cur = re.sub(r"\([^()]*\)", " ", cur)
    return cur


_PAREN_FIG_RE = re.compile(r"\b(?:Extended Data\s+|Supplementary\s+)?(?:Figs?\.|Figures?|Tables?|Supplementary\s+Data|Supplementary\s+Table|Supplementary\s+Movie|Video|Movie|Data\s+S)(?=\s|\d|$)", re.I)
_PAREN_CITE_AY_RE = re.compile(r"^[A-Z][A-Za-z\-]+(?:\s+et\s+al\.|\s+(?:and|&)\s+[A-Z][A-Za-z\-]+)?,?\s*(?:19|20)\d\d[a-z]?(?:;\s*[A-Z][^)]{2,90})*$")
_PAREN_CITE_NUM_RE = re.compile(r"^\d{1,3}(?:\s*[,–—\-]\s*\d{1,3})*$")
_PAREN_NUM_RE = re.compile(r"(?:\b[npqrPQR]\s*[=<>≤≥]\s*[-−+]?\d|\b(?:AUC|AUROC|HR|OR|CI|IQR|SD|SEM|FDR|NES|ARI|log2?FC|FC|rho|ρ|C-?index)\b|\d+(?:\.\d+)?\s*(?:%|fold|-fold|µm|μm|mm|cm|nm|mg|kg|mM|µM|μM|h|d|days|weeks|months|years|patients|mice|tumou?rs|cells|nuclei|samples|cohorts|genes|spots|bins|slides)|\b\d+\s*(?:of|/)\s*\d+\b|\b\d+(?:\.\d+)?\s*[–\-−±]\s*\d+(?:\.\d+)?)", re.I)


def analyze_parens(clean_text: str) -> dict:
    """Measure raw vs paren-stripped pure prose, parenthetical word share, and Fig/NonFig paren composition."""
    raw_w = max(1, count_words(clean_text))
    pure_w = count_words(strip_parens(clean_text))
    paren_w = max(0, raw_w - pure_w)
    paren_share_pct = round(100.0 * paren_w / raw_w, 1)

    n_fig = n_fig_stat = n_nf = n_nf_num = 0
    for inner in re.findall(r"\(([^()]{1,240})\)", clean_text):
        inn = inner.strip()
        if not inn or _PAREN_CITE_AY_RE.match(inn) or _PAREN_CITE_NUM_RE.match(inn):
            continue
        if _PAREN_FIG_RE.search(inn):
            n_fig += 1
            if _PAREN_NUM_RE.search(inn):
                n_fig_stat += 1
        else:
            n_nf += 1
            if _PAREN_NUM_RE.search(inn):
                n_nf_num += 1
    tot = n_fig + n_nf
    sents = split_sents(clean_text)
    ge3 = 0
    max_p = 0
    for s in sents:
        ps = [m.strip() for m in re.findall(r"\(([^()]{1,240})\)", s) if m.strip() and not _PAREN_CITE_AY_RE.match(m.strip()) and not _PAREN_CITE_NUM_RE.match(m.strip())]
        if len(ps) >= 3:
            ge3 += 1
        if len(ps) > max_p:
            max_p = len(ps)
    return {
        "raw_w": raw_w, "pure_w": pure_w, "paren_w": paren_w, "paren_share_pct": paren_share_pct,
        "tot": tot, "n_fig": n_fig, "n_fig_stat": n_fig_stat, "n_nf": n_nf, "n_nf_num": n_nf_num,
        "tot_1kw": round(1000.0 * tot / raw_w, 1),
        "fig_stat_1kw": round(1000.0 * n_fig_stat / raw_w, 1),
        "nf_1kw": round(1000.0 * n_nf / raw_w, 1),
        "nf_num_1kw": round(1000.0 * n_nf_num / raw_w, 1),
        "ge3_pct": round(100.0 * ge3 / max(1, len(sents)), 1),
        "max_p_sent": max_p,
    }


def split_sents(text: str):
    t = re.sub(r"\b(Fig|Figs|vs|et al|e\.g|i\.e|Dr|Prof|No)\.", r"\1<D>", text)
    t = re.sub(r"(\d)\.(\d)", r"\1<P>\2", t)
    return [s.replace("<D>", ".").replace("<P>", ".").strip() for s in re.split(r"(?<=[.!?])\s+", t.strip()) if len(s.split()) >= 4]


def scan_chinglish(text: str, findings: list):
    for pat, msg in CHINGLISH_PATTERNS:
        if re.search(pat, text, re.I):
            findings.append(("WARN", f"Style/Chinglish: {msg}"))


def extract_citations(text: str):
    """
    Extract inline references across numeric ([1], [1,2], [1-4], (1,2)), author-year
    ((Smith et al., 2024; Lee et al., 2025)), and verifiable draft placeholders ([CITE: ...]).
    Returns (unique_id_set, total_mentions_int, cluster_sizes_list).
    """
    mentions = []
    clusters = []

    def expand_num(s: str):
        s = s.replace("–", "-").replace("—", "-").replace("−", "-")
        out = []
        for part in re.split(r"[,;\s]+", s.strip()):
            if not part:
                continue
            m = re.fullmatch(r"(\d{1,3})-(\d{1,3})", part)
            if m:
                a, b = int(m.group(1)), int(m.group(2))
                if 1 <= a <= b <= 300 and (b - a) <= 30:
                    out.extend([f"num:{x}" for x in range(a, b + 1)])
            elif re.fullmatch(r"\d{1,3}", part):
                v = int(part)
                if 1 <= v <= 300:
                    out.append(f"num:{v}")
        return out

    # 1. Bracket numeric citations: [1], [1, 2], [3-5]
    for m in re.finditer(r"\[(\d{1,3}(?:\s*[,–—\-]\s*\d{1,3})*)\]", text):
        ids = expand_num(m.group(1))
        if ids:
            mentions.extend(ids)
            clusters.append(len(ids))

    # 2. Structured verifiable draft placeholders: [CITE: topic/author]
    for m in re.finditer(r"\[CITE:\s*([^\]]{3,120})\]", text, re.I):
        key = "cite:" + re.sub(r"\s+", " ", m.group(1).strip().lower())
        mentions.append(key)
        clusters.append(1)

    # 3. Parenthetical author-year: (Smith et al., 2024; Jones and Lee, 2025)
    for m in re.finditer(r"\(([A-Z][A-Za-z\-]+(?:\s+et\s+al\.|\s+(?:and|&)\s+[A-Z][A-Za-z\-]+)?,?\s*(?:19|20)\d\d[a-z]?(?:;\s*[A-Z][^)]{4,80})*)\)", text):
        parts = [p.strip() for p in m.group(1).split(";") if re.search(r"(?:19|20)\d\d", p)]
        if parts:
            ids = ["ay:" + re.sub(r"[^a-z0-9]", "", p.lower())[:28] for p in parts]
            mentions.extend(ids)
            clusters.append(len(ids))

    # 4. Science-style parenthetical numeric (1, 2) or (3-5) — exclude Fig./Table/n=/year
    for m in re.finditer(r"(?<!Fig\.\s)(?<!Figure\s)(?<!Table\s)(?<!n\s=\s)\((\d{1,3}(?:\s*[,–—\-]\s*\d{1,3})+)\)", text):
        ids = expand_num(m.group(1))
        if ids:
            mentions.extend(ids)
            clusters.append(len(ids))

    # 5. Nature/LaTeX markdown superscripts: $^{1-5}$, $^{14,19}$, $^{20}$ (exclude 10^{...}, mm^{3}, cm^{2}, ml^{-1})
    for m in re.finditer(r"(?<!10)(?<!mm)(?<!cm)(?<!ml)(?<!µm)\$\^\{(\d{1,3}(?:\s*[,–—\-]\s*\d{1,3})*)\}\$", text):
        ids = expand_num(m.group(1))
        if ids:
            mentions.extend(ids)
            clusters.append(len(ids))

    return set(mentions), len(mentions), clusters


def audit_title(text: str, spec: dict, journal: str):
    findings = []
    t = " ".join(text.strip().splitlines()).strip().rstrip(".")
    wc = count_words(t)
    cc = len(t)
    findings.append(("INFO", f"Title length: {wc} words, {cc} chars (target for {journal}: <={spec['title_max_w']} words)."))
    if wc > spec["title_max_w"]:
        findings.append(("WARN", f"Title exceeds {journal} empirical norm ({wc} > {spec['title_max_w']} words); tighten by removing filler nouns."))
    if ":" in t and not spec["title_colon_ok"]:
        findings.append(("FAIL", f"Colon ':' detected in title — {journal} publishes 0% colon titles in 2025-2026; remove colon."))
    if re.match(r"^(a study on|study of|investigation of|analysis of|the role of|comprehensive analysis of)\b", t, re.I):
        findings.append(("FAIL", "Deadwood opener ('A study on / Analysis of / The role of'); promote the active biological entity or discovery to subject."))
    if re.search(r"\b(novel|first|new)\b", t, re.I):
        findings.append(("WARN", "Avoid empty novelty adjectives ('novel', 'first', 'new') in CNS titles."))
    if journal == "nat_med" and re.search(r"\b(drives|controls|governs|orchestrates|fuels|licenses)\b", t, re.I):
        findings.append(("WARN", "Nat Med rarely uses strong causal title verbs (2.4%); consider conservative clinical descriptive + colon trial/cohort design."))
    # Check Title Case overuse
    cap_words = sum(1 for w in t.split()[1:] if len(w) > 3 and w[0].isupper() and not w.isupper())
    if cap_words >= max(4, wc // 2):
        findings.append(("WARN", "Title appears to be in Title Case; CNS journals mandate Sentence case."))
    return findings


def audit_abstract(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    sents = split_sents(text)
    findings.append(("INFO", f"Abstract: {wc} words, {len(sents)} sentences (target for {journal}: {spec['abs_min_w']}-{spec['abs_max_w']}w)."))
    if wc > spec["abs_max_w"]:
        findings.append(("FAIL", f"Word count ({wc}w) exceeds {journal} ceiling ({spec['abs_max_w']}w). Trim background/methods immediately."))
    elif wc < spec["abs_min_w"]:
        findings.append(("WARN", f"Word count ({wc}w) is below typical {journal} density ({spec['abs_min_w']}w); ensure quantitative findings and implication are present."))
    if not re.search(r"\b(however|yet|despite|nevertheless|remains? (unclear|unknown|poorly understood|elusive|challenging|limited)|little is known|paradox|unmet|challenge|question of whether)\b", text, re.I):
        findings.append(("WARN", "No explicit Gap/Problem pivot detected ('However, ... remains poorly understood')."))
    if not re.search(r"\b(here,?\s+we|in this study,?\s+we|we here|we show|we identify|we demonstrate|we present|we develop|we report)\b", text, re.I):
        findings.append(("WARN", "No clear main-result pivot ('Here, we show/identify/present...')."))
    # Empirical Abstract quantitative & stat-equation restraint (n=775 published 2025-26 CNS Abstracts: med=0.0 nums, 98.2% zero stat equations!)
    ab_clean = re.sub(r"\$\^\{[^}]+\}\$|\$_\{[^}]+\}\$|\*\*|\*|`", "", text)
    ab_pvals = re.findall(r"\b[PpQq]\s*(?:value|val|adj)?\s*[<=>≤≥]\s*[0-9\.]", ab_clean)
    if ab_pvals and journal != "nat_med":
        findings.append(("WARN", f"Raw P-value(s) detected in Abstract ({len(ab_pvals)}); only 0.3% of 1,436 published 2025-26 Abstracts include raw P values (0.0% in NCB/Nat Commun/Cell/Cancer Cell). Move P values to Figures/Results."))
    ab_stat_eq = re.findall(r"(?:\b(?:AUC|AUROC|C-?index|HR|OR|NES|r|ρ|rho)\s*[=<>≤≥]\s*[-−+]?[0-9\.]|\bn\s*=\s*\d+)", ab_clean, re.I)
    ab_quant_nums = re.findall(r"(?:\b\d+(?:,\d+)+(?:\.\d+)?\b|\b\d+(?:\.\d+)?%|\b\d+(?:\.\d+)?\s*(?:µm|μm|mm|cm|fold|-fold|plex|-plex|million|patients|tumou?rs|samples|cohorts|mice|cells|nuclei)\b|\b(?:AUC|AUROC|HR|OR|r|ρ|rho)\s*[=<>≤≥]\s*[-−+]?[0-9\.])", ab_clean, re.I)
    ab_num_lim = spec.get("abs_num_warn", 7)
    if len(ab_stat_eq) >= 2 and journal != "nat_med":
        findings.append(("WARN", f"Stat equations inside Abstract ({len(ab_stat_eq)}: {ab_stat_eq[:5]}); 98.2-100% of published 2025-26 CNS Abstracts contain ZERO inline 'rho=/r=/AUC=/n=' equations! Keep narrative conceptual and retain at most 1 headline predictive/clinical metric if essential."))
    if len(ab_quant_nums) >= ab_num_lim:
        findings.append(("WARN", f"Data-crammed Abstract ({len(ab_quant_nums)} quantitative numbers >= {journal} warn limit {ab_num_lim}; 2025-26 CNS median=0.0, Q75=1-2). Trim secondary micrometer/sub-cohort/correlation numbers to 2-5 crisp headline anchors so the Abstract reads like a published {journal} summary."))
    # Methods-bloat detector
    method_sents = sum(1 for s in sents if re.search(r"\b(seurat|harmony|cellchat|gsea|10x genomics|filtered|normalized|clustered|western blot|qpcr|pcr|flow cytometry|kit|software|pipeline|we collected|we performed|we analyzed)\b", s, re.I))
    if method_sents >= 3 or (len(sents) >= 3 and method_sents / len(sents) >= 0.45):
        findings.append(("FAIL", f"Methods bloat detected ({method_sents}/{len(sents)} method-heavy sentences); compress methodology to <=1 sentence and allocate ~50% to concrete findings."))
    if re.search(r"\[\d+\]|\(\w+ et al\., \d{4}\)", text):
        findings.append(("FAIL", "Citations detected inside Abstract; remove all references from Abstract."))
    scan_chinglish(text, findings)
    return findings


def audit_intro(text: str, spec: dict, journal: str):
    findings = []
    paras = [p.strip() for p in re.split(r"\n{2,}", text.strip()) if len(p.split()) >= 15]
    wc = count_words(text)
    pure_wc = count_words(strip_parens(re.sub(r"\$\^\{[^}]+\}\$|\*\*|\*", "", text)))
    findings.append(("INFO", f"Introduction: {wc} words ({pure_wc}w pure prose excl. parens) across {len(paras)} paragraphs (target for {journal}: {spec['intro_min_w']}-{spec['intro_max_w']}w, med={spec['intro_med_w']}w, 3-4 paras)."))
    if wc > spec["intro_max_w"] + 120:
        findings.append(("WARN", f"Introduction is lengthy ({wc}w vs {journal} norm {spec['intro_min_w']}-{spec['intro_max_w']}w, med={spec['intro_med_w']}w); prune textbook background that does not pay off in Results."))
    elif 150 <= wc < spec["intro_min_w"]:
        findings.append(("WARN", f"Introduction is shorter than {journal} norm ({wc}w < {spec['intro_min_w']}w floor; published {journal} median={spec['intro_med_w']}w). Expand focused P2-P3 biological tension & prior-art contrast."))
    if len(paras) < 2 or len(paras) > 6:
        findings.append(("WARN", f"Paragraph count ({len(paras)}) outside optimal 3-4 paragraph CNS funnel."))
    if not re.search(r"\b(however|yet|despite|nevertheless|remains? (unclear|unknown|poorly understood|elusive|limited|challenging)|little is known|poorly characterized)\b", text, re.I):
        findings.append(("FAIL", "No clear Gap/Unknown statement detected in Introduction."))
    if paras and not re.search(r"\b(here,?\s+we|in this study,?\s+we|to address|to investigate|to elucidate|to overcome|we here)\b", paras[-1], re.I):
        findings.append(("WARN", "Final Introduction paragraph lacks an active 'Here, we...' / 'In this study, we...' approach-and-findings preview."))
    if re.search(r"\[\s*\d+\s*[-–,]\s*\d+(?:\s*,\s*\d+){4,}\s*\]", text):
        findings.append(("WARN", "Heavy citation stuffing (6+ refs clustered together); 95.1% of CNS citations use 1-3 targeted refs per claim (only 2.5% use 5+)."))
    # Also check range stuffing like [1-8] or (1-8)
    for m in re.finditer(r"[\[\(]\s*(\d{1,3})\s*[-–]\s*(\d{1,3})\s*[\]\)]", text):
        if int(m.group(2)) - int(m.group(1)) >= 4:
            findings.append(("WARN", f"Citation range stuffing '{m.group(0)}' ({int(m.group(2))-int(m.group(1))+1} refs in one cluster); split into specific claims with 1-3 refs each."))
            break
    iu, im, _ = extract_citations(text)
    idens = round(100.0 * im / max(1, wc), 2)
    if im > 0 or wc >= 280:
        findings.append(("INFO", f"Introduction citations: {len(iu)} unique refs ({im} mentions, {idens}/100w; CNS median: 21 unique, 4.5/100w)."))
    if wc >= 280 and len(iu) < spec["intro_ref_min"]:
        findings.append(("WARN", f"Introduction is under-cited ({len(iu)} unique refs < {journal} floor {spec['intro_ref_min']}; CNS median 21, 62-69% of P1-P3 sentences cited). Cite disease burden, key axes, and every Gap claim."))
    scan_chinglish(text, findings)
    return findings


def audit_subheadings(text: str, spec: dict, journal: str):
    findings = []
    lines = [re.sub(r"^#+\s*|^\d+[\.\)]\s*|^[-*]\s*", "", ln).strip() for ln in text.strip().splitlines() if ln.strip()]
    findings.append(("INFO", f"Results subheadings: {len(lines)} modules (CNS median: 6-7 modules)."))
    if len(lines) < 4 or len(lines) > 10:
        findings.append(("WARN", f"Module count ({len(lines)}) differs from CNS standard (5-8 modules matching main figures)."))
    long_sh = [ln for ln in lines if count_words(ln) > spec["sub_max_w"]]
    if long_sh:
        findings.append(("WARN", f"{len(long_sh)} subheading(s) exceed {journal} length norm ({spec['sub_max_w']}w), e.g.: '{long_sh[0][:75]}'"))
    if spec.get("style_family") == "cell":
        finite_n = sum(1 for ln in lines if re.search(r"\b(is|are|was|were|drives?|promotes?|reveals?|enhances?|induces?|suppresses?|inhibits?|controls?|regulates?|mediates?|predicts?|identifies?|improves?|reprograms?|requires?|exhibits?|impairs?|attenuates?|potentiates?|increases?|reduces?|correlates?|restores?|localizes?|colocalizes?|organizes?|shapes?|remodels?|rescues?|abolishes?|synergizes?|sensitizes?|reverses?|prevents?|triggers?|orchestrates?|defines?|determines?|links?|uncovers?|establishes?|activates?|limits?|alters?|enables?|boosts?|fuels?|licenses?|governs?)\b", ln, re.I))
        if lines and finite_n / len(lines) < 0.45:
            findings.append(("WARN", f"Cell Press prefers declarative biological-takeaway subheadings (~52%+); only {finite_n}/{len(lines)} contain an active verb."))
    return findings


def audit_results(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    inline_fig = len(re.findall(r"\((?:Extended Data |Supplementary )?(?:Fig(?:s)?\.|Figure(?:s)?)\s*[S]?\d+[a-zA-Z0-9,\s–\-]*\)", text))
    subj_fig = len(re.findall(r"(?:^|[.!?]\s+)(?:Extended Data |Supplementary )?(?:Fig(?:s)?\.|Figure(?:s)?)\s*[S]?\d+[a-zA-Z]?\s+(?:shows?|demonstrates?|illustrates?|depicts?|reveals?|presents?|displays?)", text, re.M))
    findings.append(("INFO", f"Results prose: {wc} words | Figure citations: {inline_fig} inline parenthetical vs {subj_fig} subject-style ('Fig. X shows')."))
    if subj_fig > 0:
        findings.append(("FAIL", f"Detected {subj_fig} subject-style figure citation(s) ('Fig. X shows...'); CNS ratio is 765:1 inline parenthetical '(Fig. 1a)'."))
    if inline_fig == 0 and wc > 120:
        findings.append(("WARN", "No parenthetical figure citations '(Fig. 1a)' detected in Results prose."))
    past_c = len(re.findall(r"\b(was|were|showed|revealed|demonstrated|identified|observed|found|exhibited|increased|reduced|induced|promoted|suppressed|inhibited|performed|analyzed|confirmed|established)\b", text, re.I))
    pres_c = len(re.findall(r"\b(is|are|shows|reveals|demonstrates|identifies|exhibits|increases|reduces|induces|promotes|suppresses|inhibits|confirms|establishes)\b", text, re.I))
    if pres_c > past_c and wc > 100:
        findings.append(("WARN", f"Present tense ({pres_c}) outweighs Past tense ({past_c}) in Results; CNS Results maintain ~4.9:1 Past:Present for empirical observations."))
    if re.search(r"\bdata not shown\b", text, re.I):
        findings.append(("WARN", "'data not shown' detected (only 2.9% of 2025-2026 CNS papers); consider moving to Extended Data / Supplementary Figures."))
    # Overclaiming on computational inference
    if re.search(r"\b(cellchat|nichenet|pseudotime|monocle|trajectory|correlation|kaplan|cox|tcga|bioinformatic)[^\.]{0,80}\b(proved|demonstrated causality|caused|drove)\b", text, re.I):
        findings.append(("FAIL", "Certainty Verb Ladder violation: strong causal verb ('proved/caused/drove') paired with correlative/computational analysis; downgrade to Tier 3/4 ('predicted/indicated/associated with')."))
    ru, rm, _ = extract_citations(text)
    rdens = round(100.0 * rm / max(1, wc), 2)
    if rm > 0 or wc >= 600:
        findings.append(("INFO", f"Results citations: {len(ru)} unique refs ({rm} mentions, {rdens}/100w; CNS 2024-26 median: 31 unique / +27 NEW, ~4/subheading)."))
    if wc >= 600 and len(ru) < spec["res_ref_min"]:
        findings.append(("WARN", f"Results is under-cited ({len(ru)} unique refs < {journal} floor {spec['res_ref_min']}; CNS median 31, 85.3% of subheadings cite >=1 ref!). Cite published signatures/markers, named tools on first use, external cohorts, mouse/assay models, premise pivots & prior concordance."))

    # --- Forensic CNS Prose Realism & Statistical Restraint Checks (calibrated on 1,436 published 2025-26 papers) ---
    prose_lines = [ln for ln in text.splitlines() if not re.match(r"^\s*#{1,4}\s+", ln) and ln.strip() != "---"]
    clean_res = re.sub(r"\$\^\{[^}]+\}\$|\$_\{[^}]+\}\$|\*\*|\*|`", "", "\n".join(prose_lines))
    clean_wc = max(1, count_words(clean_res))

    # 1. P/q/FDR density & Human CNS Median Bullseye detector (Published 2025-26 med = 0.6/1kw, P90 = 5.9/1kw!)
    p_hits = re.findall(r"(?:\b[PpQq]\s*(?:value|val|adj|_?adj)?\s*[<=>≤≥]\s*[0-9\.]|\bFDR\s*[<=>≤≥]\s*[0-9\.])", clean_res)
    p_rate = round(1000.0 * len(p_hits) / clean_wc, 1)
    p_med, p_bull, p_warn, p_fail = CNS_JOURNAL_P_TARGETS.get(journal, (0.6, 2.0, 5.5, 10.0))
    if clean_wc >= 400:
        findings.append(("INFO", f"Results inline P/q/FDR count: {len(p_hits)} ({p_rate}/1,000w; {journal} median={p_med}/1kw, bullseye <= {p_bull}/1kw, P90=5.9/1kw)."))
        if p_rate > p_fail:
            findings.append(("FAIL", f"Severe P-value overload in Results prose ({len(p_hits)} total, {p_rate}/1,000w > {p_fail} redline; {journal} median={p_med}/1kw!). Move exact P/q values to Figure panels, Captions & Source Data. CNS Pattern: replace '... (P = 0.003)' with '... reduced X by 63% (Fig. 2a)' and retain inline P ONLY for primary survival, multivariable Cox/interaction & decisive in vivo endpoints."))
        elif p_rate > p_warn:
            findings.append(("WARN", f"High inline P-value density in Results ({len(p_hits)} total, {p_rate}/1,000w > ceiling {p_warn}/1kw; {journal} median={p_med}/1kw). Trim routine inline P values toward bullseye <= {p_bull}/1kw (e.g., 'Baseline covariates were balanced between groups (Extended Data Fig. 1b)' instead of listing each P value)."))
        elif p_rate > p_bull:
            findings.append(("WARN", f"Results P-value density ({p_rate}/1,000w) is inside safe ceiling but above {journal} Median Bullseye (<= {p_bull}/1kw; published median={p_med}/1kw). Trim secondary inline P values onto figure panels/captions to land near the human CNS median."))

    # 1b. Per-Journal Flexible Non-P inline stat-equation restraint (n=, rho/r=, AUC=, HR=, OR=, C-index=, NES=, log2FC=)
    if clean_wc >= 400:
        n_eq_hits = re.findall(r"\bn\s*=\s*\d+(?:,\d+)*", clean_res)
        corr_eq_hits = re.findall(r"\b(?:AUC|AUROC|C-?index|HR|OR|NES|ARI|r|ρ|rho|log2?FC)\s*[=<>≤≥]\s*[-−+]?[0-9\.]", clean_res, re.I)
        nonp_tot = len(n_eq_hits) + len(corr_eq_hits)
        nonp_rate = round(1000.0 * nonp_tot / clean_wc, 1)
        corr_rate = round(1000.0 * len(corr_eq_hits) / clean_wc, 1)
        n_rate = round(1000.0 * len(n_eq_hits) / clean_wc, 1)
        nonp_med = spec["nonp_med"]
        nonp_bull = spec["nonp_bull"]
        nonp_warn = spec["nonp_warn"]
        findings.append(("INFO", f"Results non-P inline metrics: {nonp_tot} ({nonp_rate}/1,000w: {len(n_eq_hits)} 'n=' [{n_rate}/1kw] + {len(corr_eq_hits)} 'rho/AUC/HR/OR/NES/log2FC=' [{corr_rate}/1kw]; {journal} med={nonp_med}/1kw, flex <= {nonp_bull}/1kw, warn > {nonp_warn}/1kw)."))
        if nonp_rate > nonp_warn or corr_rate > max(6.5, nonp_bull * 0.8):
            findings.append(("WARN", f"High non-P inline metric density in Results ({nonp_tot} hits = {nonp_rate}/1,000w > {journal} limit {nonp_warn}/1kw; published {journal} med={nonp_med}/1kw). Handle flexibly: state each cohort's n naturally ONCE per module ('across 24 patients') instead of repeating '(n = 24)', retain 1 headline AUC/HR/% per key claim, and let Figures/Captions carry secondary rho, log2FC, NES and subgroup AUCs."))

        # 1c. Per-Journal Paren-Stripped Pure-Prose Length & Parenthesis Composition Audit (n=1,436 papers!)
        pm = analyze_parens(clean_res)
        findings.append(("INFO", f"Results pure prose (excl. parens): {pm['pure_w']}w / {pm['raw_w']}w raw ({pm['paren_w']}w = {pm['paren_share_pct']}% inside '(...)'; {journal} pure med={spec['res_pure_med']}w, paren share med={spec['paren_share_med']}%)."))
        findings.append(("INFO", f"Results parentheses (excl. cites): {pm['tot']} ({pm['tot_1kw']}/1kw; {journal} med={spec['paren_tot_med']}) | Fig={pm['n_fig']} (Fig+stat={pm['fig_stat_1kw']}/1kw) | NonFig={pm['n_nf']} (numeric={pm['nf_num_1kw']}/1kw vs {journal} med={spec['paren_nfnum_med']}) | >=3 parens/sent={pm['ge3_pct']}% (max={pm['max_p_sent']}, {journal} med={spec['ge3p_med']}%)."))
        if pm["paren_share_pct"] > spec["paren_share_warn"]:
            findings.append(("WARN", f"Parenthetical hollow-out in Results: {pm['paren_share_pct']}% of Results words ({pm['paren_w']}w) sit inside '(...)' (>{journal} limit {spec['paren_share_warn']}%; published med={spec['paren_share_med']}%). Stripping parens leaves only {pm['pure_w']}w of narrative prose vs {journal} pure median {spec['res_pure_med']}w!"))
        if pm["tot_1kw"] > spec["paren_tot_warn"] or pm["nf_num_1kw"] > spec["paren_nfnum_warn"] or pm["ge3_pct"] > spec["ge3p_warn"]:
            findings.append(("WARN", f"Results parenthesis overload for {journal} (tot={pm['tot_1kw']}/1kw [lim {spec['paren_tot_warn']}], non-Fig numeric={pm['nf_num_1kw']}/1kw [lim {spec['paren_nfnum_warn']}], >=3p sents={pm['ge3_pct']}% [lim {spec['ge3p_warn']}%]). In published CNS papers ~48% of non-Fig parens are brief acronym definitions, NOT stacked stat blocks — offload inline stat parens onto figures/captions and reinvest space into biological narrative!"))
        if pm["raw_w"] >= 1000 and pm["pure_w"] < spec["res_pure_min"]:
            findings.append(("WARN", f"Results pure narrative prose (excl. parens) is thin for {journal} ({pm['pure_w']}w < {spec['res_pure_min']}w floor; {journal} pure med={spec['res_pure_med']}w, raw med={spec['res_med_w']}w). After trimming parenthetical stat dumps, expand mechanistic explanation, biological specificity contrasts & experimental transitions."))

        # 1d. Per-Subheading Zero-Citation Detector (85.3% of CNS Results subheadings cite >=1 ref!)
        sub_blocks = [s.strip() for s in re.split(r"\n(?=##\s+)", text.strip()) if s.strip().startswith("## ")]
        zero_cite_subs = []
        for sb in sub_blocks:
            s_lines = sb.splitlines()
            s_hdr = s_lines[0].lstrip("# ").strip()
            s_body = "\n".join(s_lines[1:]).strip()
            if count_words(s_body) >= 250:
                su, sm, _ = extract_citations(s_body)
                if sm == 0:
                    zero_cite_subs.append(f"'{s_hdr[:50]}' ({count_words(s_body)}w)")
        if zero_cite_subs:
            findings.append(("WARN", f"{len(zero_cite_subs)} Results subheading(s) >=250w contain ZERO inline citations ({', '.join(zero_cite_subs[:4])}; 85.3% of CNS subheadings cite >=1 ref). Anchor published tools, cohorts, pathways or prior benchmarks inside each module."))

    # 2. Monster sentence, burstiness & anti-consecutive bare-NP opener check (Published 2025-26 med mean=27.7w, CV=0.49, <=18w=23.1%, >40w=12.2%, >55w=2.7%)
    if clean_wc >= 400:
        rsents = split_sents(clean_res)
        if rsents:
            slens = [len(s.split()) for s in rsents]
            s_mean = round(sum(slens) / len(slens), 1)
            s_sd = round((sum((l - s_mean) ** 2 for l in slens) / max(1, len(slens) - 1)) ** 0.5, 1) if len(slens) >= 3 else 0.0
            s_cv = round(s_sd / max(1e-6, s_mean), 2)
            short_pct = round(100.0 * sum(1 for l in slens if l <= 18) / len(slens), 1)
            gt40 = round(100.0 * sum(1 for l in slens if l > 40) / len(slens), 1)
            gt55 = round(100.0 * sum(1 for l in slens if l > 55) / len(slens), 1)
            s_max = max(slens)
            findings.append(("INFO", f"Results sentence rhythm: mean={s_mean}w (med 27.7w, bullseye 25-29w) | CV={s_cv} (med 0.49, bullseye 0.44-0.55) | <=18w={short_pct}% (med 23.1%) | >40w={gt40}% (med 12.2%) | >55w={gt55}% (med 2.7%) | max={s_max}w."))
            if s_mean > 42.0 or gt55 > 20.0:
                findings.append(("FAIL", f"Wall-of-text monster sentences in Results (mean={s_mean}w, {gt55}% >55w, max={s_max}w vs CNS median 27.7w / 2.7% >55w). Split stacked clauses into crisp 1-claim sentences (bullseye 25-29w)!"))
            elif s_mean > 34.0 or gt55 > 10.0 or s_max > 85:
                findings.append(("WARN", f"Long compound sentences in Results (mean={s_mean}w, {gt55}% >55w, max={s_max}w); tighten toward 25-29w CNS median cadence."))
            elif gt55 > 4.5 and len(slens) >= 40:
                findings.append(("WARN", f"Paragraph-opening long sentences slightly above human CNS median ({gt55}% >55w vs med 2.7%, max={s_max}w); split 55-65w 'To [verb]..., we...' sentences into 2 crisp sentences (cohort/assay -> key finding)."))
            if len(slens) >= 25 and s_cv < 0.36:
                findings.append(("WARN", f"Low sentence-length burstiness / metronome AI cadence (CV={s_cv} < 0.36, <=18w={short_pct}% vs human CNS median CV=0.49 / 23.1% <=18w). Interleave 1 crisp 10-17w sentence every 3-4 sentences — e.g.: {' | '.join(CNS_SHORT_BURST_MODELS[:2])}"))
            elif len(slens) >= 25 and (s_cv < 0.43 or short_pct < 19.0):
                findings.append(("WARN", f"Sentence burstiness below Human CNS Median Bullseye (CV={s_cv}, <=18w={short_pct}% vs bullseye CV 0.44-0.55, <=18w 20-28%). Add crisp short topic/negative-control sentences — e.g.: '{CNS_SHORT_BURST_MODELS[1]}'"))
            # Anti-consecutive bare article-less NP subject streaks & active human 'We' voice balance (flexible!)
            if len(rsents) >= 30:
                we_re = re.compile(r"^(?:We\b|Here,?\s+we\b|Next,?\s+we\b|Finally,?\s+we\b|To\s+[a-z]+[^\.]{0,120}\bwe\b|(?:Using|By|Combining|Integrating|Applying|Profiling|Comparing)\b[^\.]{0,120}\bwe\b)", re.I)
                nat_open_re = re.compile(r"^(?:We\b|To\b|In\b|By\b|Across\b|Consistent\b|Unlike\b|Although\b|Whereas\b|While\b|However\b|Thus\b|Together\b|Taken\b|Conversely\b|Notably\b|Specifically\b|For\b|Because\b|When\b|After\b|Before\b|The\b|This\b|These\b|Our\b|Using\b|Here\b|Next\b|Finally\b|Moreover\b|Furthermore\b|Neither\b|Both\b|Only\b)", re.I)
                we_pct = round(100.0 * sum(1 for s in rsents if we_re.match(s.strip())) / len(rsents), 1)
                cur_streak = best_streak = 0
                best_ex = ""
                for s in rsents:
                    if not nat_open_re.match(s.strip()):
                        cur_streak += 1
                        if cur_streak > best_streak:
                            best_streak = cur_streak
                            best_ex = s[:75]
                    else:
                        cur_streak = 0
                findings.append(("INFO", f"Results opener voice (flexible): active 'We'={we_pct}% (human target 20-40%) | max consecutive bare-NP streak={best_streak} (target <=3-4)."))
                if best_streak >= 5 or we_pct < 15.0:
                    findings.append(("WARN", f"Executive-summary bare-NP opener streak in Results (max streak={best_streak}, active 'We'={we_pct}%; e.g. '{best_ex}...'). Keep domain terms freely, but break 5+ bare noun-phrase chains by interleaving active 'We next...', 'Using [Tool], we identified...', 'The...', or 'Consistent with...' openings."))

    # 3. Internal notebook/code/sample-ID jargon leaks (Published 2025-26 med = 0.0, P90 = 1.0!)
    jargon_re = re.compile(r"\b(?:[a-z]\d{2}_[A-Za-z0-9_]+|[A-Z]\d+_[A-Z]\d+_[A-Za-z]+|(?:Primary|Temporal|Cohort|Val|Discovery)\d{2,3}|pt\d{1,3}(?:-pre|-post)?|CNA(?:Pure|Gate)|L\d+-H&E|Ensemble-(?:Top)?\d+|F[1-9][a-d]?\b|Panel\s+[A-C]\b|v2\s+slides)\b")
    j_hits = jargon_re.findall(clean_res)
    if len(j_hits) >= 5:
        ex_j = sorted(set(j_hits))[:8]
        findings.append(("FAIL", f"Internal notebook/pipeline/patient-ID jargon leaked into Main Results ({len(j_hits)} hits, e.g. {ex_j}; published CNS median=0.0). Replace with clean biological/cohort prose (e.g. 'the discovery cohort (n = ...)', 'a representative responder', '*POSTN*+ fibroblasts') and move IDs to Methods/Captions/Source Data."))
    elif j_hits:
        findings.append(("WARN", f"Possible internal pipeline/sample-ID jargon in Results ({len(j_hits)} hits: {sorted(set(j_hits))[:6]}); replace with clean biological/cohort names in main prose (ensure 1:1 sync with legends/figures)."))

    # 4. Defensive Kaggle/QC/leakage audit log prose in Main Results (Published 2025-26 med = 0.0, P90 = 0.0!)
    def_re = re.compile(r"\b(without outcome[- ]label leakage|outcome[- ]blind|zero[- ]outcome[- ]peeking|adversarial removal|sensitivity audits?|quarantined|bidirectional rescue disabled|conflict[- ]free|guarding against technical batch|zero batch confounding|negative penalty|fragile antibodies|strictly isolated|overfitted)\b", re.I)
    d_hits = def_re.findall(clean_res)
    if len(d_hits) >= 8:
        findings.append(("FAIL", f"Defensive QC/anti-leakage audit prose saturates Main Results ({len(d_hits)} hits; published CNS median=0.0!). Replace with plain CNS specificity prose: {suggest_lexicon_fixes(d_hits, CNS_DEFENSIVE_REPLACEMENTS)}."))
    elif len(d_hits) >= 1:
        findings.append(("WARN", f"Defensive audit/QC wording in Main Results ({len(d_hits)} hit(s); CNS median=0.0). Suggested CNS replacements: {suggest_lexicon_fixes(d_hits, CNS_DEFENSIVE_REPLACEMENTS)}."))

    # 5. Nested brackets [...] inside parentheses (...) (Published med = 0.0)
    br_hits = re.findall(r"\([^)]*\[[^\]]+\][^)]*\)", clean_res)
    if len(br_hits) >= 3:
        findings.append(("WARN", f"Nested brackets '[...]' inside parentheses '()' detected {len(br_hits)} times in Results (published median=0); move nested subgroup counts/metadata to tables or clean separate clauses."))

    scan_chinglish(text, findings)
    return findings


def audit_discussion(text: str, spec: dict, journal: str):
    findings = []
    paras = [p.strip() for p in re.split(r"\n{2,}", text.strip()) if len(p.split()) >= 15]
    wc = count_words(text)
    pure_wc = count_words(strip_parens(re.sub(r"\$\^\{[^}]+\}\$|\*\*|\*", "", text)))
    findings.append(("INFO", f"Discussion: {wc} words ({pure_wc}w pure prose excl. parens) across {len(paras)} paragraphs (target for {journal}: {spec['disc_min_w']}-{spec['disc_max_w']}w, med={spec['disc_med_w']}w)."))
    disc_floor = spec["disc_min_w"]
    if 250 <= wc < disc_floor:
        findings.append(("WARN", f"Discussion is compressed for {journal} ({wc}w < {disc_floor}w floor; published {journal} median={spec['disc_med_w']}w). Expand comparative literature triangulation (+11-15 NEW refs), concrete translational roadmap, and balanced constructive Limitations."))
    elif wc > spec["disc_max_w"] + 250:
        findings.append(("WARN", f"Discussion exceeds {journal} upper norm ({wc}w > {spec['disc_max_w']}w; median={spec['disc_med_w']}w); tighten repetitive result recaps."))
    if len(paras) >= 3 and count_words(paras[-1]) < 45:
        findings.append(("WARN", f"Closing Discussion paragraph is an ultra-short stub ({count_words(paras[-1])}w < 45w); either fold into the preceding paragraph or flesh out a grounded 60-110w forward-looking horizon."))
    if paras:
        p1 = paras[0]
        if re.search(r"\b(p\s*[<=>]\s*0\.\d+|hr\s*=\s*\d|auc\s*=\s*0\.\d+|\d+\.\d+%)\b", p1, re.I):
            findings.append(("FAIL", "Discussion P1 repeats raw statistics (P/HR/AUC/%); 99.6% of top Discussions open with a conceptual synthesis without raw stat dumps."))
    if not re.search(r"\b(consistent with|in line with|in contrast to|unlike previous|previous studies|prior studies|prior work|in agreement with|whereas)\b", text, re.I):
        findings.append(("WARN", "No explicit literature comparison/triangulation stems detected ('Consistent with...', 'In contrast to...')."))
    has_lim = bool(re.search(r"\b(limitation|limitations of|several limitations|caveat|cannot rule out)\b", text, re.I))
    if spec["disc_lim_mandatory"] and not has_lim:
        findings.append(("FAIL", f"{journal} mandates explicit Limitations (Cell Press requires a dedicated 'Limitations of the study' subheading; Nat Med ~70%)."))
    elif not has_lim:
        findings.append(("WARN", "No explicit scope limitation or caveat detected; consider weaving a constructive 3-part limitation + next-step sentence."))
    if spec.get("style_family") == "cell" and not re.search(r"limitations of the study", text, re.I):
        findings.append(("WARN", "Cell Press expects the exact subheading 'Limitations of the study'."))
    if not re.search(r"\b(therapeutic|clinical|trial|patient stratification|biomarker|target|future studies|prospective|translation)\b", text, re.I):
        findings.append(("WARN", "No forward-looking clinical/translational or future-extension statement detected (present in 76.8% of oncology Discussions)."))
    du, dm, _ = extract_citations(text)
    ddens = round(100.0 * dm / max(1, wc), 2)
    if dm > 0 or wc >= 350:
        findings.append(("INFO", f"Discussion citations: {len(du)} unique refs ({dm} mentions, {ddens}/100w; CNS median: 20 unique / +12 NEW, 1.9/100w)."))
    if wc >= 350 and len(du) < spec["disc_ref_min"]:
        findings.append(("WARN", f"Discussion is under-cited ({len(du)} unique refs < {journal} floor {spec['disc_ref_min']}; CNS median 20 including +11-14 NEW trial/cross-cancer/reconciliation refs)."))
    # Discussion High-Grounding Human CNS Opener Check (550 flagship papers; real human median ~65-74%)
    dsents = split_sents(re.sub(r"\$\^\{[^}]+\}\$|\*\*|\*", "", text))
    if len(dsents) >= 10:
        disc_open_re = re.compile(r"^(?:In (?:this|our|the present|the current) study|In (?:line|contrast|addition|summary|conclusion|support|agreement)|Consistent with|This (?:is consistent|suggests|indicates|may|pattern|finding|study)|These (?:findings|results|data|observations)|Our (?:data|findings|results|study)|We (?:found|show|demonstrate|observed|identified|speculate|propose|hypothesize|have shown)|Here,?\s+we|Together,?|Taken together|However,?|Nevertheless,?|Importantly,?|Notably,?|Interestingly,?|Although\b|While\b|Whereas\b|Unlike\b|First,|Second,|Third,|Finally,|Future (?:studies|work)|Previous (?:studies|reports|work)|Prior (?:studies|reports|work)|A (?:recent|key|notable)|It is (?:important|notable|worth)|To our knowledge|Furthermore,?|Moreover,?|Thus,?|Therefore,?|By contrast)", re.I)
        grounded_d = sum(1 for s in dsents if disc_open_re.match(s.strip()))
        dpct = round(100.0 * grounded_d / len(dsents), 1)
        findings.append(("INFO", f"Discussion CNS opener grounding: {grounded_d}/{len(dsents)} sentences ({dpct}%; target >=55% using verified 550-paper Discussion openers)."))
        if dpct < 45.0:
            findings.append(("WARN", f"Low Discussion CNS opener grounding ({dpct}% < 45%; avoids abstract nominalized openings). Replace abstract openings with high-frequency 550-paper CNS stems: {' | '.join(CNS_DISC_OPENER_MODELS[:6])}"))
    scan_chinglish(text, findings)
    return findings


def audit_cover_letter(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    findings.append(("INFO", f"Cover Letter: {wc} words (target: 300-500 words, <=1 page)."))
    if wc > 550:
        findings.append(("FAIL", f"Cover Letter exceeds 1-page ceiling ({wc}w > 550w); editors triage in 30-60s—cut to 350-480w."))
    elif wc < 200:
        findings.append(("WARN", f"Cover Letter is very short ({wc}w); ensure core advance, journal fit, and all 4 compliance declarations are included."))
    if re.search(r"\b(dear sir|dear madam|to whom it may concern)\b", text, re.I):
        findings.append(("FAIL", "Generic salutation ('Dear Sir/Madam' / 'To Whom It May Concern'); address the specific Editor or 'Dear Editors of [Journal],'"))
    if re.search(r"\b(groundbreaking|paradigm-shifting|revolutionary|first ever|unprecedented|world-leading|extremely significant)\b", text, re.I):
        findings.append(("FAIL", "Empty hype superlative detected ('groundbreaking/revolutionary/first ever'); replace with restrained, evidence-anchored significance."))
    # 4 mandatory compliance statements
    if not re.search(r"\b(original|not been published|not under consideration|unpublished)\b", text, re.I):
        findings.append(("FAIL", "Missing Compliance #1: Originality & exclusivity statement ('not published elsewhere and not under consideration...')."))
    if not re.search(r"\b(all authors|approved)\b", text, re.I):
        findings.append(("WARN", "Missing Compliance #2: All-authors approval statement."))
    if not re.search(r"\b(competing\s+(?:financial\s+|non-financial\s+)?interests?|conflicts?\s+of\s+interest|financial\s+interests?)\b", text, re.I):
        findings.append(("FAIL", "Missing Compliance #3: Competing / conflict of interest declaration."))
    if not re.search(r"\b(ethics|irb|iacuc|helsinki|informed consent|approved by)\b", text, re.I):
        findings.append(("WARN", "Missing Compliance #4 (if human/animal data): IRB/IACUC ethics & informed consent note."))
    if not re.search(r"\b(readership|scope|recent|published in|et al\.,?\s*202\d)\b", text, re.I):
        findings.append(("WARN", "Missing explicit journal-scope fit / citation of 1-2 recent papers from the target journal."))
    elif not re.search(r"\bet al\.,?\s*(?:\(?\d{4}\)?)?", text):
        findings.append(("WARN", "Cover Letter mentions journal scope generically without citing 1-2 specific recent papers ('Author et al., 2024/2025') published in the target journal."))
    if re.search(r"\b[Pp]\s*[<=>]\s*0\.\d+", re.sub(r"\*", "", text)):
        findings.append(("WARN", "Raw P value detected in Cover Letter; keep editor pitch conceptual and effect-size driven (no raw P-value dumps)."))
    return findings


def audit_caption(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    findings.append(("INFO", f"Figure Caption: {wc} words (target for {journal}: <={spec['cap_max_w']}w)."))
    if wc > spec["cap_max_w"]:
        findings.append(("WARN", f"Caption length ({wc}w) exceeds {journal} guideline ({spec['cap_max_w']}w); consolidate repeated stats into a closing sentence."))
    if re.search(r"\b(this figure shows|the figure illustrates|as shown in this figure)\b", text, re.I):
        findings.append(("FAIL", "Avoid 'This figure shows...'; use telegraphic participial syntax ('UMAP projection showing...', 'Box plots comparing...')."))
    if re.search(r"\b(box ?plot|violin|bar ?plot|scatter|kaplan|survival|quantification|comparison)\b", text, re.I):
        if not re.search(r"\bn\s*=\s*\d+|\b\d+\s+(patients|mice|samples|replicates|tumou?rs)\b", text, re.I):
            findings.append(("FAIL", "Quantitative plot detected without explicit sample size 'n' and biological unit."))
        if re.search(r"\bbox ?plot\b", text, re.I) and not re.search(r"\b(median|interquartile|iqr|whisker|quartile)\b", text, re.I):
            findings.append(("FAIL", "Box plot mentioned without defining center line (median), box bounds (IQR/quartiles), and whiskers."))
        if re.search(r"\b(error bar|mean|bar ?plot)\b", text, re.I) and not re.search(r"\b(s\.d\.|s\.e\.m\.|sd|sem|standard deviation|standard error|95%\s*ci)\b", text, re.I):
            findings.append(("WARN", "Error bars / means mentioned without defining dispersion metric (mean +/- s.d. or s.e.m.)."))
        if re.search(r"\bp\s*[<=>]|mann|wilcoxon|t-?test|anova|kruskal|log-?rank|fisher\b", text, re.I) and not re.search(r"\b(two-sided|two-tailed|one-sided|one-tailed)\b", text, re.I):
            findings.append(("WARN", "Statistical test cited without specifying sidedness ('two-sided' / 'two-tailed')."))
    if re.search(r"\b(immunofluorescence|mif|ihc|h&e|microscop|codex|imaging|histolog|spatial|mri)\b", text, re.I):
        if not re.search(r"\bscale bar\b", text, re.I):
            findings.append(("FAIL", "Microscopy / tissue / MRI imaging panel detected without 'Scale bar, XX um/mm/cm' disclosure."))
        elif not re.search(r"scale bar[^\.]{0,25}\b\d+(?:\.\d+)?\s*(?:µm|μm|um|mm|cm)\b", text, re.I):
            findings.append(("WARN", "Scale bar mentioned without an explicit numeric physical unit (e.g., 'Scale bar, 100 um' or 'Scale bar, 1 cm')."))
    if re.search(r"\*\*[pqP]\*\s*[<=>]", text):
        findings.append(("WARN", "Broken Markdown bold/italic collision around significance stars (e.g., '**q* < 0.01'); escape asterisks '\\*\\*q < 0.01' or use plain notation."))
    return findings


def audit_highlights(text: str, spec: dict, journal: str):
    findings = []
    bullets = [re.sub(r"^[-*•\d\.\)]\s*", "", ln).strip() for ln in text.strip().splitlines() if ln.strip()]
    findings.append(("INFO", f"Highlights: {len(bullets)} bullet(s) (Cell Press standard: 3-4 bullets, <=85 chars each)."))
    if len(bullets) < 3 or len(bullets) > 4:
        findings.append(("WARN", f"Bullet count ({len(bullets)}) outside Cell Press standard (3-4 bullets)."))
    over = [(i + 1, len(b), b) for i, b in enumerate(bullets) if len(b) > 85]
    for idx, ch, b in over:
        findings.append(("FAIL", f"Highlight #{idx} exceeds 85-character Cell Press hard limit ({ch} chars): '{b[:60]}...'"))
    return findings


def audit_in_brief(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    findings.append(("INFO", f"In brief / eTOC blurb: {wc} words (Cell Press hard limit: <=50 words, 3rd-person present tense)."))
    if wc > 55:
        findings.append(("FAIL", f"In brief exceeds 50-word Cell Press ceiling ({wc}w)."))
    if re.search(r"\b(we |our )\b", text, re.I):
        findings.append(("FAIL", "First-person ('we/our') detected in In brief; Cell Press requires 3rd-person ('Author et al. reveal that...')."))
    if not re.search(r"\b(et al\.|and colleagues)\b", text, re.I):
        findings.append(("WARN", "Standard Cell Press In brief opens with '[FirstAuthor] et al. [present verb]...' or '[FirstAuthor] and colleagues...'"))
    return findings


def audit_methods(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    passive = len(re.findall(r"\b(was|were)\s+[a-z]+(ed|en|wn|pt|lt)\b", text, re.I))
    active_we = len(re.findall(r"\bwe\s+[a-z]+(ed|d)\b", text, re.I))
    findings.append(("INFO", f"Methods: {wc} words | Past-passive ({passive}) vs Active 'we' ({active_we})."))
    if active_we > 0 and passive / max(1, active_we) < 2.0 and wc > 200:
        findings.append(("WARN", f"Active 'we' ratio is high ({passive}:{active_we}); CNS Methods average 9.89:1 past-passive dominance."))
    if re.search(r"\b(patient|human|biopsy|clinical|cohort|tumor specimen)\b", text, re.I) and not re.search(r"\b(irb|institutional review board|ethics committee|helsinki|informed consent)\b", text, re.I):
        findings.append(("FAIL", "Human specimens mentioned without IRB/ethics approval and written informed consent disclosure."))
    if re.search(r"\b(mouse|mice|murine|xenograft|pdx)\b", text, re.I) and not re.search(r"\b(iacuc|animal care|ethics committee|institutional animal)\b", text, re.I):
        findings.append(("FAIL", "Animal experiments mentioned without IACUC / institutional animal ethics approval."))
    if re.search(r"\b(cell line|hepg2|hela|a549|mcf7|hek293|rt4|t24|mb49|cultured in dmem|rpmi|mccoy)\b", text, re.I):
        has_myco = bool(re.search(r"\bmycoplasma\b", text, re.I))
        has_str = bool(re.search(r"\b(str profiling|str authenticat|short tandem repeat|authenticated by str|cell line authentication)\b", text, re.I))
        if not has_myco or not has_str:
            missing_cl = [x for x, ok in [("STR authentication", has_str), ("mycoplasma testing", has_myco)] if not ok]
            findings.append(("WARN", f"Cell lines mentioned without {' and '.join(missing_cl)} disclosure(s)."))
    if re.search(r"\b(seurat|scanpy|cell ranger|deseq2|harmony|star|bwa|gatk|cellchat|python|r\b)\b", text, re.I) and not re.search(r"\bv?\d+\.\d+(?:\.\d+)?\b", text):
        findings.append(("FAIL", "Bioinformatics software cited without exact version numbers (e.g., Seurat v4.3.0, R v4.3.2)."))
    if wc > 400 and not re.search(r"\b(data availability|code availability|github|zenodo|gse\d+|hra\d+|egas\d+|prjna\d+)\b", text, re.I):
        findings.append(("WARN", "No Data/Code Availability statement or repository accession (GEO/GSA/EGA/GitHub/Zenodo) detected."))
    if spec.get("style_family") == "cell" and wc > 500 and not re.search(r"key resources table|resource availability|quantification and statistical analysis", text, re.I):
        findings.append(("WARN", "Cell Press STAR Methods requires 'KEY RESOURCES TABLE', 'RESOURCE AVAILABILITY', and 'QUANTIFICATION AND STATISTICAL ANALYSIS'."))
    if spec.get("style_family") == "nature" and re.search(r"key resources table", text, re.I):
        findings.append(("WARN", f"Cell Press 'Key Resources Table' detected inside a {journal} Methods file; Nature Portfolio uses a Reporting Summary + Supplementary Tables (remove KRT cross-references from prose before submission)."))
    mu, mm, _ = extract_citations(text)
    if wc >= 1500 and len(mu) < 8:
        findings.append(("WARN", f"Methods section ({wc}w) has only {len(mu)} inline citation(s); Nature Portfolio allocates ~32.4% of total refs (15-27 refs) to Methods software, databases & protocols!"))
    placeholders = re.findall(r"\[(?:Supplier|Cat#|TODO|Zenodo DOI|GEO / GSA|accession placeholder)[^\]]*\]", text, re.I)
    if placeholders:
        findings.append(("WARN", f"Unfilled submission placeholder(s) detected in Methods ({len(placeholders)}): {placeholders[:5]} — fill prior to submission."))
    return findings


def split_full_manuscript(text: str):
    """Split a Markdown/plain manuscript by top-level section headers for --section all."""
    sec_map = {
        "title": "title", "abstract": "abstract", "summary": "abstract",
        "highlights": "highlights", "in brief": "in_brief", "etoc": "in_brief",
        "introduction": "intro", "results": "results", "subheadings": "subheadings",
        "discussion": "discussion", "cover letter": "cover_letter",
        "figure caption": "caption", "figure captions": "caption", "figure legend": "caption",
        "methods": "methods", "star methods": "methods", "materials and methods": "methods",
        "references": "references", "bibliography": "references",
    }
    stop_headers = {
        "authors", "affiliations", "acknowledgements", "acknowledgments",
        "author contributions", "competing interests", "conflict of interest",
        "data availability", "code availability", "funding", "ethics",
        "supplementary", "extended data", "reporting summary",
    }
    sections = {}
    cur = None
    buf = []
    for ln in text.splitlines():
        m = re.match(r"^(#{1,2})\s+(.+)$", ln.strip())
        if m:
            hashes, raw_hdr = m.group(1), m.group(2).strip()
            hdr = raw_hdr.lower().rstrip(":")
            matched = next((v for k, v in sec_map.items() if hdr == k or hdr.startswith(k)), None)
            is_stop = any(hdr == k or hdr.startswith(k) for k in stop_headers)
            if matched and (len(hashes) == 1 or cur != "results"):
                if cur and buf:
                    sections[cur] = "\n".join(buf).strip()
                cur = matched
                buf = []
                continue
            elif is_stop and (len(hashes) == 1 or cur != "results"):
                if cur and buf:
                    sections[cur] = "\n".join(buf).strip()
                cur = None
                buf = []
                continue
        if cur:
            buf.append(ln)
    if cur and buf:
        sections[cur] = "\n".join(buf).strip()
    # Extract Results H2/H3 subheadings automatically if present
    if "results" in sections and "subheadings" not in sections:
        shs = re.findall(r"^#{2,3}\s+(.+)$", sections["results"], re.M)
        if shs:
            sections["subheadings"] = "\n".join(shs)
    return sections


SCAFFOLDS = {
    "mechanistic": """# Manuscript Strategic Scaffold — Mechanistic Axis + Perturbation ({journal})

## Title (Target: {title_w}w | Declarative Causal Clause — 84.3% CNS norm)
- Option 1 (Causal): [Driver/Metabolite/Axis] drives/reprograms [phenotype] via [pathway] in [cancer]
- Option 2 (Therapeutic): Targeting [axis] overcomes [resistance] by restoring [immune/cell state]

## Abstract (Target: {abs_w}w | Hook: Fundamental Biology Paradox — 68.5%)
- [S1-S2 Background + Gap] Broad biological premise -> However, how [X] drives [Y] remains poorly understood.
- [S3 Pivot + <=1s Method] Here, combining [single-cell/spatial profiling] with [in vivo genetic perturbation], we show that [main finding].
- [S4-S6 Quantitative Escalation (~50%)] (1) Cell-state/niche discovery (n = ...); (2) Mechanistic axis; (3) In vivo KO/rescue + human cohort validation.
- [S7 Implication] Together, these findings establish [X-Y axis] and nominate [target] for [cancer] therapy.

## Introduction (Target: 3-4 paras, ~450-530w | Reverse-Engineered from Results!)
- P1 (Broad Stakes — <=10% Results entities): Clinical/biological importance of [cancer/process].
- P2 (Focused Entities — ~37% Results entities): Known biology of ONLY the 2-3 core entities in Results.
- P3 (Strong Mechanistic Gap — 78.7%): However, the causal mechanism linking [A] to [B] remains elusive -> Question/Hypothesis.
- P4 (Approach & Preview): Here, we integrated [...] and demonstrate that [...].

## Results Subheadings (6-7 Domino Modules)
- H1: [Unbiased discovery / human cohort phenotype]
- H2: [Spatial localization / key cellular niche]
- H3: [Transcriptional / metabolic / signaling signature]
- H4: [Upstream driver / molecular interaction]
- H5: [In vivo genetic KO/depletion establishes causal necessity]
- H6: [Pharmacological blockade synergizes with standard therapy / anti-PD-1]
- H7: [Human clinical cohort validation & prognostic relevance]

## Discussion (MIT/Harvard 5-Block Elevation — ZERO raw P values in P1!)
- P1: Unified conceptual model answering Introduction's big question.
- P2: Literature triangulation & paradox reconciliation ('Whereas prior studies..., our data...').
- P3: Mechanistic implications & open upstream/downstream questions.
- P4: Actionable translational roadmap (delivery, combination regimen, patient selection).
- P5 / Limitations of the study: 3-Part Constructive Limitations (Boundary -> Mitigation -> Next step) + Forward-looking close.

## Cover Letter (350-450w, 1 page)
- P1: Targeted Editor salutation + Title + Article type.
- P2: Core paradox resolved + flagship causal evidence (NOT mini-abstract).
- P3: Target journal scope fit + cite 1-2 recent papers in {journal}.
- P4: 4 Compliance statements (Originality, Authorship approval, COI, IRB/IACUC).
""",
    "clinical": """# Manuscript Strategic Scaffold — Clinical Biomarker / Immunotherapy ({journal})

## Title (Target: {title_w}w | Nat Med: Conservative + Colon Trial/Cohort Design; Cancer Cell: Declarative)
- Option 1 (Clinical): [Biomarker / Regimen] in [patient population]: [a phase 1/2 trial / multi-cohort study]
- Option 2 (Translational): [Spatial/Cellular signature] predicts/shapes response and resistance to [therapy] in [cancer]

## Abstract (Target: {abs_w}w | Hook: Clinical Burden / Treatment Resistance — 66.1%)
- [S1-S2] High mortality / low durable response to [standard of care]; predictive biomarkers or resistance mechanisms remain unclear.
- [S3] Here, we profiled [n patients, pre/on-treatment] using [modalities] across [discovery + external validation cohorts].
- [S4-S6] (1) Responder vs non-responder cellular/spatial hallmark (with n, AUC/HR, P); (2) Mechanistic correlate; (3) Independent validation & clinical utility.
- [S7] These findings inform patient stratification and rational combination strategies for [cancer].

## Introduction (3-4 paras | Gap: Clinical Resistance / Biomarker Failure — 71.0%)
- P1: Clinical standard of care & durability/response bottleneck.
- P2: Limitations of existing biomarkers (e.g., PD-L1/TMB) and prior bulk cohorts.
- P3: Sharp clinical/mechanistic gap -> study objective.
- P4: Cohort design + top-line predictive & biological discoveries.

## Results Subheadings (6-7 Clinical -> Mechanistic -> Validation Modules)
- H1: Cohort design, clinical characteristics, and primary outcomes
- H2: Baseline TME / cellular states associated with treatment response
- H3: On-treatment longitudinal remodeling in responders vs non-responders
- H4: Spatial architecture / immune niches distinguishing durable benefit
- H5: Development and external multi-center validation of predictive signature
- H6: Preclinical / mechanistic validation of resistance target

## Discussion (Primary Gravity: Clinical Translation 34.4% + Cohort Limitations 10.2%)
- P1: Conceptual clinical synthesis (zero raw stat dumps).
- P2: Comparison with landmark clinical trials & prior biomarkers.
- P3: Clinical deployment pathway (FFPE/H&E/cfDNA feasibility, adaptive trial design).
- P4 / Limitations of the study: Cohort size/heterogeneity/retrospective caveats -> External validation mitigation -> Prospective trial roadmap.
""",
    "atlas": """# Manuscript Strategic Scaffold — Single-Cell / Spatial Atlas Resource ({journal})

## Title (Target: {title_w}w | Atlas/Landscape NP or Atlas + Verb Hybrid)
- Option 1 (Hybrid): Single-cell and spatial atlas of [cancer] reveals [key ecotype/vulnerability]
- Option 2 (Pure Resource): Pan-cancer human [organ/stage] atlas at single-cell and spatial resolution

## Abstract (Target: {abs_w}w | Hook: TME Architecture 64.5% + Resolution Blindspot 12.8%)
- [S1-S2] TME heterogeneity governs [cancer] progression, yet limited cohort scale and lack of spatial context have hindered systematic mapping.
- [S3] Here, we integrate [N cells, M samples, spatial + scRNA-seq] across [stages/lineages].
- [S4-S6] (1) Recurrent malignant metaprograms; (2) Distinct multicellular ecotypes/niches; (3) Clinical prognosis & therapeutic vulnerability validated orthogonally.
- [S7] This atlas defines shared hallmarks of [disease] and provides a foundational resource for precision oncology.

## Results Subheadings (6-7 Multi-Scale Modules)
- H1: Construction of a multi-omic single-cell and spatial atlas of [disease]
- H2: Recurrent malignant cell states and transcriptional metaprograms
- H3: Remodeling of myeloid and lymphoid immune compartments
- H4: Spatial multicellular neighborhoods and tumor-stroma boundary niches
- H5: Ligand-receptor crosstalk hubs driving immunosuppression
- H6: Distinct TME ecotypes stratify patient survival and therapy response
- H7: Orthogonal mIF / functional validation of lead niche target

## Discussion (Resource Generality 14.7% — 2x higher than Mechanistic!)
- P1: Overarching spatial/ecological organizing principles uncovered by the atlas.
- P2-P3: Cross-cancer generality & reconciliation with prior bulk/small single-cell studies.
- P4: Community utility of the open portal & translational targeting opportunities.
- P5 / Limitations of the study: Treatment-naive balance, panel gene coverage, unmatched longitudinal sampling -> Mitigation & next-gen whole-transcriptome spatial roadmap.
""",
    "evolution": """# Manuscript Strategic Scaffold — Clonal Evolution / Metastasis / Plasticity ({journal})

## Title (Target: {title_w}w | Topic NP 45% or Declarative 44% or Gerund 'Tracking...')
- Option 1 (Gerund): Tracking clonal evolution from precancer to metastasis in [cancer] using [modality]
- Option 2 (Causal): [Metabolic/Niche cue] drives clonal selection and metastatic plasticity in [cancer]

## Abstract (Target: {abs_w}w | Hook: Evolutionary Principle 61.2% + Relapse/Interception 37.5%)
- Focus on pre-existing vs de novo selection, longitudinal trajectory across stages (normal -> precancer -> invasive -> metastasis/recurrence), and early interception window.

## Results Subheadings (6-7 Temporal / Lineage Arc)
- H1: Longitudinal cohort / lineage-tracing architecture
- H2: Genomic & clonal phylogeny across disease stages
- H3: Non-genetic transcriptional plasticity & state transitions
- H4: Microenvironmental co-evolution along the progression trajectory
- H5: Stage-specific driver / resistance clone selection under therapy
- H6: Preclinical interception or adaptive targeting at the vulnerable window

## Discussion (Evolutionary Dynamics 44.9% + Literature Paradigm Contrast 18.0%)
- Contrast linear vs branched/punctuated evolution; reconcile genetic vs epigenetic plasticity; propose evolution-informed adaptive trials or precancer interception.
""",
    "method": """# Manuscript Strategic Scaffold — Computational Tool / AI Foundation Model / Assay ({journal})

## Title (Target: {title_w}w | Nat Methods: Colon Tool Brand 37.5%)
- Option 1 (Brand): [ToolName]: [capability] bridging [modality A] and [modality B]
- Option 2 (Functional NP): A [visual-omics / foundation] model to [solve bottleneck] at single-cell resolution

## Abstract (Target: {abs_w}w | Hook: Technical/Omics Bottleneck — 36.4%, 36x Mechanistic!)
- [S1-S2] Concrete trade-off (resolution vs cost/scalability/modality gap).
- [S3] Here, we present [ToolName], a [architecture/assay] trained/engineered on [scale].
- [S4-S6] (1) Benchmark superiority across X datasets & Y baselines; (2) Distinct modular capabilities; (3) Novel biological/clinical discovery enabled by [ToolName].
- [S7] Open-source availability and broad applicability across tissues and diseases.

## Results Subheadings (6-7 Modular Benchmark + Discovery Chain)
- H1: Overview of [ToolName] architecture and representation learning
- H2: Benchmark 1 — [ToolName] outperforms existing methods in [core task A]
- H3: Benchmark 2 — [ToolName] generalizes across platforms/cohorts in [task B]
- H4: Scalability, runtime, and robustness under noise/dropout
- H5: Biological discovery 1 — applying [ToolName] to [clinical cancer cohort]
- H6: Biological discovery 2 — orthogonal experimental/clinical validation

## Discussion (Method Generality 30.6% + Rigorous Technical Limitations 12.4%)
- Highlight extensibility to new modalities, computational efficiency, failure modes/boundary conditions (batch shift, rare cell types, training bias), and open-source ecosystem roadmap.
""",
}


def run_audit(section: str, journal: str, text: str) -> int:
    spec = JOURNAL_SPECS[journal]
    dispatch = {
        "title": audit_title,
        "abstract": audit_abstract,
        "highlights": audit_highlights,
        "in_brief": audit_in_brief,
        "intro": audit_intro,
        "subheadings": audit_subheadings,
        "results": audit_results,
        "discussion": audit_discussion,
        "cover_letter": audit_cover_letter,
        "caption": audit_caption,
        "methods": audit_methods,
    }
    total_fail = 0
    total_warn = 0

    if section == "all":
        parts = split_full_manuscript(text)
        if not parts:
            print("[ERROR] Could not detect markdown '# Section' headers (e.g., '# Title', '# Abstract', '# Introduction', '# Results', '# Discussion', '# Cover Letter', '# Figure Captions', '# Methods').")
            return 2
        to_check = [(k, v) for k, v in parts.items() if k in dispatch]
    else:
        to_check = [(section, text)]

    print(f"=== CNS Manuscript Audit | Journal: {journal} | Sections: {', '.join(k for k,_ in to_check)} ===")
    for sec_name, sec_txt in to_check:
        res = dispatch[sec_name](sec_txt, spec, journal)
        print(f"\n[{sec_name.upper()}]")
        for level, msg in res:
            print(f"  [{level:4s}] {msg}")
            if level == "FAIL":
                total_fail += 1
            elif level == "WARN":
                total_warn += 1

    # Full-manuscript Main-Text Reference Waterfall Audit (2024-2026 empirical floor: med=62 main refs!)
    if section == "all" and all(k in parts for k in ("intro", "results", "discussion")):
        main_wc = sum(count_words(parts[k]) for k in ("intro", "results", "discussion"))
        iu, _, ic = extract_citations(parts["intro"])
        ru, _, rc = extract_citations(parts["results"])
        du, _, dc = extract_citations(parts["discussion"])
        mu, _, mc = extract_citations(parts.get("methods", ""))
        main_u = iu | ru | du
        all_u = main_u | mu
        res_new = len(ru - iu)
        disc_new = len(du - iu - ru)
        meth_new = len(mu - main_u)
        all_clusters = ic + rc + dc + mc
        if main_wc >= 1000 or len(main_u) > 0:
            print("\n[CITATIONS & REFERENCE WATERFALL]")
            print(f"  [INFO] Waterfall: Intro={len(iu)} | Results={len(ru)} (+{res_new} NEW) | Discussion={len(du)} (+{disc_new} NEW) => MAIN-TEXT UNIQUE={len(main_u)} (target for {journal}: {spec['main_ref_target']}) | Methods=+{meth_new} NEW => TOTAL={len(all_u)}")
            if all_clusters:
                stuffed = sum(1 for c in all_clusters if c >= 5)
                if stuffed > 0:
                    print(f"  [WARN] {stuffed} citation anchor(s) stuff >=5 refs together (95.1% of CNS citations use 1-3 targeted refs per claim).")
                    total_warn += 1
            if main_wc >= 1200 and len(main_u) < spec["main_ref_min"]:
                lvl = "FAIL" if (main_wc >= 2200 and len(main_u) < max(25, spec["main_ref_min"] // 2)) else "WARN"
                print(f"  [{lvl:4s}] Main-Text unique refs ({len(main_u)}) below {journal} empirical floor ({spec['main_ref_min']}; 2024-26 CNS median=62, 75.8% >=50!). Check Intro (>={spec['intro_ref_min']}), Results (>={spec['res_ref_min']}, ~4/subheading across 7 triggers), and Discussion (>={spec['disc_ref_min']}, +11-14 NEW refs). Never fabricate refs; use verifiable [CITE: ...] slots until matched.")
                if lvl == "FAIL":
                    total_fail += 1
                else:
                    total_warn += 1
            # Orphan / Missing Reference Cross-Check against # References list
            if "references" in parts:
                listed_nums = {int(m.group(1)) for m in re.finditer(r"^\s*(\d{1,3})\.\s+", parts["references"], re.M)}
                cited_nums = {int(x.split(":")[1]) for x in all_u if x.startswith("num:")}
                orphans = sorted(listed_nums - cited_nums)
                missing_r = sorted(cited_nums - listed_nums)
                if orphans:
                    print(f"  [FAIL] {len(orphans)} ORPHAN reference(s) listed in # References but NEVER cited in body: {orphans[:15]} — either cite them at matching cohorts/tools/claims in Results/Discussion or remove them!")
                    total_fail += 1
                if missing_r:
                    print(f"  [FAIL] {len(missing_r)} citation number(s) used in body but MISSING from # References: {missing_r[:15]}!")
                    total_fail += 1
            # Strict Sequential First-Appearance Citation Numbering Audit (mandatory in Nature/Science!)
            seq_text = "\n".join(parts[k] for k in ("intro", "results", "discussion") if k in parts)
            first_seq = []
            seen_seq = set()
            for m in re.finditer(r"(?:(?<!10)(?<!mm)(?<!cm)(?<!ml)(?<!µm)\$\^\{(\d{1,3}(?:\s*[,–—\-]\s*\d{1,3})*)\}\$|\[(\d{1,3}(?:\s*[,–—\-]\s*\d{1,3})*)\])", seq_text):
                raw_s = (m.group(1) or m.group(2)).replace("–", "-").replace("—", "-")
                for part in re.split(r"[,;\s]+", raw_s.strip()):
                    if not part:
                        continue
                    mr = re.fullmatch(r"(\d{1,3})-(\d{1,3})", part)
                    ids = list(range(int(mr.group(1)), int(mr.group(2)) + 1)) if mr else ([int(part)] if part.isdigit() else [])
                    for k_id in ids:
                        if 1 <= k_id <= 300 and k_id not in seen_seq:
                            seen_seq.add(k_id)
                            first_seq.append(k_id)
            if len(first_seq) >= 10:
                ooo = [(i + 1, first_seq[i]) for i in range(len(first_seq)) if first_seq[i] != i + 1]
                if len(ooo) >= 3:
                    print(f"  [FAIL] Non-sequential reference numbering ({len(ooo)}/{len(first_seq)} out-of-order first citations; first jumps: {ooo[:6]}). Numbered journals require strict 1, 2, 3... order of first appearance in Intro -> Results -> Discussion!")
                    total_fail += 1

        # Main-Text AI Punctuation & Repetition Realism Audit (calibrated on 1,350 published 2025-26 papers)
        if main_wc >= 1200:
            main_prose = " ".join(parts[k] for k in ("intro", "results", "discussion"))
            main_clean = re.sub(r"\$\^\{[^}]+\}\$|\$_\{[^}]+\}\$|\*\*|\*|`", "", main_prose)
            # Exclude parenthetical (stat; Fig. Xa) semicolons from prose semicolon chain audit!
            no_parens_clean = re.sub(r"\([^)]*\)", " ", main_clean)
            em_rate = round(1000.0 * len(re.findall(r"—|--", main_clean)) / max(1, main_wc), 1)
            semi_prose_rate = round(1000.0 * len(re.findall(r";\s", no_parens_clean)) / max(1, main_wc), 1)
            comma_fig_n = len(re.findall(r"\([^)]*(?:=|[0-9%]),\s*(?:Extended Data |Supplementary )?Fig(?:s)?\.", main_clean))
            print("\n[PROSE REALISM & AI-TELL AUDIT (1,350 Published 2025-26 Papers)]")
            print(f"  [INFO] Punctuation density: em-dash (—)={em_rate}/1kw (med 0.0, bullseye <=0.3) | prose semicolon (;)={semi_prose_rate}/1kw (med 2.4, bullseye 1.0-4.0).")
            if em_rate > 0.8:
                print(f"  [WARN] Em-dash overuse ({em_rate}/1kw vs CNS median 0.0, bullseye <=0.3/1kw); replace '—...—' pairs with commas or crisp separate sentences.")
                total_warn += 1
            if semi_prose_rate > 7.5:
                print(f"  [WARN] Heavy prose semicolon overuse ({semi_prose_rate}/1kw vs CNS median 2.4); break chained prose clauses into crisp periods (keep ';' ONLY inside '(stat; Fig. Xa)').")
                total_warn += 1
            if comma_fig_n >= 8 and spec.get("style_family") == "nature":
                print(f"  [WARN] Parenthetical stat-to-figure separators use commas instead of semicolons ({comma_fig_n}x, e.g., '(n = 24, Fig. 1a)'); Nature house style uses ';' -> '(n = 24; Fig. 1a)'.")
                total_warn += 1
            # Overused editorializing / AI-signature words (>2x across paper)
            rep_map = {"parsimonious": "compact/minimal", "crucially": "notably/(delete)", "critically": "notably/(delete)", "strikingly": "markedly/(delete)", "remarkably": "markedly/(delete)", "pivotal": "central/key", "multifaceted": "diverse", "quarantined": "independent/held-out", "compelling": "strong"}
            overused = [(w, len(re.findall(rf"\b{w}\b", main_clean, re.I))) for w in rep_map]
            overused = [(w, c) for w, c in overused if c >= 3]
            if overused:
                rep_hint = "; ".join(f"'{w}' ({c}x) -> '{rep_map[w]}'" for w, c in overused)
                print(f"  [WARN] Repeated editorializing/AI-tell word(s) (>=3x; cap <=1-2x): {rep_hint}.")
                total_warn += 1
            # Non-CNS / tech-blog / metaphor lexicon (<0.5% in 1,312 published 2025-26 CNS papers; median = 0!)
            alien_lex = re.findall(r"\b(audited|rigorous audit|quarantined|obliterates?|crosswalk|capitalis(?:ing|ed)|capitaliz(?:ing|ed)|over-optimistic|honest (?:optical )?blind spot|upgraded clinical|locked [^\.,]{1,20} atlas|phase cliff|division of labou?r|triage cascade|parsimonious|habitats|descriptors|portals|cleanly|decodes?)\b", main_clean, re.I)
            if len(alien_lex) >= 1:
                print(f"  [WARN] Non-CNS / tech-blog lexicon detected ({len(alien_lex)} hit(s); CNS median=0!). Exact CNS replacements: {suggest_lexicon_fixes(alien_lex, CNS_LEXICON_REPLACEMENTS, 8)}.")
                total_warn += 1
            # Invented 3+ part multi-hyphen pre-modifier stacks (0.0% in 1,312 CNS papers!)
            h_stacks = re.findall(r"\b[a-z]{3,}-[a-z]{2,}-[a-z]{3,}(?:-[a-z]{2,})?\b", main_clean)
            ok_hyph = {"non-small-cell", "cell-to-cell", "single-cell-level", "dose-response", "leave-one-out", "end-to-end", "anti-pd-1", "anti-pd-l1", "anti-ctla-4", "head-and-neck", "standard-of-care", "real-world-data", "loss-of-function", "gain-of-function", "time-to-event", "one-to-one", "up-to-date", "step-by-step", "side-by-side", "short-term", "long-term", "progression-free-survival", "disease-free-survival"}
            h_stacks = [h for h in h_stacks if h.lower() not in ok_hyph]
            if len(h_stacks) >= 2:
                print(f"  [WARN] Invented 3+ part multi-hyphen compound stack(s) ({len(h_stacks)} hit(s); CNS median=0!). Unpack into plain prepositional CNS English: {suggest_hyphen_unpacks(h_stacks, 7)}.")
                total_warn += 1
            # AI-tell 2-part modifier stacks that depress 2-gram CNS grounding (references/08 §18.2)
            stack2_re = re.compile(r"\b(two-feature|three-feature|same-section|single-marker|single-metric|batch-matched|multi-compartment|macro-architectural|ambient-rna|zero-shot|out-of-fold|within-batch|per-slide|bladder-wall|dendritic-cell|signed-z)\b", re.I)
            h2_hits = stack2_re.findall(main_clean)
            if len(h2_hits) >= 3:
                print(f"  [WARN] Frequent AI-tell 2-part hyphen modifier stacks ({len(h2_hits)} hit(s); pulls 2-gram grounding below 76% CNS median). Unpack: {suggest_lexicon_fixes(h2_hits, CNS_2PART_STACK_REPLACEMENTS, 7)}.")
                total_warn += 1
            # Detect named public cohorts/tools in Results missing citations
            named_tools = sorted(set(re.findall(r"\b(Seurat|Scanpy|Harmony|UCell|ESTIMATE|VALIS|edgeR|DESeq2|DepMap|PRISM|GDSC2|CCLE|RCTD|CellChat|CellPhoneDB|NicheNet|SCENIC|Slingshot|Monocle|H-optimus-0|UNI2?-h?|CONCH|MUSK|phikon-v2|Virchow|TCGA-[A-Z]{2,5}|GSE\d{4,7}|NCT\d{6,9})\b", parts["results"])))
            if named_tools and len(ru) < spec["res_ref_min"]:
                print(f"  [INFO] Named tools/cohorts/trials in Results that can naturally raise Results citations ({len(named_tools)} detected): {named_tools[:12]}")

            # --- Main-Text Raw vs Paren-Stripped Pure-Prose Length Audit (Per-Journal or ~6,000w General Default) ---
            res_prose_lines = [ln for ln in parts["results"].splitlines() if not re.match(r"^\s*#{1,4}\s+", ln) and ln.strip() != "---"]
            res_clean_sc = re.sub(r"\$\^\{[^}]+\}\$|\$_\{[^}]+\}\$|\*\*|\*|`", "", "\n".join(res_prose_lines))
            intro_clean_sc = re.sub(r"\$\^\{[^}]+\}\$|\$_\{[^}]+\}\$|\*\*|\*|`", "", parts["intro"])
            disc_clean_sc = re.sub(r"\$\^\{[^}]+\}\$|\$_\{[^}]+\}\$|\*\*|\*|`", "", parts["discussion"])
            in_raw_sc, in_pure_sc = count_words(intro_clean_sc), count_words(strip_parens(intro_clean_sc))
            ds_raw_sc, ds_pure_sc = count_words(disc_clean_sc), count_words(strip_parens(disc_clean_sc))
            pm_sc = analyze_parens(res_clean_sc)
            main_raw_sc = in_raw_sc + pm_sc["raw_w"] + ds_raw_sc
            main_pure_sc = in_pure_sc + pm_sc["pure_w"] + ds_pure_sc
            main_paren_pct_sc = round(100.0 * max(0, main_raw_sc - main_pure_sc) / max(1, main_raw_sc), 1)
            print(f"\n[SECTION & PURE-PROSE LENGTH AUDIT — Target: {journal} (~{spec['main_target_w']}w raw | pure floor >={spec['main_pure_min']}w)]")
            print(f"  [INFO] Main Text (Intro+Results+Disc): raw={main_raw_sc}w -> pure_prose={main_pure_sc}w ({main_raw_sc - main_pure_sc}w = {main_paren_pct_sc}% inside parens) | Intro {in_raw_sc}w ({in_pure_sc}w pure) | Results {pm_sc['raw_w']}w ({pm_sc['pure_w']}w pure, {pm_sc['paren_share_pct']}% parens) | Disc {ds_raw_sc}w ({ds_pure_sc}w pure).")
            if main_raw_sc >= 1500 and (main_raw_sc < spec["main_min_w"] or main_pure_sc < spec["main_pure_min"]):
                short_pure = max(0, spec["main_pure_min"] - main_pure_sc)
                print(f"  [WARN] Main Text is shorter than {journal} target (raw={main_raw_sc}w vs target ~{spec['main_target_w']}w [floor {spec['main_min_w']}w]; pure prose excl. parens={main_pure_sc}w vs floor {spec['main_pure_min']}w, short by ~{short_pure}w!). Once bloated stat parentheses are trimmed, reinvest words into mechanistic narrative, specificity contrasts & comparative Discussion.")
                total_warn += 1
            elif main_raw_sc > spec["main_max_w"] + 500:
                print(f"  [WARN] Main Text exceeds {journal} upper norm (raw={main_raw_sc}w > {spec['main_max_w']}w; target ~{spec['main_target_w']}w); tighten secondary subgroup descriptions or move technical details to Methods.")
                total_warn += 1

            # --- Human CNS Median Scorecard (Per-Journal Bullseye vs Boundary-Hugging vs Out-of-Range) ---
            res_wc_sc = max(1, pm_sc["raw_w"])
            res_p_n = len(re.findall(r"(?:\b[PpQq]\s*(?:value|val|adj|_?adj)?\s*[<=>≤≥]\s*[0-9\.]|\bFDR\s*[<=>≤≥]\s*[0-9\.])", res_clean_sc))
            res_p_rate = round(1000.0 * res_p_n / res_wc_sc, 1)
            p_med_sc, p_bull_sc, p_warn_sc, _ = CNS_JOURNAL_P_TARGETS.get(journal, (0.6, 2.0, 5.5, 10.0))
            res_sents_sc = split_sents(res_clean_sc)
            sc_slens = [len(s.split()) for s in res_sents_sc] if res_sents_sc else [27]
            sc_mean = round(sum(sc_slens) / len(sc_slens), 1)
            sc_sd = (sum((l - sc_mean) ** 2 for l in sc_slens) / max(1, len(sc_slens) - 1)) ** 0.5 if len(sc_slens) >= 3 else 13.0
            sc_cv = round(sc_sd / max(1e-6, sc_mean), 2)
            sc_short = round(100.0 * sum(1 for l in sc_slens if l <= 18) / len(sc_slens), 1)
            sc_gt40 = round(100.0 * sum(1 for l in sc_slens if l > 40) / len(sc_slens), 1)
            sc_ai_total = len(alien_lex) + len(h_stacks) + len(h2_hits) + len(re.findall(r"\b(without outcome[- ]label leakage|outcome[- ]blind|zero[- ]outcome[- ]peeking|adversarial removal|sensitivity audits?|quarantined|bidirectional rescue disabled|guarding against technical batch|zero batch confounding|negative penalty|fragile antibodies|strictly isolated)\b", res_clean_sc, re.I))

            def _tag(ok_bull: bool, ok_safe: bool) -> str:
                return "BULLSEYE" if ok_bull else ("EDGE->pull to median" if ok_safe else "OUT-OF-RANGE")

            sc_nonp_n = len(re.findall(r"(?:\bn\s*=\s*\d+(?:,\d+)*|\b(?:AUC|AUROC|C-?index|HR|OR|NES|ARI|r|ρ|rho|log2?FC)\s*[=<>≤≥]\s*[-−+]?[0-9\.])", res_clean_sc, re.I))
            sc_nonp_rate = round(1000.0 * sc_nonp_n / res_wc_sc, 1)
            sc_nonp_med = spec["nonp_med"]
            sc_nonp_bull = spec["nonp_bull"]
            sc_nonp_safe = spec["nonp_warn"]

            print(f"\n[HUMAN CNS MEDIAN SCORECARD — Target: {journal} | Aim for BULLSEYE, Not Just Ceiling!]")
            print(f"  - Main Pure Prose (w)   : {main_pure_sc:5d} | Target ~{spec['main_target_w']}w raw (Pure >= {spec['main_pure_min']}w) -> [{_tag(main_pure_sc >= spec['main_pure_min'] and main_raw_sc <= spec['main_max_w'] + 400, main_pure_sc >= int(spec['main_pure_min'] * 0.85))}]")
            print(f"  - Res Paren Share (%)   : {pm_sc['paren_share_pct']:5.1f} | Med {spec['paren_share_med']:4.1f}% (Lim <= {spec['paren_share_warn']:4.1f}%) -> [{_tag(pm_sc['paren_share_pct'] <= spec['paren_share_med'] + 3.0, pm_sc['paren_share_pct'] <= spec['paren_share_warn'])}]")
            print(f"  - Res NF-Num '()' (/1kw): {pm_sc['nf_num_1kw']:5.1f} | Med {spec['paren_nfnum_med']:4.1f}  (Lim <= {spec['paren_nfnum_warn']:4.1f})  -> [{_tag(pm_sc['nf_num_1kw'] <= spec['paren_nfnum_med'] + 4.0, pm_sc['nf_num_1kw'] <= spec['paren_nfnum_warn'])}]")
            print(f"  - Results P/q (/1kw)    : {res_p_rate:5.1f} | Med {p_med_sc:4.1f}  (Bullseye <= {p_bull_sc:3.1f}) -> [{_tag(res_p_rate <= p_bull_sc, res_p_rate <= p_warn_sc)}]")
            print(f"  - Non-P Metrics (/1kw)  : {sc_nonp_rate:5.1f} | Med {sc_nonp_med:4.1f}  (Flex <= {sc_nonp_bull:4.1f})    -> [{_tag(sc_nonp_rate <= sc_nonp_bull, sc_nonp_rate <= sc_nonp_safe)}]")
            print(f"  - Sentence Mean (w)     : {sc_mean:5.1f} | Med 27.7  (Bullseye 25-29)  -> [{_tag(25.0 <= sc_mean <= 29.5, 22.0 <= sc_mean <= 34.0)}]")
            print(f"  - Burstiness CV         : {sc_cv:5.2f} | Med 0.49  (Bullseye 0.44-55)-> [{_tag(0.44 <= sc_cv <= 0.58, sc_cv >= 0.36)}]")
            print(f"  - Short <=18w (%)       : {sc_short:5.1f} | Med 23.1  (Bullseye 20-28%) -> [{_tag(19.5 <= sc_short <= 30.0, 15.0 <= sc_short <= 40.0)}]")
            print(f"  - Monster >40w (%)      : {sc_gt40:5.1f} | Med 12.2  (Bullseye <= 15%) -> [{_tag(sc_gt40 <= 15.5, sc_gt40 <= 21.0)}]")
            print(f"  - Em-dash '—' (/1kw)    : {em_rate:5.1f} | Med  0.0  (Bullseye <= 0.3) -> [{_tag(em_rate <= 0.3, em_rate <= 1.1)}]")
            print(f"  - Prose ';' (/1kw)      : {semi_prose_rate:5.1f} | Med  2.4  (Bullseye 1.0-4.0)-> [{_tag(0.8 <= semi_prose_rate <= 4.5, semi_prose_rate <= 7.5)}]")
            print(f"  - AI-Tell & Hyphen Hits : {sc_ai_total:5d} | Med    0  (Bullseye = 0)    -> [{_tag(sc_ai_total == 0, sc_ai_total <= 3)}]")
            print(f"  - Main Unique Refs      : {len(main_u):5d} | Med   62  (Bullseye 52-72)  -> [{_tag(52 <= len(main_u) <= 78, len(main_u) >= spec['main_ref_min'])}]")

    print(f"\n--- SUMMARY: {total_fail} FAIL(s), {total_warn} WARN(s) ---")
    return 1 if total_fail > 0 else 0


# ---------------------------------------------------------------------------
# 30-Entry-Point 6-Year Oncology Storyline Matcher (6,665 papers, 2020-2026)
# ---------------------------------------------------------------------------
ONCOLOGY_ENTRY_POINTS = [
    ("01_ICB_Resistance_Response", "ICB Primary/Acquired Resistance & Response Prediction", 1.16,
     r"\b(checkpoint blockade|anti-?pd-?1|anti-?pd-?l1|anti-?ctla-?4|immunotherap|\bicb\b|\bici\b|pembrolizumab|nivolumab|atezolizumab|responder|non-?responder)\b",
     "Despite durable responses in a subset of patients, primary/acquired resistance limits ICB efficacy in most cases, yet causal TME/tumor drivers of failure remain unclear.",
     "H1 R vs NR cohort contrast -> H2 Resistant cell state/factor -> H3 Immune exclusion mechanism -> H4 Resistant mouse model -> H5 KO/blockade synergizes with anti-PD-1 -> H6 Multi-cohort response prediction.",
     "Compare directly against PD-L1/TMB; propose biomarker-guided combination sequence."),
    ("02_Spatial_Niche_Exclusion", "Spatial Niche Architecture & Localized Immune Exclusion [HOT 2.28x]", 2.28,
     r"\b(spatial|niches?|cellular neighbou?rhood|invasive margin|tumou?r[- ]stroma|immune exclus|immune[- ]excluded|ecotypes?|visium|xenium|cosmx|merscope|codex|mibi|\bimc\b|\bmif\b)\b",
     "Dissociated scRNA-seq destroys tissue topology, leaving unresolved whether immune suppression is a global tumor state or organized within spatially restricted cellular niches.",
     "H1 Spatial+scRNA atlas -> H2 Cellular neighborhoods (CNs) -> H3 Invasive-margin CD8 exclusion gradient -> H4 Niche L-R hub confirmed by mIF -> H5 Perturbation dismantles barrier in vivo -> H6 Spatial niche prognosis.",
     "Elevate from abundance to spatial topology; reconcile bulk vs spatial studies; caveat gene-panel coverage."),
    ("03_Myeloid_TAM_Neutrophil_CAF", "Myeloid / TAM / Neutrophil / CAF Plasticity & Reprogramming", 1.29,
     r"\b(macrophages?|\btams?\b|myeloid|mdscs?|neutrophils?|\btans?\b|fibroblasts?|\bcafs?\b|dendritic cells?|cdc1|mregdc|microglia|monocytes?|spp1|c1q|trem2)\b",
     "Broad myeloid/CAF depletion strategies have largely failed clinically; what local cues polarize specific suppressive subsets—and how to selectively reprogram rather than deplete them—remains poorly understood.",
     "H1 Focal myeloid/CAF subcluster -> H2 Lineage/trajectory origin -> H3 Spatial/metabolic polarizing cue -> H4 T-cell suppression mechanism -> H5 Selective reprogramming boosts immunity in vivo -> H6 Human survival validation.",
     "Contrast selective reprogramming vs pan-depletion (e.g., CSF1R); align human/mouse nomenclature."),
    ("04_T_Cell_Exhaustion_Tpex_TLS_LN", "T Cell Exhaustion, Tpex Stemness, B Cells/TLS & Draining Lymph Nodes", 1.28,
     r"\b(exhaustion|exhausted|tpex|stem[- ]like t|progenitor exhausted|tcf1|tcf7|tregs?|regulatory t|lymph node|tdln|b cells?|plasma cells?|tertiary lymphoid|\btls\b|tcr repertoire|clonal expansion)\b",
     "Durable antitumor immunity depends on Tpex stemness and TLS/tdLN reservoirs, yet how extra-tumoral niches replenish effectors or why immature TLSs stall in cold tumors remains elusive.",
     "H1 Paired tumor+tdLN/blood scRNA+TCR-seq -> H2 Clonal Tpex->Tex trajectory -> H3 Spatial Tpex/TLS maturation states -> H4 Molecular/metabolic brake -> H5 Intervention preserves stemness/matures TLS + ICB -> H6 Patient durability.",
     "Frame immunity as a multi-organ systemic loop (tdLN+TLS+tumor); discuss surgical timing implications."),
    ("05_Neoadjuvant_Longitudinal_Trial", "Neoadjuvant / Window-of-Opportunity Longitudinal Dynamics [HOT 1.78x]", 1.78,
     r"\b(neoadjuvant|adjuvant|window[- ]of[- ]opportunity|phase [123i]+|clinical trial|on[- ]treatment|pre[- ] and post|paired biops|pathologic(?:al)? (?:complete )?response|\bpcr\b|\bmpr\b|residual disease)\b",
     "Baseline cross-sectional biopsies miss therapy-induced remodeling; paired pre/on-treatment profiling is needed to separate baseline predictors from dynamic mechanisms of pathologic response vs residual disease.",
     "H1 Trial design & pCR/MPR outcomes -> H2 Baseline correlates -> H3 Paired Pre->Post cellular & TCR remodeling -> H4 Residual tumor-bed spatial niche -> H5 Blood correlate -> H6 Preclinical target in non-responders.",
     "Guide adaptive escalation/de-escalation trials; candidly discuss small arm size and biopsy timing."),
    ("06_Precancer_Evolution_Interception", "Precancer -> Invasive Evolution & Early Interception", 0.89,
     r"\b(precancer|pre-?malignant|premalignant|preinvasive|precursor|carcinogenesis|tumou?r initiation|dysplasia|interception|barrett|adenoma|\baah\b|\bais\b|\bmia\b|\bdcis\b|clonal hematopoiesis)\b",
     "Scarcity of premalignant specimens and bulk profiling have left early epithelial-immune co-evolution—and stage-specific targets for precancer interception—poorly charted.",
     "H1 Normal->precancer->invasive atlas -> H2 Early epithelial plasticity -> H3 Innate-to-adaptive immune switch -> H4 Precancer-enriched target -> H5 Early-window (not late) blockade halts progression -> H6 Risk stratification.",
     "Champion the stage-specific interception window; note non-linear progression caveats."),
    ("07_Organ_Metastasis_Systemic", "Organ-Specific Metastasis Tropism & Systemic Host Macroenvironment", 1.08,
     r"\b(metastas|metastatic|brain metast|bone metast|liver metast|lung metast|leptomeningeal|disseminat|organotrop|tropism|colonization|anemia|cachexia|emergency granulopoiesis)\b",
     "How disseminated tumor cells hijack organ-specific resident niches (brain/bone/liver/lung) and reciprocally disrupt systemic host physiology (anemia/myelopoiesis/cachexia) remains poorly understood.",
     "H1 Primary vs organ-metastasis atlas -> H2 Hijacked resident niche cell -> H3 Metabolic/paracrine hijacking axis -> H4 Systemic host pathology -> H5 Niche-specific perturbation blocks colonization -> H6 Human metastasis risk.",
     "Reframe metastasis as organ-ecosystem co-option + systemic disease; contrast site-specific vs pan-metastatic rules."),
    ("08_NonGenetic_Plasticity_DTP_Resistance", "Non-Genetic Plasticity, DTP Persisters & Targeted/Chemo/RT Resistance", 1.23,
     r"\b(plasticity|drug[- ]tolerant|persister|\bdtp\b|targeted therap|tyrosine kinase|\btki\b|\begfr\b|\bkras\b|\balk\b|\bbraf\b|\bparp\b|chemotherap|cisplatin|radiotherap|radioresist|chemoresist|neuroendocrine|transdifferentiation|\bemt\b|stemness)\b",
     "Many tumors relapse on targeted therapy, chemo, or RT without secondary resistance mutations; how reversible non-genetic plasticity and DTP states license escape remains unclear.",
     "H1 Longitudinal mutation-free resistant/DTP state -> H2 Plastic transcriptional/EMT program -> H3 Master TF/signaling driver -> H4 Reversibility/lineage proof -> H5 Synthetic-lethal combo eradicates DTPs -> H6 Relapsed patient validation.",
     "Target transient plasticity before genetic fixation; propose intermittent/combination schedules."),
    ("09_Clonal_Evolution_CIN_ecDNA_cfDNA", "Clonal Evolution, CIN/ecDNA & Liquid Biopsy (cfDNA) Tracking", 1.09,
     r"\b(clonal evolution|subclon|phylogen|chromosomal instability|\bcin\b|aneuploid|whole[- ]genome doubling|\becdna\b|extrachromosomal|structural variant|cell[- ]free dna|\bcfdna\b|\bctdna\b|liquid biopsy|chromothripsis|tracerx)\b",
     "Whether resistant subclones pre-exist at diagnosis or arise de novo—and how CIN/ecDNA/SVs govern fitness dynamically in patients—has been limited by single-timepoint invasive biopsies.",
     "H1 Longitudinal WGS/scWGS phylogeny -> H2 Clone-specific SV/ecDNA cfDNA tracking -> H3 Selective expansion of pre-existing clone -> H4 Matched scRNA phenotype -> H5 Fitness modeling -> H6 Adaptive clinical monitoring.",
     "Contrast pre-existing selection vs de novo mutagenesis; advocate cfDNA-guided adaptive trials."),
    ("10_Antigen_Escape_Immunoediting", "Antigenic Heterogeneity, Neoantigen Loss & Subclonal Immunoediting", 1.26,
     r"\b(neoantigen|antigen presentation|mhc class|\bhla\b|hla[- ]loh|immunoediting|immune escape|immune evasion|antigen loss|immunogenicity|b2m)\b",
     "High TMB fails to ensure durable ICB response when subclonal neoantigens, HLA LOH, or MHC defects allow antigen-negative clones to escape; strategies restoring presentation or bystander killing remain needed.",
     "H1 Clonal vs subclonal neoantigen & HLA editing -> H2 Mechanism of MHC loss/escape -> H3 Mixed-clone in vivo barcoding -> H4 Intervention restores MHC or IFN-g bystander killing -> H5 ICB cohort validation.",
     "Connect genomic neoantigen architecture to epigenetic MHC visibility and antigen-low clone clearance."),
    ("11_Metabolism_Hypoxia_Cell_Death", "Tumor Metabolism, Hypoxia & Novel Cell Death (Ferro/Cuproptosis) [HOT 1.50x]", 1.50,
     r"\b(metabol|lactate|lipid|cholesterol|iron|copper|cuproptosis|ferroptosis|pyroptosis|amino acid|arginine|leucine|tryptophan|aspartate|polyamine|mitochondri|oxphos|glycolys|hypoxi|glutathione|\bros\b|autophagy)\b",
     "How tumor metabolic rewiring and true intratumoral hypoxia couple to regulated cell death (cuproptosis/ferroptosis) or exert dual effects on therapy response vs resistance remains poorly understood.",
     "H1 Metabolic/RCD signature in human tumors -> H2 Spatial co-localization with hypoxic niches -> H3 Enzyme/transporter mechanism -> H4 Genetic+chemical rescue confirms RCD -> H5 Metabolic/diet intervention synergizes with RT/ICB -> H6 Clinical prognosis.",
     "Address tumor-vs-immune metabolic duality and therapeutic safety window."),
    ("12_Epigenetics_Chromatin_Enhancer", "Epigenetic Rewiring, Chromatin Accessibility (scATAC) & Super-Enhancers", 0.85,
     r"\b(epigenet|chromatin|scatac|atac[- ]seq|multiome|enhancer|super[- ]enhancer|methylation|histone|ezh2|ezh1|kdm|dnmt|hdac|swi/snf|arid1a|bivalent|regulon)\b",
     "RNA profiling alone misses cis-regulatory chromatin accessibility and enhancer rewiring that lock in malignant plasticity or T-cell exhaustion.",
     "H1 Multiome (scRNA+scATAC) chromatin map -> H2 Motif/TF footprinting & enhancer-gene links -> H3 CUT&Tag/Hi-C locus proof -> H4 Epigenetic inhibitor reverses exhaustion/boosts immunogenicity -> H5 In vivo CAR-T/ICB synergy.",
     "Highlight reversible epigenetic druggability; caveat spike-in normalization and systemic off-target effects."),
    ("13_RNA_Splicing_Translation_Neoantigen", "RNA Splicing, Translation Rewiring & Cryptic Neoantigens [HOT 1.58x]", 1.58,
     r"\b(splicing|intron retention|translation|ribosom|eif5a|trna|codon|rna modification|m6a|non[- ]canonical|cryptic peptide|frameshift|aberrant peptide)\b",
     "Steady-state mRNA overlooks selective translational control, ribosome pausing, and aberrant splicing that rewire oncogenic proteomes and create shared non-canonical neoantigens.",
     "H1 Ribo-seq/splicing/tRNA screen -> H2 Codon/splice mechanism -> H3 Immunopeptidomics confirms MHC presentation -> H4 Perturbation disrupts oncogenic translation/boosts immunogenicity -> H5 CD8-dependent ICB synergy.",
     "Expand immunotherapy beyond canonical SNV neoantigens into shared translation/splicing antigens."),
    ("14_PTM_Proteogenomics_Secretome", "PTMs, Proteogenomics & Druggable Secretome / Surfaceome", 0.86,
     r"\b(proteogenom|phosphoproteom|proteomic|phosphorylat|ubiquitin|acetylat|lactylat|glycosylat|post[- ]?translational|secreted protein|secretome|surfaceome)\b",
     "Transcriptomic and cell-autonomous genetic screens miss post-translational signaling switches and secreted/surface regulators with direct biologic druggability.",
     "H1 Phosphoproteomic/secretome clinical screen -> H2 Enzyme-substrate/ligand mechanism -> H3 Downstream metabolic/immune cascade -> H4 Phospho-mutant or recombinant biologic validation in vivo -> H5 Human tumor specimens.",
     "Emphasize direct druggability (biologics, ADCs, PROTACs); discuss systemic vs intratumoral delivery."),
    ("15_Cancer_Neuroscience_Innervation", "Cancer Neuroscience, Tumor Innervation & Neuro-Immune Axis [HOT 1.90x]", 1.90,
     r"\b(innervat|neuron|neuronal|nerve|denervat|synap|astrocyte|glioma[- ]neuron|neuro[- ]immune|neurotransmitter|nociceptor|sympathetic|schwann|axon)\b",
     "Tumors are extensively innervated, yet the transcriptional states of tumor-infiltrating nerves and how neural signaling reprograms immune/stromal niches remain uncharted.",
     "H1 Neural tracing+scRNA maps tumor-specific neurons -> H2 3D/spatial nerve-TME colocalization -> H3 Neurotransmitter/synaptic immune-suppression mechanism -> H4 Denervation/receptor blockade sensitizes to ICB -> H5 Neuro-drug repurposing.",
     "Spotlight neuro-oncology drug repurposing while addressing autonomic off-target safety."),
    ("16_Aging_Senescence_SASP", "Aging, Cellular Senescence (SASP) & Aged Microenvironment [HOT 4.07x #1!]", 4.07,
     r"\b(aging|ageing|aged |elderly|senescen|\bsasp\b|p16|p21|inflammaging|age[- ]related|immunosenescence|telomere)\b",
     "Age is the top cancer risk factor, yet preclinical oncology relies on young hosts; how host aging and reversible cellular senescence remodel stromal metabolism and immune escape remains poorly understood.",
     "H1 Young vs aged multi-omics -> H2 Reversible senescence / aged-stroma lipid-SASP cue -> H3 Mechanistic checkpoint/driver -> H4 Age-matched perturbation/senolytic rescue -> H5 Age-stratified clinical prognosis.",
     "Challenge young-mouse bias; advocate age-stratified clinical trials and senomorphic combinations."),
    ("17_Microbiome_Diet_Host_Axis", "Gut/Intratumoral Microbiome, Diet & Microbial Metabolites [HOT 3.30x #2!]", 3.30,
     r"\b(microbio|gut micro|intratumoral bacter|bacteria|fungal|mycobiome|virome|bile acid|short[- ]chain fatty|dietary|diet\b|fasting|\bfmt\b|probiotic)\b",
     "Microbiome associations with cancer and ICB are widespread, yet moving from correlation to causal effector strains, defined microbial metabolites, and host immune sensors remains a key bottleneck.",
     "H1 Multi-cohort metagenomics or spatial intratumoral bacteria -> H2 Causal strain/diet in germ-free/murine models -> H3 Microbial gene/metabolite identification -> H4 Host receptor & immune circuit -> H5 ICB synergy + human validation.",
     "Translate modernized Koch's postulates into defined diets/postbiotics vs variable FMT."),
    ("18_Vascular_Angiogenesis_Pericyte", "Tumor Vasculature, Vascular Normalization & Endothelial/Pericyte Niche", 1.08,
     r"\b(angiogen|vascul|endothelial|\bvegf\b|vegfr|anti[- ]vegf|pericyte|blood[- ]brain barrier|blood[- ]tumor barrier|lymphangiogen|\bhev\b)\b",
     "Anti-VEGF/VEGFR-TKI plus ICB improves initial responses, yet how vascular remodeling balances immune trafficking against hypoxia-induced resistance remains unclear.",
     "H1 EC/pericyte/HEV spatial-single-cell atlas -> H2 Normalization vs hypoxia shift under therapy -> H3 Immune trafficking/Treg/B-cell circuit -> H4 Endothelial/immune Vegfr2 cKO -> H5 Clinical trial translation.",
     "Reconcile vascular normalization vs hypoxia-driven metastasis; optimize combination dosing windows."),
    ("19_ECM_Fibrosis_Mechanics_Coagulation", "ECM Remodeling, Fibrosis Mechanics & Coagulation/Fibrin Barriers [HOT 1.69x]", 1.69,
     r"\b(extracellular matrix|\becm\b|collagen|fibrosis|fibrotic|desmoplas|stiffness|mechanotransduction|yap/taz|fibrin|coagulation|serpin|pai1|integrin)\b",
     "Whether dense ECM, tissue stiffness, and fibrin deposition act solely as passive physical walls or actively signal to organize localized immunosuppressive niches—and how to dismantle them safely—remains unclear.",
     "H1 Spatial/proteomic link of ECM/fibrin to T-cell exclusion -> H2 Tumor vs CAF source -> H3 Mechanical/receptor macrophage programming -> H4 Targeted ECM/PAI1 dismantling restores T cells -> H5 Anti-PD-1 synergy + patient cohort.",
     "Contrast targeted niche dismantling against earlier failed pan-stromal ablation trials."),
    ("20_Sex_Hormone_Obesity_Comorbidity", "Sex Differences, Sex Hormones, Obesity & Metabolic Comorbidities", 0.87,
     r"\b(sex difference|sex[- ]specific|sexual dimorphism|androgen|estrogen|testosterone|y chromosome|loss of y|obesity|obese|adipocyte|adipose|\bmash\b|\bnash\b|fatty liver|colitis[- ]associated|\bibd\b)\b",
     "Biological sex, sex hormones/LOY, and comorbidities (obesity, MASH, IBD) strongly sway cancer outcomes and ICB efficacy, yet the cell-intrinsic immune/stromal circuits remain underexplored.",
     "H1 Sex/comorbidity-stratified clinical disparity -> H2 Divergent immune/stromal scRNA/spatial state -> H3 Hormonal/LOY/adipokine mechanism -> H4 Receptor cKO/hormone blockade reverses disparity -> H5 Stratified therapeutic strategy.",
     "Champion sex- and comorbidity-aware precision oncology (e.g., repurposing anti-androgens with ICB)."),
    ("21_Cell_Virus_Vaccine_ADC_Engineering", "Engineered Cell Therapy (CAR-T/TCR-T/NK), Virus, Vaccine & ADCs [HOT 1.85x]", 1.85,
     r"\b(car[- ]?t|tcr[- ]?t|adoptive t cell|adoptive cell|engineered t|til therapy|nk cell therapy|car[- ]?nk|oncolytic virus|cancer vaccine|neoantigen vaccine|mrna vaccine|bispecific|\badc\b)\b",
     "Adoptive cell therapies and biologics stall in solid tumors due to poor trafficking, hostile TMEs, tonic exhaustion, and dose-limiting systemic toxicities.",
     "H1 Rational engineering design -> H2 In vitro potency/stemness -> H3 Solid-tumor infiltration & TME remodeling in vivo -> H4 Multi-model superiority -> H5 Safety/toxicology & human primary cell/Phase 1 proof.",
     "Address GMP manufacturing scalability, lymphodepletion burden, and localized vs systemic safety."),
    ("22_PanCancer_Atlas_Taxonomy_Biomarker", "Pan-Cancer / Multi-Center Atlas, Ecotypes & Deployable Biomarkers", 1.23,
     r"\b(pan-?cancer|multi-?omic|compendium|reference atlas|molecular subtyp|taxonomy|stratification|prognostic signature|biomarker|real[- ]world|multi-?center)\b",
     "Prior small single-center or single-omic studies lacked scale to separate lineage-specific noise from shared pan-cancer hallmarks and clinically deployable ecotypes.",
     "H1 Multi-cohort atlas integration -> H2 Shared malignant metaprograms -> H3 Conserved TME ecotypes -> H4 Histological/clinical outcome links -> H5 Compact external-validated classifier -> H6 Orthogonal mIF/target validation.",
     "Highlight open portal community utility and shared pan-cancer dependencies; note batch/treatment-naive caveats."),
    ("23_AI_Foundation_Models_Comp_Methods", "AI Foundation Models, H&E-to-Omics Bridges & Comp Algorithms [HOT 1.77x]", 1.77,
     r"\b(foundation model|deep learning|graph neural|transformer|histopatholog|whole[- ]slide|h&e image|computational framework|algorithm|deconvolution|benchmark|multimodal ai|machine learning|generative model)\b",
     "High-plex spatial/single-cell profiling is too costly for routine clinics, while existing algorithms trade off accuracy, cross-cohort generalization, and scalability.",
     "H1 Architecture & pretraining scale -> H2 Benchmarks outperforming SOTA -> H3 Zero-shot external generalization & ablations -> H4 Modular downstream tasks -> H5 Novel biological/clinical discovery on slides -> H6 Speed & open-source release.",
     "Devote >=30% of Discussion to clinical H&E deployment, domain-shift failure modes, and scalability."),
    ("24_Pediatric_Rare_Organoid_Models", "Pediatric/Rare Cold Tumors & Faithful Organoid/GEMM Models", 0.96,
     r"\b(pediatric|paediatric|childhood|neuroblastoma|medulloblastoma|rhabdomyosarcoma|osteosarcoma|ewing|dipg|schwannomatosis|rare cancer|organoid|\bpdo\b|gemm|synthetic mouse|ipsc)\b",
     "Pediatric and rare tumors driven by developmental arrest or undruggable fusions suffer from a severe shortage of faithful immunocompetent or developmental preclinical models.",
     "H1 Model/organoid engineering -> H2 Histological & scRNA fidelity vs human tumors -> H3 Developmental/fusion vulnerability mechanism -> H4 Drug/CRISPR screen -> H5 In vivo survival rescue + patient validation.",
     "Emphasize dual value (enabling model platform + actionable therapeutic lead); discuss subtype generalizability."),
    ("25_Ancestry_Ethnic_Exposure_Germline", "Ethnic/Ancestry Disparities, Environmental Exposure & Germline Risk", 0.91,
     r"\b(ancestr|ethnic|east asian|african|hispanic|disparit|germline|hereditary|predisposition|susceptibility|gwas|never[- ]smoker|non[- ]smoker|air pollution|tobacco)\b",
     "Existing atlases underrepresent non-European and never-smoker populations, obscuring ancestry-specific driver interactions and exposure-driven TME trajectories.",
     "H1 Diverse ancestry/exposure multi-omics cohort -> H2 Ancestry/exposure mutational & clonal patterns -> H3 Distinct TME remodeling -> H4 Functional/germline mechanism -> H5 Equitable biomarker/screening impact.",
     "Advocate ancestry-calibrated precision oncology while accounting for environmental confounders."),
    ("26_Oncogene_DDR_cGAS_STING_CRISPR", "Oncogene Signaling, DNA Repair (DDR), cGAS-STING & CRISPR Screens", 0.85,
     r"\b(synthetic lethal|crispr screen|genetic screen|functional screen|dna damage|dna repair|\bddr\b|homologous recombination|replication stress|cgas|sting|interferon|micronuclei|tp53|p53|myc\b|pi3k|akt|mtor|wnt|notch|hippo|yap\b|nf-?kb|stat3|tgf[- ]?β|tgfb|jak/stat|cdk4|rb1|pten|brca)\b",
     "Undruggable oncogenes and DDR defects produce context-dependent survival/immune switches (e.g., chronic cGAS-STING); unbiased functional screens are required to expose synthetic lethalities.",
     "H1 Unbiased CRISPR/drug screen -> H2 Mutant-selective specificity -> H3 Biochemical/DDR/cGAS-STING mechanism -> H4 Epistatic rescue -> H5 In vivo PDX/GEMM efficacy + biomarker-selected human cohort.",
     "Pinpoint exact genetic selection biomarkers and explain context-dependent signaling duality."),
    ("27_Hematologic_Malignancy_BM_Niche", "Hematologic Malignancies (AML/DLBCL/MM/MDS) & Bone Marrow Niche", 0.81,
     r"\b(leukemia|leukaemia|\baml\b|\ball\b|\bcll\b|\bcml\b|lymphoma|\bdlbcl\b|\blbcl\b|myeloma|myelodysplastic|\bmds\b|hematopoie|haematopoie|bone marrow|hspc|\bhsc\b)\b",
     "Hematologic cancers co-opt specialized bone-marrow and lymphoid niches protecting stem clones from therapy, yet non-hematopoietic niche remodeling remains far less charted than malignant genetics.",
     "H1 Malignant+stromal BM/LN atlas -> H2 Spatial LSC/lymphoma microanatomy -> H3 Niche-driven drug/CAR-T resistance axis -> H4 Niche disruption restores sensitivity -> H5 Clinical trial risk stratification.",
     "Integrate malignant genetics with microenvironmental archetypes for frontline stratification."),
    ("28_Innate_NK_gdT_ILC_Platelet_EV", "Non-Classical Innate Immunity (NK/gdT/ILC/Platelet) & EVs [HOT 1.62x]", 1.62,
     r"\b(nk cell|natural killer|γδ t|gamma[- ]delta|ilc\d?|innate lymphoid|nkt cell|mait cell|mast cell|eosinophil|basophil|platelet|complement|extracellular vesicle|exosome)\b",
     "Immuno-oncology focuses heavily on CD8 T cells and TAMs, overlooking innate lymphocytes (NK, ILC, gdT, NKT), platelets, and EVs that can mediate MHC-independent control in cold tumors.",
     "H1 Unbiased enrichment of overlooked innate subset/EV -> H2 Human tumor specialization -> H3 Recruitment/activation/EV cargo circuit -> H4 Lineage depletion/transfer proves causality -> H5 MHC-independent therapy + survival.",
     "Highlight MHC-independent rescue opportunities in cold/MHC-I-deficient tumors."),
    ("29_Therapy_Toxicity_irAE_Decoupling", "Decoupling Therapy Toxicity & irAEs from Anti-Tumor Efficacy", 0.84,
     r"\b(iraes?|immune[- ]related adverse|toxicity|adverse event|cytokine release|\bcrs\b|neurotoxicity|colitis|myocarditis|cardiotoxicity|safety profile|decoupl)\b",
     "Severe irAEs/CRS force therapy discontinuation while broad steroids risk blunting antitumor immunity; targets that selectively decouple toxicity from efficacy remain urgently needed.",
     "H1 Head-to-head human irAE tissue vs responding tumor -> H2 Toxicity-selective mediator -> H3 Dual tumor+toxicity murine model -> H4 Targeted blockade prevents toxicity while preserving/boosting ICB -> H5 Clinical safety+efficacy signal.",
     "Champion targeted anti-cytokine prophylaxis over blunt steroids; outline safety trial endpoints."),
    ("30_Malignant_Heterogeneity_Metaprogram", "Malignant Intratumoral Heterogeneity, Metaprograms & Developmental Hijacking", 0.81,
     r"\b(intratumou?ral heterogeneity|tumou?r heterogeneity|metaprogram|meta[- ]program|malignant states?|developmental program|fetal[- ]like|regenerative[- ]like|hybrid state|cancer stem cell|\bcsc\b)\b",
     "Inter-patient genomic noise obscures recurrent malignant states that converge on conserved developmental/regenerative metaprograms; how these states organize spatially and interconvert remains unclear.",
     "H1 Pan-sample NMF metaprograms -> H2 Developmental/regenerative trajectory alignment -> H3 Spatial co-localization with distinct TME niches -> H4 Master TF/niche transition switch -> H5 State-specific vulnerability & prognosis.",
     "Contrast static subtypes vs plastic metaprogram ecosystems; argue for blocking state transitions."),
]


def match_oncology_storyline(text: str, top_k: int = 3) -> int:
    low = text.lower()
    scored = []
    for eid, name, growth, pat, gap, chain, disc in ONCOLOGY_ENTRY_POINTS:
        matches = re.findall(pat, low, re.I)
        if not matches:
            continue
        uniq = len({m.lower() if isinstance(m, str) else m[0].lower() for m in matches})
        raw_hits = len(matches)
        # Reward keyword breadth (uniq) + depth (log hits) + mild bonus for high-velocity 2024-2026 CNS frontier
        score = round(uniq * 3.0 + math.log1p(raw_hits) * 2.0 + (1.2 if growth >= 1.5 else 0.0), 2)
        scored.append((score, eid, name, growth, uniq, raw_hits, gap, chain, disc))

    scored.sort(key=lambda x: -x[0])
    print("=== 6-Year High-IF Oncology Storyline & Entry-Point Matcher (30 Empirical Playbooks, n=6,665) ===")
    if not scored:
        print("[WARN] No oncology keywords matched; include biological entities, assays, cell types, or clinical endpoints.")
        return 1

    top = scored[:top_k]
    for rank, (sc, eid, name, gr, uq, rh, gap, chain, disc) in enumerate(top, 1):
        badge = "HOT FRONTIER" if gr >= 1.5 else "MAINSTREAM"
        print(f"\n#{rank} [{eid}] {name}  (Score={sc} | {uq} distinct signals, {rh} hits | 6yr growth={gr:.2f}x [{badge}])")
        print(f"  Intro Part-2 Gap   : {gap}")
        print(f"  Results Chain H1->H: {chain}")
        print(f"  Discussion Angle   : {disc}")

    # Suggest Double-Axis CNS Elevation Combo if >= 2 distinct entry points matched
    if len(top) >= 2:
        p1, p2 = top[0], top[1]
        print(f"\n[DOUBLE-AXIS CNS ELEVATION COMBO (Nature/Cell/Cancer Cell Framing)]")
        print(f"  Combine Anchor '{p1[2]}' + Secondary Axis '{p2[2]}':")
        print(f"  -> Position Introduction P2-P3 directly at the INTERSECTION of both axes (never treat them as two separate background paragraphs!),")
        print(f"     chain Results from Axis 1 discovery -> Axis 2 causal mechanism -> In vivo rescue/clinical payoff,")
        print(f"     and close Discussion by resolving how this dual axis generalizes beyond a single tumor type.")

    # Empirical 6-Pillar Proof-of-Novelty Audit (1,960 high-IF papers: CNS vs Tier-3 chasm)
    PROOF_PILLARS = [
        ("P4", "Alternative-Hypothesis Disproof & Specificity Control", "CNS 73.7% vs Tier-3 56.7% (+17.0% #1 chasm!)",
         r"\b(ruling out|exclud(?:ed|ing) the possibility|independent of|unaffected by|did not (?:affect|alter|change)|specific(?:ally)?|selective(?:ly)?|rather than|isotype|multivariate|multivariable|adjust(?:ed|ing) for|not driven by|align(?:ed|ment) (?:with|to) reference)\b",
         "[Zero-Wet-Lab Rescue] Add explicit confounder/alternative-explanation exclusion (e.g., prove signal is independent of total abundance, tumor purity, stage, PD-L1/TMB, or canonical myCAF/TAM labels)."),
        ("P1", "Causal LOF / GOF & Genetic Rescue", "CNS 65.5% vs Tier-3 55.9% (+9.6%)",
         r"\b(knockout|\bko\b|knockdown|crispr|shrna|sirna|genetic (?:ablation|deletion|depletion)|conditional knockout|\bcko\b|dtr|adoptive transfer|overexpress|rescued|abolished|abrogated|restored|depletion)\b",
         "[Targeted Wet-Lab Rescue] Add 1 causal perturbation + rescue pair (KO/shRNA or selective blockade + genetic/ligand rescue) to lift paper from correlative atlas to mechanistic causality."),
        ("P2", "In Vivo Functional / Therapeutic Synergy", "CNS 77.7%",
         r"\b(in vivo|syngeneic|orthotopic|gemm|pdx|xenograft|mice|mouse|murine|anti-?pd-?1|anti-?pd-?l1|synergiz|sensitiz|tumor (?:burden|growth|regression)|prolonged survival|senolytic|denervat)\b",
         "[Targeted Wet-Lab Rescue] Validate functional impact or therapeutic sensitization (e.g., +/- anti-PD-1 or standard-of-care) in an immunocompetent/orthotopic murine or PDO model."),
        ("P5", "Orthogonal Spatial / Protein-Level Validation", "CNS 76.6% / Flagship 78.6%",
         r"\b(multiplex(?:ed)? (?:immunofluorescence|ihc)|\bmif\b|codex|\bimc\b|immunohistochemistry|\bihc\b|flow cytometry|facs|western blot|mass spectrometry|proteomic|rnascope|fish|visium|xenium|cosmx|merscope|tma)\b",
         "[Tissue/Assay Rescue] Confirm lead mRNA/computational finding at protein or intact tissue spatial level (mIF/IHC TMA or FACS) to defeat 'mRNA-only artifact' criticism."),
        ("P3", "Head-to-Head Superiority vs Existing Standard", "Flagship 29.9% (Nat Med/Cancer Cell/Methods)",
         r"\b(outperform|superior to|compared with (?:existing|current|standard|pd-?l1|tmb|tide|bulk|sota)|multivariable|multivariate|independent of pd-?l1|auc|roc|c-?index|benchmark|ablation)\b",
         "[Zero-Wet-Lab Rescue] Add head-to-head benchmark (ROC/C-index/multivariable Cox) directly vs PD-L1, TMB, TNM stage, or published signatures/SOTA models to prove quantifiable incremental gain."),
        ("P6", "Multi-Cohort / Pan-Cancer / Cross-Species Generality", "CNS 37.1% vs Tier-3 27.1% (+10.0%)",
         r"\b(independent (?:validation )?cohorts?|validation cohorts?|external cohorts?|multi-?cohort|pan-?cancer|across (?:multiple|\d+) (?:cancer|tumou?r)|conserved (?:across|between)|human and mouse|patient-derived organoids?|\bpdo\b)\b",
         "[Zero-Wet-Lab Rescue] Validate in >=1 truly external non-TCGA cohort or run pan-cancer specificity analysis (proving either conserved cross-cancer law OR true organ-specific divergence)."),
    ]
    present, missing = [], []
    for code, label, stat, pat, fix in PROOF_PILLARS:
        if re.search(pat, low, re.I):
            present.append((code, label, stat))
        else:
            missing.append((code, label, stat, fix))

    print(f"\n[NOVELTY & 'NO-NOVELTY' REVIEWER RISK AUDIT (1,960 High-IF Papers Benchmark)]")
    print(f"  Proof-of-Novelty Pillars Detected: {len(present)}/6  (Tier-1 CNS >=4/6 threshold: 56.5%; mean CNS=3.53 vs Tier-3=3.13)")
    if present:
        print("  [+] PRESENT : " + ", ".join(f"{c} {lbl}" for c, lbl, _ in present))
    if missing:
        print("  [!] MISSING : " + ", ".join(f"{c} {lbl} ({st})" for c, lbl, st, _ in missing))
    if len(present) <= 2:
        print("  [HIGH RISK] <=2 proof pillars detected! Reviewers are highly likely to label this 'descriptive / incremental / lacks novelty' unless you add missing controls below.")
    elif len(present) == 3:
        print("  [MODERATE RISK] 3/6 pillars present (solid Tier-2/3 base). Adding 1-2 missing pillars below unlocks Flagship/CNS conceptual novelty.")
    else:
        print("  [STRONG] >=4/6 proof pillars present — meets Tier-1 CNS multi-pillar novelty proof threshold; focus on explicit 'X, rather than Y' framing!")

    # Flag empty novelty hype if present in user's draft notes
    hype_hits = re.findall(r"\b(for the first time|first (?:study|report) to|never been (?:studied|reported)|few studies have|novel|groundbreaking|unprecedented)\b", low, re.I)
    if hype_hits:
        uniq_hype = sorted({h.lower() for h in hype_hits})
        print(f"  [HYPE WARNING] Empty novelty claim(s) detected: {uniq_hype} -> Hype Inversion Law: CNS uses 'novel'/'first study' 2.2-5.0x LESS than lower tiers! Replace with structural 'X, rather than Y' contrast.")

    # Print top 3 highest-ROI rescue moves
    if missing:
        print("  Recommended Highest-ROI Anti-'No-Novelty' Additions:")
        for code, label, _, fix in missing[:3]:
            print(f"    - Add {code} ({label}): {fix}")

    print("  4-Point Novelty Echo Formula (Make Novelty Unmissable Without Saying 'Novel'):")
    print("    -> Frame Intro P2-P3, Intro Final Para, Results Proof Pivot, and Discussion P1-P2 around ONE sharp delta:")
    print("       'Whereas prior studies attributed [phenotype] to [existing view Y], our findings establish that [X, rather than Y] governs [outcome] (independent of [Y]).'")
    return 0


# ---------------------------------------------------------------------------
# Physical Millimeter Figure Page-Budget & Overflow Rebalancer (sci-plot linkage)
# ---------------------------------------------------------------------------
FIGURE_PAGE_SPECS = {
    "general":       {"w_mm": 180, "h_mm": 220, "max_main_figs": 7, "hard_max_figs": 8, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "nature":        {"w_mm": 180, "h_mm": 220, "max_main_figs": 5, "hard_max_figs": 6, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "nat_cell_biol": {"w_mm": 180, "h_mm": 220, "max_main_figs": 7, "hard_max_figs": 8, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "nat_commun":    {"w_mm": 180, "h_mm": 220, "max_main_figs": 7, "hard_max_figs": 8, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Supplementary Fig.", "panel_case": "lower"},
    "nat_cancer":    {"w_mm": 180, "h_mm": 220, "max_main_figs": 7, "hard_max_figs": 8, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "nat_methods":   {"w_mm": 180, "h_mm": 220, "max_main_figs": 6, "hard_max_figs": 7, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "nature_sister": {"w_mm": 180, "h_mm": 220, "max_main_figs": 7, "hard_max_figs": 8, "ideal_panels": 8,  "max_panels": 10, "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "nat_med":       {"w_mm": 180, "h_mm": 215, "max_main_figs": 5, "hard_max_figs": 6, "ideal_panels": 6,  "max_panels": 8,  "supp_prefix": "Extended Data Fig.", "panel_case": "lower"},
    "cell":          {"w_mm": 174, "h_mm": 215, "max_main_figs": 7, "hard_max_figs": 7, "ideal_panels": 9,  "max_panels": 11, "supp_prefix": "Figure S",           "panel_case": "upper"},
    "cancer_cell":   {"w_mm": 174, "h_mm": 215, "max_main_figs": 7, "hard_max_figs": 7, "ideal_panels": 9,  "max_panels": 11, "supp_prefix": "Figure S",           "panel_case": "upper"},
    "immunity":      {"w_mm": 174, "h_mm": 215, "max_main_figs": 7, "hard_max_figs": 7, "ideal_panels": 9,  "max_panels": 11, "supp_prefix": "Figure S",           "panel_case": "upper"},
    "science":       {"w_mm": 184, "h_mm": 218, "max_main_figs": 6, "hard_max_figs": 7, "ideal_panels": 9,  "max_panels": 10, "supp_prefix": "Fig. S",             "panel_case": "upper"},
}

# Minimum readable physical panel footprints (w_mm, h_mm), synced 1:1 with sci-plot
# Note: Real visual evidence (MRI/CT, H&E, IHC, mIF/CODEX, gross tumor/IVIS) receives generous Hero Space
# (35-55% of Main Figure area: 174-180 mm full-width hero bands or 115 mm 2/3-width blocks)!
PANEL_FOOTPRINTS_MM = {
    "schematic": (88, 46), "working_model": (88, 46),
    "mouse_timeline_schematic": (88, 28), "cell_assay_schematic": (64, 34), "spatial_workflow_schematic": (76, 38),
    # Real visual / imaging / pathology / radiology Hero footprints (synced with sci-plot)
    "hero_pathology_strip": (174, 72), "hero_mif_codex_panel": (174, 78), "hero_radiology_mri_ct": (174, 66),
    "pathology_he_ihc": (115, 64), "mif_hero": (115, 68), "radiology_mri_ct": (115, 60),
    "gross_tumor_ivis": (115, 58), "organoid_microscopy": (88, 58), "western_blot": (86, 52),
    "spatial_zoom_mif": (88, 60), "histology": (88, 60), "ihc": (88, 60),
    # Analytical single-cell / spatial / clinical / statistical panels (strictly 1 panel = 1 unique letter!)
    "umap": (58, 55), "spatial_map": (58, 55), "atlas_umap": (88, 60),
    "heatmap": (86, 60), "pseudotime_cascade": (86, 60), "dotplot": (88, 55),
    "oncoprint": (86, 68), "km_risk_table": (86, 68), "km": (54, 52),
    "forest_plot": (86, 54), "swimmer": (86, 54),
    "chord": (64, 56), "alluvial": (64, 56), "upset": (68, 54),
    "bar": (43, 42), "box": (43, 42), "violin": (43, 42), "split_violin": (56, 42),
    "raincloud": (48, 44), "paired_slope": (44, 44),
    "lollipop": (62, 46), "diverging_enrichment": (68, 48),
    "volcano": (46, 46), "multi_cluster_volcano": (88, 48),
    "scatter": (46, 46), "roc": (46, 46), "boundary_gradient": (54, 45), "ripley": (52, 45),
    "roe_matrix": (54, 52), "corr_matrix": (54, 52), "neighborhood_matrix": (54, 52),
    "waterfall": (58, 46), "spider": (58, 46), "milo": (58, 46), "shap": (58, 46), "radar": (52, 52),
}

REAL_VISUAL_TYPES = {
    "hero_pathology_strip", "hero_mif_codex_panel", "hero_radiology_mri_ct",
    "pathology_he_ihc", "mif_hero", "radiology_mri_ct", "gross_tumor_ivis",
    "organoid_microscopy", "western_blot", "spatial_zoom_mif", "histology", "ihc",
}

HIGH_DENSITY_DATA_TYPES = {
    "atlas_umap", "spatial_map", "heatmap", "pseudotime_cascade", "dotplot",
    "oncoprint", "km_risk_table", "multi_cluster_volcano", "chord", "alluvial",
    "roe_matrix", "neighborhood_matrix", "swimmer",
}

# Lower triage score = demote to Extended Data / Supplementary FIRST (based on 1,215-paper empirical ratios)
# Note: Flagship representative real images ('visual_hero_image') are protected at priority 93!
ROLE_PRIORITY = {
    "schematic": 100, "working_model": 98, "in_vivo_rescue": 95, "visual_hero_image": 93, "core_discovery": 92,
    "clinical_primary": 88, "spatial_headline": 85, "mechanism_key": 82, "crosstalk_hub": 80,
    "pathway_key": 76, "trajectory_key": 72, "in_vitro_key": 70,
    "marker_dotplot_full": 45, "subgroup_breakdown": 40, "secondary_cohort": 38,
    "extra_imaging_replicates": 36, "method_ablation": 35, "negative_control": 25,
    "qc_batch": 15, "gating_toxicity_ko_check": 10,
}


def shelf_pack_height(panels: list, page_w: float, gap_mm: float = 4.0) -> tuple:
    """2D row shelf-packing simulator returning (total_height_mm, list_of_rows)."""
    if not panels:
        return 0.0, []
    # Sort wide panels first within a figure or preserve narrative order? Preserve narrative order (real figures read a->h!)
    rows = []
    cur_row = []
    cur_w = 0.0
    cur_h = 0.0
    for p in panels:
        pw, ph = p["w_mm"], p["h_mm"]
        need_w = pw if not cur_row else (cur_w + gap_mm + pw)
        if cur_row and need_w > page_w + 0.5:
            rows.append((cur_row, cur_w, cur_h))
            cur_row = [p]
            cur_w = pw
            cur_h = ph
        else:
            cur_row.append(p)
            cur_w = need_w
            cur_h = max(cur_h, ph)
    if cur_row:
        rows.append((cur_row, cur_w, cur_h))
    total_h = sum(r[2] for r in rows) + gap_mm * max(0, len(rows) - 1)
    return round(total_h, 1), rows


def assign_panel_letters(panels: list, case: str = "lower"):
    for idx, p in enumerate(panels):
        ch = chr((ord("a") if case == "lower" else ord("A")) + idx)
        p["panel_letter"] = ch


def plan_and_rebalance_figures(data: dict, journal: str, do_rebalance: bool = False, out_path: str = None) -> int:
    fspec = FIGURE_PAGE_SPECS[journal]
    page_w, page_h = fspec["w_mm"], fspec["h_mm"]
    max_p, max_f = fspec["max_panels"], fspec["max_main_figs"]
    supp_prefix = fspec["supp_prefix"]

    raw_panels = data.get("panels", [])
    main_by_fig = defaultdict(list)
    supp_by_fig = defaultdict(list)

    for idx, item in enumerate(raw_panels):
        ctype = item.get("chart_type", "bar").lower()
        def_w, def_h = PANEL_FOOTPRINTS_MM.get(ctype, (48, 45))
        p = dict(item)
        p["w_mm"] = float(item.get("w_mm", def_w))
        p["h_mm"] = float(item.get("h_mm", def_h))
        role = item.get("role", "mechanism_key")
        p["priority"] = int(item.get("priority", ROLE_PRIORITY.get(role, 60)))
        p["_orig_idx"] = idx
        tier = item.get("tier", "main").lower()
        fnum = int(item.get("fig", 1))
        if tier == "main":
            main_by_fig[fnum].append(p)
        else:
            supp_by_fig[fnum].append(p)

    print(f"=== Physical Millimeter Figure Budget & Packing Audit | Journal: {journal} ({page_w}x{page_h} mm, max {max_f} Main Figs, <={max_p} panels/fig) ===")

    overflows = 0
    actions = []

    def report_layout(label, m_dict, s_dict):
        nonlocal overflows
        ov = 0
        print(f"\n[{label}] Main Figures: {len(m_dict)} (target <={max_f}) | Paired {supp_prefix}: {len(s_dict)}")
        if len(m_dict) > fspec["hard_max_figs"]:
            print(f"  [FAIL] Total Main Figure count ({len(m_dict)}) exceeds {journal} cap ({max_f}, hard {fspec['hard_max_figs']}).")
            ov += 1
        elif len(m_dict) > max_f:
            print(f"  [WARN] Total Main Figure count ({len(m_dict)}) above {journal} typical median ({max_f}); consider compressing.")
        for fn in sorted(m_dict.keys()):
            ps = m_dict[fn]
            h, rows = shelf_pack_height(ps, page_w)
            fill_pct = round(100 * h / page_h, 1)
            status = "OK"
            if h > page_h or len(ps) > max_p:
                status = "OVERFLOW"
                ov += 1
            elif h < page_h * 0.38 and len(ps) <= 3:
                status = "UNDERFILL"
            print(f"  Fig. {fn:2d}: {len(ps):2d} panels | packed={h:5.1f}/{page_h} mm ({fill_pct:5.1f}%) across {len(rows)} row(s) -> [{status}]")
            # Detect sci-plot Track-B merge opportunities
            ctypes = [p.get("chart_type", "") for p in ps]
            if ctypes.count("volcano") >= 3:
                print(f"          [TIP sci-plot] {ctypes.count('volcano')} separate volcanoes -> merge into 1 plot_multi_cluster_volcano() (88x48 mm)!")
            if ctypes.count("violin") >= 3:
                print(f"          [TIP sci-plot] {ctypes.count('violin')} violins -> consider plot_split_violin() to halve panel width!")
            # Check strict 1-Panel = 1-Unique-Letter law (ban multi-chart shared indexing!)
            explicit_letters = [str(p["panel_letter"]).lower() for p in ps if p.get("panel_letter")]
            if len(explicit_letters) != len(set(explicit_letters)):
                print(f"          [WARN 1:1-LETTER] Duplicate panel letter detected in Fig. {fn}! CNS 90.4% rule: 1 independent plot = 1 unique letter (never bundle distinct charts under Fig. {fn}a).")
            for p in ps:
                if int(p.get("bundled_subcharts", 1)) > 1 and p.get("chart_type", "").lower() not in REAL_VISUAL_TYPES:
                    print(f"          [WARN 1:1-LETTER] Panel '{p.get('id','?')}' bundles {p.get('bundled_subcharts')} subcharts under ONE letter; split into separate sequential letters!")
            # Check Real Visual Hero Space Reservation (35-55% of Main Figure!) & Anti-Sparse Visual Density
            vis_ps = [p for p in ps if p.get("chart_type", "").lower() in REAL_VISUAL_TYPES]
            hd_ps = [p for p in ps if p.get("chart_type", "").lower() in HIGH_DENSITY_DATA_TYPES]
            if vis_ps:
                vis_area = sum(p["w_mm"] * p["h_mm"] for p in vis_ps)
                plate_area = max(1.0, page_w * max(h, page_h * 0.60))
                vis_pct = round(100.0 * vis_area / plate_area, 1)
                print(f"          [VISUAL HERO] {len(vis_ps)} real-image panel(s) reserving ~{vis_pct}% of plate area (CNS visual-hero target: 35-55%).")
                for vp in vis_ps:
                    if vp["w_mm"] < 80.0 or vp["h_mm"] < 50.0:
                        print(f"          [WARN VISUAL SIZE] Real image '{vp.get('id','?')}' ({vp['w_mm']:.0f}x{vp['h_mm']:.0f} mm) is too small! Reserve >=88x60 mm (or 115-174 mm Hero Band) in sci-plot.")
            elif not hd_ps and len(ps) >= 4:
                print(f"          [WARN SPARSE-PLATE] Fig. {fn} has 0 real visual images AND 0 high-density composite charts (all basic univariate plots risk >76% white!). Add a representative microscopy/spatial ROI or upgrade to OncoPrint/heatmap/KM+Risk-Table.")
            if ctypes.count("scatter") >= 3:
                print(f"          [TIP ANTI-SPARSE] {ctypes.count('scatter')} separate scatter plots in Main Fig. {fn}; consider summarizing into a clean correlation matrix, lollipop, or paired forest plot (NEVER pad small-n scatters with decorative KDE contours!).")
            if "km" in ctypes:
                print(f"          [TIP HIGH-DENSITY] Bare 'km' detected in Fig. {fn}; upgrade to 'km_risk_table' (95% CI ribbon + aligned Number at risk + HR [95% CI]).")
            if any(c in ("schematic", "working_model", "mouse_timeline_schematic", "cell_assay_schematic", "spatial_workflow_schematic") for c in ctypes):
                print(f"          [TIP SCHEMATIC] Build schematic/timeline/working_model in Fig. {fn} strictly via editable vector graphics (programmatic SVG / R grid / Illustrator / BioRender) — NEVER plain text-box flowcharts AND NEVER direct LLM/diffusion image generation; cross-check 100% of numbers against data panels!")
            # Multi-figure experimental-design / mouse-timeline / spatial-workflow schematic nudge (52-59% of CNS papers have >=2 schematics!)
            has_schem = any(c in ("schematic", "working_model", "mouse_timeline_schematic", "cell_assay_schematic", "spatial_workflow_schematic") for c in ctypes)
            roles_f = {str(p.get("role", "")).lower() for p in ps}
            if not has_schem:
                if "in_vivo_rescue" in roles_f:
                    print(f"          [TIP MULTI-FIG SCHEMATIC] Fig. {fn} covers in vivo experiments without a dosing/timeline diagram! 26-45% of CNS Fig. 5-6 include a compact 'mouse_timeline_schematic' (88x28 mm: Day 0 implant -> treatment -> MRI/harvest) for instant reader clarity.")
                elif "in_vitro_key" in roles_f:
                    print(f"          [TIP MULTI-FIG SCHEMATIC] Fig. {fn} covers in vitro cellular assays without an assay setup diagram; consider a compact 'cell_assay_schematic' (64x34 mm).")
                elif "spatial_headline" in roles_f:
                    print(f"          [TIP MULTI-FIG SCHEMATIC] Fig. {fn} covers spatial analysis without a workflow/distance-ring concept schematic; 21-37% of CNS spatial figures include a compact 'spatial_workflow_schematic' (76x38 mm).")
        sparse_eds = []
        for fn in sorted(s_dict.keys()):
            ps = s_dict[fn]
            h, rows = shelf_pack_height(ps, page_w)
            epct = round(100 * h / page_h, 1)
            st = "OVERFLOW" if h > page_h else ("VERY-SHORT" if (len(ps) <= 4 and epct < 50.0) else "OK")
            if st == "VERY-SHORT":
                sparse_eds.append(fn)
            print(f"  {supp_prefix} {fn}: {len(ps):2d} panels | packed={h:5.1f}/{page_h} mm ({epct:5.1f}%) -> [{st}]")
        if len(sparse_eds) >= 2:
            print(f"  [TIP SUPP-MERGE] {len(sparse_eds)} very short {supp_prefix} plate(s) ({sparse_eds}; <=4 panels & <50% height). Consider merging if they share one theme, while keeping Supp figures clean and spacious (no visual padding!).")
        overflows = ov
        return ov

    ov_before = report_layout("INITIAL DRAFT", main_by_fig, supp_by_fig)

    if do_rebalance and ov_before > 0:
        print("\n=== RUNNING 4-TIER AUTOMATIC OVERFLOW REBALANCING ===")
        # Step A: Within every overflowing Main Fig, demote lowest-priority panels to paired Supp/ED Fig until height <= page_h and count <= max_p
        for fn in sorted(list(main_by_fig.keys())):
            ps = main_by_fig[fn]
            while True:
                h, _ = shelf_pack_height(ps, page_w)
                if h <= page_h and len(ps) <= max_p:
                    break
                # Pick lowest priority panel; if still >75 priority and spare Main Fig slot exists, split module instead!
                cand = min(ps, key=lambda x: (x["priority"], -x["w_mm"] * x["h_mm"]))
                if cand["priority"] >= 75 and len(main_by_fig) < max_f:
                    # Split this Main Fig cleanly into two consecutive Main Figs!
                    mid = len(ps) // 2
                    keep, move = ps[:mid], ps[mid:]
                    # Shift all figs > fn up by +1
                    new_m = defaultdict(list)
                    new_s = defaultdict(list)
                    for k in sorted(main_by_fig.keys(), reverse=True):
                        if k > fn:
                            new_m[k + 1] = main_by_fig[k]
                        elif k == fn:
                            new_m[fn] = keep
                            new_m[fn + 1] = move
                        else:
                            new_m[k] = main_by_fig[k]
                    for k in sorted(supp_by_fig.keys(), reverse=True):
                        new_s[k + 1 if k > fn else k] = supp_by_fig[k]
                    main_by_fig, supp_by_fig = new_m, new_s
                    actions.append(f"SPLIT Fig. {fn} (all high-priority panels) into Fig. {fn} ({len(keep)}p) + Fig. {fn+1} ({len(move)}p) using spare journal Main Fig slot.")
                    break
                else:
                    ps.remove(cand)
                    cand["tier"] = "supp"
                    # Find a non-overflowing paired Supp Fig slot
                    target_s = fn
                    while shelf_pack_height(supp_by_fig[target_s] + [cand], page_w)[0] > page_h:
                        target_s += 1
                    supp_by_fig[target_s].append(cand)
                    actions.append(f"DEMOTE '{cand.get('id', cand.get('label', '?'))}' ({cand.get('role')}, {cand['w_mm']}x{cand['h_mm']}mm, prio={cand['priority']}) from Fig. {fn} -> {supp_prefix} {target_s}.")

        # Step B: If total Main Figures STILL exceed journal hard cap (e.g., 6-7 figs -> Nature 5 figs), merge two lightest adjacent figures & demote spillover
        while len(main_by_fig) > max_f:
            fkeys = sorted(main_by_fig.keys())
            # Pick adjacent pair with smallest combined priority sum (excluding Fig. 1)
            best_pair = min(
                [(fkeys[i], fkeys[i + 1]) for i in range(1, len(fkeys) - 1)],
                key=lambda pair: sum(p["priority"] for p in main_by_fig[pair[0]]) + sum(p["priority"] for p in main_by_fig[pair[1]]),
            )
            a, b = best_pair
            merged = main_by_fig[a] + main_by_fig[b]
            # Demote lowest-priority panels from merged until it fits one page!
            demoted_cnt = 0
            while shelf_pack_height(merged, page_w)[0] > page_h or len(merged) > max_p:
                cand = min(merged, key=lambda x: (x["priority"], -x["w_mm"] * x["h_mm"]))
                merged.remove(cand)
                cand["tier"] = "supp"
                ts = max(supp_by_fig.keys(), default=0)
                if ts == 0 or shelf_pack_height(supp_by_fig[ts] + [cand], page_w)[0] > page_h:
                    ts += 1
                supp_by_fig[ts].append(cand)
                demoted_cnt += 1
            # Re-index Main Figs consecutively 1..K
            new_m = defaultdict(list)
            idx_new = 1
            for k in fkeys:
                if k == a:
                    new_m[idx_new] = merged
                    idx_new += 1
                elif k == b:
                    continue
                else:
                    new_m[idx_new] = main_by_fig[k]
                    idx_new += 1
            main_by_fig = new_m
            actions.append(f"COMPRESS Main Fig count -> {max_f} ({journal} limit): merged old Fig. {a}+Fig. {b} ({demoted_cnt} lower-priority panels moved to {supp_prefix}).")

        for act in actions:
            print("  ->", act)

        # Assign crisp final panel letters a..h / A..I
        for fn, ps in main_by_fig.items():
            assign_panel_letters(ps, fspec["panel_case"])
            for p in ps:
                p["fig"] = fn
                p["tier"] = "main"
        for fn, ps in supp_by_fig.items():
            assign_panel_letters(ps, fspec["panel_case"])
            for p in ps:
                p["fig"] = fn
                p["tier"] = "supp"

        ov_after = report_layout("REBALANCED STORYBOARD", main_by_fig, supp_by_fig)

        # Real Visual Evidence ("Seeing is Believing") Audit & Proactive Recommendation
        all_main_ps = [p for ps in main_by_fig.values() for p in ps]
        vis_figs = sorted({fn for fn, ps in main_by_fig.items() if any(p.get("chart_type", "").lower() in REAL_VISUAL_TYPES for p in ps)})
        n_vis_main = sum(1 for p in all_main_ps if p.get("chart_type", "").lower() in REAL_VISUAL_TYPES)
        if n_vis_main == 0:
            print("\n[VISUAL ANCHOR RECOMMENDATION ('Seeing is Believing' — 65.1% of CNS Manuscripts!)]")
            print("  0 real visual/imaging panels detected in Main Figures. Readers & reviewers trust direct physical images far more than statistics alone:")
            all_types = {p.get("chart_type", "").lower() for p in all_main_ps}
            all_roles = {p.get("role", "").lower() for p in all_main_ps}
            if all_types & {"km", "km_risk_table", "swimmer", "waterfall", "forest_plot"} or "clinical_primary" in all_roles:
                print("    -> Clinical/Cohort Anchor : Recommend pairing pre/post tumor MRI/CT ('radiology_mri_ct' 115x60mm) or H&E pathologic response ('pathology_he_ihc' 115x64mm).")
            if all_types & {"umap", "atlas_umap", "spatial_map", "boundary_gradient", "neighborhood_matrix"} or "spatial_headline" in all_roles:
                print("    -> Spatial/TME Anchor     : Recommend representative H&E + magnified mIF/CODEX/IHC boundary FOV ('hero_mif_codex_panel' 174x78mm or 'mif_hero' 115x68mm).")
            if "in_vivo_rescue" in all_roles:
                print("    -> In Vivo Efficacy Anchor: Recommend gross excised tumors with ruler / IVIS bioluminescence ('gross_tumor_ivis' 115x58mm) + IHC/mIF ('pathology_he_ihc' 115x64mm).")
            print("    -> Layout Guard (sci-plot): Reserve 35-55% of Main Figure area via create_visual_hero_layout() / compose_visual_hero_r() and keep 1 panel = 1 unique letter!")
        else:
            print(f"\n[VISUAL ANCHOR STATUS] {n_vis_main} real visual/imaging panel(s) across {len(vis_figs)}/{len(main_by_fig)} Main Figures (Figs {vis_figs}; CNS benchmark: 39-49% of flagship Main Figs).")

        if out_path:
            final_obj = {
                "journal": journal,
                "canvas_mm": {"w_mm": page_w, "h_mm": page_h},
                "strict_1to1_panel_letters": True,
                "visual_hero_figs": vis_figs,
                "rebalancing_actions": actions,
                "main_figures": {
                    f"Fig. {fn}": [
                        {k: v for k, v in p.items() if k != "_orig_idx"}
                        for p in main_by_fig[fn]
                    ]
                    for fn in sorted(main_by_fig.keys())
                },
                "supp_figures": {
                    f"{supp_prefix} {fn}": [
                        {k: v for k, v in p.items() if k != "_orig_idx"}
                        for p in supp_by_fig[fn]
                    ]
                    for fn in sorted(supp_by_fig.keys())
                },
            }
            Path(out_path).write_text(json.dumps(final_obj, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"\nSaved synchronized storyboard (for both sci-paper-writing & sci-plot) to: {out_path}")
        return 0 if ov_after == 0 else 1

    # Also assign 1-to-1 panel letters, print Visual Anchor check & save --out when 0 overflow (or no --rebalance)
    for fn, ps in main_by_fig.items():
        assign_panel_letters(ps, fspec["panel_case"])
        for p in ps:
            p["fig"] = fn
            p["tier"] = "main"
    for fn, ps in supp_by_fig.items():
        assign_panel_letters(ps, fspec["panel_case"])
        for p in ps:
            p["fig"] = fn
            p["tier"] = "supp"
    all_main_ps = [p for ps in main_by_fig.values() for p in ps]
    vis_figs = sorted({fn for fn, ps in main_by_fig.items() if any(p.get("chart_type", "").lower() in REAL_VISUAL_TYPES for p in ps)})
    n_vis_main = sum(1 for p in all_main_ps if p.get("chart_type", "").lower() in REAL_VISUAL_TYPES)
    if n_vis_main == 0:
        print("\n[VISUAL ANCHOR RECOMMENDATION ('Seeing is Believing' — 65.1% of CNS Manuscripts!)]")
        print("  0 real visual/imaging panels detected in Main Figures! If you have (or can acquire) clinical MRI/CT, H&E, IHC, mIF/CODEX, or gross tumor/IVIS photos, reserve 35-55% Hero Visual Space in 1-2 Main Figures.")
        all_types = {p.get("chart_type", "").lower() for p in all_main_ps}
        all_roles = {p.get("role", "").lower() for p in all_main_ps}
        if all_types & {"km", "km_risk_table", "swimmer", "waterfall", "forest_plot"} or "clinical_primary" in all_roles:
            print("    -> Clinical/Cohort Anchor : Pair pre/post tumor MRI/CT ('radiology_mri_ct' 115x60mm) or H&E pathologic response ('pathology_he_ihc' 115x64mm).")
        if all_types & {"umap", "atlas_umap", "spatial_map", "boundary_gradient", "neighborhood_matrix"} or "spatial_headline" in all_roles:
            print("    -> Spatial/TME Anchor     : Add representative H&E + magnified mIF/CODEX/IHC boundary FOV ('hero_mif_codex_panel' 174x78mm or 'mif_hero' 115x68mm).")
        if "in_vivo_rescue" in all_roles:
            print("    -> In Vivo Efficacy Anchor: Add gross excised tumors with ruler / IVIS bioluminescence ('gross_tumor_ivis' 115x58mm) + IHC/mIF ('pathology_he_ihc' 115x64mm).")
    else:
        print(f"\n[VISUAL ANCHOR STATUS] {n_vis_main} real visual/imaging panel(s) across {len(vis_figs)}/{len(main_by_fig)} Main Figures (Figs {vis_figs}; CNS benchmark: 39-49% of flagship Main Figs).")
    if out_path:
        final_obj = {
            "journal": journal,
            "canvas_mm": {"w_mm": page_w, "h_mm": page_h},
            "strict_1to1_panel_letters": True,
            "visual_hero_figs": vis_figs,
            "rebalancing_actions": actions,
            "main_figures": {
                f"Fig. {fn}": [{k: v for k, v in p.items() if k != "_orig_idx"} for p in main_by_fig[fn]]
                for fn in sorted(main_by_fig.keys())
            },
            "supp_figures": {
                f"{supp_prefix} {fn}": [{k: v for k, v in p.items() if k != "_orig_idx"} for p in supp_by_fig[fn]]
                for fn in sorted(supp_by_fig.keys())
            },
        }
        Path(out_path).write_text(json.dumps(final_obj, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nSaved synchronized storyboard (for both sci-paper-writing & sci-plot) to: {out_path}")
    return 0 if ov_before == 0 else 1


def main():
    p = argparse.ArgumentParser(description="CNS Scientific Manuscript Auditor, Storyline Scaffolder & Figure Page-Budget Rebalancer")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("audit", help="Audit a manuscript section or full markdown manuscript")
    pa.add_argument("--section", required=True, choices=["title", "abstract", "highlights", "in_brief", "intro", "results", "subheadings", "discussion", "cover_letter", "caption", "methods", "all"])
    pa.add_argument("--journal", default="general", choices=list(JOURNAL_SPECS.keys()), help="Target journal profile (default: 'general' = ~6,000-word Main Text CNS standard)")
    pa.add_argument("--file", required=True, help="Path to draft text/markdown file")

    ps = sub.add_parser("scaffold", help="Generate a strategic narrative scaffold by study archetype")
    ps.add_argument("--archetype", required=True, choices=list(SCAFFOLDS.keys()))
    ps.add_argument("--journal", default="general", choices=list(JOURNAL_SPECS.keys()))

    pf = sub.add_parser("plan-figures", help="Check millimeter page-size budgets & rebalance overflowing Main Figures to Extended Data/Supp")
    pf.add_argument("--journal", default="general", choices=list(FIGURE_PAGE_SPECS.keys()))
    pf.add_argument("--input", required=True, help="JSON file with 'panels' list")
    pf.add_argument("--rebalance", action="store_true", help="Automatically demote/split/compress overflowing Main Figures")
    pf.add_argument("--out", default=None, help="Optional path to save finalized storyboard JSON (shared with sci-plot)")

    pm = sub.add_parser("match-storyline", help="Match existing data/results notes against 30 6-year CNS oncology entry points")
    pm.add_argument("--file", default=None, help="Path to results description / notes file")
    pm.add_argument("--text", default=None, help="Inline text summary of existing data and results")
    pm.add_argument("--top", type=int, default=3, help="Number of top entry-point playbooks to return")

    args = p.parse_args()
    if args.cmd == "scaffold":
        spec = JOURNAL_SPECS[args.journal]
        print(SCAFFOLDS[args.archetype].format(
            journal=args.journal,
            title_w=spec["title_max_w"],
            abs_w=spec["abs_max_w"],
        ))
        return 0
    elif args.cmd == "plan-figures":
        data = json.loads(Path(args.input).read_text(encoding="utf-8-sig"))
        return plan_and_rebalance_figures(data, args.journal, do_rebalance=args.rebalance, out_path=args.out)
    elif args.cmd == "match-storyline":
        txt = Path(args.file).read_text(encoding="utf-8") if args.file else (args.text or "")
        return match_oncology_storyline(txt, top_k=args.top)
    else:
        txt = Path(args.file).read_text(encoding="utf-8")
        return run_audit(args.section, args.journal, txt)


if __name__ == "__main__":
    sys.exit(main())
