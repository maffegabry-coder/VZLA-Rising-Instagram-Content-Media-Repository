import asyncio
from pathlib import Path
from eco2 import *

OUT = Path('/home/claude/build/out4')
DV = 'background:linear-gradient(180deg,rgba(12,9,6,.40) 0%,rgba(12,9,6,0) 13%,rgba(12,9,6,.05) 30%,rgba(12,9,6,.52) 44%,rgba(12,9,6,.66) 70%,rgba(12,9,6,.82) 100%)'

# ---------------- POST 01 ----------------
L1, T1 = 'Venezuela Uncovered', 6
p1 = [
 ('slide01', slide('photo', L1, 1, T1, '''<div class=txt>
  <div class=kick>Six landscapes, one country</div>
  <div class=h style="font-size:146px">More than <em>the headlines</em></div>
  <div class=p>Beaches, tepuis, Andes and coral islands.</div></div>''',
  'Choroní, Aragua. Photo: Maria Isabella Bernotti / Pexels', 'pexels-35434553-choroni.jpg', '50% 50%')),
 ('slide02', slide('photo', L1, 2, T1, '''<div class=txt>
  <div class=kick>Angel Falls, Canaima</div>
  <div class=num style="font-size:340px">979<small>m</small></div>
  <div class=h style="font-size:88px;margin-top:30px">One of the <em>tallest</em> waterfalls on Earth</div>
  <div class=p>Canaima is a UNESCO World Heritage Site since 1994.</div></div>''',
  'Sources: UNESCO; Robertson survey, 1949. Photo: Ederik Palencia Ferreira / Pexels', 'pexels-7360544-canaima.jpg', '50% 50%')),
 ('slide03', slide('photo', L1, 3, T1, '''<div class=txt>
  <div class=kick>Los Roques</div>
  <div class=num style="font-size:300px">340+</div>
  <div class=h style="font-size:88px;margin-top:30px">islands, cays and shoals in <em>one park</em></div>
  <div class=p>Protected since 1972. 221,120 hectares, mostly sea.</div></div>''',
  'Source: Ramsar Sites Information Service. Photo: Fuka jaz / Pexels', 'pexels-18558367-losroques-aerial.jpg', '50% 25%')),
 ('slide04', slide('photo', L1, 4, T1, '''<div class=txt>
  <div class=kick>The Andes, Mérida</div>
  <div class=num style="font-size:300px">4,978<small>m</small></div>
  <div class=h style="font-size:88px;margin-top:30px">Pico Bolívar, <em>the top</em> of Venezuela</div></div>''',
  'Source: Pérez et al., Interciencia 2005. Photo: Arturo A / Pexels', 'pexels-16654093-merida-bluesky.jpg', '50% 40%')),
 ('slide05', slide('photo', L1, 5, T1, '''<div class=txt>
  <div class=kick>The Caribbean coast</div>
  <div class=num style="font-size:300px">2,800<small>km</small></div>
  <div class=h style="font-size:88px;margin-top:30px">of coastline, <em>mostly Caribbean</em></div></div>''',
  'Source: CIA World Factbook. Photo: Daniel Patiño / Pexels', 'pexels-1434406-falcon-beach.jpg', '50% 50%')),
 ('slide06', slide('cream', L1, 6, T1, f'''
  <div style="position:absolute;left:72px;right:72px;top:160px">
   <div class=kick>One of 17 megadiverse countries</div>
   <div class=h style="font-size:96px">Where would you<br><em>go first?</em></div></div>
  <div style="position:absolute;left:72px;top:430px">{venmap([('roques','Los Roques','start'),('margarita','Margarita','start'),('bolivar','Andes','end'),('llanos','Llanos','end'),('angel','Canaima','end'),('roraima','Roraima','start')])}</div>
  <div style="position:absolute;left:72px;right:72px;top:1065px;font:400 34px/1.35 Jost">Tell us in the comments. Save it for your next trip.</div>''',
  'Source: Conservation International')),
]

