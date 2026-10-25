# Phase 6C: robustness-oriented training

- **What it tested:** TRACE and XGBoost-40 were retrained with source removal and noise applied to the training data only, then scored once on the 500 unseen users (C2). C1 recomputes the Phase 6B contrasts with 50,000 bootstrap replicates.
- **Paper items:** Table 10 columns "Aug." (Section IV-J).
- **Key files:** `C2_AURC.csv`, `C2_CONTRASTS_HOLM.csv`, `C2_ALL_MODEL_VIEW_METRICS.csv`, `C2_OPERATIONAL_COUNTS.csv`, `C1_FULL_SIDE_BY_SIDE.csv`. The phase report gives every table.
- **Code:** `reproducibility_code/`.
- **Status:** exploratory; contrasts are Holm-corrected.
