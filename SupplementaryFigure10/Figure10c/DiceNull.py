import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

DiceNull = pandas.read_csv(r"\FunctionalConnectomeHubs\SupplementaryFigure10\Figure10c\DiceNull.csv", header=None)

fig = pyplot.figure(figsize=(3/2.54, 2.5/2.54))
ax = fig.add_subplot()

pyplot.plot( [0.8329, 0.8329], [0, 14.5], color="tab:red", linewidth=1.5, zorder=0 )
seaborn.kdeplot(x=DiceNull.loc[0], fill=True, color="tab:gray", alpha=1, linewidth=0)

ax.set_xlim([0.1, 0.9])
ax.set_xticks([ 0.2, 0.4, 0.6, 0.8 ])
ax.set_ylim([-0.5, 15.5])
ax.set_yticks([ 0, 5, 10, 15 ])

fig.subplots_adjust(left=0.04, bottom=0.04, right=0.99, top=0.99)
fig.savefig(r"\FunctionalConnectomeHubs\SupplementaryFigure10\Figure10c\DiceNull.tiff", dpi=600)

pyplot.show()