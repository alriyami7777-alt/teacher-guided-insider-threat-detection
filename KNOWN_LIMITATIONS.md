# Known Limitations

1. CERT activity is synthetic; results on real organisational logs may differ.
2. Public datasets contain few insiders (25 held-out insiders in the unseen-user test; six positive users in the r4.2 test), which limits statistical power for every model.
3. No analyst study of the alerts has been made.
4. TRACE did not transfer zero-shot to CERT r6.1 or r6.2; a new release needs labelled data of its own and revalidation (Section IV-M).
5. Explanation faithfulness is supported locally (day, feature, tree and route interventions), not as a global tree ranking; the global top-k tree-ranking test was negative.
6. The early-warning result is measured from a known first malicious day, so it is retrospective.
7. An attacker with full access to TRACE's gradients can lower its ranking substantially; model parameters should be protected like any security control.
8. Overlapping windows are correlated observations, and endpoint labels support end-of-day detection, not real-time intra-day prediction.

Earlier limitation statements that applied to the August 2026 resubmission are superseded by the R2 unseen-user, r6.2 and route-intervention results.
