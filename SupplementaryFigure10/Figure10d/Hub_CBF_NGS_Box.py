import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

Hub_Metabolism = pandas.read_csv(r"\FunctionalConnectomeHubs\SupplementaryFigure10\Figure10d\Hub_Metabolism_NGS.csv", header=None)

fig = pyplot.figure(figsize=(6/2.54, 1.3/2.54))
ax = fig.add_subplot()

pyplot.plot( [1, 1], [-1, 2], color="0", linewidth=1.25, zorder=0 )
seaborn.boxplot(y=Hub_Metabolism.loc[0] > -1, x=Hub_Metabolism.loc[4], hue=Hub_Metabolism.loc[0], hue_order=[ 0, 1 ], palette=["tab:blue", "tab:red"], orient="h", width=0.6, linewidth=1.25, flierprops=dict(marker='o', markersize=1))

ax.set_ylim([-0.7, 0.5])
ax.set_yticks([])
ax.set_xlim(0.9, 1.3)
ax.set_xticks([0.9, 1, 1.1, 1.2, 1.3])
ax.set_xticklabels([])
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
pyplot.legend([],[], frameon=False)

fig.subplots_adjust(left=0.01, bottom=0.1, right=0.99, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\SupplementaryFigure10\Figure10d\Hub_CBF_NGS_Box.pdf")

pyplot.show()