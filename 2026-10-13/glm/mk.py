import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
NAVY='#0B1F3A';GOLD='#C9A227';TEAL='#1B998B';W='#F5F1E6'
def base(title):
    fig=plt.figure(figsize=(16,9),dpi=100,facecolor=NAVY)
    fig.text(0.05,0.92,title,color=W,fontsize=34,fontweight='bold',va='top')
    return fig
# Chart 1 JPM
fig=base('JPM: income beat, profit line missed')
ax1=fig.add_axes([0.07,0.20,0.40,0.52]);ax2=fig.add_axes([0.57,0.20,0.40,0.52])
for ax,labs,vals,t,fmt in [(ax1,['Street expected','Reported'],[26.9,27.1],'Net interest income, \\$B','{:.1f}'),(ax2,['Street expected','Adjusted'],[5.90,5.75],'Earnings per share, \\$','{:.2f}')]:
    ax.set_facecolor(NAVY)
    b=ax.bar(labs,vals,color=[GOLD,TEAL],width=0.55)
    lo=min(vals)*0.9
    ax.set_ylim(lo,max(vals)*1.04)
    for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v,fmt.format(v),ha='center',va='bottom',color=W,fontsize=28,fontweight='bold')
    ax.set_title(t,color=W,fontsize=24,pad=18)
    ax.tick_params(colors=W,labelsize=20);ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
fig.text(0.05,0.08,'Axes truncated to show the gap. Sources: JPMorgan 3Q26 results via Reuters/TradingView (Oct 13, 2026); consensus per CNBC/LSEG (\\$5.90 EPS) and\nAdmiral Markets (\\$26.9B NII). Adjusted EPS excludes a \\$658M securities loss.',color='#A9B4C6',fontsize=13,va='top')
fig.text(0.97,0.92,'LEAD-LAG',color=GOLD,fontsize=22,fontweight='bold',ha='right',va='top')
fig.savefig('jpm_nii_eps.png',facecolor=NAVY)
# Chart 2 WFC
fig=base('WFC: loans +11%, NII +5%, provision +51%')
ax=fig.add_axes([0.08,0.20,0.86,0.58]);ax.set_facecolor(NAVY)
labs=['Average loans','Net interest income','Total revenue','Provision for\ncredit losses']
vals=[11,5,2,51]
cols=[TEAL,TEAL,TEAL,GOLD]
b=ax.bar(labs,vals,color=cols,width=0.55)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+1,f'+{v}%',ha='center',va='bottom',color=W,fontsize=30,fontweight='bold')
ax.set_ylim(0,60);ax.set_yticks([]);ax.tick_params(colors=W,labelsize=22)
for s in ax.spines.values(): s.set_visible(False)
ax.set_title('Wells Fargo Q3 2026 vs Q3 2025',color=W,fontsize=22,pad=14,loc='left')
fig.text(0.05,0.08,'Source: Wells Fargo 3Q26 results via Quiver FilingTracker (Oct 13, 2026). Provision \\$1.029B vs \\$681M a year earlier. Loans are year-over-year averages.',color='#A9B4C6',fontsize=13,va='top')
fig.text(0.97,0.92,'LEAD-LAG',color=GOLD,fontsize=22,fontweight='bold',ha='right',va='top')
fig.savefig('wfc_credit.png',facecolor=NAVY)
