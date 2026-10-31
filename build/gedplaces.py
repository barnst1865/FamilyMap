import re
RULES=[
 (r'montr[ée]al|beauharnois|howick','__MTL'),(r'barnard castle','barnardcastle'),(r'^county durham','gainford'),(r'beverley','beverley'),
 (r'^austria','kawenczyn'),(r'la valle','morbegno'),(r'new brunswick|^new jersey','newbrunswick'),(r'^ct$','middletown'),
 (r'west camp|^ulster','westcamp'),(r'kingston','kingston'),(r'nieuw amsterdam','nyc'),(r'loonenbrug','athens'),(r'rengsdorf|elschied|elscheid','rengsdorf'),
 (r'feldkirchen|nieder-hattert|rodt, freud|hackenberg|sulzbach, aich|ruschberg|rotenburg|bellen, ober','__SKIP'),
 (r'south glens falls','sglensfalls'),(r'glens falls','glensfalls'),(r'fort edward','fortedward'),
 (r'salem, new hampshire','salemnh'),(r'riverfield','riverfield'),
 (r'higganum|haddam','haddam'),(r'middlefield','middlefield'),(r'new brit','newbritain'),
 (r'portland','portland'),(r'middle ?town|randolph road|^middlesex','middletown'),(r'^connecticut','middletown'),
 (r'kawenczyn','kawenczyn'),(r'^poland','kawenczyn'),
 (r'marbegno|morbegno|soudiro','morbegno'),(r'tonco','tonco'),(r'genova','genova'),(r'cherbourg','cherbourg'),
 (r'kippagh','cork'),(r'^ireland','cork'),
 (r'brooklyn','brooklyn'),(r'new york city|new york, new york','nyc'),
 (r'stuyvesant','stuyvesantfalls'),(r'clermont','clermont'),(r'livingston','livingston'),
 (r'rhinebeck','rhinebeck'),(r'red ?hook','redhook'),(r'linlithgo','linlithgo'),(r'saugerties','saugerties'),
 (r'loonenburg','athens'),(r'charlton','charlton'),(r'saratoga','saratoga'),(r'canadian expedition','expedition1711'),
 (r'germantown|east camp|columbia','germantown'),
 (r'gandles|gaundles','gandles'),(r'evenwood','evenwood'),(r'darlington','darlington'),(r'st\. helen','sthelen'),
 (r'west auckland','westauckland'),(r'bishop auckland','bishopauckland'),(r'eldon','eldon'),(r'bolam','bolam'),
 (r'gainford','gainford'),(r'^durham','durham'),(r'cotherstone','cotherstone'),(r'huntwell|northumberland','huntwell'),
 (r'driffield','driffield'),(r'beeford','beeford'),(r'whitwell','whitwell'),(r'crambe','crambe'),(r'hornsea','hornsea'),
 (r'bridlington','bridlington'),(r'^york','york'),
 (r'ho(ch|ck|c|k)speyer','hochspeyer'),(r'remscheid','remscheid'),(r'heddesdorf','heddesdorf'),(r'dierdorf','dierdorf'),
 (r'nordhofen','nordhofen'),(r'wölferlingen','wolferlingen'),(r'segendorf','segendorf'),(r'rockenf','rockenfeld'),
 (r'bonefeld','bonefeld'),(r'rendorf','rengsdorf'),(r'neuwied','neuwied'),(r'grötzingen','grotzingen'),
 (r'bochum','bochum'),(r'auf dem beller','hof'),(r'freu?n?denberg','freudenberg'),(r'leonberg','leonberg'),
 (r'traunstein','traunstein'),(r'middle franconia|^bavaria|^bayern, germany','nuremberg'),
 (r'westerwald|eldschied|lower saxony|preußen','westerwald'),(r'germany or france','germany'),(r'^france','france'),
 (r'rhineland-palatinate, germany$|^germany','germany'),
 (r'^new york|^united states','nystate'),
]
SKIP=re.compile(r'^(haiti|cones|goundrey, stacia|england)$',re.I)
def lookup(raw):
    s=raw.strip()
    if not s or SKIP.match(s): return None
    low=s.lower()
    for rx,k in RULES:
        if re.search(rx,low):
            if k=='__SKIP': return None
            if k=='__MTL': return 'montreal' if 'montr' in low else 'riverfield'
            return k
    return 'UNMATCHED:'+s
