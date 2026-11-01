import asyncio
from pathlib import Path
from eco2 import *

OUT = Path('/home/claude/build/out3')

# ---------------- POST 01 - Venezuela Uncovered ----------------
L1, T1 = 'Venezuela Uncovered', 6
p1 = [
 ('slide01', slide('photo', L1, 1, T1, f'''<div class=txt>
  <div class=kick>Seis paisajes, un país</div>
  <div class=h style="font-size:138px">Venezuela es <em>más</em><br>que los titulares</div>
  <div class=p>Tepuyes, arrecifes, cumbres andinas y llanos sin fin.</div></div>''',
  'Cerro Autana, Amazonas. Foto: Frank Araujo / Pexels', 'pexels-12693427-autana.jpg', '58% 50%')),
 ('slide02', slide('photo', L1, 2, T1, f'''<div class=txt>
  <div class=kick>Salto Ángel, Canaima</div>
  <div class=num style="font-size:330px">979<small>m</small></div>
  <div class=h style="font-size:84px;margin-top:34px">Una de las cascadas <em>más altas</em> del mundo</div>
  <div class=p>807 m de caída libre desde el Auyán-tepui. Canaima es Patrimonio UNESCO desde 1994.</div></div>''',
  'Fuentes: UNESCO; medición Robertson, 1949. Foto: Ederik Palencia Ferreira / Pexels', 'pexels-7360544-canaima.jpg', '50% 50%')),
 ('slide03', slide('photo', L1, 3, T1, f'''<div class=txt>
  <div class=kick>Archipiélago Los Roques</div>
  <div class=num style="font-size:250px">221.120<small>ha</small></div>
  <div class=h style="font-size:84px;margin-top:34px">Un parque nacional <em>de coral</em> desde 1972</div>
  <div class=p>Unas 50 islas y cerca de 292 cayos. Humedal Ramsar desde 1996.</div></div>''',
  'Fuente: Ramsar Sites Information Service. Foto: Fuka jaz / Pexels', 'pexels-18558367-losroques-aerial.jpg', '50% 22%')),
 ('slide04', slide('photo', L1, 4, T1, f'''<div class=txt>
  <div class=kick>Los Andes, Mérida</div>
  <div class=num style="font-size:300px">4.978<small>m</small></div>
  <div class=h style="font-size:84px;margin-top:34px">El Pico Bolívar, <em>el techo</em> de Venezuela</div>
  <div class=p>Del nivel del mar a casi cinco kilómetros de altura, en un solo país.</div></div>''',
  'Fuente: Pérez et al., Interciencia 2005 (GPS). Foto: Pedro Romero / Unsplash', 'unsplash-LoBZJg-390E-merida-valley.jpg', '50% 30%')),
 ('slide05', slide('photo', L1, 5, T1, f'''<div class=txt>
  <div class=kick>Los Llanos</div>
  <div class=h style="font-size:128px">Sabanas hasta <em>el horizonte</em></div>
  <div class=p>La tierra del llanero: ganado, ríos y cielos enormes entre los Andes y el Orinoco.</div></div>''',
  'Elorza, Apure. Foto: Jean-Luc Crucifix / Unsplash', 'unsplash-19tQv51x4-A-llanos.jpg', '50% 50%')),
 ('slide06', slide('cream', L1, 6, T1, f'''
  <div style="position:absolute;left:72px;right:72px;top:160px">
   <div class=kick>Uno de los 17 países megadiversos</div>
   <div class=h style="font-size:96px">¿Cuál visitarías <em>primero?</em></div></div>
  <div style="position:absolute;left:72px;top:420px">{venmap([('roques','Los Roques','start'),('margarita','Margarita','start'),('bolivar','Andes','end'),('llanos','Llanos','end'),('angel','Canaima','end'),('roraima','Roraima','start')])}</div>
  <div style="position:absolute;left:72px;right:72px;top:1050px;font:400 32px/1.35 Jost">Cuéntanos en los comentarios y guarda el post para tu próximo viaje.</div>''',
  'Fuentes: Conservation International; CIA World Factbook')),
]

