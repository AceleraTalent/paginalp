# -*- coding: utf-8 -*-
"""Genera el sitio web-v2 (estático) desde data/*.json y data/recursos/*.md.
Uso:  python scripts/build_site.py   (desde la raíz del repo)
Sin dependencias externas."""
import json, io, os, re, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
R = json.load(io.open(os.path.join(DATA, 'resources.json'), encoding='utf-8'))
V = json.load(io.open(os.path.join(DATA, 'videos.json'), encoding='utf-8'))
C = json.load(io.open(os.path.join(DATA, 'challenges.json'), encoding='utf-8'))
CATS, RES = R["categories"], R["resources"]
VIDS, ROUTES, TOPICS = V["videos"], V["routes"], V["topics"]
CHAL, SHOW = C["challenges"], C["showcase"]
by_slug = {r["slug"]: r for r in RES}
by_vid = {v["id"]: v for v in VIDS}
HERO_VIDEO = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260314_131748_f2ca2a28-fed7-44c8-b9a9-bd9acdd5ec31.mp4'
SITE = 'Luciano Musella'
YEAR = datetime.date.today().year
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_NE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
CHEV_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>'

def e(s):
    return html.escape(str(s or ''), quote=True)

def btn(label, href, kind='', icon=ARROW, track=None, props=None, attrs=''):
    t = f' data-track="{track}"' if track else ''
    p = f" data-track-props='{json.dumps(props, ensure_ascii=False)}'" if props else ''
    return f'<a class="btn {kind}" href="{href}"{t}{p} {attrs}><span class="btn__t">{e(label)}</span><span class="btn__ic">{icon}</span></a>'

def link_arrow(label, href, track=None):
    t = f' data-track="{track}"' if track else ''
    return f'<a class="link-arrow" href="{href}"{t}>{e(label)} {ARROW}</a>'

