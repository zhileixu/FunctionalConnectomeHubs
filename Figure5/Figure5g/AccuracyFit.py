import pandas
import seaborn
import matplotlib.pyplot as pyplot
from loess.loess_1d import loess_1d

seaborn.set( style="ticks" )

Accuracy = pandas.read_csv( r"\FunctionalConnectomeHubs\Figure5\Figure5g\AccuracyFit.csv", header=None )

fig = pyplot.figure( figsize=( 4.5/2.54, 4/2.54 ) )
ax = fig.add_subplot()

seaborn.scatterplot( x=Accuracy.loc[0], y=Accuracy.loc[1], marker=".", color="0", sizes=(1.8, 1.8), edgecolor="none", alpha=0.5 )
xout, yout, weigts = loess_1d( Accuracy.loc[0].values, Accuracy.loc[1].values, frac=0.3 )
seaborn.lineplot( x=xout, y=yout, color="0", linewidth=1.25 )

ax.set_xlim( [ 100, 300 ] )
ax.set_xticks( [ 100, 150, 200, 250, 300 ] )
ax.set_xticklabels( [] )
ax.set_ylim( [0.662, 0.688 ] )
ax.set_yticks( [0.67, 0.68] )
ax.set_yticklabels( [] )

fig.subplots_adjust( left=0.04, bottom=0.04, right=0.99, top=0.99 )
fig.savefig( r"\FunctionalConnectomeHubs\Figure5\Figure5g\AccuracyFit.pdf" )

pyplot.show()