# ---------------- POST 02 - Venezuela in Motion ----------------
L2, T2 = 'Venezuela in Motion', 5
p2 = [
 ('slide01', slide('photo', L2, 1, T2, f'''<div class=txt>
  <div class=kick>Negocios</div>
  <div class=h style="font-size:146px">El capital <em>llega</em> a Caracas</div>
  <div class=p>25 fondos, una fintech de US$100 millones y nuevas rutas aéreas. Qué se mueve y qué falta probar.</div></div>''',
  'Caracas. Foto: Andy Art and design / Pexels', 'pexels-29518260-caracas-sunset.jpg', '50% 60%')),
 ('slide02', slide('photo', L2, 2, T2, f'''<div class=txt>
  <div class=kick>Startup Venezuela Summit</div>
  <div class=num style="font-size:330px">25</div>
  <div class=h style="font-size:84px;margin-top:30px">fondos de inversión en <em>la sexta edición</em></div>
  <div class=p>Del 21 al 23 de octubre, inaugurada por Richard Branson. Unos 40 invitados internacionales, frente a 10 en 2023.</div></div>''',
  'Fuente: Bloomberg Línea, oct. 2026 (cifras de los organizadores). Foto: Joaquim Pacheco / Pexels', 'pexels-38556235-caracas-aerial.jpg', '40% 50%')),
 ('slide03', slide('cream', L2, 3, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Fintech</div>
   <div class=h style="font-size:96px">Cashea levantó</div>
   <div class=num style="font-size:300px;margin-top:20px">US$100<small>M</small></div>
   <div class=lab style="margin-top:30px">En 2026, en dos rondas</div>
   <div style="display:flex;height:70px;margin-top:40px"><div style="width:40%;background:{EARTH}"></div><div style="width:60%;background:{INK}"></div></div>
   <div style="display:flex;margin-top:18px;font:500 30px Jost"><div style="width:40%">Serie A · 40M<div style="font:400 26px Jost;opacity:.7">marzo</div></div><div style="width:60%">Serie B · 60M<div style="font:400 26px Jost;opacity:.7">junio</div></div></div>
   <div class=p style="margin-top:56px">Más de <b>10 millones</b> de cuentas y <b>40.000</b> comercios aliados.</div></div>''',
  'Fuente: Intelligent CIO, ago. 2026 (cifras de la empresa)').replace('Serie A · 40M','Serie A - 40M').replace('Serie B · 60M','Serie B - 60M')),
 ('slide04', slide('photo', L2, 4, T2, f'''<div class=txt style="bottom:220px">
  <div class=kick>Conectividad aérea</div>
  <div class=h style="font-size:92px;margin-bottom:34px">Vuelven <em>los vuelos</em></div>
  <div class=row><div style="flex:1"><div class=tag>Operando</div><div class=t>Qatar Airways, Doha - Caracas</div><div class=d>Desde el 22 de julio</div></div></div>
  <div class=row><div style="flex:1"><div class=tag>Operando</div><div class=t>Avianca, Bogotá - Caracas</div><div class=d>Desde el 1 de septiembre</div></div></div>
  <div class=row><div style="flex:1"><div class=tag>Anunciado</div><div class=t>Copa, Panamá - Margarita</div><div class=d>Desde el 26 de noviembre</div></div></div>
  <div class=row><div style="flex:1"><div class=tag>Por confirmar</div><div class=t>United y JetBlue desde EE.UU.</div><div class=d>Pendientes de autorización</div></div></div></div>''',
  'Fuente: Bloomberg Línea, 7 oct. 2026. Foto: Juan Carlos Fernández Alemán / Pexels', 'pexels-39879583-avila.jpg', '50% 30%',
  veil='background:linear-gradient(180deg,rgba(12,9,6,.5) 0%,rgba(12,9,6,.15) 18%,rgba(12,9,6,.72) 42%,rgba(12,9,6,.92) 100%)')),
 ('slide05', slide('dark', L2, 5, T2, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Nuestra lectura</div>
   <div class=h style="font-size:100px;margin-bottom:46px">El impulso es real. <em>La debida diligencia</em> también.</div>
   <div class=row><div class=n>01</div><div><div class=t>Cifras de empresas y organizadores</div><div class=d>Señales útiles, no datos auditados.</div></div></div>
   <div class=row><div class=n>02</div><div><div class=t>Anunciado no es operativo</div><div class=d>Varias rutas esperan autorización.</div></div></div>
   <div class=row><div class=n>03</div><div><div class=t>Cumplimiento primero</div><div class=d>Sanciones y asesoría legal en cada operación.</div></div></div>
   <div class=h style="font-size:58px;margin-top:40px;color:{GOLD}"><em>¿Qué necesitarías ver para invertir?</em></div></div>''',
  'No es asesoría de inversión')),
]

