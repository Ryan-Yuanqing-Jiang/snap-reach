# Landing Page — Design System Reference

This reference provides the **design tokens, page scaffold, and component catalog** for generating adaptive, mobile-first sales landing pages. There is no fixed template — compose the page by selecting and arranging components based on the content.

---

## 0. Theme System

Every generated page uses a **design theme** that controls colours, fonts, and accent tints via CSS custom properties. Theme files live in `./references/design_themes/` — each contains a drop-in `:root` block, a Google Fonts `<link>`, and any component-specific CSS overrides.

### Available Themes

Each theme file in `./references/design_themes/` starts with a YAML metadata block detailing its `theme_name`, `mode`, `accent_color`, `vibe`, and `best_for` keywords. Here is a summary of the available themes:

| Theme file | Mode | Accent | Vibe | Best for (`best_for`) |
|-----------|------|--------|------|------------------------|
| `midnight_blue.md` **(DEFAULT)** | Dark | Blue | Tech-forward, professional, modern | Tech, SaaS, AI, consulting |
| `clean_frost.md` | Light | Cyan / Green | Fresh, modern, minimal, clean | Modern SaaS, fintech, health |
| `luxury_noir.md` | Dark | Gold | Refined, exclusive, premium, elegant | Luxury, fashion, premium brands |
| `corporate_trust.md` | Light | Navy Blue | Authoritative, credible, trustworthy | Enterprise, govt, finance, legal |
| `warm_earth.md` | Light | Green / Pink | Organic, approachable, warm, nature-inspired | Wellness, food, organic, retail |
| `vibrant_tech.md` | Dark | Neon Green | Bold, high-energy, energetic | Startups, gaming, dev tools |

### How to Apply a Theme

1. **Open the chosen theme file** (e.g. `clean_frost.md`).
2. **Replace the `:root { … }` block** in Section 1 below with the theme's `:root` block.
3. **Replace the Google Fonts `<link>`** in `<head>` with the theme's font link.
4. **Append the Component Overrides CSS** from the theme file into the `<style>` block — these adjust topbar, bottom nav, gradients, and card surfaces for the theme's light/dark mode.

If no theme is specified, use `midnight_blue.md` — its variables are identical to the defaults in Section 1 below, so no changes are needed.

---

## 1. Design Tokens & Base Styles

All pages share these CSS custom properties, fonts, and reset styles. Include them verbatim in every generated page.

```css
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
```

**Google Fonts link** (place in `<head>`):
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

---

## 2. Page Scaffold

Every generated page must include these structural elements. The **sections in between** are composed dynamically.

### Top Bar
Fixed header showing seller name and prospect personalisation chip.

```html
<div class="topbar">
  <div class="tb-name">{Seller Name}</div>
  <div class="tb-chip">✦ For {Prospect Name}</div>
</div>
```

```css
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
```

### Bottom Navigation
Fixed tab bar that highlights the active section on scroll. Generate one `<a class="ntab">` per section. Mark the first tab `.active`.

```html
<nav class="bnav" id="bnav">
  <a href="#sec-{id}" class="ntab active" data-sec="sec-{id}">
    <span class="ntab-ic">{emoji}</span>
    <span class="ntab-lb">{Label}</span>
  </a>
  <!-- repeat for each section -->
</nav>
```

```css
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
```

### Scroll Reveal & Nav Highlight JS
Place at the bottom of `<body>`. The `secs` array must match the section IDs you generated.

```html
<script>
  // Scroll-reveal animation
  const obs = new IntersectionObserver(es => {
    es.forEach(e => { if (e.isIntersecting) e.target.classList.add('vis'); });
  }, { threshold: 0.12 });
  document.querySelectorAll('.r').forEach(el => obs.observe(el));

  // Tab click handler
  function setTab(el) {
    document.querySelectorAll('.ntab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
  }

  // Auto-highlight on scroll
  const secs = [/* 'sec-value', 'sec-challenges', 'sec-trends', ... */];
  const tabs = document.querySelectorAll('.ntab');
  const scrollObs = new IntersectionObserver(es => {
    es.forEach(e => {
      if (e.isIntersecting) {
        const i = secs.indexOf(e.target.id);
        tabs.forEach((t, j) => t.classList.toggle('active', i === j));
      }
    });
  }, { threshold: 0.45 });
  secs.map(id => document.getElementById(id)).forEach(el => { if (el) scrollObs.observe(el); });
</script>
```

