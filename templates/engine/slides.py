import json, os, sys, asyncio, html
from pathlib import Path
from playwright.async_api import async_playwright

B = Path(__file__).resolve().parent
FONTS = B / 'node_modules/@fontsource'
LOGO = Path(__file__).resolve().parents[2] / 'brand' / 'logo'
MAPS = json.load(open(B / 'maps.json'))

C = dict(ivory='#F5F0E8', sand='#E4D6C4', taupe='#B7A28D', earth='#685344', espresso='#302820', ink='#241E18')

CSS = f"""
@font-face{{font-family:'Cormorant';font-weight:300;src:url('file://{FONTS}/cormorant-garamond/files/cormorant-garamond-latin-300-normal.woff2')}}
@font-face{{font-family:'Cormorant';font-weight:400;src:url('file://{FONTS}/cormorant-garamond/files/cormorant-garamond-latin-400-normal.woff2')}}
@font-face{{font-family:'Cormorant';font-weight:500;src:url('file://{FONTS}/cormorant-garamond/files/cormorant-garamond-latin-500-normal.woff2')}}
@font-face{{font-family:'Cormorant';font-style:italic;font-weight:300;src:url('file://{FONTS}/cormorant-garamond/files/cormorant-garamond-latin-300-italic.woff2')}}
@font-face{{font-family:'Cormorant';font-style:italic;font-weight:400;src:url('file://{FONTS}/cormorant-garamond/files/cormorant-garamond-latin-400-italic.woff2')}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}}
.serif,.h1,.h2,.stat{{font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1}}
svg text{{paint-order:stroke;stroke:#F5F0E8;stroke-width:7px;stroke-linejoin:round}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;background:var(--bg);color:var(--fg)}}
.top{{position:absolute;left:96px;right:96px;top:84px;display:flex;justify-content:space-between;align-items:center;
  font-size:17px;letter-spacing:.24em;text-transform:uppercase;font-weight:500;color:var(--muted)}}
.top:after{{content:'';position:absolute;left:0;right:0;top:40px;height:1px;background:var(--line)}}
.foot{{position:absolute;left:96px;right:96px;bottom:78px;display:flex;justify-content:space-between;align-items:flex-end}}
.foot img{{height:58px;display:block}}
.src{{font-size:15px;letter-spacing:.04em;color:var(--muted);max-width:640px;text-align:right;line-height:1.45}}
.serif{{font-family:'Cormorant',serif;font-weight:300}}
.it{{font-style:italic}}
.eyebrow{{font-size:17px;letter-spacing:.24em;text-transform:uppercase;font-weight:500;color:var(--accent)}}
.h1{{font-family:'Cormorant',serif;font-weight:300;font-size:84px;line-height:1.02;letter-spacing:-.01em}}
.h2{{font-family:'Cormorant',serif;font-weight:300;font-size:70px;line-height:1.04;letter-spacing:-.005em}}
.body{{font-size:24px;line-height:1.5;color:var(--soft);font-weight:400}}
.lbl{{font-size:16px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;color:var(--muted)}}
.rule{{height:1px;background:var(--line)}}
.stat{{font-family:'Cormorant',serif;font-weight:300;line-height:.9;letter-spacing:-.02em}}
.chip{{display:inline-block;font-size:14px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;padding:7px 12px;border:1px solid currentColor;border-radius:2px}}
"""

THEMES = {
  'light': {'--bg': C['ivory'], '--fg': C['ink'], '--soft': '#4A3F35', '--muted': '#8A7868', '--line': '#D9CBB8', '--accent': C['earth']},
  'sand':  {'--bg': C['sand'], '--fg': C['ink'], '--soft': '#463A2F', '--muted': '#7B6857', '--line': '#C9B59E', '--accent': C['earth']},
  'dark':  {'--bg': C['espresso'], '--fg': '#F5F0E8', '--soft': '#D9CDBE', '--muted': '#A8978A', '--line': '#4C4036', '--accent': C['taupe']},
}

def logo(theme):
    f = 'white-colorflag' if theme == 'dark' else 'espresso-colorflag'
    return f"file://{LOGO}/vzla-rising-wordmark-{f}.png"

def frame(theme, pillar, idx, total, inner, src=''):
    vars_ = ';'.join(f'{k}:{v}' for k, v in THEMES[theme].items())
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div class=s style="{vars_}">
<div class=top><span>{pillar}</span><span>{idx:02d} / {total:02d}</span></div>
{inner}
<div class=foot><img src="{logo(theme)}"><div class=src>{src}</div></div>
</div></body></html>"""

# ---------- templates ----------
def cover(pillar, idx, total, eyebrow, t1, t2, dek, theme='dark'):
    inner = f"""