# ---------------- POST 03 - Investment Perspectives ----------------
L3, T3 = 'Investment Perspectives', 6
p3 = [
 ('slide01', slide('photo', L3, 1, T3, f'''<div class=txt>
  <div class=kick>Destinos</div>
  <div class=h style="font-size:140px">Isla Margarita, ¿el Caribe <em>subestimado?</em></div>
  <div class=p>Playas, historia de puerto libre y un nuevo vuelo a Panamá.</div></div>''',
  'Isla Margarita. Foto: RITRATTO VISUAL / Pexels', 'pexels-32699741-margarita-aerial.jpg', '50% 60%')),
 ('slide02', slide('photo', L3, 2, T3, f'''<div class=txt>
  <div class=kick>Pampatar, Nueva Esparta</div>
  <div class=num style="font-size:300px">70+</div>
  <div class=h style="font-size:84px;margin-top:30px">playas en <em>78 km</em> de isla</div>
  <div class=p>1.020 km² y una larga tradición de destino turístico venezolano.</div></div>''',
  'Fuente: datos geográficos de Isla Margarita. Foto: Vika Glitter / Pexels', 'pexels-26241556-pampatar.jpg', '30% 50%')),
 ('slide03', slide('cream', L3, 3, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Estado Nueva Esparta</div>
   <div class=h style="font-size:96px">Dos penínsulas, <em>una isla</em></div></div>
  <div style="position:absolute;left:72px;top:440px">{margmap([('asuncion','La Asunción','end',-4,'cap'),('porlamar','Porlamar','end',12,'dot'),('pampatar','Pampatar','start',-30,'dot'),('juangriego','Juan Griego','end',-8,'dot'),('airport','Aeropuerto','end',26,'dot'),('macanao','Macanao','',0,'area'),('restinga','La Restinga','',12,'area')])}</div>
  <div style="position:absolute;left:72px;right:72px;top:1060px;font:400 32px/1.35 Jost">La Asunción es la capital del estado. Porlamar, el principal centro comercial.</div>''',
  'Fuente: datos geográficos de Isla Margarita')),
 ('slide04', slide('photo', L3, 4, T3, f'''<div class=txt>
  <div class=kick>Conectividad</div>
  <div class=num style="font-size:300px">3<small>vuelos / semana</small></div>
  <div class=h style="font-size:84px;margin-top:30px">Panamá - Porlamar <em>desde el 26 de noviembre</em></div>
  <div class=p>Copa conecta la isla con su hub regional: martes, jueves y domingo. Ruta anunciada.</div></div>''',
  'Fuentes: El Diario, ago. 2026; Bloomberg Línea, oct. 2026. Foto: RITRATTO VISUAL / Pexels', 'pexels-32699745-margarita-lighthouse.jpg', '50% 20%')),
 ('slide05', slide('photo', L3, 5, T3, f'''<div class=txt style="bottom:220px">
  <div class=kick>Hipótesis, no pronósticos</div>
  <div class=h style="font-size:92px;margin-bottom:34px">Dónde podría estar <em>la oportunidad</em></div>
  <div class=row><div class=n>01</div><div><div class=t>Reposicionar antes que construir</div><div class=d>Renovar hoteles existentes.</div></div></div>
  <div class=row><div class=n>02</div><div><div class=t>Boutique de baja densidad</div><div class=d>Macanao y La Restinga, con el paisaje.</div></div></div>
  <div class=row><div class=n>03</div><div><div class=t>Puerta al Caribe</div><div class=d>Itinerarios con Los Roques.</div></div></div></div>''',
  'Análisis editorial VZLA Rising. Foto: RITRATTO VISUAL / Pexels', 'pexels-32690921-nueva-esparta.jpg', '55% 50%',
  veil='background:linear-gradient(180deg,rgba(12,9,6,.5) 0%,rgba(12,9,6,.15) 18%,rgba(12,9,6,.72) 45%,rgba(12,9,6,.92) 100%)')),
 ('slide06', slide('dark', L3, 6, T3, f'''
  <div style="position:absolute;left:72px;right:72px;top:170px">
   <div class=kick>Antes de invertir</div>
   <div class=h style="font-size:100px;margin-bottom:40px">Seis cosas <em>que verificar</em></div>
   <div class=row style="padding:20px 0"><div class=n>01</div><div class=t>Títulos de propiedad y registro</div></div>
   <div class=row style="padding:20px 0"><div class=n>02</div><div class=t>Sanciones y cumplimiento</div></div>
   <div class=row style="padding:20px 0"><div class=n>03</div><div class=t>Agua y electricidad</div></div>
   <div class=row style="padding:20px 0"><div class=n>04</div><div class=t>Zonificación costera y permisos</div></div>
   <div class=row style="padding:20px 0"><div class=n>05</div><div class=t>Moneda, pagos y repatriación</div></div>
   <div class=row style="padding:20px 0"><div class=n>06</div><div class=t>Demanda real: llegadas y ocupación</div></div>
   <div class=h style="font-size:56px;margin-top:30px;color:{GOLD}"><em>¿Qué haría a Margarita invertible para ti?</em></div></div>''',
  'Checklist editorial. No es asesoría legal ni financiera')),
]

POSTS = {'post01': p1, 'post02': p2, 'post03': p3}
async def main():
    for k, v in POSTS.items():
        await render(v, OUT / k)
        sheet(OUT / k, [n for n, _ in v], OUT / f'{k}_sheet.jpg')
asyncio.run(main())
