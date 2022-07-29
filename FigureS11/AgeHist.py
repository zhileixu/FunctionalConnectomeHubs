import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

fig = pyplot.figure(figsize=(7.3/2.54, 5/2.54))
ax = fig.add_subplot()

ax.plot( ( 5.8074, 5.8074 ),    ( 0, 45 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
ax.plot( ( 8.0553, 8.0553 ),    ( 0, 45 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
ax.plot( ( 9.3015, 9.3015 ),    ( 0, 45 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
ax.plot( ( 12.1818, 12.1818 ),  ( 0, 45 ), 'k--', color="0.7", linewidth=1.25, zorder=0)
ax.plot( ( 12.8853, 12.8853 ),  ( 0, 45 ), 'k--', color="0.7", linewidth=1.25, zorder=0)

Age = pandas.read_csv(r"\FunctionalConnectomeHubs\FigureS11\Age.csv", header=None)
seaborn.histplot(x=Age.loc[0], hue=Age.loc[1], hue_order=[0, 1], binwidth=0.1, multiple="stack", palette=[ "tab:blue", "tab:red" ], edgecolor="none", legend=False )

ax.set_xlim(5.7, 14)
ax.set_xticks([5.8074, 8.0553, 9.3015, 12.1818, 12.8853])
ax.set_xticklabels([])
ax.set_ylim(0, 45)
ax.set_yticks([0, 10, 20, 30, 40])
ax.set_yticklabels([])

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(True)
ax.spines["left"].set_visible(True)
ax.spines["right"].set_visible(False)

fig.subplots_adjust(left=0.03, bottom=0.03, right=1, top=0.97)
fig.savefig(r"\FunctionalConnectomeHubs\FigureS11\Age.pdf")