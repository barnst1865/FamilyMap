import json,re,math
from places import P as PL
import gedplaces, manual
D=json.load(open('ged.json'));GP=D['people'];GF=D['fams']
# ---- source classification
L=open('tree.ged',encoding='utf-8-sig').read().splitlines()
stitle={};cur=None
for l in L:
    m=re.match(r'^0 (@S[^@]+@) SOUR',l)
    if m: cur=m.group(1); stitle[cur]=''; continue
    if l.startswith('0 '): cur=None
    if cur and l.startswith('1 TITL '): stitle[cur]=l[7:]
psrc={};cur=None
for l in L:
    m=re.match(r'^0 (@I[^@]+@) INDI',l)
    if m: cur=m.group(1); psrc[cur]=set(); continue
    if l.startswith('0 '): cur=None
    m=re.match(r'^\d (?:SOUR) (@S[^@]+@)',l)
    if cur and m: psrc[cur].add(stitle.get(m.group(1),''))
TREE_SRC=re.compile(r'Family Trees|Community Trees|Family Histories',re.I)
def gconf(pid):
    s=psrc.get(pid,set())
    if any(t and not TREE_SRC.search(t) for t in s): return 'rec'
    return 'tree'
def dist(a,b):
    la1,lo1=math.radians(PL[a][1]),math.radians(PL[a][2]);la2,lo2=math.radians(PL[b][1]),math.radians(PL[b][2])
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 12742*math.asin(min(1,math.sqrt(h)))
def clean(stops,b):
    # 1) same-time conflicts: drop child stops that disagree with another stop at ~same time
    out=[]
    for i,s in enumerate(stops):
        if s[4]=='child':
            rivals=[t for t in stops if t is not s and abs(t[0]-s[0])<0.6 and t[1]!=s[1] and dist(t[1],s[1])>80]
            if rivals: continue
        out.append(s)
    # 2) bounce / outlier removal for child stops
    changed=True
    while changed:
        changed=False
        seq=[(b[0],b[1],'',False,'birth')]+out if b and b[1] else out
        for i in range(1,len(seq)-1):
            x=seq[i]
            if x[4]!='child': continue
            p,n=seq[i-1],seq[i+1]
            if not p[1] or not n[1]: continue
            if n[0]-p[0]<15 and dist(p[1],n[1])<150 and min(dist(x[1],p[1]),dist(x[1],n[1]))>40:
                out.remove(x); changed=True; break
    # 3) collapse consecutive same-place stops (keep first; keep informative text)
    res=[]
    for s in out:
        if res and res[-1][1]==s[1] and s[4] in('res','child'): continue
        res.append(s)
    return res
# ---- dates
MON={m:i+1 for i,m in enumerate('jan feb mar apr may jun jul aug sep oct nov dec'.split())}
def gyear(s):
    if not s: return None
    low=s.lower()
    m=re.search(r'(\d{4})',s)
    if not m:
        m=re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})',s)
        return None
    y=int(m.group(1))
    mm=None
    for k,v in MON.items():
        if re.search(r'\b'+k,low) or re.search(r'\d'+k,low): mm=v;break
    if mm is None:
        m2=re.match(r'^(\d{1,2})[ -](\d{1,2})[ -](\d{4})$',s.strip())
        if m2: mm=int(m2.group(2))
    d=re.match(r'^(\d{1,2})\s',s.strip())
    dd=int(d.group(1)) if d and mm else 1
    return round(y+((mm or 7)-1)/12+(dd-1)/365,3) if mm else y+0.5
def approxdate(s): return bool(re.search(r'abt|about|bef|aft|~|\?',s or '',re.I))
# ---- GEDCOM ancestors
def gparents(p):
    out=[]
    for f in GP[p]['famc']:
        x=GF.get(f)
        if x: out.append((x['h'],x['w']))
    return out[0] if out else (None,None)
