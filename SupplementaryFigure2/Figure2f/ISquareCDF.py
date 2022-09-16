import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot
from matplotlib.collections import LineCollection

seaborn.set(style='ticks')

fig = pyplot.figure( figsize=( 2.9/2.54, 3.1/2.54 ) )
ax = fig.add_subplot()

pyplot.plot( [0.25, 0.25], [0, 1], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0.50, 0.50], [0, 1], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0.75, 0.75], [0, 1], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )

pyplot.plot( [0, 1], [0.2, 0.2], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0, 1], [0.4, 0.4], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0, 1], [0.6, 0.6], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0, 1], [0.8, 0.8], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )

ISquare = pandas.read_csv(r"\FunctionalConnectomeHubs\SupplementaryFigure2\Figure2f\ISquare.csv", header=None)

x = numpy.arange( 0, 100.01, 0.1 )
y = numpy.percentile( ISquare.loc[0], x )

seaborn.scatterplot( y, x/100, hue=y, palette="magma", legend=False, marker=".", sizes=(0.1, 0.1), edgecolor="none" )

ax.set_xlim(0, 1)
ax.set_xticks([0, 0.50, 1])
ax.set_xticklabels([])

ax.set_ylim(0, 1)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax.set_yticklabels([])

fig.subplots_adjust(left=0.04, bottom=0.04, right=0.99, top=0.99)
fig.savefig(r"\FunctionalConnectomeHubs\SupplementaryFigure2\Figure2f\ISquareCDF.pdf")

pyplot.show()