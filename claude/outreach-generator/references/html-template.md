# Outreach Generator — HTML Output Template

This is the complete HTML/CSS for the prospect-facing microsite. Replace every `{{PLACEHOLDER}}` with generated content. Component patterns for multi-item sections are at the bottom.

---

## Complete HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
  <title>For {{PROSPECT_NAME}} · {{SELLER_NAME}}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #07090e;
      --sur: #0d1120;
      --sur2: #131929;
      --bdr: rgba(255,255,255,0.07);
      --ac: #4f6ef7;
      --ac2: #7c3aed;
      --gn: #10b981;
      --rd: #f43f5e;
      --tx: #f1f5f9;
      --mt: rgba(241,245,249,0.48);
      --f: 'Space Grotesk', -apple-system, sans-serif;
    }
    html { scroll-behavior: smooth; }
    body { font-family: var(--f); background: var(--bg); color: var(--tx); min-height: 100vh; padding-bottom: 76px; }

    /* TOP BAR */
    .topbar {
      position: fixed; top: 0; left: 0; right: 0; z-index: 99;
      background: rgba(7,9,14,0.88); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--bdr);
      padding: 13px 20px;
      display: flex; align-items: center; justify-content: space-between;
    }
    .tb-name { font-size: 14px; font-weight: 700; }
    .tb-chip {
      display: inline-flex; align-items: center; gap: 5px;
      background: rgba(79,110,247,0.13); border: 1px solid rgba(79,110,247,0.22);
      border-radius: 100px; padding: 4px 12px; font-size: 11px; color: #818cf8; font-weight: 600;
    }

    /* SECTIONS */
    .sec { padding: 88px 22px 52px; }
    .sec + .sec { border-top: 1px solid var(--bdr); }

    /* EYEBROW */
    .ey { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: var(--ac); margin-bottom: 14px; }

    /* HERO TITLE */
    .htitle {
      font-size: clamp(26px, 7.5vw, 38px); font-weight: 700; line-height: 1.15; margin-bottom: 14px;
      background: linear-gradient(140deg, var(--tx) 40%, rgba(241,245,249,0.6));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }
    .hsub { font-size: 16px; color: var(--mt); line-height: 1.6; margin-bottom: 26px; }

    /* INTRO BLOCK */
    .intro-block {
      background: var(--sur); border: 1px solid var(--bdr); border-left: 3px solid var(--ac);
      border-radius: 0 12px 12px 0; padding: 18px 20px;
      font-size: 15px; line-height: 1.68; color: rgba(241,245,249,0.82); margin-bottom: 30px;
    }

    /* SECTION LABEL */
    .slabel { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--mt); margin-bottom: 14px; }

    /* VALUE PROP CARDS */
    .vp-card {
      display: flex; gap: 14px; align-items: flex-start;
      background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 15px;
      margin-bottom: 10px; transition: border-color 0.2s, transform 0.25s;
    }
    .vp-card:hover { border-color: rgba(79,110,247,0.28); transform: translateX(4px); }
    .vp-icon { font-size: 22px; flex-shrink: 0; line-height: 1; }
    .vp-title { font-size: 14px; font-weight: 700; margin-bottom: 5px; }
    .vp-desc { font-size: 13px; color: var(--mt); line-height: 1.55; }

    /* WHY BOX */
    .why-box {
      background: linear-gradient(135deg, rgba(79,110,247,0.09), rgba(124,58,237,0.06));
      border: 1px solid rgba(79,110,247,0.14); border-radius: 12px; padding: 20px; margin: 24px 0 20px;
    }
    .why-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.09em; color: #818cf8; margin-bottom: 10px; }
    .why-body { font-size: 14px; line-height: 1.65; color: rgba(241,245,249,0.78); }

    /* PRIMARY CTA */
    .cta-main {
      display: block; text-align: center; background: var(--ac); color: white;
      padding: 15px 24px; border-radius: 12px; font-size: 16px; font-weight: 600;
      text-decoration: none; transition: all 0.2s; width: 100%; border: none; cursor: pointer; font-family: var(--f);
    }
    .cta-main:hover { background: #3d5af5; transform: translateY(-2px); box-shadow: 0 8px 28px rgba(79,110,247,0.38); }

    /* CHALLENGE CARDS */
    .chal-card {
      display: flex; gap: 14px; align-items: flex-start;
      background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 16px; margin-bottom: 11px;
    }
    .chal-icon { font-size: 22px; flex-shrink: 0; line-height: 1; }
    .chal-title { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
    .chal-desc { font-size: 13px; color: var(--mt); line-height: 1.55; }

    /* SHIFT */
    .shift-box {
      background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 20px; margin: 26px 0;
    }
    .shift-title { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--gn); margin-bottom: 10px; }
    .shift-body { font-size: 14px; line-height: 1.65; color: rgba(241,245,249,0.8); }

    /* OUTCOMES */
    .out-row { display: flex; gap: 10px; overflow-x: auto; padding-bottom: 6px; margin: 20px 0 10px; scrollbar-width: none; }
    .out-row::-webkit-scrollbar { display: none; }
    .out-card { min-width: 130px; flex-shrink: 0; background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 16px 14px; text-align: center; }
    .out-metric {
      font-size: 22px; font-weight: 700;
      background: linear-gradient(135deg, var(--ac), #a78bfa);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
      line-height: 1.2; margin-bottom: 5px;
    }
    .out-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--mt); margin-bottom: 6px; }
    .out-desc { font-size: 11px; color: var(--mt); line-height: 1.4; }

    /* TREND */
    .trend-box { background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 20px; margin: 20px 0 28px; font-size: 15px; line-height: 1.68; color: rgba(241,245,249,0.82); }
    .leader { display: flex; gap: 14px; align-items: flex-start; padding: 15px 0; border-bottom: 1px solid var(--bdr); }
    .leader:last-child { border-bottom: none; }
    .leader-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--ac); flex-shrink: 0; margin-top: 5px; }
    .leader-title { font-size: 13px; font-weight: 700; color: #818cf8; margin-bottom: 5px; }
    .leader-body { font-size: 13px; color: var(--mt); line-height: 1.55; }

    /* GAP GRID */
    .gap-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 20px 0 28px; }
    .gap-card { background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 16px; }
    .gap-card-title { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }
    .gap-card.early .gap-card-title { color: var(--gn); }
    .gap-card.late .gap-card-title { color: var(--rd); }
    .gap-card-body { font-size: 12px; color: var(--mt); line-height: 1.5; }

    /* CONTACT */
    .contact-box {
      background: linear-gradient(135deg, rgba(79,110,247,0.1), rgba(124,58,237,0.07));
      border: 1px solid rgba(79,110,247,0.15); border-radius: 16px;
      padding: 28px 22px; text-align: center; margin-top: 28px;
    }
    .contact-name { font-size: 20px; font-weight: 700; margin-bottom: 5px; }
    .contact-co { font-size: 13px; color: var(--mt); margin-bottom: 8px; }
    .contact-cta { font-size: 14px; color: rgba(241,245,249,0.7); line-height: 1.6; margin-bottom: 22px; }
    .btn-cta { display: block; text-decoration: none; text-align: center; padding: 14px 20px; border-radius: 12px; font-size: 15px; font-weight: 600; font-family: var(--f); transition: all 0.2s; margin-bottom: 10px; }
    .btn-cta-solid { background: var(--ac); color: white; }
    .btn-cta-solid:hover { background: #3d5af5; transform: translateY(-1px); }
    .btn-cta-outline { background: transparent; color: var(--tx); border: 1px solid var(--bdr); }
    .btn-cta-outline:hover { border-color: rgba(255,255,255,0.2); }

    /* BOTTOM NAV */
    .bnav {
      position: fixed; bottom: 0; left: 0; right: 0; z-index: 99;
      background: rgba(7,9,14,0.94); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border-top: 1px solid var(--bdr); padding: 10px 12px 16px;
      display: flex; justify-content: space-around;
    }
    .ntab { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 7px 18px; border-radius: 10px; cursor: pointer; border: none; background: none; color: var(--mt); font-family: var(--f); text-decoration: none; transition: all 0.2s; }
    .ntab.active { color: var(--ac); background: rgba(79,110,247,0.1); }
    .ntab-ic { font-size: 18px; line-height: 1; }
    .ntab-lb { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; }

    /* REVEAL ANIMATION */
    .r { opacity: 0; transform: translateY(18px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .r.vis { opacity: 1; transform: none; }
  </style>
</head>
<body>

<!-- TOP BAR -->
<div class="topbar">
  <div class="tb-name">{{SELLER_NAME}}</div>
  <div class="tb-chip">✦ For {{PROSPECT_NAME}}</div>
</div>

<!-- ===== SECTION 1: INTRO ===== -->
<section class="sec" id="sec-intro">
  <div class="ey">Prepared for {{PROSPECT_NAME}} · {{PROSPECT_INDUSTRY}}</div>
  <h1 class="htitle">{{P1_HEADLINE}}</h1>
  <p class="hsub">{{P1_SUBHEAD}}</p>

  <div class="intro-block r">{{P1_INTRO}}</div>

  <div class="slabel">What we do</div>

  {{VALUE_PROPS_HTML}}

  <div class="why-box r">
    <div class="why-title">Why {{PROSPECT_NAME}}</div>
    <div class="why-body">{{P1_WHY_YOU}}</div>
  </div>

  <a href="#sec-challenges" class="cta-main">{{P1_CTA}} →</a>
</section>

<!-- ===== SECTION 2: CHALLENGES ===== -->
<section class="sec" id="sec-challenges">
  <div class="ey">Understanding your world</div>
  <h1 class="htitle">{{P2_HEADLINE}}</h1>
  <p class="hsub">{{P2_SUBHEAD}}</p>

  {{CHALLENGES_HTML}}

  <div class="shift-box r">
    <div class="shift-title">The shift we enable</div>
    <div class="shift-body">{{P2_SHIFT}}</div>
  </div>

  <div class="slabel">The outcome for your team</div>
  <div class="out-row">
    {{OUTCOMES_HTML}}
  </div>

  <a href="#sec-trends" class="cta-main" style="margin-top:20px">See the bigger picture →</a>
</section>

<!-- ===== SECTION 3: TRENDS ===== -->
<section class="sec" id="sec-trends">
  <div class="ey">Industry intelligence</div>
  <h1 class="htitle">{{P3_HEADLINE}}</h1>

  <div class="trend-box r">{{P3_TREND}}</div>

  <div class="slabel">Who's leading</div>
  <div style="margin-bottom:28px">
    {{LEADERS_HTML}}
  </div>

  <div class="slabel">The widening gap</div>
  <div class="gap-grid">
    <div class="gap-card early r">
      <div class="gap-card-title">Early movers</div>
      <div class="gap-card-body">{{P3_EARLY_ADVANTAGE}}</div>
    </div>
    <div class="gap-card late r">
      <div class="gap-card-title">Late adopters</div>
      <div class="gap-card-body">{{P3_LATE_RISK}}</div>
    </div>
  </div>

  <div class="contact-box r">
    <div class="contact-name">{{CONTACT_NAME}}</div>
    <div class="contact-co">{{SELLER_NAME}} · {{SELLER_TARGET_INDUSTRY}}</div>
    <div class="contact-cta">{{P3_FINAL_CTA}}</div>
    <a href="mailto:{{CONTACT_EMAIL}}" class="btn-cta btn-cta-solid">✉ {{CONTACT_EMAIL}}</a>
    {{PHONE_BUTTON_HTML}}
  </div>
</section>

<!-- BOTTOM NAV -->
<nav class="bnav" id="bnav">
  <a href="#sec-intro" class="ntab active" data-sec="sec-intro" onclick="setTab(this)">
    <span class="ntab-ic">✦</span>
    <span class="ntab-lb">Intro</span>
  </a>
  <a href="#sec-challenges" class="ntab" data-sec="sec-challenges" onclick="setTab(this)">
    <span class="ntab-ic">⚡</span>
    <span class="ntab-lb">Challenge</span>
  </a>
  <a href="#sec-trends" class="ntab" data-sec="sec-trends" onclick="setTab(this)">
    <span class="ntab-ic">📈</span>
    <span class="ntab-lb">Trends</span>
  </a>
</nav>

<script>
  const obs = new IntersectionObserver(es => {
    es.forEach(e => { if (e.isIntersecting) e.target.classList.add('vis'); });
  }, { threshold: 0.12 });
  document.querySelectorAll('.r').forEach(el => obs.observe(el));

  function setTab(el) {
    document.querySelectorAll('.ntab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
  }

  const secs = ['sec-intro','sec-challenges','sec-trends'];
  const tabs = document.querySelectorAll('.ntab');
  const scrollObs = new IntersectionObserver(es => {
    es.forEach(e => {
      if (e.isIntersecting) {
        const i = secs.indexOf(e.target.id);
        tabs.forEach((t,j) => t.classList.toggle('active', i === j));
      }
    });
  }, { threshold: 0.45 });
  secs.map(id => document.getElementById(id)).forEach(el => scrollObs.observe(el));
</script>
</body>
</html>
```

---

## Component Patterns

Use these HTML snippets when rendering multi-item sections.

### Value Prop Card (`{{VALUE_PROPS_HTML}}`)
Render one `<div class="vp-card r">` per value prop:
```html
<div class="vp-card r">
  <div class="vp-icon">⚡</div>
  <div>
    <div class="vp-title">Title Here</div>
    <div class="vp-desc">Description sentence one. Description sentence two.</div>
  </div>
</div>
```

### Challenge Card (`{{CHALLENGES_HTML}}`)
Render one per challenge:
```html
<div class="chal-card r">
  <div class="chal-icon">💢</div>
  <div>
    <div class="chal-title">Challenge Title</div>
    <div class="chal-desc">2–3 sentence industry-specific description.</div>
  </div>
</div>
```

### Outcome Card (`{{OUTCOMES_HTML}}`)
Render 3 cards inside `.out-row` (horizontal scroll on mobile):
```html
<div class="out-card r">
  <div class="out-metric">3×</div>
  <div class="out-label">Throughput</div>
  <div class="out-desc">Process 3× more shipments with the same team.</div>
</div>
```

### Leader Item (`{{LEADERS_HTML}}`)
Render 2 items (last child has no border via CSS):
```html
<div class="leader r">
  <div class="leader-dot"></div>
  <div>
    <div class="leader-title">Global 3PLs</div>
    <div class="leader-body">Leading third-party logistics providers have deployed carrier AI across 40+ lanes, cutting exception handling time by 60%.</div>
  </div>
</div>
```

### Phone Button (`{{PHONE_BUTTON_HTML}}`)
Only render this if a phone number was provided. If no phone, use an empty string:
```html
<a href="tel:+15550001234" class="btn-cta btn-cta-outline">📞 +1 (555) 000-1234</a>
```
