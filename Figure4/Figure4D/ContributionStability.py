import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

ContributionStability = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure4\Figure4D\ContributionStability.csv", header=None)

fig = pyplot.figure(figsize=(3.4/2.54, 3.4/2.54))
ax = fig.add_subplot()

seaborn.regplot(x=ContributionStability.loc[0], y=ContributionStability.loc[1], ci=None, color="0.2", scatter_kws={"s": 0.8}, line_kws={"linewidth": 0.8})

ax.set_xlim([-1.7, 0.7])
ax.set_xticks([-1.5, -1, -0.5, 0, 0.5])
ax.set_ylim([-1.7, 0.7])
ax.set_yticks([-1.5, -1, -0.5, 0, 0.5])

fig.subplots_adjust(left=0.04, bottom=0.04, right=0.99, top=0.99)
fig.savefig(r"\FunctionalConnectomeHubs\Figure4\Figure4D\ContributionStability.tiff", dpi=600)

pyplot.show()