```css
/* Reveal animation */
.r { opacity: 0; transform: translateY(18px); transition: opacity 0.5s ease, transform 0.5s ease; }
.r.vis { opacity: 1; transform: none; }
```

---

## 3. Section Shell

Use this pattern to create each top-level section. Every section gets an `id` (for nav linking), an eyebrow label, a headline, and an optional subhead.

```html
<section class="sec" id="sec-{id}">
  <div class="ey">{Eyebrow text}</div>
  <h1 class="htitle">{Section headline}</h1>
  <p class="hsub">{Optional subhead — 1-2 sentences}</p>

  <!-- Compose components below -->
</section>
```

```css
.sec { padding: 88px 22px 52px; }
.sec + .sec { border-top: 1px solid var(--bdr); }
.ey { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: var(--ac); margin-bottom: 14px; }
.htitle {
  font-size: clamp(26px, 7.5vw, 38px); font-weight: 700; line-height: 1.15; margin-bottom: 14px;
  background: linear-gradient(140deg, var(--tx) 40%, rgba(241,245,249,0.6));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hsub { font-size: 16px; color: var(--mt); line-height: 1.6; margin-bottom: 26px; }
```

### Section Label
Use within a section to introduce a sub-group of components (e.g. "Our competitive edge", "Your challenges, our solutions").

```html
<div class="slabel">{Label text}</div>
```

```css
.slabel { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--mt); margin-bottom: 14px; }
```

### Section CTA
Place at the bottom of a section to link the reader to the next section.

```html
<a href="#sec-{next}" class="cta-main" style="margin-top:24px">{CTA label} →</a>
```

```css
.cta-main {
  display: block; text-align: center; background: var(--ac); color: white;
  padding: 15px 24px; border-radius: 12px; font-size: 16px; font-weight: 600;
  text-decoration: none; transition: all 0.2s; width: 100%; border: none; cursor: pointer; font-family: var(--f);
}
.cta-main:hover { background: #3d5af5; transform: translateY(-2px); box-shadow: 0 8px 28px rgba(79,110,247,0.38); }
```

---

## 4. Component Catalog

Pick from these components as needed. Use as many or as few of each as the content requires.

---

### Intro Block
**When to use:** To present a positioning summary or executive overview paragraph.

```html
<div class="intro-block r">{Paragraph text}</div>
```

```css
.intro-block {
  background: var(--sur); border: 1px solid var(--bdr); border-left: 3px solid var(--ac);
  border-radius: 0 12px 12px 0; padding: 18px 20px;
  font-size: 15px; line-height: 1.68; color: rgba(241,245,249,0.82); margin-bottom: 30px;
}
```

---

### Market Fit Pills
**When to use:** To display category/segment tags as compact pills.

```html
<div class="market-fit r">
  <div class="mf-pill"><span class="mf-dot"></span> {Category or segment}</div>
  <!-- repeat as needed -->
</div>
```

```css
.market-fit { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }
.mf-pill {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--sur); border: 1px solid var(--bdr);
  border-radius: 100px; padding: 6px 14px; font-size: 12px; color: var(--mt); font-weight: 500;
}
.mf-pill .mf-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--ac); flex-shrink: 0; }
```

---

### Value Prop Card
**When to use:** To highlight competitive advantages, unique attributes, or key differentiators. Render one per attribute.

Choose contextually appropriate emoji icons: ⚡ speed/efficiency, 🎯 precision, 🔧 customisation, 💰 cost savings, 🛡️ reliability, 🚀 growth.

```html
<div class="vp-card r">
  <div class="vp-icon">{emoji}</div>
  <div>
    <div class="vp-title">{Attribute name}</div>
    <div class="vp-desc">{How it beats the status quo for the prospect}</div>
  </div>
</div>
```

