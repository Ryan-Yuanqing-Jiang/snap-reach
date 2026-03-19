---
theme_name: Luxury Noir
mode: Dark
accent_color: Gold
vibe: Refined, exclusive, premium, elegant
best_for: luxury, fashion, premium, high-end, jewelry, real estate, architecture, fine dining, hospitality, automotive, watches, spirits, heritage brands
---
# Luxury Noir

> Dark, refined theme with gold accents and serif typography. Conveys exclusivity and premium quality.

## Best-for Keywords
luxury, fashion, premium, high-end, jewelry, real estate, architecture, fine dining, hospitality, automotive, watches, spirits, heritage brands

## CSS Variables

```css
:root {
  --bg: #0c0a09;
  --sur: #1c1917;
  --sur2: #292524;
  --bdr: rgba(202,138,4,0.12);
  --ac: #CA8A04;
  --ac2: #EAB308;
  --ac-hover: #a16207;
  --ac-bg: rgba(202,138,4,0.10);
  --gn: #84cc16;
  --rd: #f43f5e;
  --tx: #fafaf9;
  --mt: rgba(250,250,249,0.50);
  --f: 'Montserrat', -apple-system, sans-serif;
}
```

## Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Component Overrides

```css
/* Serif headings for luxury feel */
.htitle, .contact-name {
  font-family: 'Cormorant', Georgia, serif;
  font-weight: 600;
}

/* Gold-tinted accent areas */
.tb-chip {
  background: rgba(202,138,4,0.13);
  border: 1px solid rgba(202,138,4,0.22);
  color: var(--ac);
}
.ntab.active { color: var(--ac); background: rgba(202,138,4,0.1); }

/* Metric gradient — gold */
.out-metric {
  background: linear-gradient(135deg, var(--ac), #EAB308);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

/* Contact box gradient */
.contact-box {
  background: linear-gradient(135deg, rgba(202,138,4,0.09), rgba(234,179,8,0.05));
  border: 1px solid rgba(202,138,4,0.15);
}

/* Why box gradient */
.why-box {
  background: linear-gradient(135deg, rgba(202,138,4,0.08), rgba(234,179,8,0.05));
  border: 1px solid rgba(202,138,4,0.14);
}

/* Leader title */
.leader-title { color: var(--ac); }

/* Why title */
.why-title { color: var(--ac); }
```
