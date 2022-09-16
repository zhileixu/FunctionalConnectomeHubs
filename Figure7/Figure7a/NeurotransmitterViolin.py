import numpy
import pandas
import seaborn
import matplotlib.pyplot as pyplot

seaborn.set(style="ticks")

fig = pyplot.figure(figsize=(16/2.54, 5/2.54))
ax = fig.add_subplot()
SubplotCounter = 1

for Neurotransmitter in [ "GABAa_FLUMAZENIL_c11", "mGluR5_abp_hc73_smart", "MU_carfentanil_hc39_turtonen", 
		"CB1_FMPEPd2_hc22_laurikainen", "VAChT_feobv_hc18_aghourian", 
        "D1_SCH23390_c11", "D2_fallypride_hc49_jaworska", "DAT_DATSPECT", "FDOPA_f18", 
		"5HT1a_WAY_HC36", "5HT1b_P943_HC22", "5HT2a_ALT_HC19", 
        "5HT4_sb20_hc59_beliveau", "SERT_DASB_HC30", "NAT_MRB_c11" ]:
    ax=pyplot.subplot( 1, 15, SubplotCounter )
     
    Data = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure7\Figure7a\%s.csv"%Neurotransmitter, header=None)
    ax = seaborn.violinplot(x=Data.loc[1] > -1, y=Data.loc[0], hue=Data.loc[1], hue_order=[ 0, 1 ], palette=["#84C1D9", "#F7A280"], split=True, inner="quartile", linewidth=0)
    
    ax.lines[0].set_linestyle('--')
    ax.lines[0].set_linewidth(0.75)
    ax.lines[0].set_color("0.3")
    ax.lines[1].set_linestyle('-')
    ax.lines[1].set_linewidth(1)
    ax.lines[1].set_color("0.3")
    ax.lines[2].set_linestyle('--')
    ax.lines[2].set_linewidth(0.75)
    ax.lines[2].set_color("0.3")
    
    ax.lines[3].set_linestyle('--')
    ax.lines[3].set_linewidth(0.75)
    ax.lines[3].set_color("0.3")
    ax.lines[4].set_linestyle('-')
    ax.lines[4].set_linewidth(1)
    ax.lines[4].set_color("0.3")
    ax.lines[5].set_linestyle('--')
    ax.lines[5].set_linewidth(0.75)
    ax.lines[5].set_color("0.3")
    
    ax.plot( ( 0, 0 ), ( -4.2, -4 ), color="0", linewidth=1.25)
    
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-4, 4])
    if SubplotCounter == 1:
        ax.plot( ( -0.7, -0.5 ), ( -4, -4 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( -2, -2 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 0, 0 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 2, 2 ), color="0", linewidth=1.25)
        ax.plot( ( -0.7, -0.5 ), ( 4, 4 ), color="0", linewidth=1.25)
    pyplot.axis("off")
    pyplot.legend([],[], frameon=False)
    
    SubplotCounter = SubplotCounter + 1


fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
fig.savefig(r"\FunctionalConnectomeHubs\Figure7\Figure7a\NeurotransmitterViolin.pdf")

pyplot.show()