heads={'@I222280913104@':'goundrey','@I222280913228@':'romegialli'}
people={}
CLAIMED=re.compile(r'roquefeuil|haller|rieter|reiter|goddard|pauli|kockenf|rockenfeller|lotzia|britzen',re.I)
def norm(n): return re.sub(r'[^a-z]','',n.lower().replace('de roquefeuil','').replace('rockefeller',''))
seen_key={}
alias={}
def walk(pid,branch,depth,frac_lo,frac_hi,path):
    pp=GP[pid]
    name=re.sub(r'\s+',' ',pp['name'].replace('*','').replace('💟🧬','').replace('9th GGF','').replace('9th GGM','')).strip()
    by=None
    for e in pp['ev']:
        if e['t']=='BIRT': by=gyear(e['d'])
    key=(norm(name),int(by) if by else None)
    if depth>0:
        if key in seen_key and key[1]:
            alias[pid]=seen_key[key]; return
        seen_key[key]=pid
    f,m=gparents(pid)
    if depth>0:
        people[pid]=dict(id=pid,gid=pid,name=name,sex=pp['sex'],branch=branch,depth=depth,frac=(frac_lo+frac_hi)/2,father=f,mother=m,src='ged',path=path)
    mid=(frac_lo+frac_hi)/2
    if f: walk(f,branch,depth+1,frac_lo,mid,path+[GP[f]['name'].split()[-1] if GP[f]['name'] else '?'])
    if m: walk(m,branch,depth+1,mid,frac_hi,path+[GP[m]['name'].split()[-1] if GP[m]['name'] else '?'])
for h,b in heads.items(): walk(h,b,0,0.0,1.0,[])
# children map (all GEDCOM)
children={}
for fid,F in GF.items():
    for par in (F['h'],F['w']):
        if par: children.setdefault(par,[]).extend(F['c'])
def gbirth(pid):
    for e in GP[pid]['ev']:
        if e['t']=='BIRT': return gyear(e['d']),e['p'],e['d']
    return None,None,None
# per-person overrides / extra stops for GEDCOM people
def ym(y,m=7,d=1): return manual.ym(y,m,d)
EXTRA={
 'James Goundrey':[(1832,'montreal','First child born at Montréal, 1832',True),(1834,'riverfield','Settles at Riverfield (“Goundrey’s Rapids”), Beauharnois seigneury',True)],
 'Elizabeth (Frost) Cowan':[(1832,'montreal','First child born at Montréal, 1832',True),(1834,'riverfield','Riverfield, Châteauguay',True)],
 'George Goundrey':[(1869,'fortedward','In New York State by 1870',True)],
 'Andrea Romegialli':[],
 'Claudina Ferraris Romegialli':[(ym(1903,4,8),'cherbourg','Sails, probably from Cherbourg',True)],
 'Ernest Huber':[(1885,'nyc','Comes to America about 1880–90 (records disagree)',True)],
 'Catherine H Borewise':[(1907,'nyc','Arrives in America (1901 or 1907)',True)],
}
PALATINE=['Sebastian Lasher','Johan George Lasher','John Henrick Haemmer','Maria (Magdalena) Haemmer','Elizabeth Livingston','Johannis Schumacher','Anna Barbara Wagner','Johann Adam Segendorf','Johann Herman Segendorff','Maria Catharina Schneider']
BPLACE_OVR={'Thomas H. Goundrey':('fortedward',True),'Lydia L. Hanford':('fortedward',True),'Mary Huber':('nyc',True),
 'Andrew Lasher':('germantown',True),'Eliza Catherine Staats':('germantown',True),'Johannes Staats':('germantown',True),'Rachel Cooke':('germantown',True),
 'PETER SCHUMACHER':('germany',True),'John Goundry@1600':('gainford',True),'Isabela (Isabell) Naitby (Neteby)':('gainford',True)}
TREENOTE={'PETER SCHUMACHER':'The tree gives his birthplace as Germantown, NY, which was not settled until 1710.',
 'Dieterici Schneider':'The tree’s death at Livingston Manor in 1703 predates the Palatine settlement of 1710.',
 'Elizabeth Livingston':'Entered as “Livingston”, but her parents in the tree are Haemmers; she is also the wife in two Lasher families.',
 'Giovanna Maria GENOVESIO\\FERRARIS':'Entered as Claudina’s father; the name is muddled in the tree.',
 'George Goundrey':'Whether George or his brother Thomas was Thomas H. Goundrey’s father is still open.'}
DPLACE_OVR={'Margaret J. McSweeney':('glensfalls',True),'Dieterici Schneider':('germany',True),'Johannes Staats':('germantown',True)}
NOCHILD={'Dieterici Schneider','Anna Maria Duenschmann Schneider','Thoengess Anthonius Rockenfeller'}
SKIP_NAMES={'Giovanna Maria GENOVESIO\\FERRARIS','FNU LNU','Narz Borowicz','Annae Mariae','Christofor Neteby','Mark Bell','Mary Bell','Ann Johnson','Rose Bevilaqua'}
def place_of(raw,nm,year):
    k=gedplaces.lookup(raw) if raw else None
    if k and k.startswith('UNMATCHED'): print('UNMATCHED',nm,raw); k=None
    approx = bool(k and PL[k][3])
    if k=='nystate' and year:
        k = 'germantown' if year<1850 else 'nyc'; approx=True
    return k,approx
