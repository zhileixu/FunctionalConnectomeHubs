import numpy.random as random
import pandas
import seaborn
import matplotlib.pyplot as pyplot

def jitter(values):
    return values + random.normal(0,50,values.shape)
    
seaborn.set(style='ticks')

fig = pyplot.figure( figsize=( 2.1, 2.1 ) )
ax = fig.add_subplot()

NetworkSize = pandas.read_csv(r"\FunctionalConnectomeHubs\SupplementaryFigure4\NetworkSize.csv", header=None)

#seaborn.scatterplot(x=jitter(NetworkSize.loc[0]), y=NetworkSize.loc[1], s=0.5, alpha=0.1, color="tab:orange")
#seaborn.scatterplot(x=jitter(NetworkSize.loc[0]), y=NetworkSize.loc[2], s=0.5, alpha=0.1, color="tab:green")
seaborn.scatterplot(x=jitter(NetworkSize.loc[0]), y=NetworkSize.loc[3], s=0.5, alpha=0.1, color="tab:blue")

ax.set_xlim(2000, 12000)
ax.set_xticks([3000, 5000, 7000, 9000, 11000])
ax.set_xticklabels([])

ax.set_ylim(-1.5, 1.5)
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels([])

fig.subplots_adjust(left=0.03, bottom=0.04, right=0.99, top=0.99)
fig.savefig(r"\FunctionalConnectomeHubs\SupplementaryFigure4\NetworkSize3.tiff", dpi=600)

pyplot.show()