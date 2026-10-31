import asyncio, sys
from pathlib import Path
from slides import *

OUT = Path('/home/claude/build/out')

# ---------------- POST 01 ----------------
P1 = 'Venezuela Uncovered'
p1 = [
 ('slide01', cover(P1, 1, 8, 'No. 01 &nbsp;-&nbsp; Landscapes', 'Venezuela', 'More than you imagine.',
   'Ancient tepuis, a coral archipelago, Andean summits and endless plains. A first look at one of the most biodiverse countries on Earth.')),
 # slide02 = photo Canaima
 ('slide03', fact(P1, 3, 8, 'Canaima National Park', '5&deg;58&prime;N &nbsp; 62&deg;32&prime;W',
   'Where the water falls for almost a kilometre.', '979', 'm', 'Angel Falls, total height, from Auy&aacute;n-tepui',
   [('807 m', 'Longest single drop'), ('1994', 'UNESCO World Heritage Site'), ('30,000 km&sup2;', 'Area of the national park')],
   'Sources: UNESCO World Heritage Centre; Robertson survey, 1949')),
 # slide04 = photo Los Roques
 ('slide05', fact(P1, 5, 8, 'Los Roques Archipelago', '11&deg;51&prime;N &nbsp; 66&deg;45&prime;W',
   'A coral archipelago, protected since 1972.', '221,120', 'ha', 'National park area, more than 80% under water',
   [('~50', 'Islands'), ('~292', 'Cays and shoals'), ('1996', 'Ramsar wetland of international importance')],
   'Sources: Ramsar Sites Information Service; Los Roques National Park records', theme='sand')),
 # slide06 = photo Andes (Merida)
 ('slide07', vbars(P1, 7, 8, 'From sea level to summit', 'Almost five vertical kilometres in a single country.',
   [('Los Roques', 0, 'Caribbean, sea level'), ('Angel Falls', 979, 'Height of the fall'), ('Mount Roraima', 2810, 'Tepui summit'), ('Pico Bol&iacute;var', 4978, 'Highest peak, Andes')],
   'Bars drawn to scale. Angel Falls shows the height of the waterfall; the other values are elevations above sea level.',
   'Sources: P&eacute;rez et al., Interciencia 2005 (GPS survey of Pico Bol&iacute;var); UNESCO', theme='light')),
 ('slide08', venmap(P1, 8, 8, 'Six landscapes, one country', 'One of the world&rsquo;s 17 megadiverse countries.',
   [('roques', 'Los Roques', 'start'), ('margarita', 'Margarita', 'start'), ('bolivar', 'Andes', 'end'), ('llanos', 'Los Llanos', 'end'),
    ('angel', 'Canaima', 'end'), ('roraima', 'Roraima', 'start')],
   [('2,800 km', 'Of coastline'), ('4,978 m', 'Pico Bol&iacute;var'), ('17', 'Megadiverse countries, Venezuela among them')],
   '',
   'Sources: CIA World Factbook; Conservation International (1998)')),
]

