# Phase 6B: representation and explanation tests on unseen users

- **What it tested:** on the 500 unseen users, representation tests H1–H5 (what the sequence representation adds) and the three-level explanation test H6, which hides the days, features or trees that TRACE ranks highest and compares the score change with hiding random items.
- **Paper items:** Table 8 and Fig. 8 (Section IV-G).
- **Key files:** `H1_H5_FULL_CONTRASTS_HOLM.csv`, `H6_TEMPORAL_CONTRASTS_HOLM.csv`, `H6_FEATURE_CONTRASTS_HOLM.csv`, `H6_TREE_CONTRASTS_HOLM.csv`, `figure_e_three_level_explanation.csv` (the data behind Fig. 8, drawn by `../paper_figures/plot_unseen_explanations.py`).
- **Code:** `reproducibility_code/`.
- **Status:** exploratory; contrasts are Holm-corrected.
