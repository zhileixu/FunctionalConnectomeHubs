import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

Accuracy = pandas.read_csv(r"\FunctionalConnectomeHubs\FigureS8\FigureS8B\Accuracy.csv", header=None)

fig = pyplot.figure(figsize=(4.5/2.54, 4/2.54))
ax = fig.add_subplot()

seaborn.lineplot([-0.6, 1.6], [0.5, 0.5], linestyle="dashed", color="0.3", linewidth=1.25, zorder=0 )
seaborn.stripplot(x=Accuracy.loc[0], y=Accuracy.loc[2], hue=Accuracy.loc[1], palette=["tab:orange", "tab:blue"], dodge=True, jitter=0.35, size=3, edgecolor="none", alpha=0.5)

ax.set_xlim([-0.4, 1.4])
ax.set_xticks([])
ax.set_ylim([0, 1])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
pyplot.legend(bbox_to_anchor=(100, 100), borderaxespad=0)

fig.subplots_adjust(left=0.03, bottom=0.01, right=1, top=0.99)
fig.savefig(r"\FunctionalConnectomeHubs\FigureS8\FigureS8B\AccuracyStrip.pdf")

pyplot.show()