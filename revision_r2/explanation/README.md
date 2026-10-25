# Integrated Gradients and faithfulness on the validation cohort

- **What it tested:** how much each daily feature and each tree contributes to TRACE's score (Integrated Gradients, 50 steps, training-median reference), and whether hiding the highest-attributed inputs changes the score more than hiding others.
- **Paper items:** Fig. 9 (Section IV-I).
- **Key files:** `integrated_gradients_features.csv` (the data behind Fig. 9, drawn by `../paper_figures/plot_ig.py`), `integrated_gradients.json`, `integrated_gradients_days.csv`, `faithfulness.csv`. The phase report summarises them.
- **Code:** `code/` (see `CODE_NOTE.md`).
- **Status:** exploratory.
