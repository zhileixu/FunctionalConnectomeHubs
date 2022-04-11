import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style='ticks')


for Hub in range(1, 36):
    fig = pyplot.figure( figsize=( 0.89370079, 0.89370079 ) )
    ax = fig.add_subplot()
    
    WeakConnection = pandas.read_csv(r"\FunctionalConnectomeHubs\FigureS7\FunctionalConnection_Hub%02d.csv"%(Hub), header=None)
    seaborn.histplot(x=WeakConnection.loc[1], hue=WeakConnection.loc[0], hue_order=[0, 1], binwidth=0.01, binrange=[0, 1], multiple="stack", palette=[ "tab:blue", "tab:red" ], edgecolor=None, legend=False )

    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax.set_xticklabels([])

    ax.set_ylim(0, 1500)
    ax.set_yticks([0, 500, 1000, 1500])
    ax.set_yticklabels([])

    fig.subplots_adjust(left=0.03, bottom=0.04, right=0.99, top=0.99)
    fig.savefig(r"\FunctionalConnectomeHubs\FigureS7\FunctionalConnection_Hub%02d.tiff"%(Hub), dpi=600)