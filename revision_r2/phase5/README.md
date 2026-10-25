# Phase 5: cross-release, degraded-input, operational and calibration analyses

- **What it tested:** models trained on r5.2 were applied once to CERT r5.1 and r6.2; on the 500 unseen users, log sources were removed or noise was added without retraining, and insider-level, operational, calibration and secondary ranking measures were computed.
- **Paper items:** Table 13 (Section IV-M; the r6.1 column comes from the earlier frozen run in `../evidence/`), Table 10 columns "Orig." (Section IV-J), Table 7 (Section IV-D), and the calibration and Holm-corrected secondary contrasts (Section IV-C).
- **Key files:** `A_TRANSFER_RESULTS.csv`, `B_AURC.csv`, `C_INSIDER_DETECTION.csv`, `E_CALIBRATION_METRICS.csv`, `F_HOLM_SECONDARY_CONTRASTS.csv`. The phase report gives every table.
- **Code:** `reproducibility_code/`.
- **Status:** exploratory.
