# Phase 8: more seeds, gradients, routing, explanation and input checks

- **What it tested:** TRACE and the task-only control with five further seeds on the 500 unseen users (Q1), gradient flow across days (Q2), routing and leaf occupancy of the trees (Q3), an explanation check under parameter randomisation (Q4) and a label-free input-shift monitor (Q5).
- **Paper items:** Fig. 7 (eight seeds, Section IV-C); gradients by day (Section IV-F); routing, leaf occupancy and the randomisation check (Section IV-I); the input monitor (Section IV-M).
- **Key files:** `figure_Q1_more_seeds.csv`, `Q1_PAIRED_AP_CONTRASTS.csv`, `Q2_GRADIENT_BY_DAY.csv`, `Q3_LEAF_OCCUPANCY.csv`, `Q5_RELEASE_FLAGS.csv`. The phase report gives every table.
- **Code:** `reproducibility_code/`.
- **Status:** exploratory (seeds 42, 52 and 62 are the pre-registered ones; the other five are an exploratory repeat).