```css
.vp-card {
  display: flex; gap: 14px; align-items: flex-start;
  background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 15px;
  margin-bottom: 10px; transition: border-color 0.2s, transform 0.25s;
}
.vp-card:hover { border-color: rgba(79,110,247,0.28); transform: translateX(4px); }
.vp-icon { font-size: 22px; flex-shrink: 0; line-height: 1; }
.vp-title { font-size: 14px; font-weight: 700; margin-bottom: 5px; }
.vp-desc { font-size: 13px; color: var(--mt); line-height: 1.55; }
```

---

### Engagement Step Card
**When to use:** To show a numbered process or engagement workflow (for service-based sellers). Can also be adapted for product features by replacing the number with an icon.

```html
<div class="engage-card r">
  <div class="engage-num">{step number}</div>
  <div>
    <div class="engage-title">{Step name}</div>
    <div class="engage-desc">{Description of what happens}</div>
  </div>
</div>
```

```css
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
```

---

### Executive Gap Block
**When to use:** To present the "status quo vs future state" narrative — a compelling paragraph about the cost of inaction.

```html
<div class="exec-gap r">{Gap paragraph}</div>
```

```css
.exec-gap {
  background: var(--sur); border: 1px solid var(--bdr); border-left: 3px solid var(--rd);
  border-radius: 0 12px 12px 0; padding: 18px 20px;
  font-size: 14px; line-height: 1.68; color: rgba(241,245,249,0.78); margin-bottom: 28px;
}
```

---

### Challenge Card
**When to use:** To map a prospect pain point to a solution. Each card includes pain, solution, and ROI rows. Render one per challenge — use as many as the content contains.

Choose contextually appropriate emoji icons: 💢 frustration, 📦 logistics, 🛒 e-commerce, 🔄 process, 📊 data, 🕐 time.

```html
<div class="chal-card r">
  <div class="chal-header">
    <div class="chal-icon">{emoji}</div>
    <div class="chal-title">{Challenge name}</div>
  </div>
  <div class="chal-row">
    <div class="chal-tag pain">Pain</div>
    <div class="chal-body">{Specific pain point}</div>
  </div>
  <div class="chal-row">
    <div class="chal-tag solution">Fix</div>
    <div class="chal-body">{How the seller solves it}</div>
  </div>
  <div class="chal-row">
    <div class="chal-tag roi">ROI</div>
    <div class="chal-body">{Expected measurable outcome}</div>
  </div>
</div>
```

```css
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
```

---

### Why Now Box
**When to use:** To present the strategic advantage and cost-of-inaction argument as a highlighted callout.

```html
<div class="why-box r">
  <div class="why-title">{Title, e.g. "Why [Seller]? Why now?"}</div>
  <div class="why-body">{Compelling paragraph combining strategic advantage and urgency}</div>
</div>
```

```css
.why-box {
  background: linear-gradient(135deg, rgba(79,110,247,0.09), rgba(124,58,237,0.06));
  border: 1px solid rgba(79,110,247,0.14); border-radius: 12px; padding: 20px; margin: 24px 0 20px;
}
.why-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.09em; color: #818cf8; margin-bottom: 10px; }
.why-body { font-size: 14px; line-height: 1.65; color: rgba(241,245,249,0.78); }
```

---

### Outcome Card
**When to use:** To display quantifiable ROI metrics in a horizontally scrollable row. Extract metrics from Expected ROI values. Render as many as the content supports.

Wrap all outcome cards in a `.out-row` container.

```html
<div class="out-row">
  <div class="out-card r">
    <div class="out-metric">{metric, e.g. "30%"}</div>
    <div class="out-label">{short label}</div>
    <div class="out-desc">{One sentence context}</div>
  </div>
  <!-- repeat as needed -->
</div>
```

```css
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
```

---

### Trend Box
**When to use:** To present market trends and threats side by side using labeled rows. Use one row per trend/threat pair.