# ---------------- POST 02 ----------------
P2 = 'Venezuela in Motion'
summit_chart = f"""
<div style="position:absolute;left:96px;right:96px;top:520px">
 <div class=lbl style="margin-bottom:30px">International guests at the summit</div>
 <div style="display:grid;grid-template-columns:150px 1fr;row-gap:34px;align-items:center">
  <div class=serif style="font-size:46px">2023</div>
  <div style="display:flex;align-items:center;gap:22px"><div style="height:56px;width:{round(640*10/40)}px;background:var(--accent)"></div><div class=serif style="font-size:54px">10</div></div>
  <div class=serif style="font-size:46px">2026</div>
  <div style="display:flex;align-items:center;gap:22px"><div style="height:56px;width:640px;background:var(--fg)"></div><div class=serif style="font-size:54px">~40</div></div>
 </div>
 <div class=body style="font-size:18px;color:var(--muted);margin-top:22px">First edition (2023) vs sixth edition (2026). Bars to scale.</div>
</div>
<div style="position:absolute;left:96px;right:96px;top:930px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">
 <div style="border-top:1px solid var(--line);padding-top:28px"><div class=serif style="font-size:62px;line-height:1">25</div><div class=lbl style="margin-top:14px;font-size:15px;letter-spacing:.14em">Investment funds</div></div>
 <div style="border-top:1px solid var(--line);padding-top:28px"><div class=serif style="font-size:62px;line-height:1">35+</div><div class=lbl style="margin-top:14px;font-size:15px;letter-spacing:.14em">Supporting tech companies</div></div>
 <div style="border-top:1px solid var(--line);padding-top:28px"><div class=serif style="font-size:62px;line-height:1">21-23 Oct</div><div class=lbl style="margin-top:14px;font-size:15px;letter-spacing:.14em">Opened by Richard Branson</div></div>
</div>"""
cashea_chart = f"""
<div style="position:absolute;left:96px;right:96px;top:520px">
 <div style="display:flex;align-items:baseline;gap:18px"><div class=stat style="font-size:200px">100</div><div class=serif style="font-size:64px;color:var(--accent)">US$ million</div></div>
 <div class=lbl style="margin-top:14px">Raised by Cashea in 2026, in two rounds</div>
 <div style="display:flex;margin-top:46px;height:64px">
  <div style="width:40%;background:var(--accent)"></div><div style="width:60%;background:var(--fg)"></div></div>
 <div style="display:flex;margin-top:16px">
  <div style="width:40%" class=lbl>Series A &nbsp;US$40M<br><span style="text-transform:none;letter-spacing:0;font-weight:400;color:var(--soft)">March 2026</span></div>
  <div style="width:60%" class=lbl>Series B &nbsp;US$60M<br><span style="text-transform:none;letter-spacing:0;font-weight:400;color:var(--soft)">June 2026</span></div></div>
</div>
<div style="position:absolute;left:96px;right:96px;top:1000px;display:grid;grid-template-columns:repeat(2,1fr);gap:40px">
 <div style="border-top:1px solid var(--line);padding-top:26px"><div class=serif style="font-size:62px;line-height:1">10M+</div><div class=lbl style="margin-top:12px;font-size:15px;letter-spacing:.14em">Consumer accounts</div></div>
 <div style="border-top:1px solid var(--line);padding-top:26px"><div class=serif style="font-size:62px;line-height:1">40,000</div><div class=lbl style="margin-top:12px;font-size:15px;letter-spacing:.14em">Partner stores</div></div>
</div>"""
OPER, ANN, TBC = '#4F6B4A', '#8A6A3A', '#9A5A4A'
p2 = [
 ('slide01', cover(P2, 1, 7, 'No. 02 &nbsp;-&nbsp; Business', 'Capital comes', 'to Caracas.',
   'Twenty-five investment funds, a US$100 million fintech year and new air routes. What is moving, and what still needs proof.')),
 # slide02 = photo Caracas
 ('slide03', hbars_custom(P2, 3, 7, 'Startup Venezuela Summit &nbsp;-&nbsp; Caracas', 'The sixth edition drew 25 investment funds.', summit_chart,
   'Source: Bloomberg L&iacute;nea, Oct 2026 (organiser figures)', theme='light')),
 ('slide04', hbars_custom(P2, 4, 7, 'Fintech &nbsp;-&nbsp; Cashea', 'A US$100 million year for a Venezuelan fintech.', cashea_chart,
   'Source: Intelligent CIO, Aug 2026 (company figures)', theme='sand')),
 # slide05 = photo Avila
 ('slide06', listslide(P2, 6, 7, 'Air connectivity', 'New routes, with different levels of certainty.', [
   {'chip': 'Operating', 'chipc': OPER, 't': 'Qatar Airways &nbsp;Doha - Caracas', 'r': 'Since 22 Jul 2026'},
   {'chip': 'Operating', 'chipc': OPER, 't': 'Avianca &nbsp;Bogot&aacute; - Caracas', 'r': 'Since 1 Sep 2026'},
   {'chip': 'Announced', 'chipc': ANN, 't': 'Copa &nbsp;Panama - Porlamar, Margarita', 'r': 'From 26 Nov 2026'},
   {'chip': 'Announced', 'chipc': ANN, 't': 'LATAM &nbsp;Santiago - Caracas', 'r': 'From 3 Jan 2027'},
   {'chip': 'Not confirmed', 'chipc': TBC, 't': 'United and JetBlue &nbsp;US - Caracas', 'r': 'Pending approvals'},
  ], 'Source: Bloomberg L&iacute;nea, 7 Oct 2026', top_list=470, row_gap=30, title_size=29)),
 ('slide07', listslide(P2, 7, 7, 'Our read', 'Momentum is real. So is the due diligence.', [
   {'t': 'Most figures come from organisers and companies', 'd': 'Useful signals, not audited market data.'},
   {'t': 'Several routes still await authorisations', 'd': 'Announced is not the same as operating.'},
   {'t': 'Compliance comes first', 'd': 'Sanctions screening and legal advice remain part of any deal.'},
  ], 'What would you need to see before investing in Venezuela?', theme='dark', numbered=True, top_list=560, row_gap=40)),
]
# fix: last slide question placed as src -> use dedicated layout
p2[-1] = ('slide07', listslide(P2, 7, 7, 'Our read', 'Momentum is real. So is the due diligence.', [
   {'t': 'Most figures come from organisers and companies', 'd': 'Useful signals, not audited market data.'},
   {'t': 'Several routes still await authorisations', 'd': 'Announced is not the same as operating.'},
   {'t': 'Compliance comes first', 'd': 'Sanctions screening and legal advice remain part of any deal.'},
  ], '', theme='dark', numbered=True, top_list=520, row_gap=40).replace('<div class=foot>',
  '<div class="serif it" style="position:absolute;left:96px;right:96px;top:1050px;font-size:46px;line-height:1.15;color:#E4D6C4">What would you need to see before investing in Venezuela?</div><div class=foot>'))

