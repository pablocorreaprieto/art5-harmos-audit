import sys, json
import numpy as np, pandas as pd
sys.path.insert(0, sys.argv[1])
import analyze as A
df=pd.read_csv(sys.argv[1]+"/results/measures.csv",keep_default_na=False,na_values=["","nan","NaN"]); df["kept"]=A.as_bool(df["kept"])
ax=A.axes(df[df["label"].isin(A.GRADED_LABELS)])
labs=A.GRADED_LABELS; M,G,T=len(ax["models"]),6,len(ax["topics"])
sums=np.zeros((len(labs),M,G,T)); counts=np.zeros_like(sums)
mi={m:i for i,m in enumerate(ax["models"])}; ti={t:i for i,t in enumerate(ax["topics"])}
for r in df[df.kept & df.label.isin(labs)].itertuples():
    k=(labs.index(r.label),mi[r.model],A.GRADES.index(r.grade),ti[r.topic]); sums[k]+=r.mean_zipf_content; counts[k]+=1
means=A.cell_means(sums,counts)
i5=labs.index("L5")
for m in ("anthropic_light","mistral_light","openai_light","anthropic_balanced"):
    mm=mi[m]; ruler=means[i5,mm]; b=np.polyfit(A.AGES,ruler,1)[0]; curve=A.pava_decreasing(ruler)
    print(m,"ruler (L5 means by grade):",np.round(ruler,3),"| isotonic:",np.round(curve,3),"| local slopes per year:",np.round(np.diff(ruler),3),"| linear slope",round(b,4))
    for lab in ("L1","L1P"):
        li=labs.index(lab)
        iso=[A.age_equivalent(curve,means[li,mm,g],b) for g in range(6)]
        lin=[A.AGES[g]+ (means[li,mm,g]-ruler[g])/ (b) for g in range(6)]  # grade-wise linear-slope reading: age + dZipf/b
        print(f"   {lab} offsets in years (reading − requested age) by grade 3H..8H: isotonic lookup",[f"{a-A.AGES[g]:+.1f}{'*' if f!='inside' else ''}" for g,(a,f) in enumerate(iso)]," | per-grade dZipf/b (linear slope)",[f"{x-A.AGES[g]:+.1f}" for g,x in enumerate(lin)])
l1=json.load(open(sys.argv[1]+"/results/numbers.json"))["age_equivalent"]["by_label"]["L1"]["by_model"]
for m in ("anthropic_light","mistral_light"):
    w=l1[m]; mids=A.AGES; mean_mid=mids.mean()
    print(m,"linear-implied offset 3H: %.1f ; 8H: %.1f"%(w["shift_years"]+(w["tracking"]-1)*(6.5-mean_mid), w["shift_years"]+(w["tracking"]-1)*(11.5-mean_mid)))
