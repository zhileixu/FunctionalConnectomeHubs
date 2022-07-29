import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

HubTranscriptionLevel = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure5\Figure5A\HubTranscriptionLevel.csv", header=None)

fig = pyplot.figure(figsize=(4, 3))
ax = fig.add_subplot()

ColorMap = [ "tab:blue", "tab:orange", "tab:green", "tab:brown", "tab:purple", "tab:red", "darkcyan", "hotpink" ]

for Process in range( 1, 9 ):
    ax=pyplot.subplot( 1, 8, Process )
    seaborn.boxplot(x=1 - HubTranscriptionLevel.loc[0], y=HubTranscriptionLevel.loc[Process], hue=HubTranscriptionLevel.loc[0], palette=[ColorMap[Process - 1], ColorMap[Process - 1]], width=1, linewidth=1.25, flierprops=dict(marker='o', markersize=1, color="0.5"))

    ax.set_xlim([-0.3, 1.3])
    ax.set_ylim([-0.01, 1.01])
    pyplot.axis("off")
    pyplot.legend([],[], frameon=False)

ax.plot( ( 1.1, 1.3 ), ( 0.0, 0.0 ), color="0", linewidth=1.25, zorder=0)
ax.plot( ( 1.1, 1.3 ), ( 0.2, 0.2 ), color="0", linewidth=1.25, zorder=0)
ax.plot( ( 1.1, 1.3 ), ( 0.4, 0.4 ), color="0", linewidth=1.25, zorder=0)
ax.plot( ( 1.1, 1.3 ), ( 0.6, 0.6 ), color="0", linewidth=1.25, zorder=0)
ax.plot( ( 1.1, 1.3 ), ( 0.8, 0.8 ), color="0", linewidth=1.25, zorder=0)
ax.plot( ( 1.1, 1.3 ), ( 1.0, 1.0 ), color="0", linewidth=1.25, zorder=0)
ax.plot( ( 1.1, 1.1 ), ( 0.0, 1.0 ), color="0", linewidth=1.25, zorder=0)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure5\Figure5A\HubTranscriptionLevelBox.pdf")

pyplot.show()