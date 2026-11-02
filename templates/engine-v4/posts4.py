import asyncio
from pathlib import Path
from eco2 import *

OUT = Path('/home/claude/build/out5')
DV = 'background:linear-gradient(180deg,rgba(12,9,6,.40) 0%,rgba(12,9,6,0) 13%,rgba(12,9,6,.05) 30%,rgba(12,9,6,.52) 44%,rgba(12,9,6,.66) 70%,rgba(12,9,6,.82) 100%)'

# ---------------- P04 Mérida (Mon 9 Nov) ----------------
L1, T1 = 'Venezuela Uncovered', 6
p4 = [
 ('slide01', slide('photo', L1, 1, T1, '''<div class=txt>
  <div class=kick>Mérida, the Venezuelan Andes</div>
  <div class=h style="font-size:146px">Venezuela has an <em>alpine</em> side</div>
  <div class=p>Cable cars, glacial lakes and mountain lodges.</div></div>''',
  'Mérida. Photo: Arturo A / Pexels', 'pexels-16654093-merida-bluesky.jpg', '60% 50%')),
 ('slide02', slide('photo', L1, 2, T1, '''<div class=txt>
  <div class=kick>Mukumbarí cable car</div>
  <div class=num style="font-size:300px">4,765<small>m</small></div>
  <div class=h style="font-size:88px;margin-top:30px">One of the <em>highest</em> cable cars on Earth</div>
  <div class=p>Back in service since August 19, 2026.</div></div>''',
  'Source: El Diario, Aug 2026. Photo: Arturo A / Pexels', 'pexels-18122957-merida-panorama.jpg', '55% 50%')),
 ('slide03', slide('photo', L1, 3, T1, '''<div class=txt>
  <div class=kick>From city to summit</div>
  <div class=num style="font-size:300px">12.5<small>km</small></div>
  <div class=h style="font-size:88px;margin-top:30px">from Mérida to <em>Pico Espejo</em></div>
  <div class=p>Four sections, starting at 1,577 m.</div></div>''',
  'Source: Mérida cable car, Wikipedia. Photo: Arturo A / Pexels', 'pexels-16799369-merida-river.jpg', '50% 30%')),
 ('slide04', slide('photo', L1, 4, T1, '''<div class=txt>
  <div class=kick>Sierra Nevada National Park</div>
  <div class=num style="font-size:230px">276,446<small>ha</small></div>
  <div class=h style="font-size:88px;margin-top:30px">protected <em>since 1952</em></div>
  <div class=p>Ten glacial lakes. Peaks up to 4,978 m.</div></div>''',
  'Source: Britannica via Wikipedia. Mérida. Photo: Arturo A / Pexels', 'pexels-14951613-merida-palms.jpg', '45% 50%')),
 ('slide05', slide('photo', L1, 5, T1, '''<div class=txt>
  <div class=kick>Where to stay</div>
  <div class=h style="font-size:128px">Valley towns, <em>mountain air</em></div>
  <div class=p>Lodges and posadas across the Mérida valleys.</div></div>''',
  'Mérida. Photo: Arturo A / Pexels', 'pexels-18206815-merida-town.jpg', '30% 50%')),
 ('slide06', slide('dark', L1, 6, T1, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Plan the trip</div>
   <div class=h style="font-size:112px;margin-bottom:46px">Dry season: <em>December to March</em></div>
   <div class=row><div class=n>01</div><div class=t>Ride: confirm the cable car schedule</div></div>
   <div class=row><div class=n>02</div><div class=t>Stay: a lodge in the valleys</div></div>
   <div class=row><div class=n>03</div><div class=t>Walk: the Sierra Nevada lakes</div></div>
   <div class=h style="font-size:66px;margin-top:44px;color:{GOLD}"><em>Cable car or hiking boots?</em></div></div>''',
  'Source: Britannica via Wikipedia')),
]

# ---------------- P05 IMF 2027 (Wed 11 Nov) ----------------
L2, T2 = 'Venezuela in Motion', 6
SA = [('Guyana',16.8),('Venezuela',7.0),('Suriname',4.1),('Paraguay',4.0),('Argentina',3.5),('Peru',2.9),('Chile',2.6),('Ecuador',2.5),('Uruguay',2.4),('Colombia',2.3),('Brazil',1.9),('Bolivia',-1.5)]
def chart():
    px = 32; zero = 262; rows = ''
    for name, v in SA:
        ve = name == 'Venezuela'
        col = EARTH if ve else '#B9AA94'
        w = abs(v) * px
        left = zero if v >= 0 else zero - w
        fw = 500 if ve else 400
        lab_left = zero + w + 14 if v >= 0 else zero + 14
        rows += f'''<div style="position:relative;height:58px">
          <div style="position:absolute;left:0;top:8px;font:{fw} 31px Jost;color:{INK}">{name}</div>
          <div style="position:absolute;left:{left}px;top:9px;height:38px;width:{w}px;background:{col}"></div>
          <div style="position:absolute;left:{lab_left}px;top:8px;font:{500 if ve else 400} 31px Jost;color:{INK}">{v:.1f}%</div></div>'''
    axis = f'<div style="position:absolute;left:{zero}px;top:0;bottom:0;width:1px;background:{INK};opacity:.5"></div>'
    return f'<div style="position:relative">{axis}{rows}</div>'

p5 = [
 ('slide01', slide('photo', L2, 1, T2, '''<div class=txt>
  <div class=kick>IMF projection, Oct 2026</div>
  <div class=num style="font-size:360px">7%</div>
  <div class=h style="font-size:92px;margin-top:30px">growth forecast for Venezuela <em>in 2027</em></div>
  <div class=p>Only Guyana ranks higher in the region.</div></div>''',
  'Source: IMF WEO, Oct 2026. Caracas. Photo: Edwin Mijares / Pexels', 'pexels-40492546-caracas-sunset2.jpg', '50% 40%', veil=DV)),
 ('slide02', slide('cream', L2, 2, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:150px">
   <div class=kick>Real GDP growth, 2027</div>
   <div class=h style="font-size:92px;margin-bottom:30px">South America, <em>ranked</em></div>
   {chart()}</div>''',
  'Source: IMF WEO, Oct 2026, Table A4. Projections, not results.')),
 ('slide03', slide('photo', L2, 3, T2, '''<div class=txt>
  <div class=kick>The IMF path</div>
  <div style="display:flex;gap:64px;align-items:flex-end">
   <div><div class=num style="font-size:210px">9%</div><div class=lab style="margin-top:22px">2025 est.</div></div>
   <div><div class=num style="font-size:210px">5%</div><div class=lab style="margin-top:22px">2026</div></div>
   <div><div class=num style="font-size:210px;color:#E9C46A">7%</div><div class=lab style="margin-top:22px">2027</div></div></div>
  <div class=p>Latin America and the Caribbean: 2.5% in 2027.</div></div>''',
  'Source: IMF WEO, Oct 2026. Caracas. Photo: Jorge Kardousli Khabbaze / Pexels', 'pexels-20733321-caracas-green.jpg', '50% 55%')),
 ('slide04', slide('photo', L2, 4, T2, '''<div class=txt>
  <div class=kick>The context</div>
  <div class=num style="font-size:320px">70%+</div>
  <div class=h style="font-size:88px;margin-top:24px">of GDP lost, <em>2014 to 2021</em></div>
  <div class=p>High growth, from a very low base.</div></div>''',
  'Source: Banca y Negocios, Oct 2026. Carabobo coast. Photo: Hiurich G. / Pexels', 'pexels-13831431-carabobo-coast.jpg', '40% 50%')),
 ('slide05', slide('photo', L2, 5, T2, '''<div class=txt>
  <div class=kick>The other number</div>
  <div class=num style="font-size:300px">174.7%</div>
  <div class=h style="font-size:88px;margin-top:24px">average inflation <em>projected for 2027</em></div>
  <div class=p>Down from 467.9% in 2026, still very high.</div></div>''',
  'Source: IMF WEO, Oct 2026. El Ávila, Caracas. Photo: Juan Carlos Fernández Alemán / Pexels', 'pexels-39879583-avila.jpg', '50% 45%')),
 ('slide06', slide('dark', L2, 6, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Our take</div>
   <div class=h style="font-size:112px;margin-bottom:46px">A strong forecast. <em>Not a result.</em></div>
   <div class=row><div class=n>01</div><div class=t>Projections change, often</div></div>
   <div class=row><div class=n>02</div><div class=t>GDP is not household income</div></div>
   <div class=row><div class=n>03</div><div class=t>Data quality still matters</div></div>
   <div class=h style="font-size:62px;margin-top:44px;color:{GOLD}"><em>Which number would you watch first?</em></div></div>''',
  'Not investment advice')),
]

# ---------------- P06 Los Roques (Fri 13 Nov) ----------------
L3, T3 = 'Investment Perspectives', 6
p6 = [
 ('slide01', slide('photo', L3, 1, T3, '''<div class=txt>
  <div class=kick>Hospitality in Los Roques</div>
  <div class=h style="font-size:146px">Inside a <em>national park</em></div>
  <div class=p>Here, the rules shape the business.</div></div>''',
  'Gran Roque. Photo: Maria Isabella Bernotti / Pexels', 'pexels-2570472-gran-roque-palms.jpg', '50% 30%', veil=DV)),
 ('slide02', slide('photo', L3, 2, T3, '''<div class=txt>
  <div class=kick>The park</div>
  <div class=num style="font-size:240px">221,120<small>ha</small></div>
  <div class=h style="font-size:88px;margin-top:30px">of land and sea, <em>over 80% under water</em></div>
  <div class=p>A national park since 1972.</div></div>''',
  'Source: Ramsar RIS via Wikipedia. Photo: Fuka jaz / Pexels', 'pexels-18558367-losroques-aerial.jpg', '50% 62%')),
 ('slide03', slide('photo', L3, 3, T3, '''<div class=txt>
  <div class=kick>The model</div>
  <div class=num style="font-size:320px">60</div>
  <div class=h style="font-size:88px;margin-top:24px">registered lodges, surveyed at <em>8 to 38 beds</em></div>
  <div class=p>Only Gran Roque has a permanent population.</div></div>''',
  'Source: Cavada-Blanco et al., Frontiers in Marine Science, 2021. Photo: Fuka jaz / Pexels', 'pexels-16230240-gran-roque.jpg', '55% 100%;background-size:auto 125%')),
 ('slide04', slide('photo', L3, 4, T3, '''<div class=txt>
  <div class=kick>The rulebook</div>
  <div class=num style="font-size:320px">5.5<small>m</small></div>
  <div class=h style="font-size:88px;margin-top:24px">maximum height, <em>one floor</em></div>
  <div class=p>Article 28 of the park's 1991 use plan.</div></div>''',
  'Source: PORU, quoted by Alianza Rebelde Investiga. Gran Roque. Photo: Fuka jaz / Pexels', 'pexels-18558470-gran-roque-hut.jpg', '50% 45%')),
 ('slide05', slide('photo', L3, 5, T3, '''<div class=txt>
  <div class=kick>Access</div>
  <div class=num style="font-size:320px">40<small>min</small></div>
  <div class=h style="font-size:88px;margin-top:24px">from Caracas, by <em>small plane</em></div>
  <div class=p>About 85% of visitors arrive by air.</div></div>''',
  'Sources: Best Beach Reviews, Oct 2026; Wikipedia. Gran Roque. Photo: Maria Isabella Bernotti / Pexels', 'pexels-2570473-gran-roque-beach.jpg', '40% 100%;background-size:auto 125%')),
 ('slide06', slide('dark', L3, 6, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Before any project</div>
   <div class=h style="font-size:112px;margin-bottom:40px">Check <em>these five</em></div>
   <div class=row style="padding:24px 0"><div class=n>01</div><div class=t>Concession status</div></div>
   <div class=row style="padding:24px 0"><div class=n>02</div><div class=t>Park and coastal permits</div></div>
   <div class=row style="padding:24px 0"><div class=n>03</div><div class=t>Water, power and waste</div></div>
   <div class=row style="padding:24px 0"><div class=n>04</div><div class=t>Air seat capacity</div></div>
   <div class=row style="padding:24px 0"><div class=n>05</div><div class=t>Sanctions compliance</div></div>
   <div class=h style="font-size:60px;margin-top:34px;color:{GOLD}"><em>Should Los Roques stay small by design?</em></div></div>''',
  'Not legal or financial advice')),
]

POSTS = {'p04': p4, 'p05': p5, 'p06': p6}
async def main():
    for k, v in POSTS.items():
        await render(v, OUT / k)
        sheet(OUT / k, [n for n, _ in v], OUT / f'{k}_sheet.jpg')
asyncio.run(main())
