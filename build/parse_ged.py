import re, json, collections
lines=open('tree.ged',encoding='utf-8-sig').read().splitlines()
recs={};cur=None;stack=[]
for ln in lines:
    m=re.match(r'^(\d+) (@[^@]+@ )?(\S+)(?: (.*))?$',ln)
    if not m: continue
    lvl=int(m.group(1)); xref=m.group(2); tag=m.group(3); val=m.group(4) or ''
    if lvl==0:
        cur={'id':xref.strip() if xref else None,'tag':tag,'kids':[]}
        if xref: recs[xref.strip()]=cur
        stack=[cur]; continue
    node={'tag':tag,'val':val,'kids':[]}
    stack=stack[:lvl]; stack[-1]['kids'].append(node); stack.append(node)
def kid(n,t): return [k for k in n['kids'] if k['tag']==t]
def v(n,t):
    k=kid(n,t); return k[0]['val'] if k else ''
people={};fams={}
for i,r in recs.items():
    if r['tag']=='INDI':
        nm=v(r,'NAME').replace('/','').strip()
        ev=[]
        for k in r['kids']:
            if k['tag'] in ('BIRT','DEAT','RESI','IMMI','EMIG','BURI','NATU','CENS','EVEN','MARR','RESI','_MILT','OCCU','DIV'):
                d=v(k,'DATE');p=v(k,'PLAC')
                if d or p: ev.append({'t':k['tag'],'d':d,'p':p,'v':k['val'],'ty':v(k,'TYPE')})
        people[i]={'id':i,'name':nm,'sex':v(r,'SEX'),'famc':[k['val'] for k in kid(r,'FAMC')],'fams':[k['val'] for k in kid(r,'FAMS')],'ev':ev}
    elif r['tag']=='FAM':
        ev=[]
        for k in r['kids']:
            if k['tag'] in ('MARR','DIV','RESI','EVEN'):
                ev.append({'t':k['tag'],'d':v(k,'DATE'),'p':v(k,'PLAC')})
        fams[i]={'h':v(r,'HUSB'),'w':v(r,'WIFE'),'c':[k['val'] for k in kid(r,'CHIL')],'ev':ev}
json.dump({'people':people,'fams':fams},open('ged.json','w'),ensure_ascii=False,indent=1)
# ancestors of Mary
root='@I222280913034@'
def parents(p):
    out=[]
    for f in people[p]['famc']:
        F=fams.get(f)
        if F:
            for x in (F['h'],F['w']):
                if x: out.append(x)
    return out
anc={}  # id -> (gen, path)
q=[(root,0,[])]
while q:
    p,g,path=q.pop(0)
    if p in anc: continue
    anc[p]=(g,path)
    for x in parents(p): q.append((x,g+1,path+[x]))
print(len(anc),'ancestors incl root')
tag_c=collections.Counter(e['t'] for p in anc for e in people[p]['ev'])
print(tag_c)
places=collections.Counter(e['p'] for p in anc for e in people[p]['ev'] if e['p'])
print(len(places))
for p,c in places.most_common(): print(c,'|',p)
