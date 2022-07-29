import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style='ticks')

fig = pyplot.figure( figsize=( 5.5/2.54, 5.5/2.54 ) )
ax = fig.add_subplot()

pyplot.plot( [0.25, 0.25], [0, 1], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0.50, 0.50], [0, 1], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0.75, 0.75], [0, 1], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )

pyplot.plot( [0, 1], [0.2, 0.2], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0, 1], [0.4, 0.4], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0, 1], [0.6, 0.6], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )
pyplot.plot( [0, 1], [0.8, 0.8], color="0.7", linewidth=0.8, linestyle='--', zorder=0 )

ISquareCDF = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure2\Figure2C\ISquare.csv", header=None)

seaborn.ecdfplot( x=ISquareCDF.loc[0], hue=ISquareCDF.loc[1], legend=False, palette=["tab:blue", "k", "tab:orange", "tab:green", "tab:red", "tab:brown", "tab:cyan"] )

ax.set_xlim(0, 1)
ax.set_xticks([0, 0.25, 0.50, 0.75, 1])
ax.set_xticklabels([])

ax.set_ylim(0, 1)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax.set_yticklabels([])

fig.subplots_adjust(left=0.03, bottom=0.03, right=0.99, top=0.99)
fig.savefig(r"\FunctionalConnectomeHubs\FigureS1\ISquareCDFSeparate.pdf")

pyplot.show()