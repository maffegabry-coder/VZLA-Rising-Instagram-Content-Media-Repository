import asyncio
from pathlib import Path
from eco2 import *

OUT = Path('/home/claude/build/out7')
DV = 'background:linear-gradient(180deg,rgba(12,9,6,.40) 0%,rgba(12,9,6,0) 13%,rgba(12,9,6,.05) 30%,rgba(12,9,6,.52) 44%,rgba(12,9,6,.66) 70%,rgba(12,9,6,.82) 100%)'

# ---------------- P13 Henri Pittier (Mon 30 Nov) ----------------
L1, T1 = 'Venezuela Uncovered', 5
def profile():
    # simple altitude profile, sea level to ~2,400 m, Portachuelo pass at 1,136 m
    return f'''<svg width="936" height="440" viewBox="0 0 936 440">
  <line x1="0" y1="400" x2="936" y2="400" stroke="{EARTH}" stroke-width="1.5" opacity=".5"/>
  <path d="M0 400 C120 395 180 300 260 230 C320 180 360 210 420 262 C460 296 500 290 540 250 C610 170 660 60 720 40 C790 20 850 120 936 200 L936 400 Z" fill="#DCCBB3" stroke="{EARTH}" stroke-width="2"/>
  <circle cx="440" cy="276" r="9" fill="{INK}"/><circle cx="440" cy="276" r="17" fill="none" stroke="{EARTH}" stroke-width="1.5"/>
  <text x="440" y="340" text-anchor="middle" font-family="Jost" font-weight="500" font-size="24" letter-spacing="3" fill="{INK}">PORTACHUELO 1,136 M</text>
  <text x="720" y="22" text-anchor="middle" font-family="Jost" font-weight="500" font-size="24" letter-spacing="3" fill="{INK}">OVER 2,300 M</text>
  <text x="10" y="380" font-family="Jost" font-weight="500" font-size="24" letter-spacing="3" fill="{INK}">SEA LEVEL</text>
</svg>'''

