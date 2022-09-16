import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot
from loess.loess_1d import loess_1d

seaborn.set(style='ticks')

MyPalette = ["tab:blue", "tab:orange", "tab:green", "tab:brown", "tab:purple", "tab:red", "darkcyan", "hotpink"];
ColorIndex = 0

for Process in ["NeuronDifferentiation", "NeuronMigration", "DendriteDevelopment", "SynapseDevelopment", "AxonDevelopment", "Myelination", "OP", "AG"]:
    Data = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure6\Figure6b\DevelopmentTrajectory-%s-Data.csv"%Process, header=None)
    MAD = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure6\Figure6b\DevelopmentTrajectory-%s-MAD.csv"%Process, header=None)
        
    AgeUnique = numpy.unique( Data.loc[0] )
    _, Trajectory_Hub, _    = loess_1d(Data.loc[0, Data.loc[2] > 0.5].values, Data.loc[1, Data.loc[2] > 0.5].values, xnew=AgeUnique, frac=0.1)
    _, Trajectory_NonHub, _ = loess_1d(Data.loc[0, Data.loc[2] < 0.5].values, Data.loc[1, Data.loc[2] < 0.5].values, xnew=AgeUnique, frac=0.1)
    
    
    fig = pyplot.figure(figsize=(7.3/2.54, 2/2.54))
    ax = fig.add_subplot()
    
    ax.plot( ( 5.8074, 5.8074 ),    ( -0.25, 0.25 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
    ax.plot( ( 8.0553, 8.0553 ),    ( -0.25, 0.25 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
    ax.plot( ( 9.3015, 9.3015 ),    ( -0.25, 0.25 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
    ax.plot( ( 12.1818, 12.1818 ),  ( -0.25, 0.25 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
    ax.plot( ( 12.8853, 12.8853 ),  ( -0.25, 0.25 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
    
    Difference = Trajectory_Hub - Trajectory_NonHub
    ax.fill_between(AgeUnique, Difference, 0, color=MyPalette[ColorIndex], zorder=1)
    ColorIndex = ColorIndex + 1
    
    ax.fill_between(MAD.loc[0], MAD.loc[1], -MAD.loc[1], color="0", alpha = 0.3, zorder=2)
    ax.plot( ( 5.807, 13.860 ), ( 0, 0 ), color="0", linewidth=1.25, zorder=3)
    
    ax.set_xlim(5.7, 14)
    ax.set_xticks([])
    ax.set_ylim(-0.25, 0.25)
    ax.set_yticks([-0.2, 0, 0.2])
    ax.set_yticklabels([])

    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.subplots_adjust(left=0.03, bottom=0, right=1, top=1)
    fig.savefig(r"\FunctionalConnectomeHubs\Figure6\Figure6c\DevelopmentTrajectoryDifference-%s.pdf"%Process)