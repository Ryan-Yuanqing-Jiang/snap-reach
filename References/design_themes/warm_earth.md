---
theme_name: Warm Earth
mode: Light
accent_color: Green / Pink
vibe: Organic, approachable, warm, nature-inspired
best_for: wellness, health, organic, food, agriculture, sustainability, eco, natural, beauty, spa, fitness, yoga, cafe, restaurant, retail, lifestyle
---
# Warm Earth

> Light, organic theme with green and pink accents. Warm, approachable, nature-inspired.

## Best-for Keywords
wellness, health, organic, food, agriculture, sustainability, eco, natural, beauty, spa, fitness, yoga, cafe, restaurant, retail, lifestyle

## CSS Variables

```css
:root {
  --bg: #faf5f0;
  --sur: rgba(255,255,255,0.80);
  --sur2: #fef3e2;
  --bdr: rgba(21,128,61,0.10);
  --ac: #15803D;
  --ac2: #22C55E;
  --ac-hover: #166534;
  --ac-bg: rgba(21,128,61,0.08);
  --gn: #22C55E;
  --rd: #e11d48;
  --tx: #14532D;
  --mt: rgba(20,83,45,0.52);
  --f: 'Raleway', -apple-system, sans-serif;
}
```

## Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Component Overrides

Because this is a **light theme**, the following component styles need adjustment:

```css
/* Serif headings for warmth */
.htitle, .contact-name {
  font-family: 'Lora', Georgia, serif;
  font-weight: 600;
}

/* Topbar — warm glass */
.topbar {
  background: rgba(250,245,240,0.88);
  border-bottom: 1px solid var(--bdr);
}

/* Bottom nav — warm glass */
.bnav {
  background: rgba(250,245,240,0.94);
}

/* Title gradient for light bg */
.htitle {
  background: linear-gradient(140deg, var(--tx) 40%, rgba(20,83,45,0.6));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

/* Softer border radius */
.vp-card, .engage-card, .chal-card, .rec-item, .ns-item, .out-card, .intro-block, .trend-box, .contact-box {
  border-radius: 16px;
}

/* Accent chip */
.tb-chip {
  background: rgba(21,128,61,0.10);
  border: 1px solid rgba(21,128,61,0.20);
  color: var(--ac);
}
.ntab.active { color: var(--ac); background: rgba(21,128,61,0.08); }

/* Contact box gradient */
.contact-box {
  background: linear-gradient(135deg, rgba(21,128,61,0.07), rgba(34,197,94,0.05));
  border: 1px solid rgba(21,128,61,0.12);
}

/* Why box gradient */
.why-box {
  background: linear-gradient(135deg, rgba(21,128,61,0.06), rgba(34,197,94,0.04));
  border: 1px solid rgba(21,128,61,0.10);
}

/* Metric gradient — green */
.out-metric {
  background: linear-gradient(135deg, var(--ac), var(--ac2));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

.leader-title { color: var(--ac); }
.why-title { color: var(--ac); }
```
