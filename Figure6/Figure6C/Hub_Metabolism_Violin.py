import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

Hub_Metabolism = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure6\Figure6C\Hub_Metabolism.csv", header=None)


fig = pyplot.figure(figsize=(1/15*16/2.54, 3/2.54))
ax = fig.add_subplot()
ax = seaborn.violinplot(x=Hub_Metabolism.loc[0] > -1, y=Hub_Metabolism.loc[1], hue=Hub_Metabolism.loc[0], hue_order=[ 0, 1 ], palette=["#84C1D9", "#F7A280"], split=True, inner="quartile", linewidth=0)

ax.lines[0].set_linestyle('--')
ax.lines[0].set_linewidth(1)
ax.lines[0].set_color("0.3")
ax.lines[1].set_linestyle('-')
ax.lines[1].set_linewidth(1.25)
ax.lines[1].set_color("0.3")
ax.lines[2].set_linestyle('--')
ax.lines[2].set_linewidth(1)
ax.lines[2].set_color("0.3")

ax.lines[3].set_linestyle('--')
ax.lines[3].set_linewidth(1)
ax.lines[3].set_color("0.3")
ax.lines[4].set_linestyle('-')
ax.lines[4].set_linewidth(1.25)
ax.lines[4].set_color("0.3")
ax.lines[5].set_linestyle('--')
ax.lines[5].set_linewidth(1)
ax.lines[5].set_color("0.3")

ax.set_xlim([-0.5, 0.5])
ax.set_xticks([])
ax.set_ylim([-200, 200])
ax.set_yticks([-200, -100, 0, 100, 200])
ax.set_yticklabels([])

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)

pyplot.legend([],[], frameon=False)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure6\Figure6C\Hub_AG_Violin.pdf")

pyplot.show()


fig = pyplot.figure(figsize=(1/15*16/2.54, 3/2.54))
ax = fig.add_subplot()
ax = seaborn.violinplot(x=Hub_Metabolism.loc[0] > -1, y=Hub_Metabolism.loc[2], hue=Hub_Metabolism.loc[0], hue_order=[ 0, 1 ], palette=["#84C1D9", "#F7A280"], split=True, inner="quartile", linewidth=0)

ax.lines[0].set_linestyle('--')
ax.lines[0].set_linewidth(1)
ax.lines[0].set_color("0.3")
ax.lines[1].set_linestyle('-')
ax.lines[1].set_linewidth(1.25)
ax.lines[1].set_color("0.3")
ax.lines[2].set_linestyle('--')
ax.lines[2].set_linewidth(1)
ax.lines[2].set_color("0.3")

ax.lines[3].set_linestyle('--')
ax.lines[3].set_linewidth(1)
ax.lines[3].set_color("0.3")
ax.lines[4].set_linestyle('-')
ax.lines[4].set_linewidth(1.25)
ax.lines[4].set_color("0.3")
ax.lines[5].set_linestyle('--')
ax.lines[5].set_linewidth(1)
ax.lines[5].set_color("0.3")

ax.set_xlim([-0.5, 0.5])
ax.set_xticks([])
ax.set_ylim([0.75, 1.45])
ax.set_yticks([0.8, 1.0, 1.2, 1.4])
ax.set_yticklabels([])

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)

pyplot.legend([],[], frameon=False)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure6\Figure6C\Hub_CMRO2_Violin.pdf")

pyplot.show()


fig = pyplot.figure(figsize=(1/15*16/2.54, 3/2.54))
ax = fig.add_subplot()
ax = seaborn.violinplot(x=Hub_Metabolism.loc[0] > -1, y=Hub_Metabolism.loc[4], hue=Hub_Metabolism.loc[0], hue_order=[ 0, 1 ], palette=["#84C1D9", "#F7A280"], split=True, inner="quartile", linewidth=0)

ax.lines[0].set_linestyle('--')
ax.lines[0].set_linewidth(1)
ax.lines[0].set_color("0.3")
ax.lines[1].set_linestyle('-')
ax.lines[1].set_linewidth(1.25)
ax.lines[1].set_color("0.3")
ax.lines[2].set_linestyle('--')
ax.lines[2].set_linewidth(1)
ax.lines[2].set_color("0.3")

ax.lines[3].set_linestyle('--')
ax.lines[3].set_linewidth(1)
ax.lines[3].set_color("0.3")
ax.lines[4].set_linestyle('-')
ax.lines[4].set_linewidth(1.25)
ax.lines[4].set_color("0.3")
ax.lines[5].set_linestyle('--')
ax.lines[5].set_linewidth(1)
ax.lines[5].set_color("0.3")

ax.set_xlim([-0.5, 0.5])
ax.set_xticks([])
ax.set_ylim([0.8, 1.4])
ax.set_yticks([0.8, 1.0, 1.2, 1.4])
ax.set_yticklabels([])

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)

pyplot.legend([],[], frameon=False)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure6\Figure6C\Hub_CBF_Violin.pdf")

pyplot.show()