out=[]
for pid,p in people.items():
    nm=p['name']; pp=GP[pid]
    if nm in SKIP_NAMES: continue
    stops=[]; b=None; d=None
    for e in pp['ev']:
        y=gyear(e['d']); k,ap=place_of(e['p'],nm,y)
        ap = ap or approxdate(e['d'])
        t=e['t']
        if t=='BIRT':
            ov=BPLACE_OVR.get(nm) or BPLACE_OVR.get(f'{nm}@{int(y) if y else ""}')
            if ov: k,ap=ov[0],True
            b=(y,k,ap)
        elif t=='DEAT':
            if d: continue
            ov=DPLACE_OVR.get(nm)
            if ov: k,ap=ov[0],True
            d=(y,k,ap)
        elif t in('RESI',) and y and k:
            stops.append((y,k,'Living at %s'%PL[k][0],ap,'res'))
        elif t=='EVEN' and y and k and 'Arrival' in (e['ty'] or ''):
            stops.append((y,'ellis' if k in('nyc','nystate') else k,'Arrives in New York',ap,'arr'))
        elif t=='_MILT' and y and k:
            stops.append((y,k,'Revolutionary War service',ap,'mil'))
        elif t=='MARR' and y and k:
            stops.append((y,k,'Marries',ap,'marr'))
    # family marriages
    for f in pp['fams']:
        F=GF.get(f)
        if not F: continue
        for e in F['ev']:
            if e['t']=='MARR':
                y=gyear(e['d']); k,ap=place_of(e['p'],nm,y)
                if y and k: stops.append((y,k,'Marries',ap or approxdate(e['d']),'marr'))
    # child births
    cb=[]
    for c in (set(children.get(pid,[])) if nm not in NOCHILD else set()):
        cy,cp,cd=gbirth(c)
        if cy and cp:
            k,ap=place_of(cp,nm,cy)
            if c in people and people[c]['name'] in BPLACE_OVR: k=BPLACE_OVR[people[c]['name']][0]; ap=True
            if k and k not in('nystate','germany','france'):
                cname=GP[c]['name'].split()[0] if GP[c]['name'] else 'a child'
                stops.append((cy,k,'Child %s born at %s'%(cname,PL[k][0]),ap or approxdate(cd),'child'))
            cb.append(cy)
    for (y,k,txt,ap) in EXTRA.get(nm,[]): stops.append((y,k,txt,ap,'x'))
    if nm in PALATINE and b and b[0] and b[0]<1709 and (not d or not d[0] or d[0]>1710):
        stops += [(ym(1709,6),'london','Probably among the Palatine refugees camped at London, 1709',True,'x'),
                  (ym(1710,6,14),'nyc','Probably with the Palatine fleet that reached New York, June 1710',True,'x'),
                  (ym(1710,10),'germantown','East Camp settlement on Livingston Manor',True,'x')]
        if nm=='Johann Adam Segendorf': d=(ym(1711,9),'expedition1711',True)
    # estimate birth
    if not b or not b[0]:
        est=None
        if cb: est=min(cb)-(28 if p['sex']=='M' else 25)
        if est is None: continue
        bk=b[1] if b and b[1] else None
        b=(est,bk,True)
    stops.sort(key=lambda s:s[0])
    stops=clean(stops,b)
    appear=None
    if not b[1]:
        if stops: b=(b[0],stops[0][1],True); appear=stops[0][0]
        else: continue
    if d and not d[1]:
        d=(d[0], stops[-1][1] if stops else b[1], True)
    if d and not d[0]: d=None
    conf=gconf(pid)
    rec=dict(id=pid,name=nm,sex=p['sex'],branch=p['branch'],depth=p['depth'],frac=p['frac'],
             line=pp['name'].split()[-1] if pp['name'] else '',path=p['path'],conf=conf,
             b=[b[0],b[1],b[2],'Born'],d=[d[0],d[1],d[2],'Dies'] if d else None,
             stops=[[y,k,t,ap] for (y,k,t,ap,_) in stops if (not d or y<=d[0]) and y>=b[0]],
             last=max([s[0] for s in stops]+[b[0]]) if not d else None, rel='anc', appear=appear,
             note=TREENOTE.get(nm,''), src='Ancestry tree')
    out.append(rec)
