# Study Status

Last consolidated status: 25 October 2026.

## Submission status

- Current IEEE Access submission: Access-2026-42960
- Original prescreened manuscript: Access-2026-37987
- Revised title: Teacher-Guided Differentiable Sequence–Ensemble Learning for
  Explainable Insider Threat Detection
- Status: R2 revision submitted October 2026; the cited version is tag
  `ieee-access-r2` (commit `ff55cc5`). New R2 evidence is in `revision_r2/`
  (see the README section "Revision R2: where to find each result"). The
  sections below record the evidence state of the August 2026 resubmission.

## Current evidence (R2)

- **Confirmatory:** pre-registered test on 500 unseen CERT r5.2 users. TRACE 0.712 vs task-only control 0.692 (+0.020 [0.008, 0.040]); XGBoost-40 0.824; TRACE found 24 of 25 insiders in each pre-registered seed.
- **Exploratory:** r5.2 validation results, eight seeds, insider-level and operational results, explanation tests (day, feature, tree and route), degraded inputs, attacks, cross-release r5.1/r6.1/r6.2 and r6.2 training.
- **Where to find each result:** README section "Revision R2" and `revision_r2/RESULTS_MAP.md`.
- **Limitations:** `KNOWN_LIMITATIONS.md`.

The detailed status of the August 2026 resubmission is preserved in the repository history and in the cited tag.