```html
<div class="trend-box r">
  <div class="trend-row">
    <div class="trend-label trend">Trend</div>
    <div class="trend-body">{Trend sentence}</div>
  </div>
  <div class="trend-row">
    <div class="trend-label threat">Risk</div>
    <div class="trend-body">{Threat sentence}</div>
  </div>
  <!-- add more rows if multiple trends exist -->
</div>
```

```css
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
```

---

### Leader Insight
**When to use:** To show how industry leaders are winning and how the seller provides an edge.

```html
<div class="leader r">
  <div class="leader-dot"></div>
  <div>
    <div class="leader-title">{How leaders win}</div>
    <div class="leader-body">{The seller's edge}</div>
  </div>
</div>
```

```css
.leader { display: flex; gap: 14px; align-items: flex-start; padding: 15px 0; border-bottom: 1px solid var(--bdr); }
.leader:last-child { border-bottom: none; }
.leader-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--ac); flex-shrink: 0; margin-top: 5px; }
.leader-title { font-size: 13px; font-weight: 700; color: #818cf8; margin-bottom: 5px; }
.leader-body { font-size: 13px; color: var(--mt); line-height: 1.55; }
```

---

### Recommendation Item
**When to use:** To list strategic recommendations as check-marked items.

```html
<div class="rec-list">
  <div class="rec-item r">
    <div class="rec-check">✅</div>
    <div class="rec-text">{Recommendation text}</div>
  </div>
  <!-- repeat as needed -->
</div>
```

```css
.rec-list { margin: 20px 0 28px; }
.rec-item {
  display: flex; gap: 12px; align-items: flex-start;
  background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px; padding: 15px;
  margin-bottom: 8px; transition: border-color 0.2s;
}
.rec-item:hover { border-color: rgba(16,185,129,0.3); }
.rec-check { font-size: 16px; flex-shrink: 0; line-height: 1; }
.rec-text { font-size: 14px; color: rgba(241,245,249,0.82); line-height: 1.55; }
```

---

### Next Step Item
**When to use:** To list actionable next steps for the prospect.

```html
<div class="next-steps">
  <div class="ns-item r">
    <div class="ns-arrow">→</div>
    <div>{Next step text}</div>
  </div>
  <!-- repeat as needed -->
</div>
```

```css
.next-steps { margin: 20px 0; }
.ns-item {
  display: flex; gap: 12px; align-items: center;
  padding: 14px 16px; background: var(--sur); border: 1px solid var(--bdr); border-radius: 12px;
  margin-bottom: 8px; font-size: 14px; color: rgba(241,245,249,0.85); transition: border-color 0.2s;
}
.ns-item:hover { border-color: rgba(79,110,247,0.28); }
.ns-arrow { color: var(--ac); font-size: 16px; flex-shrink: 0; }
```

---

### Contact Box
**When to use:** As the final element in the last section. Includes salesperson name, email, and optional phone.

```html
<div class="contact-box r">
  <div class="contact-name">{Salesperson name}</div>
  <div class="contact-co">{Seller name} · {Industry}</div>
  <div class="contact-cta">Let's explore how we can accelerate your growth.</div>
  <a href="mailto:{email}" class="btn-cta btn-cta-solid">✉ {email}</a>
  <!-- Optional phone: -->
  <a href="tel:{phone}" class="btn-cta btn-cta-outline">📞 {phone}</a>
</div>
```

```css
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
```

---

## 5. Composition Rules

When assembling the page, follow these guidelines:

1. **Section ordering**: The recommended default is Value → Fit → Trends, but reorder if the content flow calls for it.
2. **Section labels before component groups**: Always place a `.slabel` above a group of related components (e.g. before a set of `.vp-card` elements).
3. **CTA placement**: End each section (except the last) with a `.cta-main` linking to the next section.
4. **Reveal class**: Add `class="r"` to any element that should animate in on scroll. Best used on cards, text blocks, and callout boxes.
5. **Component count**: Match the number of components to the actual content — never pad or omit items to hit a fixed count.
6. **Contact box**: Always place as the last element in the last section.
7. **Phone button**: Only include the phone `<a>` in the contact box if a phone number was provided; otherwise omit it entirely.