# ---- manual
M={p['id']:p for p in manual.PEOPLE}
def mwalk(pid,depth,lo,hi,path):
    p=M[pid]; p['depth']=depth; p['frac']=(lo+hi)/2; p['path']=path
    mid=(lo+hi)/2
    if p.get('father') in M: mwalk(p['father'],depth+1,lo,mid,path+[M[p['father']].get('line') or M[p['father']]['name'].split()[-1]])
    if p.get('mother') in M: mwalk(p['mother'],depth+1,mid,hi,path+[M[p['mother']].get('line') or M[p['mother']]['name'].split()[-1]])
mwalk('KHEAD',0,0,1,[]); mwalk('RHEAD',0,0,1,[])
for p in manual.PEOPLE:
    if p['rel']=='rel':
        par=M[p['father']]; p['depth']=par['depth']-1; sib='L-016' if p['id'] in('L-014','L-013') else 'L-020'; p['frac']=M[sib]['frac']; p['path']=M[sib]['path']
for p in manual.PEOPLE:
    if p['rel']=='head': continue
    if 'depth' not in p: print('UNLINKED',p['id']); continue
    b=p['b']; d=p['d']
    rec=dict(id=p['id'],name=p['name'],sex=p['sex'],branch=p['branch'],depth=p['depth'],frac=p['frac'],
             line=p.get('line') or p['name'].split()[-1],path=p['path'],conf=p['conf'],
             b=[b[0],b[1],(b[3] if len(b)>3 else False),b[2]],
             d=[d[0],d[1],(d[3] if len(d)>3 else False),d[2]] if d else None,
             stops=[[s[0],s[1],s[2],(s[3] if len(s)>3 else False)] for s in sorted(p['stops'])],
             last=p['last'],rel=p['rel'],note=p['note'],src='Family research, Oct 2026')
    out.append(rec)
def clean_name(n):
    n=re.sub(r'\s*\(\d{4}\)','',n).replace('*','').strip()
    n=re.sub(r'\s+',' ',n)
    if n.isupper() or re.search(r'\b[A-Z]{4,}\b',n):
        n=' '.join(w.capitalize() if w.isupper() and len(w)>2 else w for w in n.split())
    return n
LINE_OVR={'Mary (Lasher) Anderson':'Lasher','Elizabeth Livingston':'Haemmer','Elizabeth (Frost) Cowan':'Cowan','Isabela (Isabell) Naitby (Neteby)':'Naitby',
 'Catharina Stickel 💟🧬':'Stickel','Johann Adam Segendorf 9th GGF':'Sagendorf','Anna Margaretha -?- 9th GGM':'Sagendorf','Anna Margaretha -?-':'Sagendorf',
 'Johann Wilhelm Rockenfeller SR.':'Rockefeller','Johann Wilhelm Altzdorff\\Alsdorf':'Alsdorf','Christ Britzen (Britz)':'Britzen','Margaret':'Goundry',
 'Annae Mariae':'Schneider','Izabella von Kockenfeldt married as Pauli NFI':'Kockenfeldt','Magdalena de Rockenfeller (Goddard)':'Goddard',
 'Thomas H. Goundrey':'Goundrey','Mary Theresa Huber Romegialli':'Huber','Claudina Ferraris Romegialli':'Ferraris','Catherine H Borewise':'Borowicz',
 'Lt. Johann Adam Segendorf':'Sagendorf','Johann Herman Segendorff':'Sagendorf','Hermann Segendorff':'Sagendorf','Maria Catharina Segendorf':'Sagendorf',
 'Tommasso Romegialli':'Romegialli','Assunta Ronconi':'Ronconi','Hannah Oconnell':"O'Connell",'Eugene McSweeney':'McSweeney','Margaret J. McSweeney':'McSweeney'}
NORM_LINE={'Goundry':'Goundrey','Cowen':'Cowan','Rockafellar':'Rockefeller','Rockenfeller':'Rockefeller','Alsdorff':'Alsdorf','Segendorf':'Sagendorf','Segendorff':'Sagendorf','Oconnell':"O'Connell",'Moor':'Mohr','Borewise':'Borowicz','Kockenfelt':'Kockenfeldt','Hallerstein':'Haller','Kornburg':'Rieter'}
byid={r['id']:r for r in out}
for r in out:
    if r['src']!='Ancestry tree': continue
    raw=r['name']; nm=clean_name(raw); r['name']=nm
    ln=LINE_OVR.get(raw) or LINE_OVR.get(nm)
    if not ln:
        words=[w for w in re.findall(r"[A-Za-zÀ-ÿ'’]+",nm) if w.lower() not in('von','de','van','sr','jr','nfi','ggf','ggm','th','i','ii','iii') or len(re.findall(r"[A-Za-z]+",nm))<2]
        ln=words[-1] if words else nm
        if ln.isupper(): ln=ln.capitalize()
    if 'roquefeuil' in nm.lower(): ln='Roquefeuil'
    r['line']=NORM_LINE.get(ln,ln)