# ---------------- POST 02 ----------------
L2, T2 = 'Venezuela in Motion', 5
p2 = [
 ('slide01', slide('photo', L2, 1, T2, '''<div class=txt>
  <div class=kick>Business</div>
  <div class=h style="font-size:136px">Capital is <em>coming</em> to Caracas</div>
  <div class=p>Funds, fintech and flights. What is real, and what to check.</div></div>''',
  'Caracas. Photo: Andy Art and design / Pexels', 'pexels-29518260-caracas-sunset.jpg', '50% 55%')),
 ('slide02', slide('photo', L2, 2, T2, '''<div class=txt>
  <div class=kick>Startup Venezuela Summit</div>
  <div class=num style="font-size:340px">25</div>
  <div class=h style="font-size:88px;margin-top:24px">investment funds in <em>Caracas</em></div>
  <div class=p>October 21-23, opened by Richard Branson. ~40 international guests, up from 10 in 2023.</div></div>''',
  'Source: Bloomberg Línea, Oct 2026 (organiser figures). Photo: Juan Carlos Fernández Alemán / Pexels', 'pexels-39879583-avila.jpg', '50% 30%')),
 ('slide03', slide('cream', L2, 3, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Fintech</div>
   <div class=h style="font-size:100px">Cashea raised</div>
   <div class=num style="font-size:300px;margin-top:20px">$100<small>M</small></div>
   <div class=lab style="margin-top:30px">In 2026, in two rounds</div>
   <div style="display:flex;height:70px;margin-top:40px"><div style="width:40%;background:{EARTH}"></div><div style="width:60%;background:{INK}"></div></div>
   <div style="display:flex;margin-top:18px;font:500 32px Jost"><div style="width:40%">Series A - $40M</div><div style="width:60%">Series B - $60M</div></div>
   <div class=p style="margin-top:56px"><b>10M+</b> accounts. <b>40,000</b> partner stores.</div></div>''',
  'Source: Intelligent CIO, Aug 2026 (company figures)')),
 ('slide04', slide('photo', L2, 4, T2, '''<div class=txt style="bottom:220px">
  <div class=kick>Air links</div>
  <div class=h style="font-size:100px;margin-bottom:30px">Flights <em>are back</em></div>
  <div class=row><div style="flex:1"><div class=tag>Flying</div><div class=t>Qatar Airways - Doha</div></div></div>
  <div class=row><div style="flex:1"><div class=tag>Flying</div><div class=t>Avianca - Bogotá</div></div></div>
  <div class=row><div style="flex:1"><div class=tag>From Nov 26</div><div class=t>Copa - Panama to Margarita</div></div></div>
  <div class=row><div style="flex:1"><div class=tag>Not confirmed</div><div class=t>United and JetBlue - USA</div></div></div></div>''',
  'Source: Bloomberg Línea, Oct 7 2026. Photo: Maria Isabella Bernotti / Pexels', 'pexels-2570473-gran-roque-beach.jpg', '40% 100%;background-size:auto 125%', veil=DV)),
 ('slide05', slide('dark', L2, 5, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Our take</div>
   <div class=h style="font-size:112px;margin-bottom:46px">The momentum is real. <em>So is the homework.</em></div>
   <div class=row><div class=n>01</div><div class=t>Most figures come from companies</div></div>
   <div class=row><div class=n>02</div><div class=t>Announced is not operating</div></div>
   <div class=row><div class=n>03</div><div class=t>Compliance comes first</div></div>
   <div class=h style="font-size:62px;margin-top:44px;color:{GOLD}"><em>What would you need to see to invest?</em></div></div>''',
  'Not investment advice')),
]

