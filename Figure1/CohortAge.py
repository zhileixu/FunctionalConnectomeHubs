import seaborn
import pandas
import math
import matplotlib.pyplot as pyplot

seaborn.set( style="ticks" )

fig = pyplot.figure( figsize=( 5.4/2.54, 19.4/2.54 ) )
ax = fig.add_subplot()

SiteAge = pandas.read_csv( r"\FunctionalConnectomeHubs\Figure1\Age.csv", header=None )

seaborn.boxenplot( x=SiteAge.loc[1], y=SiteAge.loc[0], orient="h", color="tab:gray", scale="area", k_depth="proportion", outlier_prop=math.exp(-100) )

pyplot.xlim( 17.3, 36.7 )
ax.set_xticks( [ 18, 21, 24, 27, 30, 33, 36 ] )
ax.set_yticks( [] )

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

pyplot.subplots_adjust( left=0, bottom=0.01, right=1, top=1 )
pyplot.savefig( r'\FunctionalConnectomeHubs\Figure1\CohortAge.pdf' )

pyplot.show()