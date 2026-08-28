# -*- coding: utf-8 -*-
import os, glob, re, collections
root = [d for d in glob.glob(os.path.expanduser("~/mnt/*/")) if "realitykit" not in d][0]
s = open(os.path.join(root,"Experiences","성향 누적.md"), encoding="utf-8").read()

sec = s[s.index("## 관찰 로그"): s.index("### 세지 않은 것")]
rows = [l for l in sec.split("\n") if l.startswith("| 20")]
print("행 수:", len(rows))

FACETS = {
 "E/I": [("Initiating","Receiving"),("Expressive","Contained"),("Gregarious","Intimate"),("Active","Reflective"),("Enthusiastic","Quiet")],
 "S/N": [("Concrete","Abstract"),("Realistic","Imaginative"),("Practical","Conceptual"),("Experiential","Theoretical"),("Traditional","Original")],
 "T/F": [("Logical","Empathetic"),("Reasonable","Compassionate"),("Questioning","Accommodating"),("Critical","Accepting"),("Tough","Tender")],
 "J/P": [("Systematic","Casual"),("Planful","Open Ended"),("Early Starting","Pressure Prompted"),("Scheduled","Spontaneous"),("Methodical","Emergent")],
}
def facet_of(axis, name):
    for i,(l,r) in enumerate(FACETS[axis]):
        if name == l or name == r: return i, (l if name==l else r)
    return None, None

era_counts = collections.Counter()
tally = collections.defaultdict(lambda: collections.Counter())  # (era,axis,facetidx) -> dir
unassigned = 0
for l in rows:
    c = [x.strip() for x in l.strip("|").split("|")]
    date, src, axis, facet, direction = c[0], c[1], c[2], c[3], c[4]
    era = "중학생" if "중학생 시절" in src else "현재"
    era_counts[era]+=1
    if facet == "미배정":
        unassigned += 1; continue
    fi, pole = facet_of(axis, facet)
    if fi is None:
        print("  !! 패싯 이름 불일치:", axis, facet); continue
    d = direction.replace("*","")
    tally[(era,axis)][ (fi, d) ] += 1

print("시기별 일화 수:", dict(era_counts), "| 미배정:", unassigned)
print()
for era in ["중학생","현재"]:
    print("==", era)
    for axis in ["E/I","S/N","T/F","J/P"]:
        per = collections.defaultdict(dict)
        for (fi,d),n in tally[(era,axis)].items():
            per[fi][d]=n
        votes = collections.Counter(); ties=0
        for fi, dd in sorted(per.items()):
            names = FACETS[axis][fi]
            if len(dd)==2 and len(set(dd.values()))==1:
                ties+=1; res="동점(무효)"
            else:
                w = max(dd, key=dd.get); votes[w]+=1; res=w
            print(f"   {names[0]}–{names[1]:<18} {dd} -> {res}")
        L,R = axis.split("/")
        nf = len(per)
        vl, vr = votes[L], votes[R]
        if nf>=3 and abs(vl-vr)>=2: verdict = (L if vl>vr else R)
        elif nf>=2 and (vl==0 or vr==0) and (vl+vr)>0 and ties==0: verdict = (L if vl>vr else R).lower()
        else: verdict = "?"
        print(f"   => {axis}: 근거패싯 {nf}, 표 {L}{vl}:{R}{vr}, 동점 {ties}  ==> {verdict}")
    print()
