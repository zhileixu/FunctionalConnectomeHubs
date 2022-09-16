import seaborn
import pandas
import matplotlib.pyplot as pyplot

seaborn.set( style="ticks" )

DiceTract = pandas.read_csv( r"\FunctionalConnectomeHubs\SupplementaryFigure3\Figure3l\DiceAcrossRandomlySelectedCohorts.csv", header=None )

fig = pyplot.figure( figsize=( 3/2.54, 3/2.54 ) )
ax = fig.add_subplot()

DiceMax = 29200/31528;

seaborn.lineplot( x=DiceTract.loc[0], y=DiceTract.loc[1], ci="sd", linewidth=1.25, color="b" )
pyplot.plot( [ 9, 61 ], [ DiceMax*0.99, DiceMax*0.99 ], linewidth=1.25, color="r", linestyle='--' )
pyplot.plot( [ 33.4, 33.4 ], [ 0.86, DiceMax*0.99 ], linewidth=1.25, color="r", linestyle='--' )
pyplot.scatter( x=61, y=DiceMax, s=8, color="r", marker="^" )

ax.set_xticks( [ 10, 35, 60 ] )
ax.set_yticks( [ 0.87, 0.89, 0.91, 0.93 ] )

pyplot.xlim( 9, 65 )
pyplot.ylim( 0.86, 0.94 )
fig.subplots_adjust( left=0.03, bottom=0.03, right=0.99, top=0.99 )

fig.savefig( r"\FunctionalConnectomeHubs\SupplementaryFigure3\Figure3l\DiceTractCohorts.pdf" )

pyplot.show()