# ---------------- POST 03 ----------------
L3, T3 = 'Investment Perspectives', 6
p3 = [
 ('slide01', slide('photo', L3, 1, T3, '''<div class=txt>
  <div class=kick>Destinations</div>
  <div class=h style="font-size:146px">Isla Margarita, <em>underrated?</em></div>
  <div class=p>Venezuela's classic island, with a new link to Panama.</div></div>''',
  'Nueva Esparta. Photo: Diego Ruso Pérez / Pexels', 'pexels-29154539-nueva-esparta-aerial.jpg', '50% 50%')),
 ('slide02', slide('photo', L3, 2, T3, '''<div class=txt>
  <div class=kick>Pampatar, Margarita</div>
  <div class=num style="font-size:320px">70+</div>
  <div class=h style="font-size:88px;margin-top:24px">beaches on <em>78 km</em> of island</div>
  <div class=p>1,020 km², a former free port, decades of tourism.</div></div>''',
  'Source: Margarita Island geography. Photo: Vika Glitter / Pexels', 'pexels-26241556-pampatar.jpg', '30% 50%')),
 ('slide03', slide('cream', L3, 3, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Nueva Esparta State</div>
   <div class=h style="font-size:96px">Two peninsulas,<br><em>one island</em></div></div>
  <div style="position:absolute;left:72px;top:450px">{margmap([('asuncion','La Asunción','end',-4,'cap'),('porlamar','Porlamar','end',12,'dot'),('pampatar','Pampatar','start',-30,'dot'),('juangriego','Juan Griego','end',-8,'dot'),('airport','Airport','end',26,'dot'),('macanao','Macanao','',0,'area'),('restinga','La Restinga','',12,'area')])}</div>
  <div style="position:absolute;left:72px;right:72px;top:1065px;font:400 34px/1.35 Jost">Wild west, busy east.</div>''',
  'Source: Margarita Island geography')),
 ('slide04', slide('photo', L3, 4, T3, '''<div class=txt>
  <div class=kick>Connectivity</div>
  <div class=num style="font-size:320px">3<small>flights a week</small></div>
  <div class=h style="font-size:88px;margin-top:24px">Panama - Margarita, <em>from Nov 26</em></div>
  <div class=p>Copa links the island to its regional hub. Announced route.</div></div>''',
  'Sources: El Diario; Bloomberg Línea, 2026. Photo: RITRATTO VISUAL / Pexels', 'pexels-32699745-margarita-lighthouse.jpg', '50% 15%')),
 ('slide05', slide('photo', L3, 5, T3, '''<div class=txt style="bottom:220px">
  <div class=kick>Hypotheses, not forecasts</div>
  <div class=h style="font-size:100px;margin-bottom:30px">Where the <em>opportunity</em> could be</div>
  <div class=row><div class=n>01</div><div class=t>Upgrade hotels before building new</div></div>
  <div class=row><div class=n>02</div><div class=t>Low-density boutique stays</div></div>
  <div class=row><div class=n>03</div><div class=t>Margarita + Los Roques trips</div></div></div>''',
  'VZLA Rising analysis. Photo: RITRATTO VISUAL / Pexels', 'pexels-32690921-nueva-esparta.jpg', '55% 50%', veil=DV)),
 ('slide06', slide('dark', L3, 6, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Before you invest</div>
   <div class=h style="font-size:112px;margin-bottom:40px">Check <em>these six</em></div>
   <div class=row style="padding:22px 0"><div class=n>01</div><div class=t>Land title</div></div>
   <div class=row style="padding:22px 0"><div class=n>02</div><div class=t>Sanctions compliance</div></div>
   <div class=row style="padding:22px 0"><div class=n>03</div><div class=t>Water and power</div></div>
   <div class=row style="padding:22px 0"><div class=n>04</div><div class=t>Zoning and permits</div></div>
   <div class=row style="padding:22px 0"><div class=n>05</div><div class=t>Currency and payments</div></div>
   <div class=row style="padding:22px 0"><div class=n>06</div><div class=t>Real demand data</div></div>
   <div class=h style="font-size:60px;margin-top:34px;color:{GOLD}"><em>What would make Margarita investable?</em></div></div>''',
  'Not legal or financial advice')),
]

POSTS = {'post01': p1, 'post02': p2, 'post03': p3}
async def main():
    for k, v in POSTS.items():
        await render(v, OUT / k)
        sheet(OUT / k, [n for n, _ in v], OUT / f'{k}_sheet.jpg')
asyncio.run(main())
