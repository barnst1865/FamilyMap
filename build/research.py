# Corrections from the Goundrey/Romegialli research of 31 Oct 2026 (Goundrey branch/01 Findings.md).
# Keys: (name as it comes out of the GEDCOM build, depth). Values replace fields wholesale.
def ym(y,m=7,d=1): return round(y+(m-1)/12+(d-1)/365,3)
R='Goundrey research, Oct 2026'
OVR={
('George Eugene Goundrey',1):dict(conf='doc',src=R,b=(ym(1910,8,17),'sglensfalls',False,'Born at South Glens Falls'),stops=[
  (1930,'sglensfalls','Accountant, at his parents’ home (1930 census)',False),(1935,'brooklyn','In Brooklyn (1935)',False),
  (ym(1940,4),'middletown','Accountant, rooming in Middletown; works at Russell Manufacturing Co.',False),
  (ym(1941,6,21),'haddam','Marries Stacia Czepiel at Haddam',False),(ym(1941,7),'middletown','Middletown; a CPA by 1950',True)],
  d=(ym(1984,2,25),'middletown',False,'Dies in Middletown; buried Calvary Cemetery')),
('Stacia Czepiel',1):dict(conf='doc',src=R,b=(ym(1913,3,31),'haddam',False,'Born at Higganum'),stops=[
  (ym(1941,6,21),'haddam','Marries George Eugene Goundrey',False),(ym(1941,7),'middletown','Middletown',True)],
  d=(ym(2004,8,20),'middletown',False,'Dies in Middletown; buried Calvary Cemetery')),
('Thomas H. Goundrey',2):dict(conf='doc',src=R,b=(ym(1870,12,10),'sglensfalls',False,'Born at South Glens Falls'),stops=[
  (1875,'queensbury','Aged 4, with his parents George and Lydia at Queensbury',False),
  (1900,'sglensfalls','Paper maker, boarding at Moreau with his grandmother Mary Fish and her husband',False),
  (ym(1907,6,11),'glensfalls','Marries Margaret J. McSweeney at Glens Falls',False),
  (1910,'sglensfalls','Owns 130 Main St, South Glens Falls; bartender, later papermaker',False)],
  d=(ym(1945,2,9),'sglensfalls',False,'Killed in a 40-foot fall from the roof of the Finch-Pruyn paper mill')),
('Margaret J. McSweeney',2):dict(conf='doc',src=R,b=(ym(1878,7,12),'glensfalls',False,'Born at Glens Falls'),stops=[
  (1880,'queensbury','Aged 2, in her father’s household at Queensbury',False),(1900,'glensfalls','At home, Glens Falls',False),
  (ym(1907,6,11),'glensfalls','Marries Thomas H. Goundrey',False),(1910,'sglensfalls','130 Main St, South Glens Falls',False)],
  d=(ym(1966,1,3),'sglensfalls',True,'Dies aged 87; buried St Mary’s Cemetery, South Glens Falls')),
('George Goundrey',3):dict(conf='doc',src=R,note='His New Hampshire death record names his parents as James Goundrey and Elizabeth Cowan.',
  b=(ym(1850,5,27),'riverfield',False,'Born in Québec, son of James Goundrey and Elizabeth Cowan'),stops=[
  (1869.5,'queensbury','Marries Lydia Andrews about 1870 (record not found)',True),(1870.9,'sglensfalls','Son Thomas born at South Glens Falls',False),
  (1875,'queensbury','Head of household at Queensbury with Lydia and Thomas',False),(1878.9,'glensfalls','Widowed; Lydia dies at Glens Falls',False)],
  d=(ym(1933,3,6),'salemnh',False,'Dies at Salem, New Hampshire; buried Bay Street Cemetery, Glens Falls')),
('Lydia L. Hanford',3):dict(name='Lydia L. Andrews (“Hanford”)',line='Andrews',conf='prob',src=R,
  note='Probably born Lydia L. Andrews: “Hanford” is the first name of her stepfather, Hanford Fish.',
  b=(ym(1846,11,5),'queensbury',True,'Born about 1846'),stops=[
  (1850,'queensbury','Aged 4, with Judson and Mary Andrews at Queensbury',False),(1855,'chester','At Chester',False),
  (1860,'chester','In the household of her stepfather Hanford Fish at Chester',False),
  (1869.5,'queensbury','Marries George Goundrey about 1870',True),(1870.9,'sglensfalls','Son Thomas born',False),(1875,'queensbury','Queensbury',False)],
  d=(ym(1878,11,27),'glensfalls',False,'Dies at Glens Falls, 17 days after her infant son Arthur; buried Bay Street Cemetery')),
('Eugene McSweeney',3):dict(conf='doc',src=R,b=(1845,'cork',True,'Born in Co. Cork about 1843–48 (“Kippagh” unsourced)'),stops=[
  (ym(1870,3,10),'queenstown','Sails from Queenstown, probably on the SS Minnesota',True),(ym(1870,3,28),'ellis','Arrives in New York, 1870',True),
  (1870.5,'queensbury','Upstate New York; marries Hannah O’Connell about 1874',True),(1880,'queensbury','Sawmill worker at Queensbury',False),
  (1900,'glensfalls','Restaurant keeper, 12 William St, Glens Falls; later a saloon owner',False)],
  d=(ym(1913,11,26),'glensfalls',False,'Dies at Glens Falls; buried St Mary’s, South Glens Falls')),
('Hannah Oconnell',3):dict(name='Hannah O’Connell',conf='doc',src=R,b=(ym(1850,1),'cork',True,'Born in Ireland'),stops=[
  (1874,'queensbury','Marries Eugene McSweeney about 1874',True),(1880,'queensbury','Queensbury',False),(1900,'glensfalls','Glens Falls',False)],
  d=(ym(1910,10,31),'glensfalls',False,'Dies at Glens Falls; buried St Mary’s, South Glens Falls')),
('James Goundrey',4):dict(conf='doc',src=R,note='A miller. His first wife, Isabella Vasey, died in Montréal in May 1829.',
  b=(ym(1798,5,18),'westauckland',False,'Born at West Auckland, third son of John Goundry and Mary Castle'),stops=[
  (ym(1804,9,9),'sthelen','Baptised at St Helen Auckland with his baby brother',False),
  (ym(1829,5),'montreal','A miller in Montréal by 1829; his first wife Isabella dies',False),
  (ym(1831,3,4),'montreal','Marries the widow Elizabeth Sanderson (née Cowan) at Christ Church, Montréal',False),
  (1837,'stedouard','Parish of Saint-Édouard, near La Prairie',False),(1841,'beauharnois','In the seigniory of Beauharnois',False),
  (ym(1845,2),'howick','Howick village; buys land from the seigniory',False),(1847.5,'ormstown','Miller and farmer near Ormstown',False),
  (1861,'riverfield','Riverfield (St-Jean-Chrysostôme), beside “Goundrey’s Rapids”',False)],
  d=(ym(1885,3,4),'riverfield',False,'Dies; buried Riverfield Cemetery')),
('Elizabeth (Frost) Cowan',4):dict(name='Elizabeth Cowan',conf='doc',src=R,note='Widow of George Sanderson, who died in Montréal in 1830.',
  b=(ym(1805,6,18),'driffield',True,'Born about 1805 (baptism not found)'),stops=[
  (ym(1830,9,19),'montreal','Widowed in Montréal when George Sanderson dies',True),
  (ym(1831,3,4),'montreal','Marries James Goundrey at Christ Church, Montréal',False),
  (1837,'stedouard','Saint-Édouard',False),(1841,'beauharnois','Beauharnois seigniory',False),(ym(1845,2),'howick','Howick',False),
  (1847.5,'ormstown','Ormstown',False),(1861,'riverfield','Riverfield',False)],
  d=(ym(1873,6,14),'riverfield',False,'Dies; buried Riverfield Cemetery')),
('John Goundry',5):dict(conf='doc',src=R,b=(ym(1745,4,5),'darlington',True,'Born about 1745'),stops=[
  (ym(1781,6,4),'heighington','Marries Mary Castle at Heighington',False),(1787,'westauckland','Labourer of West Auckland; children baptised at St Helen Auckland',False)],
  d=(ym(1832,1,15),'sthelen',False,'Buried at St Helen Auckland, aged 87')),
('Mary Castle',5):dict(conf='doc',src=R,b=(1761,'darlington',True,'“Native of Darlington”'),stops=[
  (ym(1781,6,4),'heighington','Marries John Goundry at Heighington',False),(1787,'westauckland','West Auckland',False)],
  d=(ym(1824,5,6),'sthelen',False,'Buried at St Helen Auckland, aged 63')),
('George Goundry',6):dict(conf='tree',note='The Gainford baptism attached in the tree belongs to another child; his birth needs the Quaker register.'),
('Christopher Goundry',10):dict(conf='doc',src=R,stops=[(ym(1590,10,25),'gainford','Marries Margaret Martin at Gainford',False)]),
('Margaret Martin',10):dict(conf='doc',src=R,stops=[(ym(1590,10,25),'gainford','Marries Christopher Goundry at Gainford',False)]),
('Thomas Cowen',5):dict(name='Thomas Cowen (Cawen)',conf='doc',src=R,b=(ym(1788,7,14),'beeford',False,'Baptised at Beeford'),stops=[
  (1805,'driffield','Daughter Elizabeth born about 1805 (place from the tree)',True),(1851,'beeford','At Beeford, aged 63, with his wife Esther',False)],
  d=(ym(1862,8),'driffield',True,'Death registered in Driffield district')),
('Esther Frost',5):dict(conf='doc',src=R,b=(ym(1787,4,13),'crambe',False,'Baptised at Crambe, daughter of John Frost of Whitwell'),stops=[
  (1805,'driffield','Married to Thomas Cowen',True),(1851,'beeford','At Beeford',False)],
  d=(ym(1865,2),'driffield',True,'Death registered in Driffield district')),
('John Frost',6):dict(conf='doc',src=R,b=(1755,'whitwell',True,'Labourer of Whitwell'),stops=[(1778,'whitwell','Children baptised at Crambe, 1778–99',False)],last=1799),
('Peter Cowan',6):dict(stops=[(ym(1777,11,26),'beverley','Marries Ellis Bell at Beverley St Nicholas',False),(1788,'beeford','Son Thomas baptised at Beeford',False)]),
('Ellis Bell',6):dict(stops=[(ym(1777,11,26),'beverley','Marries Peter Cowan at Beverley St Nicholas',False),(1788,'beeford','Beeford',False)]),
('Percival Frost',7):dict(conf='claimed',note='The link to John Frost of Whitwell is unsupported and doubtful.'),
('Elizabeth Winn',7):dict(conf='claimed',note='The link to John Frost of Whitwell is unsupported and doubtful.'),
('Peter Paul Czepiel',2):dict(name='Peter Paul (Piotr) Czepiel',conf='doc',src=R,b=(ym(1881,6,22),'kawenczyn',True,'Born at Kawęczyn, Galicia'),stops=[
  (ym(1900,9,25),'hamburg','Sails from Hamburg on the Auguste Victoria',False),(ym(1900,10,6),'ellis','Arrives in New York, Oct 1900',False),
  (ym(1900,10,15),'haddam','Higganum; laborer, later at the Cutaway Harrow Co.',False),(1942,'haddam','Works at Russell Manufacturing Co., Middletown (1942)',False)],
  d=(ym(1956,11,24),'haddam',False,'Dies at Haddam')),
('Catherine H Borewise',2):dict(name='Katarzyna (Catherine) Borowicz',conf='doc',src=R,b=(1879.5,'kawenczyn',True,'Born about 1879 in Galicia'),stops=[
  (ym(1901,11,8),'ellis','Probably first crosses in 1901 (unproven)',True),(1902,'haddam','Lives at Higganum, 1900–04',False),
  (ym(1904,6),'kawenczyn','Back at Kawęczyn; son Julian born about July 1904',False),
  (ym(1905,5,1),'bremen','Sails from Bremen on the Kaiser Wilhelm II with Julian',False),
  (ym(1905,5,10),'ellis','Arrives in New York, 10 May 1905; her husband paid the ticket',False),(ym(1905,5,15),'haddam','Rejoins Peter at Higganum',False)],
  d=(ym(1964,10,10),'haddam',False,'Dies at Haddam')),
('Emilio T Romegialli',1):dict(name='Emilio T. Romegialli',conf='doc',src=R,b=(ym(1909,5,12),'berlinct',False,'Born at Berlin, Connecticut'),stops=[
  (1910,'middletown','Middletown',False),(ym(1945,12,29),'middletown','Marries Mary Theresa Huber in Middletown',False)],
  d=(ym(2003,1,7),'portland',False,'Dies at Portland, Connecticut')),
('Mary Theresa Huber Romegialli',1):dict(name='Mary Theresa Huber',conf='doc',b=(ym(1911,8,28),'portland',True,'Born in Connecticut'),stops=[
  (1920,'portland','Portland, with her parents',False),(1935,'middletown','Middletown',False),(ym(1945,12,29),'middletown','Marries Emilio Romegialli',False)],
  d=(ym(2002,7,22),'middletown',False,'Dies in Middletown')),
('Andrea Romegialli',2):dict(conf='doc',src=R,b=(ym(1876,11,29),'morbegno',False,'Born in the frazione of Valle, Morbegno'),stops=[
  (ym(1900,3,17),'havre','Sails from Le Havre on La Touraine',False),(ym(1900,3,24),'ellis','Arrives in New York, 24 Mar 1900',False),
  (ym(1900,4),'newbritain','Bound for New Britain; his brother Giacomo is at East Berlin',True),
  (ym(1904,12,10),'newhaven','Marries Claudina Ferraris at New Haven',False),(1906.2,'cromwell','Cromwell',False),
  (1907.4,'berlinct','Berlin',False),(1910,'middletown','Middletown; a brick burner at a brickyard',False),(1930,'middletown','Owns 663 High St, Middletown',False)],
  d=(ym(1967,12,19),'middletown',False,'Dies in Middletown')),
('Claudina Ferraris Romegialli',2):dict(name='Claudina Ferraris',conf='doc',src=R,b=(ym(1885,3,10),'tonco',False,'Born at Tonco'),stops=[
  (ym(1903,4,15),'cherbourg','Sails from Cherbourg on the Kaiser Wilhelm II',False),(ym(1903,4,22),'ellis','Arrives in New York, 22 Apr 1903',False),
  (ym(1903,4,25),'brooklyn','Bound for Brooklyn with two neighbours from Tonco',False),
  (ym(1904,12,10),'newhaven','Marries Andrea Romegialli at New Haven',False),(1906.2,'cromwell','Cromwell',False),
  (1907.4,'berlinct','Berlin',False),(1910,'middletown','Middletown',False)],
  d=(ym(1968,4,10),'middletown',False,'Dies in Middletown')),
('Tommasso Romegialli',3):dict(name='Tomaso Romegialli',conf='doc',src=R,b=(1823,'morbegno',True,'Born about 1823, son of Antonio Romegialli and Rosa Ronconi'),stops=[
  (ym(1874,9,26),'morbegno','Farmer at Valle, Morbegno; son Giacomo born',False)],
  d=(ym(1886,12,31),'morbegno',False,'Dies in his house at Valle, Morbegno, aged 63')),
('Assunta Ronconi',3):dict(conf='doc',src=R,b=(1845,'morbegno',True,'Daughter of Giacomo Ronconi'),stops=[
  (1874.7,'morbegno','Living at Valle, Morbegno, with Tomaso',False),(1909,'morbegno','Still in Morbegno in January 1909',False)],last=1909),
('Ernest Huber',2):dict(conf='doc',src=R,b=(ym(1875,1,12),'germany',True,'Born in Germany; place not yet found'),stops=[
  (1890,'nyc','Comes to America about 1890 (1880 in one census)',True),(ym(1903,2,18),'portland','Marries Mary (Mamie) Lasher at Portland',False),
  (1910,'portland','Machinist; Main St, Portland',False),(1940,'middletown','224 Pearl St, Middletown',False)],
  d=(ym(1957,9,22),'middletown',False,'Dies in Middletown; buried St Mary’s, Portland')),
('Mary Huber',2):dict(name='Mary (Mamie) Lasher',line='Lasher',conf='doc',src=R,b=(ym(1886,8),'newbrunswick',True,'Born in New Jersey'),stops=[
  (1900,'portland','With her parents at Portland',False),(ym(1903,2,18),'portland','Marries Ernest Huber',False),(1935,'middletown','Middletown',False)],
  d=(ym(1946,12,19),'hartford',True,'Probably dies at Hartford, 19 Dec 1946')),
('Chester Lasher',3):dict(conf='doc',src=R,b=(ym(1846,12,14),'germantown',True,'Born in New York, probably at Germantown'),stops=[
  (1850,'germantown','With his parents at Germantown',False),(1860,'nyc','New York City, Ward 9',False),
  (ym(1873,3,4),'nyc','Marries Mary Weber in Manhattan',False),(1886,'newbrunswick','New Jersey; children born there 1886–97',False),
  (1900,'portland','Portland, Connecticut',False)],d=(ym(1917,9,23),'portland',False,'Dies at Portland')),
('Mary (Lasher) Anderson',3):dict(name='Mary Weber',line='Weber',conf='doc',src=R,note='The tree’s “Anderson” has no record behind it.',
  b=(ym(1855,2,22),'nyc',False,'Born in New York, of German parents'),stops=[
  (ym(1873,3,4),'nyc','Marries Chester Lasher in Manhattan',False),(1886,'newbrunswick','New Jersey',False),(1900,'portland','Portland',False)],
  d=(ym(1917,1,23),'portland',False,'Dies at Portland')),
('John Webber',4):dict(name='John Weber',line='Weber',conf='prob',src=R,note='Candidate only: a John Weber, gardener, born in Bavaria.',
  b=(1830,'bavaria',True,'Born about 1830 in Bavaria'),stops=[(1855,'nyc','Gardener in Manhattan’s 22nd Ward (1860, 1870)',True)],d=(ym(1889,3,15),'nyc',True,'Dies, 1889 (tree)')),
('Andrew Lasher',4):dict(conf='doc',src=R,b=(ym(1820,2,6),'germantown',False,'Baptised, son of Gerhard Lasher and Christina Sagendorf'),stops=[
  (1850,'germantown','At Germantown with Eliza and their children',False),(1860,'nyc','Barge captain, New York City',False),
  (1880,'brooklyn','74 Oak St, Greenpoint, Brooklyn',False)],
  d=(ym(1891,8,7),'brooklyn',False,'Dies at 98 Franklin St, Brooklyn; buried at Germantown')),
('Eliza Catherine Staats',4):dict(conf='doc',src=R,b=(ym(1821,6,25),'germantown',True,'Born, probably at Germantown'),stops=[
  (1850,'germantown','Germantown',False),(1860,'nyc','New York City',False),(1880,'brooklyn','Greenpoint, Brooklyn',False),
  (1892,'portland','Near her children in Portland, Connecticut',True)],
  d=(ym(1899,8,10),'portland',False,'Dies at Portland; buried at Germantown')),
('Garret B. Lasher',6):dict(note='The Lasher Genealogy makes him a son of Gerrit Lasher (b. 1732), not of Sebastian and Maria Margaret Schumacher as the tree has it.'),
('Sebastian Lasher',7):dict(conf='claimed',note='Doubtful parent: the Lasher Genealogy makes Garret B. Lasher a son of Sebastian’s brother Gerrit.'),
('Maria Margaret Schumacher',7):dict(conf='claimed',note='Doubtful link: see Garret B. Lasher.'),
('Peter Schumacher',8):dict(conf='claimed'),('Christina Hoddenbrug',8):dict(conf='claimed'),
('Johannis Schumacher',9):dict(conf='claimed'),('Anna Barbara Wagner',9):dict(conf='claimed'),
('Elizabeth "Betsey" Rockefeller',6):dict(d=None,last=1865,note='Remarried John Staats in 1814; her death date in the tree was copied from her daughter.'),
('Johann Philip Rockefeller',7):dict(conf='doc',src=R,note='Adjutant of the 10th Regiment, Albany County Militia (Manor of Livingston).'),
('Johann Thiel Rockafellar',8):dict(name='Johann Diel (Thiel) Rockenfeller',conf='doc',src=R,
  b=(ym(1695,9,1),'ehlscheid',False,'Born at Ehlscheid; baptised at Rengsdorf'),stops=[
  (1723,'bonefeld','Marries Anna Gertraud Alsdorf; their first children born at Bonefeld',True),
  (1733.4,'rotterdam','Emigrates in 1733 with five children',True),(1733.7,'nyc','Arrives in New York',True),(1734,'germantown','Settles at Germantown',False)],
  d=(ym(1769,9,9),'germantown',False,'Dies at Germantown; his will leaves his house to his son Philip')),
('Anna Gertrude Alsdorf',8):dict(name='Anna Gertraud Alsdorf',conf='doc',src=R,b=(ym(1705,4,5),'bonefeld',False,'Baptised at Rengsdorf; of Bonefeld'),stops=[
  (1723,'bonefeld','Marries Johann Diel Rockenfeller',True),(1733.4,'rotterdam','Emigrates with her husband and five children',True),
  (1733.7,'nyc','Arrives in New York',True),(1734,'germantown','Germantown',False)],d=(1769.5,'germantown',True,'Dies, 1769 (tree)')),
('Thoengess Anthonius Rockenfeller',9):dict(name='Anton (Tönges) Rockenfeller',conf='doc',src=R,line='Rockefeller',
  b=(1658,'ehlscheid',True,'Born about 1658, son of Andreas Rockenfeller of Ehlscheid'),stops=[(ym(1685,1,11),'rengsdorf','Marries Anna Gertrud at Rengsdorf',False)],
  d=(ym(1707,7,15),'ehlscheid',False,'Dies at Ehlscheid')),
('Gertrud Von Kockenfelt',9):dict(name='Anna Gertrud of Rockenfeld',line='Rockenfeld',conf='doc',src=R,note='Daughter of Paulus von Rockenfeld; the tree’s “von Kockenfelt” and “Pauli” are misreadings.',
  b=(1666,'rockenfeld',True,'Born about 1666, daughter of Paulus of Rockenfeld'),stops=[(ym(1685,1,11),'rengsdorf','Marries Anton Rockenfeller at Rengsdorf',False),(1690,'ehlscheid','Ehlscheid',True)],
  d=(ym(1740,3,20),'rengsdorf',False,'Dies at Rengsdorf, aged 74; she had remarried in 1713')),
('Henrich Alsdorff',9):dict(name='Heinrich Alsdorf'),
('Lotzia Britzen',9):dict(name='Lucia Britz',line='Britz',conf='tree',b=(1670,'bonefeld',True,'Of Bonefeld')),
('Christ Britzen (Britz)',10):dict(name='Christ Britz',line='Britz'),
}
REMOVE={'Johann Wilhelm Rockenfeller SR.','Lucia Johann Rockefeller','Goddard de Rockenfeller','Magdalena de Rockenfeller (Goddard)',
 'Augier Rockefeller (de Roquefeuil)','Magdalena Goddard','Magdalena de Goddard','Rudolphe de Roquefeuil II','Rudolphe de Roquefeuil Rockefeller I',
 'Maria Haller von Hallerstein','Wolf Haller von Hallerstein','Barbara Reiter Von Kornburg','Eustachius Rieter von Kornburg','Levin Haller Von Hallerstein',
 'Petri Huberto von Pauli','Izabella von Kockenfeldt married as Pauli NFI','Augier de Roquefeuil \\ Rockefeller'}
