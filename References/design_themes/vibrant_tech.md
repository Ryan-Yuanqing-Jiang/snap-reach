# Vibrant Tech

> Dark, high-energy theme with neon green accents. Bold, startup-flavored, developer-friendly.

## Best-for Keywords
startup, gaming, developer tools, crypto, blockchain, social media, entertainment, creative agency, esports, mobile app, consumer tech, hackathon, youth

## CSS Variables

```css
:root {
  --bg: #0F172A;
  --sur: #1E293B;
  --sur2: #334155;
  --bdr: rgba(34,197,94,0.10);
  --ac: #22C55E;
  --ac2: #4ADE80;
  --ac-hover: #16a34a;
  --ac-bg: rgba(34,197,94,0.10);
  --gn: #22C55E;
  --rd: #f43f5e;
  --tx: #F8FAFC;
  --mt: rgba(248,250,252,0.50);
  --f: 'Space Grotesk', -apple-system, sans-serif;
}
```

## Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
```

## Component Overrides

```css
/* Body uses DM Sans for readability, headings keep Space Grotesk */
body { font-family: 'DM Sans', var(--f), -apple-system, sans-serif; }
.htitle, .vp-title, .engage-title, .chal-title, .slabel, .ey, .why-title, .contact-name {
  font-family: 'Space Grotesk', -apple-system, sans-serif;
}

/* Green-tinted accent areas */
.tb-chip {
  background: rgba(34,197,94,0.13);
  border: 1px solid rgba(34,197,94,0.22);
  color: var(--ac);
}
.ntab.active { color: var(--ac); background: rgba(34,197,94,0.1); }

/* Metric gradient — green */
.out-metric {
  background: linear-gradient(135deg, var(--ac), var(--ac2));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

/* Contact box gradient */
.contact-box {
  background: linear-gradient(135deg, rgba(34,197,94,0.09), rgba(74,222,128,0.05));
  border: 1px solid rgba(34,197,94,0.15);
}

/* Why box gradient */
.why-box {
  background: linear-gradient(135deg, rgba(34,197,94,0.08), rgba(74,222,128,0.05));
  border: 1px solid rgba(34,197,94,0.12);
}

/* Engage card hover — green tint */
.vp-card:hover { border-color: rgba(34,197,94,0.28); }

.leader-title { color: var(--ac); }
.why-title { color: var(--ac); }
```
