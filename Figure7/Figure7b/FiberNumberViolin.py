import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

fig = pyplot.figure(figsize=(7/15*16/2.54, 3/2.54))
ax = fig.add_subplot()
SubplotCounter = 1

FiberNumber = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure7\Figure7b\FiberNumber.csv", header=None)

for Length in range( 1, 8 ):
    ax = pyplot.subplot( 1, 7, Length )
    ax = seaborn.violinplot(x=FiberNumber.loc[0] > -1, y=FiberNumber.loc[Length], hue=FiberNumber.loc[0], hue_order=[ 0, 1 ], palette=["#84C1D9", "#F7A280"], split=True, inner="quartile", linewidth=0)
    
    ax.lines[0].set_linestyle('--')
    ax.lines[0].set_linewidth(1)
    ax.lines[0].set_color("0.3")
    ax.lines[1].set_linestyle('-')
    ax.lines[1].set_linewidth(1.25)
    ax.lines[1].set_color("0.3")
    ax.lines[2].set_linestyle('--')
    ax.lines[2].set_linewidth(1)
    ax.lines[2].set_color("0.3")
    
    ax.lines[3].set_linestyle('--')
    ax.lines[3].set_linewidth(1)
    ax.lines[3].set_color("0.3")
    ax.lines[4].set_linestyle('-')
    ax.lines[4].set_linewidth(1.25)
    ax.lines[4].set_color("0.3")
    ax.lines[5].set_linestyle('--')
    ax.lines[5].set_linewidth(1)
    ax.lines[5].set_color("0.3")
    
    ax.plot( ( 0, 0 ), ( -3.2, -3 ), color="0", linewidth=1.25)
    
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-3, 3])
    if SubplotCounter == 1:
        ax.plot( ( -0.7, -0.5 ), ( -3, -3 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( -2, -2 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( -1, -1 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 0, 0 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 1, 1 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 2, 2 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 3, 3 ), color="0", linewidth=1.25)
    pyplot.axis("off")
    pyplot.legend([],[], frameon=False)
    
    SubplotCounter = SubplotCounter + 1


fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure7\Figure7b\FiberNumberViolin.pdf")

pyplot.show()