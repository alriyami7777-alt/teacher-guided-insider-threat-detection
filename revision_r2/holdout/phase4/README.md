# Phase 4: unseen-user evaluation of 17 models

- **What it tested:** 17 models, retrained on the 1,500 development users of CERT r5.2, were scored once on the 500 held-out users at thresholds fixed on development data (seeds 42, 52 and 62).
- **Paper items:** Table 6 and Fig. 6 (Section IV-C).
- **Key files:** `HOLDOUT_RESULTS.csv` (every model, seed and view), `HOLDOUT_CONTRASTS.csv` (paired contrasts), `MODELS_FROZEN_PHASE4.json` (frozen models and thresholds), `TRAINING_LOG_PHASE4.csv`. The phase report summarises them.
- **Code:** `../code/` (training and scoring, including `../code/phase4/score.py`); seed-42 reproduction in `../reproduce/reproduce_unseen_seed42.py`; figure script `../../paper_figures/plot_holdout.py`.
- **Status:** TRACE against XGBoost-40 and TRACE against the task-only control are confirmatory (pre-registered); every other comparison is exploratory.
