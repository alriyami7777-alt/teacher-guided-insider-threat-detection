# Phase 6: development-user validation tests and the r4.2 test

- **What it tested:** TRACE was re-run on the development users to test the order and history of days, a comparison on identical inputs, window length (10, 20, 30 days) and retraining with 6, 13 or 29 features; the frozen models were also scored once on the CERT r4.2 test period.
- **Paper items:** Section IV-F (temporal evidence and feature design) and the r4.2 test (Section IV-A).
- **Key files:** `I1_ORDER_HISTORY.csv`, `I2_SAME_INFORMATION.csv`, `T2_FEATURE_SETS_data.csv`, `T2_PAIRED_CIS.csv`, and the `T3_R42_*` files for r4.2. The phase report gives every table.
- **Code:** `reproducibility_code/`.
- **Status:** exploratory.
