# Landing Page — HTML Output Template

This is the complete HTML/CSS template for generating a prospect-facing, mobile-first sales landing page. It is designed to be read in under 3 minutes.

The agent should read the 3 markdown files generated in Step-3 and replace every `{{PLACEHOLDER}}` with the appropriate content. Component patterns for multi-item sections are at the bottom.

---

## Placeholder Mapping

| Placeholder | Source File | What to Extract |
|---|---|---|
| `{{SELLER_NAME}}` | `01_Value_Proposition.md` | Seller name from the title |
| `{{PROSPECT_NAME}}` | `01_Value_Proposition.md` | Prospect name from the title |
| `{{PROSPECT_INDUSTRY}}` | `01_Value_Proposition.md` | Targeted Industry Segment value |
| `{{P1_HEADLINE}}` | `01_Value_Proposition.md` | A punchy 6-10 word headline derived from the Product/Service Positioning |
| `{{P1_SUBHEAD}}` | `01_Value_Proposition.md` | 1-2 sentence elevator pitch from Positioning, personalised to prospect |
| `{{P1_INTRO}}` | `01_Value_Proposition.md` | The full Product/Service Positioning paragraph |
| `{{P1_MARKET_CATEGORY}}` | `01_Value_Proposition.md` | Core Category value |
| `{{P1_MARKET_SEGMENT}}` | `01_Value_Proposition.md` | Targeted Industry Segment value |
| `{{VALUE_PROPS_HTML}}` | `01_Value_Proposition.md` | Render each Unique Attribute as a `.vp-card` (see component patterns) |
| `{{ENGAGE_STEPS_HTML}}` | `01_Value_Proposition.md` | Render each engagement step or key feature as an `.engage-card` (see component patterns) |
| `{{P1_CTA}}` | Generated | Short CTA label e.g. "See how we solve your challenges" |
| `{{P2_HEADLINE}}` | `02_Solution_Fit.md` | Punchy headline derived from the Executive Gap section |
| `{{P2_SUBHEAD}}` | `02_Solution_Fit.md` | 1-2 sentence summary of the Executive Gap paragraph |
| `{{P2_EXEC_GAP}}` | `02_Solution_Fit.md` | Full Executive Gap paragraph |
| `{{CHALLENGES_HTML}}` | `02_Solution_Fit.md` | Render each Challenge as a `.chal-card` with pain, solution, and ROI (see component patterns) |
| `{{P2_WHY_NOW}}` | `02_Solution_Fit.md` | Strategic Advantage + Cost of Inaction combined as a compelling paragraph |
| `{{OUTCOMES_HTML}}` | `02_Solution_Fit.md` | Render 3 outcome metric cards from the Expected ROI values (see component patterns) |
| `{{P2_CTA}}` | Generated | Short CTA e.g. "Explore the industry trends" |
| `{{P3_HEADLINE}}` | `03_Industry_Trends.md` | The document title, condensed |
| `{{P3_TREND}}` | `03_Industry_Trends.md` | The Market Reality — The Trend sentence |
| `{{P3_THREAT}}` | `03_Industry_Trends.md` | The Market Reality — The Threat sentence |
| `{{P3_LEADERS}}` | `03_Industry_Trends.md` | How Leaders Win sentence |
| `{{P3_EDGE}}` | `03_Industry_Trends.md` | The Seller Edge sentence |
| `{{REC_LIST_HTML}}` | `03_Industry_Trends.md` | Render each Strategic Recommendation bullet as a `.rec-item` (see component patterns) |
| `{{NEXT_STEPS_HTML}}` | `02_Solution_Fit.md` | Render Recommended Next Steps as list items |
| `{{CONTACT_NAME}}` | Input | Salesperson's name |
| `{{CONTACT_EMAIL}}` | Input | Salesperson's email |
| `{{PHONE_BUTTON_HTML}}` | Input | Phone button HTML if provided, else empty string |

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

    /* MARKET FIT PILLS */
    .market-fit {
      display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px;
    }
    .mf-pill {
      display: inline-flex; align-items: center; gap: 6px;
      background: var(--sur); border: 1px solid var(--bdr);
      border-radius: 100px; padding: 6px 14px; font-size: 12px; color: var(--mt); font-weight: 500;
    }
    .mf-pill .mf-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--ac); flex-shrink: 0; }

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

    /* ENGAGEMENT STEP CARDS */
    .engage-card {
      display: flex; gap: 14px; align-items: flex-start;
      background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 16px;
      margin-bottom: 10px; transition: border-color 0.2s;
    }
    .engage-card:hover { border-color: rgba(16,185,129,0.3); }
    .engage-num {
      width: 28px; height: 28px; border-radius: 8px; flex-shrink: 0;
      background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.25);
      display: flex; align-items: center; justify-content: center;
      font-size: 13px; font-weight: 700; color: var(--gn);
    }
    .engage-title { font-size: 14px; font-weight: 700; margin-bottom: 5px; }
    .engage-desc { font-size: 13px; color: var(--mt); line-height: 1.55; }

    /* PRIMARY CTA */
    .cta-main {
      display: block; text-align: center; background: var(--ac); color: white;
      padding: 15px 24px; border-radius: 12px; font-size: 16px; font-weight: 600;
      text-decoration: none; transition: all 0.2s; width: 100%; border: none; cursor: pointer; font-family: var(--f);
    }
    .cta-main:hover { background: #3d5af5; transform: translateY(-2px); box-shadow: 0 8px 28px rgba(79,110,247,0.38); }

    /* EXECUTIVE GAP BOX */
    .exec-gap {
      background: var(--sur); border: 1px solid var(--bdr); border-left: 3px solid var(--rd);
      border-radius: 0 12px 12px 0; padding: 18px 20px;
      font-size: 14px; line-height: 1.68; color: rgba(241,245,249,0.78); margin-bottom: 28px;
    }

    /* CHALLENGE CARDS (expanded with pain/solution/ROI) */
    .chal-card {
      background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 18px;
      margin-bottom: 12px;
    }
    .chal-header { display: flex; gap: 12px; align-items: center; margin-bottom: 12px; }
    .chal-icon { font-size: 22px; flex-shrink: 0; line-height: 1; }
    .chal-title { font-size: 15px; font-weight: 700; }
    .chal-row { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 8px; }
    .chal-row:last-child { margin-bottom: 0; }
    .chal-tag {
      font-size: 9px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em;
      padding: 3px 8px; border-radius: 4px; flex-shrink: 0; margin-top: 2px;
    }
    .chal-tag.pain { background: rgba(244,63,94,0.12); color: var(--rd); }
    .chal-tag.solution { background: rgba(79,110,247,0.12); color: var(--ac); }
    .chal-tag.roi { background: rgba(16,185,129,0.12); color: var(--gn); }
    .chal-body { font-size: 13px; color: var(--mt); line-height: 1.55; }

    /* WHY NOW BOX */
    .why-box {
      background: linear-gradient(135deg, rgba(79,110,247,0.09), rgba(124,58,237,0.06));
      border: 1px solid rgba(79,110,247,0.14); border-radius: 12px; padding: 20px; margin: 24px 0 20px;
    }
    .why-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.09em; color: #818cf8; margin-bottom: 10px; }
    .why-body { font-size: 14px; line-height: 1.65; color: rgba(241,245,249,0.78); }

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

    /* TREND BOX */
    .trend-box { background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 20px; margin: 20px 0 28px; }
    .trend-row { display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid var(--bdr); }
    .trend-row:last-child { border-bottom: none; }
    .trend-label {
      font-size: 9px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em;
      padding: 3px 8px; border-radius: 4px; flex-shrink: 0; margin-top: 2px;
    }
    .trend-label.trend { background: rgba(79,110,247,0.12); color: var(--ac); }
    .trend-label.threat { background: rgba(244,63,94,0.12); color: var(--rd); }
    .trend-body { font-size: 14px; color: rgba(241,245,249,0.8); line-height: 1.6; }

    /* LEADER CARDS */
    .leader { display: flex; gap: 14px; align-items: flex-start; padding: 15px 0; border-bottom: 1px solid var(--bdr); }
    .leader:last-child { border-bottom: none; }
    .leader-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--ac); flex-shrink: 0; margin-top: 5px; }
    .leader-title { font-size: 13px; font-weight: 700; color: #818cf8; margin-bottom: 5px; }
    .leader-body { font-size: 13px; color: var(--mt); line-height: 1.55; }

    /* RECOMMENDATION LIST */
    .rec-list { margin: 20px 0 28px; }
    .rec-item {
      display: flex; gap: 12px; align-items: flex-start;
      background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 15px;
      margin-bottom: 8px; transition: border-color 0.2s;
    }
    .rec-item:hover { border-color: rgba(16,185,129,0.3); }
    .rec-check { font-size: 16px; flex-shrink: 0; line-height: 1; }
    .rec-text { font-size: 14px; color: rgba(241,245,249,0.82); line-height: 1.55; }

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

    /* NEXT STEPS */
    .next-steps { margin: 20px 0; }
    .ns-item {
      display: flex; gap: 12px; align-items: center;
      padding: 14px 16px; background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px;
      margin-bottom: 8px; font-size: 14px; color: rgba(241,245,249,0.85); transition: border-color 0.2s;
    }
    .ns-item:hover { border-color: rgba(79,110,247,0.28); }
    .ns-arrow { color: var(--ac); font-size: 16px; flex-shrink: 0; }

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

<!-- ===== SECTION 1: VALUE PROPOSITION ===== -->
<section class="sec" id="sec-value">
  <div class="ey">Prepared for {{PROSPECT_NAME}} · {{PROSPECT_INDUSTRY}}</div>
  <h1 class="htitle">{{P1_HEADLINE}}</h1>
  <p class="hsub">{{P1_SUBHEAD}}</p>

  <div class="intro-block r">{{P1_INTRO}}</div>

  <div class="market-fit r">
    <div class="mf-pill"><span class="mf-dot"></span> {{P1_MARKET_CATEGORY}}</div>
    <div class="mf-pill"><span class="mf-dot"></span> {{P1_MARKET_SEGMENT}}</div>
  </div>

  <div class="slabel">Our competitive edge</div>
  {{VALUE_PROPS_HTML}}

  <div class="slabel" style="margin-top:24px">How we work with you</div>
  {{ENGAGE_STEPS_HTML}}

  <a href="#sec-challenges" class="cta-main" style="margin-top:24px">{{P1_CTA}} →</a>
</section>

<!-- ===== SECTION 2: CHALLENGES & SOLUTION FIT ===== -->
<section class="sec" id="sec-challenges">
  <div class="ey">Understanding your world</div>
  <h1 class="htitle">{{P2_HEADLINE}}</h1>
  <p class="hsub">{{P2_SUBHEAD}}</p>

  <div class="exec-gap r">{{P2_EXEC_GAP}}</div>

  <div class="slabel">Your challenges, our solutions</div>
  {{CHALLENGES_HTML}}

  <div class="why-box r">
    <div class="why-title">Why {{SELLER_NAME}}? Why now?</div>
    <div class="why-body">{{P2_WHY_NOW}}</div>
  </div>

  <div class="slabel">Expected outcomes</div>
  <div class="out-row">
    {{OUTCOMES_HTML}}
  </div>

  <a href="#sec-trends" class="cta-main" style="margin-top:20px">{{P2_CTA}} →</a>
</section>

<!-- ===== SECTION 3: INDUSTRY TRENDS & CTA ===== -->
<section class="sec" id="sec-trends">
  <div class="ey">Industry intelligence</div>
  <h1 class="htitle">{{P3_HEADLINE}}</h1>

  <div class="trend-box r">
    <div class="trend-row">
      <div class="trend-label trend">Trend</div>
      <div class="trend-body">{{P3_TREND}}</div>
    </div>
    <div class="trend-row">
      <div class="trend-label threat">Risk</div>
      <div class="trend-body">{{P3_THREAT}}</div>
    </div>
  </div>

  <div class="slabel">How leaders are winning</div>
  <div style="margin-bottom:28px">
    <div class="leader r">
      <div class="leader-dot"></div>
      <div>
        <div class="leader-title">{{P3_LEADERS}}</div>
        <div class="leader-body">{{P3_EDGE}}</div>
      </div>
    </div>
  </div>

  <div class="slabel">Strategic recommendation</div>
  <div class="rec-list">
    {{REC_LIST_HTML}}
  </div>

  <div class="slabel">Recommended next steps</div>
  <div class="next-steps">
    {{NEXT_STEPS_HTML}}
  </div>

  <div class="contact-box r">
    <div class="contact-name">{{CONTACT_NAME}}</div>
    <div class="contact-co">{{SELLER_NAME}} · {{PROSPECT_INDUSTRY}}</div>
    <div class="contact-cta">Let's explore how we can accelerate your growth.</div>
    <a href="mailto:{{CONTACT_EMAIL}}" class="btn-cta btn-cta-solid">✉ {{CONTACT_EMAIL}}</a>
    {{PHONE_BUTTON_HTML}}
  </div>
</section>

<!-- BOTTOM NAV -->
<nav class="bnav" id="bnav">
  <a href="#sec-value" class="ntab active" data-sec="sec-value" onclick="setTab(this)">
    <span class="ntab-ic">✦</span>
    <span class="ntab-lb">Value</span>
  </a>
  <a href="#sec-challenges" class="ntab" data-sec="sec-challenges" onclick="setTab(this)">
    <span class="ntab-ic">⚡</span>
    <span class="ntab-lb">Fit</span>
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

  const secs = ['sec-value','sec-challenges','sec-trends'];
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
Render one `<div class="vp-card r">` per unique attribute from `01_Value_Proposition.md`:
```html
<div class="vp-card r">
  <div class="vp-icon">⚡</div>
  <div>
    <div class="vp-title">Attribute Name</div>
    <div class="vp-desc">How it beats the status quo for the prospect.</div>
  </div>
</div>
```

Choose contextually appropriate emoji icons: ⚡ for speed/efficiency, 🎯 for precision, 🔧 for customisation, 💰 for cost savings, 🛡️ for reliability, 🚀 for growth, etc.

### Engagement Step Card (`{{ENGAGE_STEPS_HTML}}`)
Render one per engagement step or key feature from `01_Value_Proposition.md`. Use numbered steps for service businesses, or feature cards for product businesses:
```html
<div class="engage-card r">
  <div class="engage-num">1</div>
  <div>
    <div class="engage-title">Step Name</div>
    <div class="engage-desc">Description of what happens in this step.</div>
  </div>
</div>
```

### Challenge Card (`{{CHALLENGES_HTML}}`)
Render one per challenge from `02_Solution_Fit.md`. Each card includes pain, solution, and ROI rows:
```html
<div class="chal-card r">
  <div class="chal-header">
    <div class="chal-icon">💢</div>
    <div class="chal-title">Challenge Name</div>
  </div>
  <div class="chal-row">
    <div class="chal-tag pain">Pain</div>
    <div class="chal-body">The specific pain point described.</div>
  </div>
  <div class="chal-row">
    <div class="chal-tag solution">Fix</div>
    <div class="chal-body">How the seller's solution addresses this.</div>
  </div>
  <div class="chal-row">
    <div class="chal-tag roi">ROI</div>
    <div class="chal-body">Expected measurable outcome.</div>
  </div>
</div>
```

Choose contextually appropriate emoji icons: 💢 for frustration, 📦 for logistics, 🛒 for e-commerce, 🔄 for process, 📊 for data, 🕐 for time, etc.

### Outcome Card (`{{OUTCOMES_HTML}}`)
Render 3 cards inside `.out-row` (horizontal scroll on mobile). Extract metrics from the Expected ROI values:
```html
<div class="out-card r">
  <div class="out-metric">30%</div>
  <div class="out-label">Fewer tickets</div>
  <div class="out-desc">Reduction in tier-1 support tickets through AI automation.</div>
</div>
```

### Recommendation Item (`{{REC_LIST_HTML}}`)
Render one per strategic recommendation bullet from `03_Industry_Trends.md`:
```html
<div class="rec-item r">
  <div class="rec-check">✅</div>
  <div class="rec-text">Protect profit margins by optimizing inventory and reducing bloat.</div>
</div>
```

### Next Step Item (`{{NEXT_STEPS_HTML}}`)
Render one per recommended next step from `02_Solution_Fit.md`:
```html
<div class="ns-item r">
  <div class="ns-arrow">→</div>
  <div>Schedule a Custom ROI Discovery Call to audit your current stack.</div>
</div>
```

### Phone Button (`{{PHONE_BUTTON_HTML}}`)
Only render this if a phone number was provided. If no phone, use an empty string:
```html
<a href="tel:+61400000000" class="btn-cta btn-cta-outline">📞 +61 400 000 000</a>
```