# ---------------------------------------------------------------- markdown mínimo
def inline(s):
    s = e(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = s.replace('\\*', '*').replace('\\_', '_')
    return s

def md_to_html(md, slug=''):
    lines = md.split('\n'); out = []; i = 0; code_i = 0
    def flush_list(items, ordered, todo=False):
        tag = 'ol' if ordered else 'ul'
        li = ''.join(f'<li>{("<input type=checkbox disabled> " if todo else "")}{inline(x)}</li>' for x in items)
        return f'<{tag}>{li}</{tag}>'
    while i < len(lines):
        raw = lines[i]; l = raw.strip()
        if not l:
            i += 1; continue
        if l.startswith('```'):
            lang = l[3:].strip(); buf = []; i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1; code_i += 1
            ind = min((len(x) - len(x.lstrip()) for x in buf if x.strip()), default=0)
            code = '\n'.join(x[ind:] for x in buf)
            out.append(f'<div class="codeblock"><div class="codeblock__bar"><span>{e(lang) or "texto"}</span><button class="copy" type="button" data-i="{code_i}">Copiar</button></div><pre>{e(code)}</pre></div>')
            continue
        if l.startswith(':::callout'):
            buf = []; i += 1
            while i < len(lines) and lines[i].strip() != ':::':
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<div class="callout">' + md_to_html('\n'.join(buf), slug) + '</div>'); continue
        if l.startswith(':::figure'):
            cap = l[len(':::figure'):].strip()
            if re.search(r'\.(png|jpe?g|gif|webp)$', cap, re.I) or cap.lower().startswith(('screenshot', 'captura', 'image')): cap = ''
            out.append(f'<div class="fig-ph"><b>Imagen del recurso original</b><span>{e(cap) or "Captura pendiente de migrar desde Notion"}</span></div>'); i += 1; continue
        if l.startswith(':::file'):
            out.append(f'<div class="fig-ph"><b>Archivo adjunto</b><span>{e(l[len(":::file"):].strip())} · se migrará con los assets</span></div>'); i += 1; continue
        if l.startswith(':::note'):
            out.append(f'<div class="fig-ph"><span>{e(l[len(":::note"):].strip())}</span></div>'); i += 1; continue
        if l.startswith(':::embed'):
            src = l[len(':::embed'):].strip(); m = re.search(r'(?:youtu\.be/|v=|embed/)([A-Za-z0-9_-]{11})', src)
            if m: out.append(f'<div class="embed"><div data-yt="{m.group(1)}" class="card__media" style="aspect-ratio:16/9;cursor:pointer"><img src="https://img.youtube.com/vi/{m.group(1)}/hqdefault.jpg" alt=""><div class="play"><span class="play__b">{PLAY}</span></div></div></div>')
            elif src.startswith('http'): out.append(f'<div class="fig-ph"><b>Enlace</b><a href="{e(src)}" target="_blank" rel="noopener">{e(src)}</a></div>')
            else: out.append('<div class="fig-ph"><b>Video adjunto del recurso original</b><span>Se migrará con los assets</span></div>')
            i += 1; continue
        if l == '---':
            out.append('<hr>'); i += 1; continue
        m = re.match(r'^(#{2,4})\s+(.*)', l)
        if m:
            n = len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i += 1; continue
        if l.startswith('> '):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('> '):
                buf.append(lines[i].strip()[2:]); i += 1
            out.append('<blockquote>' + ' '.join(inline(x) for x in buf) + '</blockquote>'); continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                r = lines[i].strip()
                if not re.match(r'^\|[\s\-|]+\|$', r): rows.append([c.strip() for c in r.strip('|').split('|')])
                i += 1
            if rows:
                th = ''.join(f'<th>{inline(c)}</th>' for c in rows[0])
                tb = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows[1:])
                out.append(f'<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>')
            continue
        if re.match(r'^(-|\d+\.)\s', l):
            items = []; ordered = l[0].isdigit(); todo = l.startswith('- [ ]')
            while i < len(lines) and re.match(r'^\s*(-|\d+\.)\s', lines[i]):
                t = re.sub(r'^\s*(-|\d+\.)\s+', '', lines[i]); t = re.sub(r'^\[ \]\s*', '', t)
                items.append(t); i += 1
            out.append(flush_list(items, ordered, todo)); continue
        # párrafo
        buf = [l]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(```|:::|#{2,4}\s|>\s|\||-\s|\d+\.\s|---$)', lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)

# ---------------------------------------------------------------- layout
NAV = [('Inicio', '/'), ('Tutoriales', '/tutoriales/'), ('Recursos', '/recursos/'), ('Retos', '/retos/'), ('Programa', '/programa/'), ('Agenda', '/agenda/')]

def layout(title, body, page='page', desc='', props=None, extra_head=''):
    links = ''.join(f'<li><a href="{h}">{n}</a></li>' for n, h in NAV)
    menu = ''.join(f'<a href="{h}">{n}<small>0{i + 1}</small></a>' for i, (n, h) in enumerate(NAV))
    pp = f" data-page-props='{json.dumps(props, ensure_ascii=False)}'" if props else ''
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | {SITE}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
{extra_head}
</head>
<body data-page="{page}"{pp}>
<a class="sr" href="#main">Ir al contenido</a>
<header class="nav" id="nav">
  <div class="nav__in">
    <a class="nav__brand" href="/">Luciano<span>.</span>Musella</a>
    <ul class="nav__links">{links}</ul>
    <div class="nav__cta">
      {btn('Agenda', '/agenda/', 'btn--ghost btn--sm', ARROW, 'agenda_click', {'from': 'nav'})}
      <button class="burger" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="menu" id="menu"><nav class="wrap"><div class="menu__list">{menu}</div><div class="menu__foot">{btn('Agenda una conversación', '/agenda/', 'btn--light', ARROW, 'agenda_click', {'from': 'menu'})}</div></nav></div>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap foot__in">
    <div><div class="foot__brand">Luciano Musella</div><p style="max-width:34ch;margin:12px 0 0">Aprende a construir con IA. Tutoriales, recursos y retos gratis; y un programa para llevarlo al trabajo.</p></div>
    <div><h6>Explora</h6><ul>{''.join(f'<li><a href="{h}">{n}</a></li>' for n, h in NAV[1:])}</ul></div>
    <div><h6>Canales</h6><ul><li><a href="https://www.youtube.com/@LucianoMusellaa" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://www.linkedin.com/in/luciano-parra-m" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="https://www.instagram.com/" target="_blank" rel="noopener">Instagram</a></li></ul></div>
  </div>
  <div class="wrap foot__legal"><span>© {YEAR} Luciano Musella</span><span>Preview · web-v2 · no es la versión final</span></div>
</footer>
<div class="preview-badge">Preview web-v2</div>
<script src="/assets/js/site.js" defer></script>
</body>
</html>'''

# ---------------------------------------------------------------- componentes
def video_card(v, i=0, small=False):
    return f'''<a class="card" href="/tutoriales/{v["slug"]}/" data-reveal style="--i:{i}" data-track="tutorial_click" data-track-props='{{"video_id":"{v["id"]}","from":"card"}}'>
  <div class="card__media"><img src="{v["thumb"]}" alt="" loading="lazy" onerror="this.src='https://img.youtube.com/vi/{v["id"]}/hqdefault.jpg'"><div class="play"><span class="play__b">{PLAY}</span></div><span class="dur">{v["duration_label"]}</span></div>
  <div class="card__body"><div class="card__meta"><span>{e(v["topic_label"])}</span></div><div class="card__title">{e(v["title"])}</div>
  <div class="card__foot"><span>{len(v["related_resources"])} recurso{'s' if len(v["related_resources"]) != 1 else ''} para practicar</span><span class="card__arrow">{ARROW}</span></div></div></a>'''

def vitem(v):
    return f'''<a class="vitem" href="/tutoriales/{v["slug"]}/" data-track="tutorial_click" data-track-props='{{"video_id":"{v["id"]}","from":"list"}}'>
  <div class="vitem__th"><img src="https://img.youtube.com/vi/{v["id"]}/mqdefault.jpg" alt="" loading="lazy"></div>
  <div><div class="vitem__t">{e(v["title"])}</div><div class="vitem__m">{e(v["topic_label"])} · {v["duration_label"]}</div></div></a>'''

def res_card(r, size='sm', i=0):
    cat = CATS[r["category"]]["name"]
    extra = ''
    if size == 'xl':
        extra = f'<div class="card__desc">{e(r["summary"])}</div>'
    elif size == 'md':
        extra = f'<div class="card__desc">{e(r["summary"][:140])}{"…" if len(r["summary"]) > 140 else ""}</div>'
    return f'''<a class="res res--{size}" href="/recursos/{r["slug"]}/" data-reveal style="--i:{i}" data-track="resource_click" data-track-props='{{"resource":"{r["slug"]}","from":"card"}}'>
  <div class="card__meta"><span class="res__type">{e(r["type_label"])}</span><span>· {e(cat)}</span></div>
  <div class="card__title">{e(r["title"])}</div>{extra}
  <div class="card__foot"><span>{r["read_min"]} min · {'con tutorial' if r["related_tutorials"] else 'lectura'}</span><span class="card__arrow">{ARROW}</span></div></a>'''

def row(cards, label=None):
    return f'''<div class="row"><div class="row__scroll">{''.join(cards)}</div></div>'''

def section(inner, theme='cream', cls='', id_=''):
    return f'<section class="sec sec--{theme} {cls}" data-bg="{theme}"{f" id={id_}" if id_ else ""}>{inner}</section>'

def head(eyebrow, title, lead='', cta=''):
    return f'''<div class="wrap sec__head"><div><span class="eyebrow eyebrow--dot" data-reveal>{e(eyebrow)}</span><h2 class="h2" data-reveal style="--i:1;margin-top:14px">{title}</h2></div>
  <div data-reveal style="--i:2;display:grid;gap:16px;justify-items:end">{f'<p class="lead">{lead}</p>' if lead else ''}{cta}</div></div>'''


def coll_item(r, i):
    n = "Hub" if r["slug"] == "houston-agentes-negocio" else f"0{i}"
    t = e(r["title"].replace("Houston AI: ", "").replace("Houston: ", ""))
    props = html.escape(json.dumps({"resource": r["slug"], "from": "collection"}), quote=True)
    return (f'<a class="coll__i" href="/recursos/{r["slug"]}/" data-track="resource_click" data-track-props="{props}">'
            f'<span class="coll__n">{n}</span><div><div class="coll__t">{t}</div><div class="coll__d">{e(r["summary"][:150])}</div></div>'
            f'<span class="card__arrow">{ARROW}</span></a>')

# ---------------------------------------------------------------- páginas
def page_home():
    feat = [v for v in VIDS if v["featured"]]
    main_v = by_vid["wpYDisTBlE8"]; sec_v = [v for v in feat if v["id"] != main_v["id"]][:4]
    featured_res = [by_slug[s] for s in ['skill-debrief-claude', '5-niveles-de-claude', 'roadmap-claude-5-dias', 'hermes', 'atajos-de-prompt-claude', 'notebooklm-presentaciones']]
    ch = CHAL[0]
    hero = f'''<section class="hero" id="hero">
  <div class="hero__media"><div class="hero__poster"></div><video muted loop playsinline autoplay preload="metadata" poster="/assets/img/hero-poster.jpg" aria-hidden="true"><source src="{HERO_VIDEO}" type="video/mp4"></video></div>
  <div class="hero__in">
    <div>
      <h1 class="display display--xl"><span class="hero__line"><span>Construye con IA.</span></span><span class="hero__line"><span><em class="serif">Aprende haciendo.</em></span></span></h1>
      <p class="hero__sub">Tutoriales, recursos y retos gratis para profesionales que quieren usar la IA de verdad en su trabajo. Y cuando quieras ir más lejos, un programa para construirlo con Luciano.</p>
      <div class="hero__actions actions">{btn('Empieza gratis', '#empezar', 'btn--light')}{btn('Ver tutoriales', '/tutoriales/', 'btn--ghost', ARROW, 'tutorial_click', {'from': 'hero'})}</div>
    </div>
    <div class="hero__aside"><b>{len(VIDS)} tutoriales</b> en YouTube<b>{len(RES)}+ recursos</b> abiertos, sin registro<b>1 reto</b> para hacerlo tú</div>
  </div>
  <div class="hero__cue" aria-hidden="true"></div>
</section>'''
    routes = ''.join(f'''<a class="route" href="/tutoriales/?ruta={r["slug"]}" data-reveal style="--i:{i}" data-track="related_content_click" data-track-props='{{"route":"{r["slug"]}"}}'>
      <span class="route__n">0{i + 1}</span>
      <div><div class="route__t">{e(r["title"])}</div><p class="route__d">{e(r["desc"])}</p>
        <div class="route__items">{''.join(f'<span>▶ {e(by_vid[v]["title"][:38])}…</span>' for v in r["videos"][:2])}{''.join(f'<span>◆ {e(by_slug[s]["title"][:34])}…</span>' for s in r["resources"][:1])}</div></div>
      <span class="card__arrow">{ARROW}</span></a>''' for i, r in enumerate(ROUTES))
    start = section(head('¿Por dónde empiezo?', 'Cuatro rutas. Elige la tuya <em class="serif tint">y empieza hoy.</em>', 'Cada ruta combina tres tutoriales y recursos para ponerlos en práctica. Sin registro.') + f'<div class="wrap routes">{routes}</div>', 'cream', id_='empezar')
    tut = section(head('Tutoriales', 'Ver cómo se construye, <em class="serif tint">paso a paso.</em>', f'{len(VIDS)} videos del canal, organizados por tema. Cada uno enlaza a los recursos que usa.', link_arrow('Todos los tutoriales', '/tutoriales/')) + f'''<div class="wrap vgrid">
      <a class="vfeature" href="/tutoriales/{main_v["slug"]}/" data-reveal data-track="tutorial_click" data-track-props='{{"video_id":"{main_v["id"]}","from":"home_feature"}}'>
        <img src="{main_v["thumb"]}" alt="" loading="lazy"><div class="play"><span class="play__b">{PLAY}</span></div>
        <div class="vfeature__body"><div class="card__meta" style="color:rgba(255,255,255,.6)"><span>{e(main_v["topic_label"])}</span><span>· {main_v["duration_label"]}</span><span>· el más visto</span></div><div class="card__title">{e(main_v["title"])}</div>
        <div class="card__desc" style="color:rgba(255,255,255,.75)">{len(main_v["related_resources"])} recursos para ponerlo en práctica</div></div></a>
      <div class="vlist" data-reveal style="--i:1">{''.join(vitem(v) for v in sec_v)}<div style="padding:10px 8px">{link_arrow('Explorar por tema', '/tutoriales/')}</div></div></div>''', 'paper')
    res = section(head('Recursos para construir', 'No son videos. <em class="serif tint">Son piezas para usar hoy.</em>', 'Guías, prompts, configuraciones y sistemas. Abiertos, completos, sin dejar el email.', link_arrow('Toda la biblioteca', '/recursos/')) + f'''<div class="wrap rgrid">{res_card(featured_res[0], 'xl', 0)}{res_card(featured_res[1], 'md', 1)}{res_card(featured_res[2], 'md', 2)}{res_card(featured_res[3], 'sm', 3)}{res_card(featured_res[4], 'sm', 4)}{res_card(featured_res[5], 'sm', 5)}</div>
      <div class="wrap mt-3 pill-nav" data-reveal>{''.join(f'<a class="chip" href="/recursos/#{k}">{e(c["name"])}</a>' for k, c in CATS.items())}</div>''', 'sand')
    days = ''.join(f'<div class="day"><span class="day__n">Día {d["n"]}</span><div><div class="day__t">{e(d["title"])}</div><div class="day__d">{e(d["text"])}</div></div></div>' for d in ch["days"])
    reto = section(f'''<div class="wrap challenge">
      <div data-reveal><span class="eyebrow eyebrow--dot" style="color:var(--on-dark-2)">Retos · ahora hazlo tú</span>
        <h2 class="h2" style="margin-top:14px">La IA no se aprende viendo. <em class="serif tint">Se aprende construyendo.</em></h2>
        <p class="lead" style="color:var(--on-dark-2);margin-top:18px">{e(ch["summary"])} Al terminar: {e(ch["result"])}</p>
        <div class="facts"><div class="fact"><b>{e(ch["duration"].split('·')[0].strip())}</b><span>Duración</span></div><div class="fact"><b>20 min</b><span>al día</span></div><div class="fact"><b>{e(ch["level"].split(' a ')[0])}</b><span>Nivel</span></div></div>
        <div class="actions">{btn('Reservar mi lugar', f'/retos/{ch["slug"]}/#registro', 'btn--light', ARROW, 'challenge_click', {'challenge': ch["slug"], 'from': 'home'})}{link_arrow('Cómo funciona', f'/retos/{ch["slug"]}/')}</div></div>
      <div class="days" data-reveal style="--i:1">{days}</div></div>''', 'ink')
    show = ''.join((f'''<a class="show__i" href="/tutoriales/{by_vid[s["ref"]]["slug"]}/" data-reveal style="--i:{i}" data-track="tutorial_click" data-track-props='{{"video_id":"{s["ref"]}","from":"showcase"}}'><img src="{by_vid[s["ref"]]["thumb"]}" alt="" loading="lazy"><div class="show__b"><div class="card__meta"><span>{e(s["tag"])}</span><span>· video</span></div><div class="card__title">{e(s["title"])}</div></div></a>''' if s["kind"] == 'video' else
                    f'''<a class="show__i show__i--res" href="/recursos/{s["ref"]}/" data-reveal style="--i:{i}" data-track="resource_click" data-track-props='{{"resource":"{s["ref"]}","from":"showcase"}}'><div class="show__b"><div class="card__meta" style="color:rgba(255,255,255,.7)"><span>{e(s["tag"])}</span><span>· recurso</span></div><div class="card__title">{e(s["title"])}</div></div></a>''') for i, s in enumerate(SHOW))
    showcase = section(head('Cosas reales que puedes construir', 'Esto no es teoría. <em class="serif tint">Se construyó de verdad.</em>', 'Cada pieza sale de un video o un recurso donde Luciano lo construye delante de ti.') + f'<div class="wrap show">{show}</div>', 'paper')
    program = section(f'''<div class="wrap split split--wide">
      <div data-reveal><span class="eyebrow eyebrow--dot">Programa</span><h2 class="h2" style="margin-top:14px">¿Quieres acelerar esto <em class="serif tint">con Luciano?</em></h2>
        <p class="lead" style="margin-top:18px">Un programa práctico para profesionales, gerentes y founders: sales construyendo tus propios agentes y soluciones, no viendo horas de contenido.</p>
        <div class="actions mt-3">{btn('Conocer el programa', '/programa/', '', ARROW, 'program_click', {'from': 'home'})}{link_arrow('Hablar con Luciano', '/agenda/', 'agenda_click')}</div></div>
      <ul class="list list--check" data-reveal style="--i:1"><li>Qué vas a construir desde la primera semana</li><li>Para quién es (y para quién no)</li><li>Metodología: aprender resolviendo un problema real de tu trabajo</li><li>Qué incluye, cómo se acompaña y cómo se empieza</li></ul></div>''', 'cream')
    luciano = section(f'''<div class="wrap split">
      <div class="portrait" data-reveal><img src="/aprende/img/luciano-hero.jpg" alt="Luciano Musella"><span class="portrait__tag">Foto provisional</span></div>
      <div data-reveal style="--i:1"><span class="eyebrow eyebrow--dot">Luciano</span><h2 class="h2" style="margin-top:14px">Construye con IA todos los días. <em class="serif tint">Y lo enseña.</em></h2>
        <p class="lead" style="margin-top:18px">Ayuda a empresas y profesionales a convertirse en AI-natives: instala los sistemas, entrena al equipo y, al final, la IA no es algo que "usan", es cómo operan.</p>
        <div class="stats"><div class="stat"><b>{len(VIDS)}</b><span>tutoriales publicados</span></div><div class="stat"><b>55</b><span>recursos creados</span></div><div class="stat"><b><span class="ph">dato pendiente</span></b><span>personas formadas</span></div></div>
        <p class="muted mt-2" style="font-size:14px">Las cifras de estudiantes, empresas y resultados se mostrarán solo cuando Luciano las confirme.</p></div></div>''', 'sand')
    agenda = section(f'''<div class="wrap" style="max-width:900px;text-align:center"><span class="eyebrow eyebrow--dot" style="color:var(--on-dark-2);justify-content:center" data-reveal>Agenda</span>
      <h2 class="display display--l" style="color:#fff;margin:18px auto 22px;max-width:16ch" data-reveal>Antes de hablar de un curso, quiero entender <em class="serif tint">qué necesitas.</em></h2>
      <p class="lead" style="color:var(--on-dark-2);margin:0 auto 32px" data-reveal>Una conversación corta para ver si el programa encaja contigo. Sin presión.</p>
      <div class="actions" style="justify-content:center" data-reveal>{btn('Agendar una conversación', '/agenda/', 'btn--accent', ARROW, 'agenda_click', {'from': 'home_footer'})}</div></div>''', 'ink')
    return layout('Aprende a construir con IA', hero + start + tut + res + reto + showcase + program + luciano + agenda, 'home', 'Tutoriales, recursos y retos gratis para construir con IA. Y un programa para profesionales que quieren ir más lejos.')

def page_tutoriales():
    ruta_cards = ''.join(f'''<div class="route" data-reveal style="--i:{i}" id="ruta-{r["slug"]}"><span class="route__n">0{i + 1}</span><div><div class="route__t">{e(r["title"])}</div><p class="route__d">{e(r["desc"])}</p>
      <div class="vlist" style="margin-top:12px">{''.join(vitem(by_vid[v]) for v in r["videos"])}</div>
      <div class="route__items" style="margin-top:14px">{''.join(f'<a class="chip chip--tone" href="/recursos/{s}/">◆ {e(by_slug[s]["title"][:40])}</a>' for s in r["resources"])}</div></div></div>''' for i, r in enumerate(ROUTES))
    topics_html = ''
    for k, name in TOPICS.items():
        vs = [v for v in VIDS if v["topic"] == k]
        if not vs: continue
        topics_html += f'<div class="cat-head" id="{k}"><h3 class="h3">{e(name)}</h3><span class="muted">{len(vs)} video{"s" if len(vs) != 1 else ""}</span></div><div class="row"><div class="row__scroll">{"".join(video_card(v, i) for i, v in enumerate(vs))}</div></div>'
    body = f'''<section class="hero hero--short" data-bg="ink"><div class="hero__media"><div class="hero__poster"></div></div><div class="hero__in"><div><span class="eyebrow" style="color:var(--on-dark-2)">Tutoriales</span>
      <h1 class="display display--l" style="margin-top:14px"><span class="hero__line"><span>Ver cómo se construye,</span></span><span class="hero__line"><span><em class="serif tint">paso a paso.</em></span></span></h1>
      <p class="hero__sub">{len(VIDS)} videos del canal de YouTube, organizados por tema y por ruta. Cada tutorial enlaza a los recursos que usa.</p>
      <div class="hero__actions pill-nav">{''.join(f'<a class="chip" href="#{k}" style="color:#fff;border-color:rgba(255,255,255,.3)">{e(n)}</a>' for k, n in TOPICS.items())}</div></div></div></section>
    {section(head('Rutas de aprendizaje', 'Un orden pensado, <em class="serif tint">no un feed.</em>', 'Tres videos y tres recursos por ruta. Empieza por la que se parezca a tu momento.') + f'<div class="wrap routes">{ruta_cards}</div>', 'cream')}
    {section(head('Por tema', 'Todos los tutoriales', 'Desliza cada fila. Los más vistos primero.') + f'<div class="wrap">{topics_html}</div>', 'paper')}'''
    return layout('Tutoriales', body, 'tutorials', 'Videos organizados por tema y ruta de aprendizaje.')

def page_video(v):
    rel = [by_slug[s] for s in v["related_resources"] if s in by_slug]
    more = [x for x in VIDS if x["topic"] == v["topic"] and x["id"] != v["id"]][:3]
    rel_html = ''.join(f'''<a class="res res--sm" href="/recursos/{r["slug"]}/" data-reveal style="--i:{i}" data-track="resource_click" data-track-props='{{"resource":"{r["slug"]}","from":"tutorial"}}'><div class="card__meta"><span class="res__type">{e(r["type_label"])}</span></div><div class="card__title">{e(r["title"])}</div><div class="card__desc">{e(r["summary"][:120])}…</div><div class="card__foot"><span>{r["read_min"]} min</span><span class="card__arrow">{ARROW}</span></div></a>''' for i, r in enumerate(rel))
    body = f'''<section class="sec sec--ink" data-bg="ink" style="padding-top:calc(var(--nav-h) + 40px)"><div class="wrap">
      <div class="crumbs" style="color:var(--on-dark-3)"><a href="/tutoriales/">Tutoriales</a><span>/</span><a href="/tutoriales/#{v["topic"]}">{e(v["topic_label"])}</a></div>
      <h1 class="display display--l" data-reveal style="max-width:22ch">{e(v["title"])}</h1>
      <div class="ahead__meta" style="color:var(--on-dark-3)"><span>{v["duration_label"]}</span><span class="dot"></span><span>{e(v["topic_label"])}</span><span class="dot"></span><a href="https://www.youtube.com/watch?v={v["id"]}" target="_blank" rel="noopener" style="color:var(--on-dark-2)">Ver en YouTube ↗</a></div>
      <div class="shell mt-3" data-reveal style="--i:1"><div class="shell__in"><div class="card__media" data-yt="{v["id"]}" data-title="{e(v["title"])}" data-video-view="{v["id"]}" style="cursor:pointer;aspect-ratio:16/9"><img src="{v["thumb"]}" alt="" onerror="this.src='https://img.youtube.com/vi/{v["id"]}/hqdefault.jpg'"><div class="play"><span class="play__b" style="width:84px;height:84px">{PLAY}</span></div><span class="dur">{v["duration_label"]}</span></div></div></div>
    </div></section>
    {section(head('Ponlo en práctica', 'Recursos para <em class="serif tint">hacerlo tú.</em>', 'Lo que necesitas para aplicar lo que viste: prompts, guías y configuraciones, abiertos.') + (f'<div class="wrap grid-3">{rel_html}</div>' if rel else '<div class="wrap"><p class="lead">Este tutorial todavía no tiene recursos asociados. <a href="/recursos/">Explora la biblioteca →</a></p></div>'), 'cream')}
    {section(head('Sigue aprendiendo', 'Más de <em class="serif tint">' + e(v["topic_label"]) + '</em>') + f'<div class="wrap grid-3">{"".join(video_card(x, i) for i, x in enumerate(more))}</div>', 'paper') if more else ''}'''
    return layout(v["title"], body, 'tutorial', v["title"], {'video_id': v["id"], 'topic': v["topic"]})

def page_recursos():
    houston = [r for r in RES if r["collection"] == 'houston']
    feat = [r for r in RES if r["featured"]]
    cats_html = ''
    for k, c in CATS.items():
        rs = [r for r in RES if r["category"] == k and r["collection"] is None]
        if not rs: continue
        cards = ''.join(res_card(r, 'md' if i == 0 else 'sm', i) for i, r in enumerate(rs))
        cats_html += f'<div class="cat-head" id="{k}"><div><h3 class="h3">{e(c["tag"])}</h3><p class="muted" style="margin:6px 0 0">{e(c["desc"])}</p></div><span class="muted">{len(rs)} recurso{"s" if len(rs) != 1 else ""}</span></div><div class="grid-3">{cards}</div>'
    _s1 = section(f'''<div class="wrap coll" id="houston"><div data-reveal><span class="eyebrow eyebrow--dot" style="color:var(--on-dark-2)">Serie · {len(houston)} recursos</span><h2 class="h2" style="margin-top:14px">Houston: agentes para tu negocio, <em class="serif tint">sin programar.</em></h2></div>
      <p class="lead" data-reveal style="--i:1;color:var(--on-dark-2)">Una colección de agentes listos para copiar: cada uno resuelve una tarea concreta de un equipo comercial u operativo. Empieza por el hub y sigue por el que te duela más.</p></div>
      <div class="wrap coll__list" data-reveal>{"".join(coll_item(r, i) for i, r in enumerate(houston))}</div>''', 'ink')
    body = f'''<section class="hero hero--short" data-bg="ink"><div class="hero__media"><div class="hero__poster"></div></div><div class="hero__in"><div><span class="eyebrow" style="color:var(--on-dark-2)">Recursos</span>
      <h1 class="display display--l" style="margin-top:14px"><span class="hero__line"><span>Piezas para usar hoy.</span></span><span class="hero__line"><span><em class="serif tint">Abiertas, completas, sin registro.</em></span></span></h1>
      <p class="hero__sub">Guías, prompts, configuraciones y sistemas que Luciano usa de verdad. Cada recurso enlaza al tutorial donde se explica.</p>
      <div class="hero__actions pill-nav">{''.join(f'<a class="chip" href="#{k}" style="color:#fff;border-color:rgba(255,255,255,.3)">{e(c["name"])}</a>' for k, c in CATS.items())}<a class="chip" href="#houston" style="color:#fff;border-color:rgba(255,255,255,.3)">Serie Houston</a></div></div></div></section>
    {section(head('Destacados', 'Por dónde <em class="serif tint">empezar.</em>') + f'<div class="wrap rgrid">{res_card(feat[0], "xl", 0)}{res_card(feat[1], "md", 1)}{res_card(feat[2], "md", 2)}{res_card(feat[3], "sm", 3)}{res_card(feat[4], "sm", 4)}{res_card(feat[5], "sm", 5)}</div>', 'cream')}
    {section(f'<div class="wrap">{cats_html}</div>', 'paper')}
    {_s1}'''
    return layout('Recursos', body, 'resources', 'Biblioteca de recursos prácticos, abiertos y sin registro.')

def page_resource(r):
    md = io.open(os.path.join(DATA, 'recursos', r["slug"] + '.md'), encoding='utf-8').read()
    body_html = md_to_html(md, r["slug"])
    cat = CATS[r["category"]]
    tuts = [by_vid[v] for v in r["related_tutorials"] if v in by_vid]
    rels = [by_slug[s] for s in r["related_resources"] if s in by_slug]
    tut_html = ''.join(f'''<a class="tv" href="/tutoriales/{v["slug"]}/" data-track="tutorial_click" data-track-props='{{"video_id":"{v["id"]}","from":"resource"}}'><div class="tv__th"><img src="https://img.youtube.com/vi/{v["id"]}/mqdefault.jpg" alt="" loading="lazy"></div><div><div class="tv__t">{e(v["title"])}</div><div class="tv__m">{v["duration_label"]} · YouTube</div></div></a>''' for v in tuts)
    rel_html = ''.join(f'''<a href="/recursos/{x["slug"]}/" data-track="related_resource_click" data-track-props='{{"from":"{r["slug"]}","to":"{x["slug"]}"}}'><span class="card__arrow">{ARROW}</span><span>{e(x["title"])}</span></a>''' for x in rels)
    coll_html = ''
    if r["collection"]:
        others = [x for x in RES if x["collection"] == r["collection"] and x["slug"] != r["slug"]]
        items = "".join(f'<a href="/recursos/{x["slug"]}/"><span class="card__arrow">{ARROW}</span><span>{e(x["title"].replace("Houston AI: ", "").replace("Houston: ", ""))}</span></a>' for x in others[:7])
        coll_html = f'<div class="aside__box"><h5>Serie Houston</h5><ul class="aside__list">{items}</ul></div>'
    boxes = ''
    if r["ideal_for"] or r["includes"]:
        boxes = '<div class="boxes">' + (f'<div class="box"><h5>Ideal para</h5><ul>{"".join(f"<li>{inline(x)}</li>" for x in r["ideal_for"])}</ul></div>' if r["ideal_for"] else '') + (f'<div class="box"><h5>Qué obtienes</h5><ul>{"".join(f"<li>{inline(x)}</li>" for x in r["includes"])}</ul></div>' if r["includes"] else '') + '</div>'
    elif r["what_you_get"]:
        boxes = f'<div class="boxes"><div class="box"><h5>Qué obtienes</h5><ul>{"".join(f"<li>{e(x)}</li>" for x in r["what_you_get"])}</ul></div></div>'
    body = f'''<div class="progress" aria-hidden="true"></div>
    <section class="ahead sec--cream" data-bg="cream"><div class="wrap">
      <div class="crumbs"><a href="/recursos/">Recursos</a><span>/</span><a href="/recursos/#{r["category"]}">{e(cat["name"])}</a>{f'<span>/</span><a href="/recursos/#houston">Serie Houston</a>' if r["collection"] else ''}</div>
      <span class="res__type" data-reveal>{e(r["type_label"])}</span>
      <h1 class="display display--l" data-reveal style="--i:1;margin-top:14px">{e(r["title"])}</h1>
      <p class="lead" data-reveal style="--i:2;margin-top:20px">{e(r["summary"])}</p>
      <div class="ahead__meta" data-reveal style="--i:3"><span>{r["read_min"]} min de lectura</span><span class="dot"></span><span>{e(cat["tag"])}</span>{''.join(f'<span class="dot"></span><span>{e(t)}</span>' for t in r["tools"][:4])}</div>
      {boxes}
    </div></section>
    <section class="sec sec--paper sec--tight" data-bg="paper"><div class="wrap article">
      <article class="prose" data-resource="{r["slug"]}">{body_html}
        <hr><p class="muted" style="font-size:14px">Recurso migrado desde Notion para esta preview. <a href="{r["notion_url"]}" target="_blank" rel="noopener">Ver original ↗</a></p></article>
      <aside class="aside">
        {f'<div class="aside__box"><h5>Aprende cómo funciona</h5>{tut_html}</div>' if tuts else ''}
        {coll_html}
        {f'<div class="aside__box"><h5>Recursos relacionados</h5><ul class="aside__list">{rel_html}</ul></div>' if rels else ''}
        <div class="aside__box" style="background:var(--ink);color:#fff;border-color:transparent"><h5 style="color:var(--on-dark-3)">Siguiente paso</h5><p style="margin:0;font-family:var(--serif);font-size:20px;line-height:1.2">¿Quieres hacerlo guiado, en 5 días?</p>{btn('Ver el reto', '/retos/claude-en-5-dias/', 'btn--light btn--sm', ARROW, 'challenge_click', {'from': r["slug"]})}</div>
      </aside></div></section>
    {section(head('Seguir construyendo', 'Recursos <em class="serif tint">relacionados</em>') + f'<div class="wrap grid-3">{"".join(res_card(x, "sm", i) for i, x in enumerate(rels))}</div>', 'cream') if rels else ''}'''
    return layout(r["title"], body, 'resource', r["summary"], {'resource': r["slug"], 'category': r["category"], 'type': r["type"]})

def page_retos():
    ch = CHAL[0]; soon = CHAL[1:]
    _s1 = section(f'''<div class="wrap challenge"><div data-reveal><span class="eyebrow eyebrow--dot">Reto activo · piloto</span><h2 class="h2" style="margin-top:14px">{e(ch["title"])}</h2><p class="lead" style="margin-top:16px">{e(ch["summary"])}</p>
      <div class="facts"><div class="fact"><b>5 días</b><span style="color:var(--ink-3)">Duración</span></div><div class="fact"><b>20 min</b><span style="color:var(--ink-3)">al día</span></div><div class="fact"><b>{e(ch["level"].split(' a ')[0])}</b><span style="color:var(--ink-3)">Nivel</span></div></div>
      <p><strong>Resultado:</strong> {e(ch["result"])}</p><div class="actions mt-2">{btn('Reservar mi lugar', f'/retos/{ch["slug"]}/#registro', '', ARROW, 'challenge_click', {'challenge': ch["slug"], 'from': 'retos_index'})}{link_arrow('Ver el día a día', f'/retos/{ch["slug"]}/')}</div></div>
      <div class="shell" data-reveal style="--i:1"><div class="shell__in" style="padding:26px">{''.join(f'<div class="day" style="border-color:var(--line)"><span class="day__n">Día {d["n"]}</span><div><div class="day__t">{e(d["title"])}</div><div class="day__d" style="color:var(--ink-2)">{e(d["text"])}</div></div></div>' for d in ch["days"])}</div></div></div>
      <div class="wrap soon">{''.join(f'<div class="soon__i" style="border-color:var(--line-strong);color:var(--ink-2)"><span class="eyebrow">Próximamente</span><b style="color:var(--ink)">{e(s["title"])}</b><span>{e(s["duration"])} · {e(s["level"])} · {e(s["result"])}</span></div>' for s in soon)}</div>''', 'cream')
    body = f'''<section class="hero hero--short" data-bg="ink"><div class="hero__media"><div class="hero__poster"></div></div><div class="hero__in"><div><span class="eyebrow" style="color:var(--on-dark-2)">Retos</span>
      <h1 class="display display--l" style="margin-top:14px"><span class="hero__line"><span>Ahora hazlo tú.</span></span><span class="hero__line"><span><em class="serif tint">Guiado, en días.</em></span></span></h1>
      <p class="hero__sub">Los retos son experiencias estructuradas: cada día una etapa, un material y un resultado. Aquí sí te pedimos registro, para enviarte cada etapa y guardar tu progreso.</p></div></div></section>
    {_s1}'''
    return layout('Retos', body, 'challenges', 'Experiencias guiadas de varios días para construir con IA.')

def page_reto(ch):
    days = ''.join(f'''<div class="day"><span class="day__n">Día {d["n"]}</span><div><div class="day__t">{e(d["title"])}</div><div class="day__d">{e(d["text"])}</div>
      <div class="pill-nav" style="margin-top:8px">{f'<a class="chip" href="/recursos/{d["resource"]}/" style="color:#fff;border-color:rgba(255,255,255,.25)">◆ {e(by_slug[d["resource"]]["title"][:36])}…</a>' if d.get('resource') else ''}{f'<a class="chip" href="/tutoriales/{by_vid[d["video"]]["slug"]}/" style="color:#fff;border-color:rgba(255,255,255,.25)">▶ {e(by_vid[d["video"]]["title"][:36])}…</a>' if d.get('video') else ''}</div></div></div>''' for d in ch["days"])
    form = f'''<form class="form" data-proto="{ch["slug"]}" novalidate>
      <div class="form__fields">
        <div class="form__row"><div class="field"><label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" required autocomplete="given-name"><span class="field__err">Escribe tu nombre</span></div>
        <div class="field"><label for="f-apellido">Apellido</label><input id="f-apellido" name="apellido" required autocomplete="family-name"><span class="field__err">Escribe tu apellido</span></div></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email" placeholder="Para enviarte cada etapa"><span class="field__err">Revisa el email</span></div>
        <div class="field"><label for="f-wa">WhatsApp</label><input id="f-wa" name="whatsapp" type="tel" required autocomplete="tel" placeholder="+57 300 000 0000"><span class="field__err">Necesitamos tu WhatsApp para los recordatorios</span></div>
        <div class="form__row"><div class="field"><label for="f-rol">Rol</label><select id="f-rol" name="rol" required><option value="">Elige</option><option>Ejecutivo / directivo</option><option>Manager</option><option>Founder</option><option>Profesional independiente</option><option>Otro</option></select><span class="field__err">Elige tu rol</span></div>
        <div class="field"><label for="f-empresa">Empresa (opcional)</label><input id="f-empresa" name="empresa" autocomplete="organization"></div></div>
        <div class="field"><label for="f-obj">¿Qué quieres lograr con Claude?</label><select id="f-obj" name="objetivo" required><option value="">Elige</option><option>Ser más productivo en mi trabajo</option><option>Automatizar tareas de mi equipo</option><option>Construir agentes y sistemas</option><option>Entender qué puede hacer por mi negocio</option></select><span class="field__err">Elige una opción</span></div>
        <label class="check"><input type="checkbox" required name="consent"><span>Acepto recibir las etapas del reto por email y WhatsApp. Puedo salir cuando quiera.</span></label>
        <div class="actions mt-1"><button class="btn btn--accent" type="submit"><span class="btn__t">Reservar mi lugar</span><span class="btn__ic">{ARROW}</span></button><span class="muted" style="font-size:13px">Prototipo: no se guarda nada todavía.</span></div>
      </div>
      <div class="form__ok"><h3 class="h3">¡Listo! Guardamos tu lugar.</h3><p style="margin:10px 0 0;color:var(--ink-2)">En la versión real recibirías ahora el día 1 por email y WhatsApp. Mientras tanto, empieza por el recurso del día 1.</p><div class="actions mt-2">{btn('Ir al día 1', f'/recursos/{ch["days"][0]["resource"]}/', 'btn--sm')}</div></div>
    </form>'''
    _s1 = section(f'''<div class="wrap split split--wide"><div data-reveal><span class="eyebrow eyebrow--dot">Qué aprenderás</span><h2 class="h2" style="margin-top:14px">Un día, una pieza. <em class="serif tint">Al final, un sistema.</em></h2>
      <p class="lead" style="margin-top:16px">{e(ch["result"])}</p>
      <div class="facts"><div class="fact"><b>5 días</b><span style="color:var(--ink-3)">Duración</span></div><div class="fact"><b>20 min</b><span style="color:var(--ink-3)">al día</span></div><div class="fact"><b>{e(ch["level"].split(' a ')[0])}</b><span style="color:var(--ink-3)">Nivel</span></div><div class="fact"><b>Email + WA</b><span style="color:var(--ink-3)">Cada etapa</span></div></div></div>
      <ul class="list list--check" data-reveal style="--i:1"><li>Cada día recibes la etapa, el recurso y el video que necesitas</li><li>Construyes sobre lo del día anterior: nada se queda en teoría</li><li>Guardamos tu progreso y te recordamos si te quedas atrás</li><li>Al terminar, decides si sigues solo, con la comunidad o con el programa</li></ul></div>''', 'cream')
    _s2 = section(f'''<div class="wrap split" id="registro"><div data-reveal><span class="eyebrow eyebrow--dot">Registro</span><h2 class="h2" style="margin-top:14px">Reserva tu lugar.</h2><p class="lead" style="margin-top:16px">Te pedimos estos datos para enviarte cada etapa, recordarte y guardar tu progreso. Nada más.</p>
      <ul class="list mt-3"><li>Un correo y un WhatsApp por día, cinco días</li><li>Los materiales quedan abiertos para siempre</li><li>Sin spam. Puedes salir con un clic</li></ul></div>
      <div class="shell" data-reveal style="--i:1"><div class="shell__in" style="padding:26px">{form}</div></div></div>''', 'paper')
    body = f'''<section class="hero hero--short" data-bg="ink"><div class="hero__media"><div class="hero__poster"></div></div><div class="hero__in"><div><span class="eyebrow" style="color:var(--on-dark-2)">Reto · piloto</span>
      <h1 class="display display--xl" style="margin-top:14px"><span class="hero__line"><span>Claude en</span></span><span class="hero__line"><span><em class="serif tint">5 días.</em></span></span></h1>
      <p class="hero__sub">{e(ch["summary"])}</p>
      <div class="hero__actions actions">{btn('Reservar mi lugar', '#registro', 'btn--light', ARROW, 'challenge_click', {'challenge': ch["slug"], 'from': 'reto_hero'})}<span class="ph">Placeholder realista · contenido por confirmar</span></div></div></div></section>
    {_s1}
    {section(head('El día a día', 'Cinco etapas, <em class="serif tint">cinco cosas construidas.</em>') + f'<div class="wrap days" style="max-width:900px">{days}</div>', 'ink')}
    {_s2}'''
    return layout(ch["title"], body, 'challenge', ch["summary"], {'challenge': ch["slug"]})

def page_programa():
    _s1 = section(f'''<div class="wrap split split--wide" id="como"><div data-reveal><span class="eyebrow eyebrow--dot">Qué vas a poder construir</span><h2 class="h2" style="margin-top:14px">Sales con sistemas <em class="serif tint">funcionando en tu trabajo.</em></h2></div>
      <ul class="list list--check" data-reveal style="--i:1"><li>Agentes que ejecutan tareas reales: correo, agenda, seguimiento, reportes</li><li>Automatizaciones de tus procesos repetitivos, conectadas a tus herramientas</li><li>Skills y configuraciones de Claude hechas para tu rol y tu empresa</li><li>Un criterio propio para decidir qué automatizar y qué no</li></ul></div>''', 'cream')
    _s2 = section(f'''<div class="wrap grid-3">
      <div class="shell" data-reveal><div class="shell__in" style="padding:28px"><span class="eyebrow eyebrow--dot">Para quién</span><h3 class="h3" style="margin:14px 0 10px">Si ya usas IA y quieres ir más allá</h3><p style="color:var(--ink-2);margin:0">Directivos, managers, founders y profesionales que quieren aplicar IA en su trabajo, no verla desde afuera.</p></div></div>
      <div class="shell" data-reveal style="--i:1"><div class="shell__in" style="padding:28px"><span class="eyebrow eyebrow--dot">Metodología</span><h3 class="h3" style="margin:14px 0 10px">Aprender resolviendo un problema tuyo</h3><p style="color:var(--ink-2);margin:0">Primero vemos qué quieres aprender o resolver, y empezamos desde ahí. Lo que aprendes lo vas usando mientras lo construyes.</p></div></div>
      <div class="shell" data-reveal style="--i:2"><div class="shell__in" style="padding:28px"><span class="eyebrow eyebrow--dot">Qué incluye</span><h3 class="h3" style="margin:14px 0 10px">Acompañamiento, no solo contenido</h3><p style="color:var(--ink-2);margin:0">Sesiones con Luciano, materiales y recursos, comunidad, y un plan concreto para tu caso. <span class="ph">detalle por confirmar</span></p></div></div></div>''', 'paper')
    _s3 = section(f'''<div class="wrap split"><div data-reveal><span class="eyebrow eyebrow--dot">Prueba</span><h2 class="h2" style="margin-top:14px">Lo que dicen quienes ya pasaron por aquí</h2><p class="lead" style="margin-top:14px">Esta sección mostrará testimonios reales cuando Luciano los comparta. No se inventan.</p></div>
      <div class="shell" data-reveal style="--i:1"><div class="shell__in" style="padding:32px;display:grid;gap:12px"><span class="ph">Testimonio pendiente</span><p class="h3" style="color:var(--ink-3)">“…”</p><span class="muted">Nombre · cargo · empresa</span></div></div></div>''', 'sand')
    _s4 = section(f'''<div class="wrap center" style="max-width:820px"><h2 class="display display--l" style="color:#fff" data-reveal>¿Hablamos?</h2><p class="lead" style="color:var(--on-dark-2);margin:18px auto 30px" data-reveal>Una conversación corta para ver si encaja. Sin presión.</p><div class="actions" style="justify-content:center" data-reveal>{btn('Agendar una conversación', '/agenda/', 'btn--accent', ARROW, 'agenda_click', {'from': 'programa_footer'})}</div></div>''', 'ink')
    _faq = section(head('Preguntas', 'Lo que la mayoría quiere saber <em class="serif tint">antes de entrar.</em>') + '''<div class="wrap wrap--narrow faq">
      <details><summary>¿Necesito saber programar?</summary><p>No. El programa está pensado para profesionales, no para desarrolladores. Se construye con herramientas de IA y criterio, no con código desde cero.</p></details>
      <details><summary>¿Cuánto tiempo a la semana?</summary><p>Lo define contigo Luciano según tu caso. La idea es que lo que hagas dentro del programa sea trabajo real tuyo, no tarea extra.</p></details>
      <details><summary>Ya intenté con un curso de IA y lo dejé. ¿Esto es distinto?</summary><p>Sí. Justamente por eso no empiezas viendo horas de contenido. Primero vemos qué quieres resolver en tu trabajo y empezamos desde ahí.</p></details>
      <details><summary>¿Cómo empiezo?</summary><p>Con una conversación corta. Antes de hablar de un curso, Luciano quiere entender qué necesitas. Si ambos ven que encaja, desde ahí defines cómo empezar.</p></details></div>''', 'cream')
    body = f'''<section class="hero hero--short" data-bg="ink"><div class="hero__media"><div class="hero__poster"></div></div><div class="hero__in"><div><span class="eyebrow" style="color:var(--on-dark-2)">Programa</span>
      <h1 class="display display--l" style="margin-top:14px"><span class="hero__line"><span>Aprende a construir con IA</span></span><span class="hero__line"><span><em class="serif tint">y conviértete en referente.</em></span></span></h1>
      <p class="hero__sub">Para profesionales, gerentes y founders que ya usan IA todos los días y quieren dominar la creación de agentes y soluciones avanzadas dentro de su trabajo.</p>
      <div class="hero__actions actions">{btn('Hablar con Luciano', '/agenda/', 'btn--light', ARROW, 'agenda_click', {'from': 'programa_hero'})}{link_arrow('Cómo funciona', '#como')}</div></div></div></section>
    {_s1}
    {_s2}
    {_s3}
    {_faq}
    {_s4}'''
    return layout('Programa', body, 'program', 'Programa práctico para profesionales que quieren construir con IA.')

def page_agenda():
    body = f'''<section class="ahead sec--cream" data-bg="cream" style="min-height:60dvh"><div class="wrap split split--wide" style="align-items:start">
      <div><span class="eyebrow eyebrow--dot" data-reveal>Agenda</span><h1 class="display display--l" data-reveal style="--i:1;margin-top:14px">Antes de hablar de un curso, quiero entender <em class="serif tint">qué necesitas.</em></h1>
        <p class="lead" data-reveal style="--i:2;margin-top:20px">Una conversación de 30 minutos con Luciano para ver dónde estás con IA y si el programa encaja contigo. Si no encaja, te lo dice y te deja con recursos para seguir solo.</p>
        <ul class="list mt-3" data-reveal style="--i:3"><li>Cuéntanos tu situación en 3 preguntas</li><li>Elige el horario que te sirva</li><li>Recibes la confirmación y el link de la reunión</li></ul>
        <p class="muted mt-3" style="font-size:14px" data-reveal style="--i:4">En esta preview el botón te lleva al flujo real de aplicación que ya funciona en <code>/aprende</code> (formulario + calendario). No se ha modificado.</p></div>
      <div class="shell" data-reveal style="--i:2"><div class="shell__in" style="padding:32px;display:grid;gap:16px"><span class="eyebrow">Alta intención</span><h3 class="h3">Aplicar al programa</h3><p style="margin:0;color:var(--ink-2)">Tres preguntas cortas y el calendario de Luciano. Tarda dos minutos.</p>
        <div class="actions">{btn('Ir al formulario de aplicación', '/aprende/#como-empezar', 'btn--accent', ARROW_NE, 'agenda_click', {'from': 'agenda_page', 'target': 'aprende'})}</div>
        <p class="muted" style="font-size:13px;margin:0">Integración existente: formulario y calendario de FunnelUp. Sin cambios.</p></div></div></div></section>
    {section(head('Mientras tanto', 'Si todavía no es el momento, <em class="serif tint">sigue construyendo.</em>') + f'<div class="wrap grid-3">{"".join(res_card(by_slug[s], "sm", i) for i, s in enumerate(["roadmap-claude-5-dias", "5-niveles-de-claude", "hermes"]))}</div>', 'paper')}'''
    return layout('Agenda', body, 'agenda', 'Agenda una conversación con Luciano.')

# ---------------------------------------------------------------- escritura
def write(path, html_):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(html_)

def main():
    write('index.html', page_home())
    write('tutoriales/index.html', page_tutoriales())
    for v in VIDS: write(f'tutoriales/{v["slug"]}/index.html', page_video(v))
    write('recursos/index.html', page_recursos())
    for r in RES: write(f'recursos/{r["slug"]}/index.html', page_resource(r))
    write('retos/index.html', page_retos())
    for ch in CHAL:
        if ch["days"]: write(f'retos/{ch["slug"]}/index.html', page_reto(ch))
    write('programa/index.html', page_programa())
    write('agenda/index.html', page_agenda())
    print(f'OK: home + {len(VIDS)} tutoriales + {len(RES)} recursos + retos + programa + agenda')

if __name__ == '__main__':
    main()
