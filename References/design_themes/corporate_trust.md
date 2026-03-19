---
theme_name: Corporate Trust
mode: Light
accent_color: Navy Blue
vibe: Authoritative, credible, trustworthy
best_for: enterprise, corporate, government, finance, banking, insurance, legal, healthcare, pharmaceutical, defence, manufacturing, logistics, professional services, accounting
---
# Corporate Trust

> Light, authoritative theme with navy and blue accents. Builds trust and credibility for enterprise audiences.

## Best-for Keywords
enterprise, corporate, government, finance, banking, insurance, legal, healthcare, pharmaceutical, defence, manufacturing, logistics, professional services, accounting

## CSS Variables

```css
:root {
  --bg: #f8fafc;
  --sur: #ffffff;
  --sur2: #f1f5f9;
  --bdr: rgba(15,23,42,0.08);
  --ac: #0369A1;
  --ac2: #0284C7;
  --ac-hover: #075985;
  --ac-bg: rgba(3,105,161,0.08);
  --gn: #16a34a;
  --rd: #dc2626;
  --tx: #020617;
  --mt: rgba(2,6,23,0.52);
  --f: 'Lexend', -apple-system, sans-serif;
}
```

## Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=Source+Sans+3:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Component Overrides

Because this is a **light theme**, the following component styles need adjustment:

```css
/* Body font */
body { font-family: 'Source Sans 3', var(--f), -apple-system, sans-serif; }
.htitle, .vp-title, .engage-title, .chal-title, .contact-name, .why-title, .slabel, .ey {
  font-family: 'Lexend', -apple-system, sans-serif;
}

/* Topbar — light solid */
.topbar {
  background: rgba(248,250,252,0.92);
  border-bottom: 1px solid var(--bdr);
}

/* Bottom nav — light solid */
.bnav {
  background: rgba(248,250,252,0.95);
}

/* Title gradient for light bg */
.htitle {
  background: linear-gradient(140deg, var(--tx) 40%, rgba(2,6,23,0.6));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

/* Card surfaces — solid white with subtle shadow */
.vp-card, .engage-card, .chal-card, .rec-item, .ns-item, .out-card, .trend-box {
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.intro-block, .exec-gap {
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

/* Contact box gradient */
.contact-box {
  background: linear-gradient(135deg, rgba(3,105,161,0.06), rgba(2,132,199,0.04));
  border: 1px solid rgba(3,105,161,0.12);
}

/* Why box gradient */
.why-box {
  background: linear-gradient(135deg, rgba(3,105,161,0.06), rgba(2,132,199,0.04));
  border: 1px solid rgba(3,105,161,0.10);
}

/* Accent chip */
.tb-chip {
  background: rgba(3,105,161,0.08);
  border: 1px solid rgba(3,105,161,0.18);
  color: var(--ac);
}
.ntab.active { color: var(--ac); background: rgba(3,105,161,0.08); }
.leader-title { color: var(--ac); }
.why-title { color: var(--ac); }
```
