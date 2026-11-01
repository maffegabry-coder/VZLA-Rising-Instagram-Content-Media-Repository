"""VZLA Rising v3 - hospitality editorial carousel. 1080x1350, phone-first.
Full-bleed real photo + gradient veil, text anchored low, Cormorant headlines, Jost text."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

LOGO = Path('/home/claude/brand/logo')
PH = Path('/home/claude/vzla-rising-instagram-content-media-repository/photos')
F = '/home/claude/build/node_modules/@fontsource'
MAPS = json.load(open('/home/claude/build/maps.json'))
GOLD, INK, CREAM, ESP, EARTH = '#E9C46A', '#1A1511', '#F3EDE3', '#231C16', '#8A6A44'

def ff(fam, w, file, style='normal'):
    return f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{style};src:url('file://{F}/{file}')}}"

CSS = '\n'.join([
 ff('Cormorant', 300, 'cormorant-garamond/files/cormorant-garamond-latin-300-normal.woff2'),
 ff('Cormorant', 400, 'cormorant-garamond/files/cormorant-garamond-latin-400-normal.woff2'),
 ff('Cormorant', 500, 'cormorant-garamond/files/cormorant-garamond-latin-500-normal.woff2'),
 ff('Cormorant', 400, 'cormorant-garamond/files/cormorant-garamond-latin-400-italic.woff2', 'italic'),
 ff('Cormorant', 300, 'cormorant-garamond/files/cormorant-garamond-latin-300-italic.woff2', 'italic'),
 ff('Jost', 300, 'jost/files/jost-latin-300-normal.woff2'),
 ff('Jost', 400, 'jost/files/jost-latin-400-normal.woff2'),
 ff('Jost', 500, 'jost/files/jost-latin-500-normal.woff2'),
]) + """
*{margin:0;padding:0;box-sizing:border-box;font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1}
html,body{width:1080px;height:1350px}
body{font-family:'Jost',sans-serif;-webkit-font-smoothing:antialiased}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--fg);background:var(--bg)}
.bg{position:absolute;inset:0;background-size:cover}
.veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,9,6,.42) 0%,rgba(12,9,6,0) 13%,rgba(12,9,6,0) 36%,rgba(12,9,6,.5) 54%,rgba(12,9,6,.8) 72%,rgba(12,9,6,.9) 100%)}
.top{position:absolute;top:60px;left:72px;right:72px;display:flex;justify-content:space-between;
  font:500 25px 'Jost';letter-spacing:.26em;text-transform:uppercase;z-index:3}