# New people: (child key, which parent) -> record
ADD=[
 (('Lydia L. Hanford',3),'mother',dict(id='GA-1',name='Mary Andrews (later Fish)',sex='F',line='Andrews',conf='prob',src=R,
   b=(1821,'queensbury',True,'Born about 1821'),stops=[(1850,'queensbury','With Judson Andrews and Lydia at Queensbury',False),
   (1860,'chester','Wife of Hanford Fish at Chester',False),(1900,'sglensfalls','At Moreau with her husband Hanford Fish and grandson Thomas',False)],
   d=(ym(1902,12,19),'sglensfalls',False,'Dies at South Glens Falls; buried with Lydia in Bay Street Cemetery'),note='Lydia’s probable mother.')),
 (('Lydia L. Hanford',3),'father',dict(id='GA-2',name='Judson Andrews',sex='M',line='Andrews',conf='prob',src=R,
   b=(1811,'queensbury',True,'Born about 1811'),stops=[(1850,'queensbury','At Queensbury with Mary and Lydia',False)],last=1850,note='Lydia’s probable father.')),
 (('Tommasso Romegialli',3),'father',dict(id='GA-3',name='Antonio Romegialli',sex='M',line='Romegialli',conf='approx',src=R,
   b=(1795,'morbegno',True,'Farmer of Morbegno; named in his son’s death act'),last=1823)),
 (('Tommasso Romegialli',3),'mother',dict(id='GA-4',name='Rosa Ronconi',sex='F',line='Ronconi',conf='approx',src=R,
   b=(1798,'morbegno',True,'Named in her son’s death act'),last=1823)),
 (('Assunta Ronconi',3),'father',dict(id='GA-5',name='Giacomo Ronconi',sex='M',line='Ronconi',conf='approx',src=R,
   b=(1815,'morbegno',True,'Named in his grandson’s birth act; dead by 1874'),last=1845)),
 (('Claudina Ferraris Romegialli',2),'father',dict(id='GA-6',name='Giovanni Ferraris',sex='M',line='Ferraris',conf='prob',src=R,
   b=(1850,'tonco',True,'Of Tonco; probably Claudina’s father'),stops=[(1896.6,'tonco','Son Felice born at Tonco',False)],last=1900,note='Probable parent (medium confidence). Dead by 1922.')),
 (('Claudina Ferraris Romegialli',2),'mother',dict(id='GA-7',name='Rosa Bevilacqua',sex='F',line='Bevilacqua',conf='prob',src=R,
   b=(1855,'tonco',True,'Of Tonco; probably Claudina’s mother'),stops=[(1922,'tonco','Living at Tonco, a widow',False)],last=1922,note='Probable parent (medium confidence).')),
 (('Thoengess Anthonius Rockenfeller',9),'father',dict(id='GA-8',name='Andreas Rockenfeller',sex='M',line='Rockefeller',conf='doc',src=R,
   b=(1630,'rockenfeld',True,'Probably a son of Johannes Wagner of Rockenfeld'),stops=[(1655,'ehlscheid','Of Ehlscheid; marries Elisabeth Kleinmann about 1655',True)],d=(1670,'ehlscheid',True,'Dies about 1670'))),
 (('Thoengess Anthonius Rockenfeller',9),'mother',dict(id='GA-9',name='Elisabeth Kleinmann',sex='F',line='Kleinmann',conf='doc',src=R,
   b=(1633,'ehlscheid',True,'Born about 1633'),stops=[(1655,'ehlscheid','Marries Andreas Rockenfeller',True)],last=1670)),
 (('Gertrud Von Kockenfelt',9),'father',dict(id='GA-10',name='Paulus of Rockenfeld',sex='M',line='Rockenfeld',conf='doc',src=R,
   b=(1635,'rockenfeld',True,'Of Rockenfeld'),last=1666)),
]
# Parents removed from the tree (disproved or misread) -- children whose GEDCOM parents vanish
