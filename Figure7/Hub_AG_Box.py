import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

Hub_Metabolism = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure7\Hub_Metabolism.csv", header=None)

fig = pyplot.figure(figsize=(6/2.54, 1.3/2.54))
ax = fig.add_subplot()

pyplot.plot( [0, 0], [-1, 2], color="0", linewidth=1.5, zorder=0 )
seaborn.boxplot(y=Hub_Metabolism.loc[0] > -1, x=Hub_Metabolism.loc[1], hue=Hub_Metabolism.loc[0], hue_order=[ 0, 1 ], palette=["tab:blue", "tab:red"], orient="h", width=0.6, linewidth=0.6, flierprops=dict(marker='o', markersize=1))

ax.set_ylim([-0.7, 0.5])
ax.set_yticks([])
ax.set_xlim(-150, 150)
ax.set_xticks([-150, -75, 0, 75, 150])
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
pyplot.legend(bbox_to_anchor=(100, 100), borderaxespad=0)

fig.subplots_adjust(left=0.01, bottom=0.1, right=0.99, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure7\Hub_AG_Box.tiff", dpi=600)

pyplot.show()