.top.ph{text-shadow:0 1px 14px rgba(0,0,0,.45)}
.rule{position:absolute;top:110px;left:72px;right:72px;height:1px;background:var(--fg);opacity:.45;z-index:3}
.foot{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end;z-index:3}
.foot img{height:128px;display:block}
.src{font:400 23px/1.35 'Jost';letter-spacing:.02em;opacity:.85;max-width:640px}
.txt{position:absolute;left:72px;right:72px;bottom:240px;z-index:2}
.kick{font:500 27px 'Jost';letter-spacing:.24em;text-transform:uppercase;color:var(--acc);margin-bottom:26px}
.h{font-family:'Cormorant',serif;font-weight:400;line-height:.98;letter-spacing:-.012em}
.h em{font-style:italic;color:var(--acc)}
.num{font-family:'Cormorant',serif;font-weight:300;line-height:.8;letter-spacing:-.035em}
.num small{font-size:.36em;letter-spacing:0;margin-left:10px}
.p{font:400 40px/1.36 'Jost';margin-top:30px;max-width:900px}
.p b{font-weight:500;color:var(--acc)}
.ph .h,.ph .num,.ph .p{text-shadow:0 2px 24px rgba(0,0,0,.35)}
.lab{font:500 24px/1.3 'Jost';letter-spacing:.18em;text-transform:uppercase}
.row{display:flex;gap:28px;align-items:baseline;padding:26px 0;border-top:1px solid var(--line)}
.row .n{font:300 54px 'Cormorant';color:var(--acc);width:70px;flex:none}
.row .t{font:500 38px/1.25 'Jost'}
.ph .row .t,.ph .tag,.ph .row .n{text-shadow:0 1px 18px rgba(0,0,0,.55)}
.row .d{font:400 30px/1.35 'Jost';opacity:.85;margin-top:6px}
.ph .kick{color:#fff;text-shadow:0 1px 16px rgba(0,0,0,.6)}
.kick:before{content:'';display:inline-block;width:56px;height:2px;background:var(--acc);vertical-align:middle;margin-right:22px;position:relative;top:-4px}
.tag{font:500 22px 'Jost';letter-spacing:.18em;text-transform:uppercase;color:var(--acc);margin-bottom:8px}
"""

THEME = {
 'photo': dict(bg='#111', fg='#FFFFFF', acc=GOLD, line='rgba(255,255,255,.35)', logo='white-colorflag'),
 'dark':  dict(bg=ESP, fg='#F6F1EA', acc=GOLD, line='rgba(246,241,234,.22)', logo='white-colorflag'),
 'cream': dict(bg=CREAM, fg=INK, acc=EARTH, line='rgba(26,21,17,.18)', logo='espresso-colorflag'),
}

def slide(theme, label, n, total, inner, src='', photo=None, pos='50% 50%', veil=None):
    t = THEME[theme]
    vars_ = f"--bg:{t['bg']};--fg:{t['fg']};--acc:{t['acc']};--line:{t['line']}"
    bg = ''
    if photo:
        bg = f'<div class=bg style="background-image:url(\'file://{PH / photo}\');background-position:{pos}"></div>'
        bg += f'<div class=veil{"" if not veil else ""} style="{veil or ""}"></div>'
    cls = 's ph' if photo else 's'
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div class="{cls}" style="{vars_}">{bg}
<div class="top{' ph' if photo else ''}"><span>{label}</span><span>{n:02d} / {total:02d}</span></div><div class=rule></div>
{inner}
<div class=foot><div class=src>{src}</div><img src="file://{LOGO}/vzla-rising-wordmark-{t['logo']}.png"></div>
</div></body></html>"""

def venmap(marks, w=936, h=640):
    m = MAPS['ven']; out = ''
    for key, label, anchor in marks:
        x, y = m['pts'][key]; tx = x + (26 if anchor == 'start' else -26)
        out += f'<circle cx="{x}" cy="{y}" r="9" fill="{INK}"/><circle cx="{x}" cy="{y}" r="17" fill="none" stroke="{EARTH}" stroke-width="1.5"/>'
        out += f'<text x="{tx}" y="{y+8}" text-anchor="{anchor}" font-family="Jost" font-weight="500" font-size="25" letter-spacing="3" fill="{INK}" stroke="{CREAM}" stroke-width="8" paint-order="stroke" stroke-linejoin="round">{label.upper()}</text>'
    return f'''<svg width="{w}" height="{h}" viewBox="40 90 820 560"><path d="{m['nb']}" fill="#E7DED1" stroke="#D6C8B4" stroke-width="1"/>
<path d="{m['d']}" fill="#DCCBB3" stroke="{EARTH}" stroke-width="1.8"/>{out}</svg>'''

def margmap(marks, w=936, h=560):
    m = MAPS['marg']; out = ''
    for key, label, anchor, dy, style in marks:
        x, y = m['pts'][key]
        if style == 'area':
            out += f'<text x="{x}" y="{y+dy}" text-anchor="middle" font-family="Cormorant" font-style="italic" font-size="38" fill="{EARTH}" stroke="#DCCBB3" stroke-width="7" paint-order="stroke">{label}</text>'; continue
        tx = x + (20 if anchor == 'start' else -20)
        out += f'<circle cx="{x}" cy="{y}" r="{9 if style=="cap" else 7}" fill="{INK}"/>'
        if style == 'cap': out += f'<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="{EARTH}" stroke-width="1.5"/>'
        out += f'<text x="{tx}" y="{y+8+dy}" text-anchor="{anchor}" font-family="Jost" font-weight="500" font-size="23" letter-spacing="2.5" fill="{INK}" stroke="#DCCBB3" stroke-width="8" paint-order="stroke" stroke-linejoin="round">{label.upper()}</text>'
    return f'''<svg width="{w}" height="{h}" viewBox="50 170 960 440"><path d="{m['d']}" fill="#DCCBB3" stroke="{EARTH}" stroke-width="1.8"/>{out}</svg>'''

async def render(jobs, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for name, h in jobs:
            f = outdir / f'{name}.html'; f.write_text(h)
            await pg.goto('file://' + str(f)); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(200)
            await pg.screenshot(path=str(outdir / f'{name}.jpg'), type='jpeg', quality=92)
        await b.close()

def sheet(outdir, names, path):
    from PIL import Image
    ims = [Image.open(outdir / f'{n}.jpg').resize((432, 540)) for n in names]
    s = Image.new('RGB', (440 * len(ims) - 8, 540), 'white')
    for i, im in enumerate(ims): s.paste(im, (i * 440, 0))
    s.save(path, quality=88)