for r in out:
    if r['src']!='Ancestry tree': continue
    # rebuild path from GEDCOM ancestry chain
    chain=[]; pid=r['id']; cur=pid
    # walk down via people[] parent links is hard; use stored path length and recompute top-down
import research
def conv(t):
    return [t[0],t[1],t[2],t[3]] if t else None
# additions first (keyed on original names)
keyidx={(r['name'],r['depth']):r for r in out if r['src']=='Ancestry tree'}
for ck,which,rec in research.ADD:
    c=keyidx[ck]; w=1/2**c['depth']
    nr=dict(id=rec['id'],name=rec['name'],sex=rec['sex'],branch=c['branch'],depth=c['depth']+1,
            frac=c['frac']+(-w/4 if which=='father' else w/4),line=rec['line'],path=None,conf=rec['conf'],
            b=conv(rec['b']),d=conv(rec.get('d')),stops=[list(s) for s in rec.get('stops',[])],
            last=rec.get('last'),rel='anc',appear=None,note=rec.get('note',''),src=rec['src'],
            parent_of=c['id'],which=which)
    out.append(nr)
for r in list(out):
    if r['src']!='Ancestry tree': continue
    if r['name'] in research.REMOVE: out.remove(r); continue
    o=research.OVR.get((r['name'],r['depth']))
    if not o: continue
    for k,v in o.items():
        if k=='b': r['b']=conv(v); r['appear']=None
        elif k=='d': r['d']=conv(v)
        elif k=='stops': r['stops']=[list(s) for s in v]
        elif k=='src': r['src']=v
        else: r[k]=v
    if 'd' in o and o['d'] is None and 'last' not in o: r['last']=max([s[0] for s in r['stops']]+[r['b'][0]])
    if o.get('d'): r['last']=None
    r['ovr']=True
byid={r['id']:r for r in out}
for h,bname in heads.items():
    def down(pid,path):
        f,m=gparents(pid)
        for x in (f,m):
            if not x: continue
            xx=alias.get(x,x)
            if xx in byid:
                rr=byid[xx]; rr['path']=path+[rr['line']]
                down(x,rr['path'])
                for a in out:
                    if a.get('parent_of')==xx: a['path']=rr['path']+[a['line']]
            elif x in people:
                down(x,path)
    down(h,[])
# validate places
used=set()
for r in out:
    for s in [r['b']]+([r['d']] if r['d'] else [])+r['stops']:
        if s[1] not in PL: print('BAD PLACE',r['name'],s)
        used.add(s[1])
for e in manual.EVENTS: used.add(e[1])
places={k:dict(n=v[0],lat=v[1],lon=v[2],ap=v[3]) for k,v in PL.items() if k in used}
events=[dict(y=e[0],p=e[1],br=e[2],t=e[3]) for e in manual.EVENTS]
# a few Goundrey/Romegialli context events
events+= [dict(y=1710.45,p='nyc',br='romegialli',t='The Palatine fleet reaches New York; Huber-side ancestors settle at East Camp (Germantown)'),
          dict(y=1832,p='montreal',br='goundrey',t='James Goundrey and Elizabeth Cowan are in Lower Canada; their first child is born at Montréal'),
          dict(y=1900.23,p='ellis',br='romegialli',t='Andrea Romegialli arrives in New York from the Valtellina'),
          dict(y=1900.76,p='ellis',br='goundrey',t='Peter Paul Czepiel arrives in New York from Galicia'),
          dict(y=1940,p='middletown',br='goundrey',t='George Eugene Goundrey is in Middletown: the Goundrey and Romegialli lines now live in the same town')]
json.dump(dict(people=out,places=places,events=events),open('data.json','w'),ensure_ascii=False)
from collections import Counter
print(len(out),'people',Counter(r['branch'] for r in out),Counter(r['conf'] for r in out))
print('maxdepth',max(r['depth'] for r in out),'years',min(r['b'][0] for r in out),max((r['d'] or [0])[0] for r in out))