# ---------------- POST 03 ----------------
P3 = 'Investment Perspectives'
route = f"""
<div style="position:absolute;left:96px;right:96px;top:520px">
 <svg width="888" height="300" viewBox="0 0 888 300">
  <path d="M 90 230 Q 444 -40 798 150" fill="none" stroke="{C['earth']}" stroke-width="2" stroke-dasharray="2 10" stroke-linecap="round"/>
  <circle cx="90" cy="230" r="11" fill="{C['espresso']}"/><circle cx="798" cy="150" r="11" fill="{C['espresso']}"/>
  <circle cx="798" cy="150" r="22" fill="none" stroke="{C['earth']}" stroke-width="1.2"/>
  <text x="90" y="285" text-anchor="middle" font-family="Cormorant" font-size="56" fill="{C['ink']}">PTY</text>
  <text x="798" y="215" text-anchor="middle" font-family="Cormorant" font-size="56" fill="{C['ink']}">PMV</text>
  <text x="444" y="40" text-anchor="middle" font-family="Inter" font-size="17" font-weight="500" letter-spacing="3" fill="{C['earth']}">COPA AIRLINES</text>
 </svg>
 <div style="display:flex;justify-content:space-between;margin-top:6px"><div class=lbl>Panama City, Tocumen</div><div class=lbl style="text-align:right">Porlamar, Santiago Mari&ntilde;o</div></div>
</div>
<div style="position:absolute;left:96px;right:96px;top:950px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">
 <div style="border-top:1px solid var(--line);padding-top:26px"><div class=serif style="font-size:58px;line-height:1">26 Nov</div><div class=lbl style="margin-top:12px;font-size:15px;letter-spacing:.14em">First flight, 2026</div></div>
 <div style="border-top:1px solid var(--line);padding-top:26px"><div class=serif style="font-size:58px;line-height:1">3 / week</div><div class=lbl style="margin-top:12px;font-size:15px;letter-spacing:.14em">Tue, Thu, Sun</div></div>
 <div style="border-top:1px solid var(--line);padding-top:26px"><div class=serif style="font-size:58px;line-height:1">6th</div><div class=lbl style="margin-top:12px;font-size:15px;letter-spacing:.14em">Copa destination in Venezuela</div></div>
</div>"""
p3 = [
 ('slide01', cover(P3, 1, 7, 'No. 03 &nbsp;-&nbsp; Destinations', 'Isla Margarita', 'An underrated Caribbean destination?',
   'Beaches, a free-port history and a new air link to Panama. Where the opportunity could be, and what to verify first.')),
 # slide02 = photo aerial beach
 ('slide03', margmap(P3, 3, 7, 'Nueva Esparta State', 'Two peninsulas, one island.', [
   ('asuncion', 'La Asunción', 'end', -2, 'cap'), ('porlamar', 'Porlamar', 'end', 10, 'dot'), ('pampatar', 'Pampatar', 'end', 30, 'dot'),
   ('juangriego', 'Juan Griego', 'end', -6, 'dot'), ('airport', 'Airport PMV', 'start', 22, 'dot'), ('macanao', 'Macanao Peninsula', '', 0, 'area'),
   ('restinga', 'La Restinga', '', 0, 'area')],
   [('1,020 km&sup2;', 'Island area'), ('78 km', 'East to west'), ('70+', 'Beaches')],
   'Sources: Wikipedia, Margarita Island; La Asunci&oacute;n is the state capital')),
 # slide04 = photo Pampatar
 ('slide05', hbars_custom(P3, 5, 7, 'Connectivity', 'Panama, three times a week.', route,
   'Sources: El Diario, Aug 2026; Bloomberg L&iacute;nea, Oct 2026. Announced route.', theme='sand')),
 ('slide06', listslide(P3, 6, 7, 'Hospitality positioning', 'Where the opportunity could be.', [
   {'t': 'Reposition, before building new', 'd': 'Upgrading existing beach hotels is often faster and lower risk than greenfield projects.'},
   {'t': 'Nature-led boutique stays', 'd': 'Low-density concepts around Macanao and La Restinga, designed with the landscape.'},
   {'t': 'A Caribbean gateway', 'd': 'Itineraries that combine Margarita with Los Roques and the mainland.'},
  ], 'Source: VZLA Rising editorial analysis', note='Investment hypotheses, not forecasts', numbered=True, top_list=600, row_gap=40)),
 ('slide07', listslide(P3, 7, 7, 'Before any investment', 'Six things to verify first.', [
   {'t': 'Land title and registry chain'}, {'t': 'Sanctions and compliance screening'}, {'t': 'Water and power reliability'},
   {'t': 'Coastal zoning and building permits'}, {'t': 'Currency, payments and repatriation'}, {'t': 'Real demand data: arrivals, occupancy, rates'},
  ], 'Editorial checklist. Not legal or financial advice.', theme='dark', numbered=True, top_list=430, row_gap=26, title_size=30).replace('<div class=foot>',
  '<div class="serif it" style="position:absolute;left:96px;right:96px;top:1075px;font-size:42px;line-height:1.15;color:#E4D6C4">What would make Margarita investable for you?</div><div class=foot>')),
]

async def main():
    await render(p1, OUT / 'post01')
    await render(p2, OUT / 'post02')
    await render(p3, OUT / 'post03')
asyncio.run(main())
