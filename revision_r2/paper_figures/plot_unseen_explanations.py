"""Fig. 8 of the R2 manuscript: three-level explanation test on the 500 unseen users.

Reads revision_r2/phase6b/figure_e_three_level_explanation.csv (class-supporting rows,
overall stratum) and draws one bar panel per explanation level (mean of seeds 42/52/62,
dots = individual seeds). Usage: python plot_unseen_explanations.py [csv] [out_prefix]
"""
import csv, sys, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

src = sys.argv[1] if len(sys.argv) > 1 else "../phase6b/figure_e_three_level_explanation.csv"
out = sys.argv[2] if len(sys.argv) > 2 else "fig_unseen_three_level_explanation_v2"

plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"], "font.size": 11})
D = collections.defaultdict(lambda: collections.defaultdict(list))
for r in csv.DictReader(open(src)):
    if r.get("sign", "class_supporting") != "class_supporting" or r.get("stratum", "overall") != "overall":
        continue
    if r.get("metric", "normalized_change_gap_from_random") != "normalized_change_gap_from_random":
        continue
    D[r["level"]][int(r["k"])].append(float(r["estimate"]))

panels = [("temporal", "Days", "(ranked by attention)", "#2A7F62"),
          ("feature", "Features", "(ranked by Integrated Gradients)", "#C98A2B"),
          ("tree", "Trees", "(ranked by tree contribution)", "#6A4C93")]
fig, ax = plt.subplots(1, 3, figsize=(10.5, 3.3))
for a, (lv, title, sub, colour) in zip(ax, panels):
    ks = sorted(D[lv]); means = [sum(D[lv][k]) / len(D[lv][k]) for k in ks]
    a.bar(range(len(ks)), means, color=colour, width=0.6)
    for i, k in enumerate(ks):
        a.scatter([i] * len(D[lv][k]), D[lv][k], color="black", s=12, zorder=3)
    a.set_xticks(range(len(ks)), ks); a.set_title(title + "\n" + sub, fontsize=11)
    a.set_xlabel("Top-ranked items hidden"); a.spines[["top", "right"]].set_visible(False); a.set_ylim(0, None)
ax[0].set_ylabel("Extra change in score\nvs. hiding random items")
plt.tight_layout(); plt.savefig(out + ".png", dpi=300); plt.savefig(out + ".pdf")