p13 = [
 ('slide01', slide('photo', L1, 1, T1, '''<div class=txt>
  <div class=kick>Henri Pittier National Park</div>
  <div class=num style="font-size:320px">1937</div>
  <div class=h style="font-size:92px;margin-top:24px">Venezuela's <em>oldest</em> national park</div>
  <div class=p>Cloud forest above, Caribbean bays below.</div></div>''',
  'Sources: Britannica; Wikipedia. Choron&iacute;. Photo: Maria Isabella Bernotti / Pexels', 'pexels-35434553-choroni.jpg', '50% 50%', veil=DV)),
 ('slide02', slide('cream', L1, 2, T1, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>From the beach to the peaks</div>
   <div class=num style="font-size:220px;color:{INK}">500<small>+</small></div>
   <div class=h style="font-size:84px;margin:10px 0 50px">bird species, <em>one park</em></div>
   {profile()}
   <div class=p style="font-size:32px;opacity:.8;margin-top:24px">Migrants cross the range at the Portachuelo pass.</div></div>''',
  'Sources: Britannica; Wikipedia. Profile is schematic')),
 ('slide03', slide('photo', L1, 3, T1, '''<div class=txt>
  <div class=kick>La Ci&eacute;naga, Ocumare de la Costa</div>
  <div class=h style="font-size:120px">Flat water, <em>turquoise</em></div>
  <div class=p>A sheltered bay for swimming and diving, reached by boat.</div></div>''',
  'Ocumare de la Costa, Aragua. Photo: El Santos Guerra / Pexels', 'pexels-27442028-ocumare-cienaga.jpg', '50% 50%', veil=DV)),
 ('slide04', slide('photo', L1, 4, T1, '''<div class=txt>
  <div class=kick>Cuyagua</div>
  <div class=h style="font-size:120px">Palms, vans <em>and surf</em></div>
  <div class=p>The park's surf beach, at the end of the coast road.</div></div>''',
  'Cuyagua, Aragua. Photo: Edwin Mijares / Pexels', 'pexels-37628214-cuyagua-van.jpg', '50% 45%', veil=DV)),
 ('slide05', slide('dark', L1, 5, T1, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>One park, three moods</div>
   <div class=h style="font-size:112px;margin-bottom:46px">Pick <em>your coast</em></div>
   <div class=row><div class=n>01</div><div class=t>Choron&iacute;: colonial village, posadas</div></div>
   <div class=row><div class=n>02</div><div class=t>La Ci&eacute;naga: calm water by boat</div></div>
   <div class=row><div class=n>03</div><div class=t>Cuyagua: waves and wild beach</div></div>
   <div class=h style="font-size:66px;margin-top:44px;color:{GOLD}"><em>Village, bay or surf?</em></div></div>''',
  'Sources: Britannica; Wikipedia')),
]

# ---------------- P14 Colombia-Venezuela trade (Wed 2 Dec) ----------------
L2, T2 = 'Venezuela in Motion', 5
def tradebars():
    data = [('2008', 7000, '7,000+'), ('2020', 222, '222'), ('2024', 1124, '1,124'), ('2025', 1170, '1,170'), ('2026*', 1017, '1,017')]
    px = 620 / 7000
    out = ''
    for y, v, lab in data:
        w = max(v * px, 4)
        col = EARTH if y.startswith('2026') else '#B9AA94'
        out += f'''<div style="display:flex;align-items:center;margin-bottom:26px">
          <div class=lab style="width:130px;flex:none;color:{INK}">{y}</div>
          <div style="height:62px;width:{w}px;background:{col}"></div>
          <div style="font:300 54px Cormorant;color:{INK};margin-left:20px">{lab}</div></div>'''
    return out

p14 = [
 ('slide01', slide('photo', L2, 1, T2, '''<div class=txt>
  <div class=kick>Colombia &amp; Venezuela</div>
  <div class=num style="font-size:300px">$1.0<small>bn</small></div>
  <div class=h style="font-size:88px;margin-top:24px">in trade, January to <em>September 2026</em></div>
  <div class=p>Up 17.9% on the same months of 2025.</div></div>''',
  'Source: C&aacute;mara Colombo Venezolana via Vanguardia, 21 Nov 2026. M&eacute;rida. Photo: Arturo A / Pexels', 'pexels-16654093-merida-bluesky.jpg', '50% 50%', veil=DV)),
 ('slide02', slide('cream', L2, 2, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:165px">
   <div class=kick>Bilateral trade, US$ million</div>
   <div class=h style="font-size:96px;margin-bottom:50px">Growing, <em>far from 2008</em></div>
   {tradebars()}
   <div class=p style="font-size:30px;margin-top:20px;opacity:.75">Bars to scale. *2026: January to September only.</div></div>''',
  'Source: C&aacute;mara Colombo Venezolana via Vanguardia and Radio Am&eacute;rica, 21 Nov 2026')),
 ('slide03', slide('photo', L2, 3, T2, '''<div class=txt>
  <div class=kick>One direction</div>
  <div class=num style="font-size:300px">92%</div>
  <div class=h style="font-size:88px;margin-top:24px">of the flow is Colombia <em>selling to Venezuela</em></div>
  <div class=p>Exports $939m, up 20.4%. Imports $79m, down 5%.</div></div>''',
  'Source: C&aacute;mara Colombo Venezolana, Jan to Sept 2026. M&eacute;rida. Photo: Arturo A / Pexels', 'pexels-18206815-merida-town.jpg', '15% 50%', veil=DV)),
 ('slide04', slide('photo', L2, 4, T2, '''<div class=txt>
  <div class=kick>Latest month</div>
  <div class=num style="font-size:300px">+33.6%</div>
  <div class=h style="font-size:88px;margin-top:24px">trade in September, <em>year on year</em></div>
  <div class=p>About $145 million in a single month.</div></div>''',
  'Source: C&aacute;mara Colombo Venezolana, Nov 2026. Caracas. Photo: Andy Art and design / Pexels', 'pexels-29518260-caracas-sunset.jpg', '50% 50%', veil=DV)),
 ('slide05', slide('dark', L2, 5, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Our take</div>
   <div class=h style="font-size:112px;margin-bottom:46px">A neighbour <em>reopening</em></div>
   <div class=row><div class=n>01</div><div class=t>Shelves and supply chains first</div></div>
   <div class=row><div class=n>02</div><div class=t>Venezuelan exports still small</div></div>
   <div class=row><div class=n>03</div><div class=t>Under a fifth of the 2008 peak</div></div>
   <div class=h style="font-size:62px;margin-top:44px;color:{GOLD}"><em>What should Venezuela sell back?</em></div></div>''',
  'Not investment advice')),
]

# ---------------- P15 Caracas housing prices (Fri 4 Dec) ----------------
L3, T3 = 'Investment Perspectives', 5
def m2bars():
    px = 620 / 2945
    out = ''
    for name, v, lab, hi in [('Chacao', 2945, '$2,945', False), ('Caracas avg', 1561, '$1,561', True), ('Libertador', 1075, '$1,075', False)]:
        out += f'''<div style="margin-bottom:40px"><div class=lab style="margin-bottom:14px;color:{INK}">{name}</div>
          <div style="display:flex;align-items:center"><div style="height:80px;width:{v*px}px;background:{EARTH if hi else '#B9AA94'}"></div>
          <div style="font:300 64px Cormorant;color:{INK};margin-left:22px">{lab}</div></div></div>'''
    return out

p15 = [
 ('slide01', slide('photo', L3, 1, T3, '''<div class=txt>
  <div class=kick>Caracas housing</div>
  <div class=num style="font-size:300px">$1,561</div>
  <div class=h style="font-size:88px;margin-top:24px">asking price per m&sup2;, <em>November</em></div>
  <div class=p>Typical apartment listing, up 1.3% on October.</div></div>''',
  'Source: &Iacute;ndice HabitaOne via Bloomberg L&iacute;nea, 7 Nov 2026. Caracas. Photo: Edwin Mijares / Pexels', 'pexels-40492546-caracas-sunset2.jpg', '50% 40%', veil=DV)),
 ('slide02', slide('cream', L3, 2, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Asking price, US$ per m&sup2;</div>
   <div class=h style="font-size:100px;margin-bottom:64px">Same city, <em>almost 3x</em></div>
   {m2bars()}
   <div class=p style="font-size:30px;opacity:.75;margin-top:10px">Bars to scale. Listings, not closed sales.</div></div>''',
  'Source: &Iacute;ndice HabitaOne via Bloomberg L&iacute;nea, Nov 2026')),
 ('slide03', slide('photo', L3, 3, T3, '''<div class=txt>
  <div class=kick>Entry level</div>
  <div class=num style="font-size:300px">&minus;20%</div>
  <div class=h style="font-size:88px;margin-top:24px">homes listed under <em>$100,000</em></div>
  <div class=p>From 769 in May to 612 in October.</div></div>''',
  'Source: &Iacute;ndice HabitaOne via Bloomberg L&iacute;nea. Caracas. Photo: Jorge Kardousli Khabbaze / Pexels', 'pexels-20733321-caracas-green.jpg', '50% 55%', veil=DV)),
 ('slide04', slide('photo', L3, 4, T3, '''<div class=txt>
  <div class=kick>Rents</div>
  <div class=num style="font-size:270px">+14&ndash;23%</div>
  <div class=h style="font-size:88px;margin-top:24px">rent per m&sup2;, <em>June to October</em></div>
  <div class=p>Depending on the municipality.</div></div>''',
  'Source: &Iacute;ndice HabitaOne via Bloomberg L&iacute;nea. El &Aacute;vila. Photo: Juan Carlos Fern&aacute;ndez Alem&aacute;n / Pexels', 'pexels-39879583-avila.jpg', '50% 45%', veil=DV)),
 ('slide05', slide('dark', L3, 5, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Before you buy</div>
   <div class=h style="font-size:112px;margin-bottom:46px">Read the <em>fine print</em></div>
   <div class=row><div class=n>01</div><div class=t>Asking prices are not sale prices</div></div>
   <div class=row><div class=n>02</div><div class=t>Check the building's structural report</div></div>
   <div class=row><div class=n>03</div><div class=t>Title, condo fees, power and water</div></div>
   <div class=h style="font-size:62px;margin-top:44px;color:{GOLD}"><em>Chacao or Libertador?</em></div></div>''',
  'Not legal or financial advice')),
]

POSTS = {'p13': p13, 'p14': p14, 'p15': p15}
async def main():
    for k, v in POSTS.items():
        await render(v, OUT / k)
        sheet(OUT / k, [n for n, _ in v], OUT / f'{k}_sheet.jpg')
asyncio.run(main())
