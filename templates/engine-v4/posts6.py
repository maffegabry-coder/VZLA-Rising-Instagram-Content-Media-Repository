import asyncio
from pathlib import Path
from eco2 import *

OUT = Path('/home/claude/build/out6')
DV = 'background:linear-gradient(180deg,rgba(12,9,6,.40) 0%,rgba(12,9,6,0) 13%,rgba(12,9,6,.05) 30%,rgba(12,9,6,.52) 44%,rgba(12,9,6,.66) 70%,rgba(12,9,6,.82) 100%)'

# ---------------- P10 Margarita beyond the beach (Mon 23 Nov) ----------------
L1, T1 = 'Venezuela Uncovered', 5
p10 = [
 ('slide01', slide('photo', L1, 1, T1, '''<div class=txt>
  <div class=kick>Isla Margarita</div>
  <div class=h style="font-size:146px">Beyond <em>the beach</em></div>
  <div class=p>Forts, mangroves and steady Caribbean wind.</div></div>''',
  'Margarita. Photo: RITRATTO VISUAL / Pexels', 'pexels-32699745-margarita-lighthouse.jpg', '50% 35%', veil=DV)),
 ('slide02', slide('photo', L1, 2, T1, '''<div class=txt>
  <div class=kick>Pampatar</div>
  <div class=num style="font-size:320px">1684</div>
  <div class=h style="font-size:88px;margin-top:24px">San Carlos Borromeo fort, <em>completed</em></div>
  <div class=p>Rebuilt after pirates burned the town. Now a museum.</div></div>''',
  'Source: Wikipedia. Pampatar. Photo: Vika Glitter / Pexels', 'pexels-26241556-pampatar.jpg', '50% 50%')),
 ('slide03', slide('photo', L1, 3, T1, '''<div class=txt>
  <div class=kick>La Restinga National Park</div>
  <div class=num style="font-size:320px">18<small>km</small></div>
  <div class=h style="font-size:88px;margin-top:24px">of channels through <em>the mangroves</em></div>
  <div class=p>A national park since 1974. Scarlet ibis and flamingos.</div></div>''',
  'Source: Wikipedia. Nueva Esparta. Photo: Diego Ruso P&eacute;rez / Pexels', 'pexels-29154539-nueva-esparta-aerial.jpg', '50% 72%', veil=DV)),
 ('slide04', slide('photo', L1, 4, T1, '''<div class=txt>
  <div class=kick>El Yaque</div>
  <div class=num style="font-size:270px">15&ndash;30<small>knots</small></div>
  <div class=h style="font-size:88px;margin-top:24px">of trade wind, <em>most of the year</em></div>
  <div class=p>Shallow water for hundreds of metres.</div></div>''',
  'Source: Wikipedia. Nueva Esparta coast. Photo: RITRATTO VISUAL / Pexels', 'pexels-32690921-nueva-esparta.jpg', '40% 50%')),
 ('slide05', slide('dark', L1, 5, T1, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>One island, one day</div>
   <div class=h style="font-size:112px;margin-bottom:46px">Plan it <em>east to west</em></div>
   <div class=row><div class=n>01</div><div class=t>Morning: the Pampatar fort</div></div>
   <div class=row><div class=n>02</div><div class=t>Midday: a boat through La Restinga</div></div>
   <div class=row><div class=n>03</div><div class=t>Afternoon: the wind at El Yaque</div></div>
   <div class=p style="font-size:34px;opacity:.85">From 26 Nov: Copa flies Panama to Porlamar, 3 times a week.</div>
   <div class=h style="font-size:66px;margin-top:40px;color:{GOLD}"><em>Fort, lagoon or wind?</em></div></div>''',
  'Sources: Wikipedia; Copa via Aviaci&oacute;n al D&iacute;a, Aug 2026')),
]

# ---------------- P11 Air links (Wed 25 Nov) ----------------
L2, T2 = 'Venezuela in Motion', 5
ROUTES = [('4 Nov', 'Qatar Airways', 'Doha, Bogot&aacute;, Caracas', '2 weekly'),
          ('20 Nov', 'Avior', 'Barcelona, Miami', '3 weekly'),
          ('26 Nov', 'Copa', 'Panama, Porlamar', '3 weekly'),
          ('15 Jan', 'American', 'Miami, Barcelona', '3 weekly')]
def routes():
    out = ''
    for d, a, r, f in ROUTES:
        out += f'''<div class=row style="padding:24px 0;align-items:center">
          <div style="font:300 60px Cormorant;color:{EARTH};width:210px;flex:none">{d}</div>
          <div style="flex:1"><div class=t>{a}</div><div class=d>{r}</div></div>
          <div class=lab style="color:{EARTH};flex:none">{f}</div></div>'''
    return out

p11 = [
 ('slide01', slide('photo', L2, 1, T2, '''<div class=txt>
  <div class=kick>Air links, Nov 2026</div>
  <div class=num style="font-size:330px">178</div>
  <div class=h style="font-size:88px;margin-top:24px">weekly international flights at <em>Maiquet&iacute;a</em></div>
  <div class=p>The record before the June quakes: 260.</div></div>''',
  'Source: ALAV via El Diario, 3 Nov 2026. Caracas. Photo: Andy Art and design / Pexels', 'pexels-29518260-caracas-sunset.jpg', '50% 50%', veil=DV)),
 ('slide02', slide('cream', L2, 2, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:160px">
   <div class=kick>New international links</div>
   <div class=h style="font-size:96px;margin-bottom:40px">Four routes, <em>three months</em></div>
   {routes()}
   <div class=p style="font-size:30px;margin-top:30px;opacity:.75">Scheduled start dates, 2026 and 2027.</div></div>''',
  'Sources: Latin Times, 6 Nov 2026; Diario Las Am&eacute;ricas; The Bulkhead Seat')),
 ('slide03', slide('photo', L2, 3, T2, '''<div class=txt>
  <div class=kick>Beyond the capital</div>
  <div class=num style="font-size:330px">44%</div>
  <div class=h style="font-size:88px;margin-top:24px">of international departures, <em>outside Caracas</em></div>
  <div class=p>Valencia leads with 32 weekly flights.</div></div>''',
  'Source: ALAV, Sept 2026, via Latin Times. Carabobo. Photo: Hiurich G. / Pexels', 'pexels-13642997-montalban.jpg', '50% 50%', veil=DV)),
 ('slide04', slide('photo', L2, 4, T2, '''<div class=txt>
  <div class=kick>Copa's sixth airport</div>
  <div class=num style="font-size:330px">26<small>Nov</small></div>
  <div class=h style="font-size:88px;margin-top:24px">first Panama flight to <em>Margarita</em></div>
  <div class=p>Copa's Panama to Venezuela flights: 36 to 46 a week.</div></div>''',
  'Source: Aviaci&oacute;n al D&iacute;a, Aug 2026. Carabobo coast. Photo: Hiurich G. / Pexels', 'pexels-13831431-carabobo-coast.jpg', '40% 50%')),
 ('slide05', slide('dark', L2, 5, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Our take</div>
   <div class=h style="font-size:112px;margin-bottom:46px">Seats come <em>before guests</em></div>
   <div class=row><div class=n>01</div><div class=t>New routes widen the visitor pool</div></div>
   <div class=row><div class=n>02</div><div class=t>Regional airports serve the resorts</div></div>
   <div class=row><div class=n>03</div><div class=t>Watch fares, permits and reliability</div></div>
   <div class=h style="font-size:62px;margin-top:44px;color:{GOLD}"><em>Which route would you book first?</em></div></div>''',
  'Schedules can change. Not travel or investment advice')),
]

# ---------------- P12 Caracas bed gap (Fri 27 Nov) ----------------
L3, T3 = 'Investment Perspectives', 5
def beds():
    px = 10.6  # px per thousand beds
    def bar(name, lo, hi, lab, ve):
        return f'''<div style="margin-bottom:46px"><div class=lab style="margin-bottom:16px;color:{INK}">{name}</div>
        <div style="position:relative;height:84px">
          <div style="position:absolute;left:0;top:0;height:84px;width:{lo*px}px;background:{EARTH if ve else '#B9AA94'}"></div>
          {f'<div style="position:absolute;left:{lo*px}px;top:0;height:84px;width:{(hi-lo)*px}px;background:repeating-linear-gradient(135deg,{EARTH} 0 6px,#DCCBB3 6px 12px)"></div>' if hi > lo else ''}
          <div style="position:absolute;left:{hi*px+22}px;top:12px;font:300 64px Cormorant;color:{INK}">{lab}</div></div></div>'''
    return bar('Caracas', 26, 30, '26&ndash;30k', True) + bar('Bogot&aacute;', 70, 70, '70k', False)

p12 = [
 ('slide01', slide('photo', L3, 1, T3, '''<div class=txt>
  <div class=kick>Hotel supply</div>
  <div class=h style="font-size:146px">Caracas has a <em>bed gap</em></div>
  <div class=p>Business travel is back. Rooms are short, says the hotel federation.</div></div>''',
  'Caracas. Photo: Edwin Mijares / Pexels', 'pexels-40492546-caracas-sunset2.jpg', '50% 40%', veil=DV)),
 ('slide02', slide('cream', L3, 2, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Hotel bed places</div>
   <div class=h style="font-size:104px;margin-bottom:70px">About <em>a third</em> of Bogot&aacute;</div>
   {beds()}
   <div class=p style="font-size:32px;opacity:.75;margin-top:10px">Bars to scale. Striped: range of the estimate.</div></div>''',
  'Source: Fenahoven via 2001online, 21 Oct 2026. Estimates.')),
 ('slide03', slide('photo', L3, 3, T3, '''<div class=txt>
  <div class=kick>Who is looking</div>
  <div class=h style="font-size:118px">Portuguese hotel groups, <em>in Caracas</em></div>
  <div class=p>A business forum on 3 November. More delegations due by early December.</div></div>''',
  'Sources: Finanzas Digital, Fedec&aacute;maras Radio, AVN. Photo: Jorge Kardousli Khabbaze / Pexels', 'pexels-20733321-caracas-green.jpg', '50% 55%')),
 ('slide04', slide('photo', L3, 4, T3, '''<div class=txt>
  <div class=kick>The catch</div>
  <div class=num style="font-size:330px">50%</div>
  <div class=h style="font-size:88px;margin-top:24px">of revenue paid in taxes, <em>at some hotels</em></div>
  <div class=p>Once about 5% of costs, says Fenahoven.</div></div>''',
  'Source: Fenahoven via Fedec&aacute;maras Radio, 5 Nov 2026. El &Aacute;vila. Photo: Juan Carlos Fern&aacute;ndez Alem&aacute;n / Pexels', 'pexels-39879583-avila.jpg', '50% 45%')),
 ('slide05', slide('dark', L3, 5, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Before the first sketch</div>
   <div class=h style="font-size:112px;margin-bottom:40px">Run <em>these five</em></div>
   <div class=row style="padding:24px 0"><div class=n>01</div><div class=t>Demand: who flies in, how often</div></div>
   <div class=row style="padding:24px 0"><div class=n>02</div><div class=t>Tax: model today's burden</div></div>
   <div class=row style="padding:24px 0"><div class=n>03</div><div class=t>Title, zoning and permits</div></div>
   <div class=row style="padding:24px 0"><div class=n>04</div><div class=t>Power and water backup</div></div>
   <div class=row style="padding:24px 0"><div class=n>05</div><div class=t>Sanctions and payments</div></div>
   <div class=h style="font-size:60px;margin-top:34px;color:{GOLD}"><em>Which check would you run first?</em></div></div>''',
  'Not legal or financial advice')),
]

POSTS = {'p10': p10, 'p11': p11, 'p12': p12}
async def main():
    for k, v in POSTS.items():
        await render(v, OUT / k)
        sheet(OUT / k, [n for n, _ in v], OUT / f'{k}_sheet.jpg')
asyncio.run(main())