<div style="position:absolute;left:96px;right:96px;top:330px">
  <div class=eyebrow style="margin-bottom:46px">{eyebrow}</div>
  <div class=serif style="font-size:150px;line-height:.95;letter-spacing:-.02em">{t1}</div>
  <div class="serif it" style="font-size:96px;line-height:1.02;margin-top:18px;color:var(--soft)">{t2}</div>
  <div class=rule style="width:120px;margin:64px 0 40px;background:var(--accent)"></div>
  <div class=body style="font-size:27px;max-width:780px">{dek}</div>
</div>
<div style="position:absolute;right:96px;bottom:168px" class=lbl>Swipe &rarr;</div>"""
    return frame(theme, pillar, idx, total, inner)

def fact(pillar, idx, total, eyebrow, coords, head, big, unit, biglabel, items, src, theme='light'):
    cells = ''.join(f"""<div style="padding:30px 0 0;border-top:1px solid var(--line)">
      <div class=serif style="font-size:58px;line-height:1">{v}</div>
      <div class=lbl style="margin-top:14px;letter-spacing:.14em;font-size:15px;line-height:1.4">{l}</div></div>""" for v, l in items)
    inner = f"""
<div style="position:absolute;left:96px;right:96px;top:190px">
  <div style="display:flex;justify-content:space-between"><div class=eyebrow>{eyebrow}</div><div class=lbl>{coords}</div></div>
  <div class=h2 style="margin-top:44px;max-width:860px">{head}</div>
</div>
<div style="position:absolute;left:96px;right:96px;top:560px">
  <div style="display:flex;align-items:baseline;gap:20px"><div class=stat style="font-size:250px">{big}</div><div class=serif style="font-size:80px;color:var(--accent)">{unit}</div></div>
  <div class=lbl style="margin-top:48px">{biglabel}</div>
</div>
<div style="position:absolute;left:96px;right:96px;top:930px;display:grid;grid-template-columns:repeat({len(items)},1fr);gap:40px">{cells}</div>"""
    return frame(theme, pillar, idx, total, inner, src)

def vbars(pillar, idx, total, eyebrow, head, bars, note, src, theme='sand', maxv=None, fmt=lambda v: f'{v:,}'):
    maxv = maxv or max(v for _, v, _ in bars)
    H = 520
    cols = ''.join(f"""<div style="display:flex;flex-direction:column;justify-content:flex-end;align-items:stretch;height:{H+150}px">
      <div class=serif style="font-size:52px;line-height:1;margin-bottom:14px">{fmt(v)}<span style="font-size:30px;color:var(--accent)"> m</span></div>
      <div style="height:{max(2, round(H*v/maxv))}px;background:{'var(--fg)' if v==maxv else 'var(--accent)'}"></div>
      <div style="height:1px;background:var(--fg);margin-top:0"></div>
      <div class=lbl style="margin-top:16px;font-size:15px;letter-spacing:.12em;line-height:1.35;height:60px">{n}<br><span style="color:var(--soft);text-transform:none;letter-spacing:0;font-weight:400">{s}</span></div></div>""" for n, v, s in bars)
    inner = f"""
<div style="position:absolute;left:96px;right:96px;top:190px">
  <div class=eyebrow>{eyebrow}</div>
  <div class=h2 style="margin-top:44px;max-width:880px">{head}</div>
</div>
<div style="position:absolute;left:96px;right:96px;top:470px;display:grid;grid-template-columns:repeat({len(bars)},1fr);gap:44px">{cols}</div>
<div class=body style="position:absolute;left:96px;right:96px;top:1150px;font-size:19px;color:var(--muted)">{note}</div>"""
    return frame(theme, pillar, idx, total, inner, src)

def venmap(pillar, idx, total, eyebrow, head, marks, facts, question, src, theme='light'):
    m = MAPS['ven']
    pts = ''
    for key, label, anchor in marks:
        x, y = m['pts'][key]
        tx = x + (28 if anchor == 'start' else -28)
        pts += f'<circle cx="{x}" cy="{y}" r="9" fill="{C["espresso"]}"/><circle cx="{x}" cy="{y}" r="17" fill="none" stroke="{C["earth"]}" stroke-width="1.2"/>'
        pts += f'<text x="{tx}" y="{y+6}" text-anchor="{anchor}" font-family="Inter" font-size="19" font-weight="500" letter-spacing="2.4" fill="{C["ink"]}">{label.upper()}</text>'
    fct = ''.join(f'<div><div class=serif style="font-size:56px;line-height:1">{v}</div><div class=lbl style="margin-top:10px;font-size:14px;letter-spacing:.14em">{l}</div></div>' for v, l in facts)
    inner = f"""
<div style="position:absolute;left:96px;right:96px;top:190px"><div class=eyebrow>{eyebrow}</div>
<div class=h2 style="margin-top:36px;font-size:62px">{head}</div></div>
<svg style="position:absolute;left:100px;top:370px" width="880" height="630" viewBox="0 70 880 630">
 <path d="{m['nb']}" fill="#EAE1D4" stroke="#D9CBB8" stroke-width="1"/>
 <path d="{m['d']}" fill="{C['sand']}" stroke="{C['earth']}" stroke-width="1.6"/>{pts}</svg>
