---
theme_name: Clean Frost
mode: Light
accent_color: Cyan / Green
vibe: Fresh, modern, minimal, clean
best_for: modern SaaS, fintech, health, wellness tech, productivity, clean, minimal, light, professional, clinic, medical tech, insurance
---
# Clean Frost

> Light, airy glassmorphism theme with cyan and green accents. Feels fresh, modern, and trustworthy.

## Best-for Keywords
modern SaaS, fintech, health, wellness tech, productivity, clean, minimal, light, professional, clinic, medical tech, insurance

## CSS Variables

```css
:root {
  --bg: #f0fdfa;
  --sur: rgba(255,255,255,0.75);
  --sur2: rgba(255,255,255,0.55);
  --bdr: rgba(8,145,178,0.12);
  --ac: #0891B2;
  --ac2: #22D3EE;
  --ac-hover: #0e7490;
  --ac-bg: rgba(8,145,178,0.10);
  --gn: #22C55E;
  --rd: #ef4444;
  --tx: #164E63;
  --mt: rgba(22,78,99,0.55);
  --f: 'Plus Jakarta Sans', -apple-system, sans-serif;
}
```

## Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Component Overrides

Because this is a **light theme**, the following component styles need adjustment:

```css
/* Topbar — light glass */
.topbar {
  background: rgba(240,253,250,0.85);
  border-bottom: 1px solid var(--bdr);
}

/* Bottom nav — light glass */
.bnav {
  background: rgba(240,253,250,0.92);
}

/* Title gradient for light bg */
.htitle {
  background: linear-gradient(140deg, var(--tx) 40%, rgba(22,78,99,0.6));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

/* Glassmorphism card surfaces */
.vp-card, .engage-card, .chal-card, .rec-item, .ns-item, .out-card, .intro-block, .exec-gap, .trend-box {
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
}

/* Contact box gradient */
.contact-box {
  background: linear-gradient(135deg, rgba(8,145,178,0.08), rgba(34,211,238,0.06));
  border: 1px solid rgba(8,145,178,0.15);
}

/* Why box gradient */
.why-box {
  background: linear-gradient(135deg, rgba(8,145,178,0.07), rgba(34,211,238,0.05));
  border: 1px solid rgba(8,145,178,0.12);
}
```
