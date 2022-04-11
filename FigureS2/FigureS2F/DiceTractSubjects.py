import seaborn
import pandas
import matplotlib.pyplot as pyplot

seaborn.set( style="ticks" )

DiceTract = pandas.read_csv( r"\FunctionalConnectomeHubs\FigureS2\FigureS2F\DiceAcrossRandomlySelectedSubjects.csv", header=None )

fig = pyplot.figure( figsize=( 1.2, 1.2 ) )
ax = fig.add_subplot()

DiceMax = 26800/30917;

seaborn.lineplot( x=DiceTract.loc[0], y=DiceTract.loc[1], ci="sd", linewidth=1.2, color="b" )
pyplot.plot( [ 100, 5200 ], [ DiceMax*0.99, DiceMax*0.99 ], linewidth=1, color="r", linestyle='--' )
pyplot.plot( [ 510, 510 ], [ 0.8, DiceMax*0.99 ], linewidth=1, color="r", linestyle='--' )
pyplot.scatter( x=5212, y=DiceMax, s=8, color="r", marker="^" )

ax.set_xticks( [ 100, 2600, 5100 ] )
ax.set_yticks( [ 0.81, 0.83, 0.85, 0.87 ] )

pyplot.xlim( 100, 5500 )
pyplot.ylim( 0.80, 0.88 )
fig.subplots_adjust( left=0.03, bottom=0.03, right=0.99, top=0.99 )

fig.savefig( r"\FunctionalConnectomeHubs\FigureS2\FigureS2F\DiceTractSubjects.tiff", dpi=600 )

pyplot.show()