<div style="position:absolute;left:96px;right:96px;top:1040px;display:grid;grid-template-columns:repeat({len(facts)},1fr);gap:40px;border-top:1px solid var(--line);padding-top:26px">{fct}</div>
<div class="serif it" style="position:absolute;left:96px;right:96px;top:1160px;font-size:40px;color:var(--accent)">{question}</div>"""
    return frame(theme, pillar, idx, total, inner, src)

def margmap(pillar, idx, total, eyebrow, head, marks, facts, src, theme='light'):
    m = MAPS['marg']
    pts = ''
    for key, label, anchor, dy, style in marks:
        x, y = m['pts'][key]
        tx = x + (16 if anchor == 'start' else (-16 if anchor == 'end' else 0))
        if style == 'area':
            pts += f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Cormorant" font-style="italic" font-size="30" fill="{C["earth"]}">{label}</text>'
            continue
        pts += f'<circle cx="{x}" cy="{y}" r="{8 if style=="cap" else 6}" fill="{C["espresso"]}"/>'
        if style == 'cap':
            pts += f'<circle cx="{x}" cy="{y}" r="14" fill="none" stroke="{C["earth"]}" stroke-width="1.2"/>'
        pts += f'<text x="{tx}" y="{y+6+dy}" text-anchor="{anchor}" font-family="Inter" font-size="17" font-weight="500" letter-spacing="2" fill="{C["ink"]}">{label.upper()}</text>'
    fct = ''.join(f'<div><div class=serif style="font-size:60px;line-height:1">{v}</div><div class=lbl style="margin-top:10px;font-size:14px;letter-spacing:.14em;line-height:1.4">{l}</div></div>' for v, l in facts)
    inner = f"""
<div style="position:absolute;left:96px;right:96px;top:190px"><div class=eyebrow>{eyebrow}</div>
<div class=h2 style="margin-top:36px;font-size:66px">{head}</div></div>
<svg style="position:absolute;left:100px;top:340px" width="880" height="560" viewBox="0 40 880 560">
 <path d="{m['d']}" fill="{C['sand']}" stroke="{C['earth']}" stroke-width="1.6"/>{pts}</svg>
<div style="position:absolute;left:96px;right:96px;top:1010px;display:grid;grid-template-columns:repeat({len(facts)},1fr);gap:40px;border-top:1px solid var(--line);padding-top:28px">{fct}</div>"""
    return frame(theme, pillar, idx, total, inner, src)

def listslide(pillar, idx, total, eyebrow, head, rows, src, theme='light', note='', numbered=False, top_list=520, row_gap=34, title_size=30):
    rws = ''
    for i, r in enumerate(rows):
        left = f'<div class=serif style="font-size:44px;color:var(--accent);width:80px;line-height:1">{i+1:02d}</div>' if numbered else ''
        chip = f'<span class=chip style="color:{r.get("chipc","var(--accent)")};margin-bottom:12px">{r["chip"]}</span><br>' if r.get('chip') else ''
        rws += f"""<div style="display:flex;gap:24px;padding:{row_gap//2+4}px 0;border-top:1px solid var(--line)">{left}
<div style="flex:1">{chip}<div style="font-size:{title_size}px;font-weight:500;line-height:1.25">{r['t']}</div>{f'<div class=body style="font-size:21px;margin-top:6px">{r["d"]}</div>' if r.get('d') else ''}</div>
{f'<div class=lbl style="text-align:right;white-space:nowrap;font-size:15px;padding-top:6px">{r["r"]}</div>' if r.get('r') else ''}</div>"""
    inner = f"""
<div style="position:absolute;left:96px;right:96px;top:190px"><div class=eyebrow>{eyebrow}</div>
<div class=h2 style="margin-top:40px;max-width:880px">{head}</div>
{f'<div class=lbl style="margin-top:26px;color:var(--accent)">{note}</div>' if note else ''}</div>
<div style="position:absolute;left:96px;right:96px;top:{top_list}px">{rws}</div>"""
    return frame(theme, pillar, idx, total, inner, src)

def hbars_custom(pillar, idx, total, eyebrow, head, inner_html, src, theme='light'):
    inner = f"""<div style="position:absolute;left:96px;right:96px;top:190px"><div class=eyebrow>{eyebrow}</div>
<div class=h2 style="margin-top:40px;max-width:880px">{head}</div></div>{inner_html}"""
    return frame(theme, pillar, idx, total, inner, src)

async def render(jobs, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
        for name, htmlstr in jobs:
            f = outdir / (name + '.html'); f.write_text(htmlstr)
            await pg.goto('file://' + str(f)); await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(150)
            await pg.screenshot(path=str(outdir / (name + '.png')), full_page=False)
            await pg.screenshot(path=str(outdir / (name + '.jpg')), type='jpeg', quality=92)
        await b.close()
