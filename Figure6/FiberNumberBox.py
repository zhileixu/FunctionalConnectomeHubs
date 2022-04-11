import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

FiberNumber = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure6\FiberNumber.csv", header=None)

fig = pyplot.figure(figsize=(4.8/2.54, 10.2/2.54))
ax = fig.add_subplot()

for Length in range( 1, 8 ):
    ax=pyplot.subplot( 7, 1, Length )
    seaborn.lineplot([0, 0], [-1, 2], color="k", linewidth=0.8, zorder=0 )
    seaborn.boxplot(y=FiberNumber.loc[0] > -1, x=FiberNumber.loc[Length], hue=FiberNumber.loc[0], hue_order=[ 0, 1 ], palette=["tab:blue", "tab:red"], orient="h", width=0.6, linewidth=0.6, flierprops=dict(marker='o', markersize=0.1))

    ax.set_xlim([-3, 3])
    ax.set_ylim([-0.5, 0.7])
    pyplot.axis("off")
    pyplot.legend(bbox_to_anchor=(100, 100), borderaxespad=0)



fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure6\FiberNumberBox.tiff", dpi=600)

pyplot.show()