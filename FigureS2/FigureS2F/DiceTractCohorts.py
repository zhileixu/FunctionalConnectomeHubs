import seaborn
import pandas
import matplotlib.pyplot as pyplot

seaborn.set( style="ticks" )

DiceTract = pandas.read_csv( r"\FunctionalConnectomeHubs\FigureS2\FigureS2F\DiceAcrossRandomlySelectedCohorts.csv", header=None )

fig = pyplot.figure( figsize=( 1.2, 1.2 ) )
ax = fig.add_subplot()

DiceMax = 28512/30867;

seaborn.lineplot( x=DiceTract.loc[0], y=DiceTract.loc[1], ci="sd", linewidth=1.2, color="b" )
pyplot.plot( [ 1, 61 ], [ DiceMax*0.99, DiceMax*0.99 ], linewidth=1, color="r", linestyle='--' )
pyplot.plot( [ 35, 35 ], [ 0.85, DiceMax*0.99 ], linewidth=1, color="r", linestyle='--' )
pyplot.scatter( x=61, y=DiceMax, s=8, color="r", marker="^" )

ax.set_xticks( [ 10, 35, 60 ] )
ax.set_yticks( [ 0.87, 0.89, 0.91, 0.93 ] )

pyplot.xlim( 10, 65 )
pyplot.ylim( 0.86, 0.94 )
fig.subplots_adjust( left=0.03, bottom=0.03, right=0.99, top=0.99 )

fig.savefig( r"\FunctionalConnectomeHubs\FigureS2\FigureS2F\DiceTractCohorts.tiff", dpi=600 )

pyplot.show()