import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
NAVY='#0B1F3A';GOLD='#C9A227';TEAL='#1B998B';W='#F5F1E6'
fig=plt.figure(figsize=(16,9),dpi=100,facecolor=NAVY)
fig.text(0.05,0.93,'Hottest producer prices since 2022. The 10-year fell anyway.',color=W,fontsize=30,fontweight='bold',va='top')
fig.text(0.97,0.985,'LEAD-LAG',color=GOLD,fontsize=20,fontweight='bold',ha='right',va='top')
specs=[([0.06,0.20,0.26,0.55],'Headline PPI, y/y %',['Expected','Actual'],[5.3,6.3],'{:.1f}%'),
       ([0.38,0.20,0.26,0.55],'Core PPI, m/m %',['Expected','Actual'],[0.3,0.7],'{:.1f}%'),
       ([0.70,0.20,0.26,0.55],'10-year Treasury yield, %',['Wed high','Thu close'],[5.33,5.09],'{:.2f}%')]
for i,(pos,t,labs,vals,fmt) in enumerate(specs):
    ax=fig.add_axes(pos);ax.set_facecolor(NAVY)
    cols=[GOLD,TEAL]
    b=ax.bar(labs,vals,color=cols,width=0.55)
    ax.set_ylim(0 if i<2 else 4.8,max(vals)*1.12 if i<2 else 5.5)
    for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v,fmt.format(v),ha='center',va='bottom',color=W,fontsize=26,fontweight='bold')
    ax.set_title(t,color=W,fontsize=20,pad=14)
    ax.tick_params(colors=W,labelsize=18);ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
fig.text(0.05,0.10,'Right panel axis starts at 4.8% to show the move. Sources: September PPI via Investing.com and Schwab (Oct 15, 2026, consensus per Investing.com);\n10-year Wednesday high per Investopedia, Thursday cash-session close near 5.09% per Investing.com and TheStreet.',color='#A9B4C6',fontsize=13,va='top')
fig.savefig('ppi_vs_10y.png',facecolor=NAVY)
