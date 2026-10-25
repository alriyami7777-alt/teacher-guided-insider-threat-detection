# Phase 10: learning the new release CERT r6.2 (first tests)

- **What it tested:** whether r6.2 can be handled without zero-shot transfer: refitting only the threshold, training and scoring within r6.2 on a user-disjoint split, light adaptation of the r5.2 model, and pooled r5.2 + r6.2 training.
- **Paper items:** Section IV-M (learning the new release).
- **Key files:** `ALL_METRICS.csv`, `PHASE10_SUMMARY.csv`, `P1_CONTRASTS.csv` to `P4_CONTRASTS.csv`, `R62_SPLIT_RECEIPT.json` (the user split, as counts and hashes; users appear only as pseudonyms). The phase report gives every table.
- **Code:** `reproducibility_code/`.
- **Status:** exploratory.
