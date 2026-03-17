<!-- THIS FILE IS OUTDATED. USE SKILL.md instead -->
---
name: outreach-generator
description: Generate a personalized B2B sales microsite from two URLs — the seller's product website and the prospect's company website. The output is a single, self-contained, mobile-first HTML file with 3 sections (intro, challenges, industry trend) plus an optional QR code PNG. Use this skill whenever a salesperson asks to create a personalized pitch page, sales microsite, outreach landing page, or "something to show a prospect" — even if they don't say "microsite". Trigger phrases: "create a sales page for [company]", "make a personalized pitch for [prospect URL]", "generate outreach materials for my meeting with [company]", "build a page I can share with [prospect]", "I'm visiting [company] next week — help me prepare something to show them", "make a QR code page for [prospect]". Also trigger when the user provides any combination of: their own website URL + a prospect's website URL + intent to meet, pitch, or share materials.
---

# Outreach Generator

You are building a personalized B2B sales microsite — a single HTML file a salesperson can deploy, share via URL, or present as a QR code at an in-person meeting. The page is dark-themed, mobile-first, and has three scrollable sections connected by a bottom tab bar.

## What You'll Produce

**Primary output**: `outreach-[prospect-slug].html` — a self-contained HTML file with:
- **Section 1 – Intro**: Personalized hero headline, seller value props, "Why [Prospect]" block
- **Section 2 – Challenge**: Industry-specific pain points + how the product reshapes things + outcome metrics
- **Section 3 – Trends**: Industry movement narrative + who's leading + early/late adopter gap + seller's contact CTA

**Optional output**: `qr-[prospect-slug].png` — QR code for the deployed URL

---

## Step 0: Gather Inputs

Confirm you have these before proceeding:

| Input | Required | Notes |
|-------|----------|-------|
| Seller URL | ✓ | The salesperson's product/company website |
| Prospect URL | ✓ | Target company's website or LinkedIn |
| Salesperson name | ✓ | For the CTA contact section |
| Salesperson email | ✓ | For the CTA contact section |
| Salesperson phone | optional | Shown as a second CTA button if provided |
| Meeting context | optional | e.g. "pitching to their CTO" — sharpens the copy |

If any required inputs are missing, ask the user before proceeding.

---

## Step 1: Research Both Websites

Use `WebFetch` on each URL. For each site, extract the signals below. If a URL is inaccessible, infer from the domain name and URL path what you can, and note the gap.

**From the seller's site — understand:**
- Core product/service (what does it actually do?)
- Target market and industry
- Market positioning — premium? self-serve? enterprise?
- The 3 strongest value propositions (not just features — the *why it matters*)
- Competitive differentiation or unique angle

**From the prospect's site — understand:**
- Industry and primary business activity
- Sub-sectors or verticals they operate in
- Approximate scale (startup, SMB, mid-market, enterprise?)
- Likely daily operational challenges that the seller's product would address
- Any visible priorities, growth signals, or recent initiatives

---

## Step 2: Generate Personalized Content

Using your research, mentally fill out the following structure. The goal is content that feels *hand-crafted* — it should reference the prospect's actual industry, use language familiar to their world, and connect the seller's specific capabilities to their specific situation.

Good: *"For logistics companies managing 50+ carrier relationships, the reconciliation problem is constant. Mismatched invoices, manual spot-checking, and week-long close cycles drain your ops team."*

Bad: *"Our solution helps businesses improve efficiency and reduce costs."*

Build the following content:

**Seller data:**
- `seller_name` — company name
- `seller_tagline` — punchy 1-line value statement
- `seller_product_summary` — 1-2 sentence description of what they sell
- `seller_target_industry` — primary market served
- 3 × value props: each with an emoji icon, a 3–4 word title, and a 2-sentence description
- `seller_edge` — 1-sentence competitive differentiation

**Prospect data:**
- `prospect_name` — company name
- `prospect_industry` — industry
- `prospect_sectors` — 1–2 sector tags
- 3 × challenges: each with an emoji icon, a title, and a 2–3 sentence description tailored to their context

**Page 1 content:**
- `p1_headline` — 6–8 word bold headline connecting seller to prospect's world
- `p1_subhead` — supporting line speaking to their industry
- `p1_intro` — 2–3 sentences connecting seller capabilities to this specific prospect
- `p1_why_you` — 2–3 sentences specifically about *this company* — mention their sector or situation
- `p1_cta` — short CTA button text (e.g. "Explore the approach")

**Page 2 content:**
- `p2_headline` — empathetic challenge headline
- `p2_subhead` — subhead that makes them feel understood
- `p2_shift` — 2–3 sentences on how this solution reshapes the status quo for their situation
- 3 × outcomes: each with a bold metric (e.g. "3× faster"), a label, and a 1-sentence benefit

**Page 3 content:**
- `p3_headline` — trend headline (5–7 words, bold)
- `p3_trend` — 2–3 sentences on the macro shift in their industry
- 2 × leaders: type of organization leading the shift + what they're doing and seeing
- `p3_early_advantage` — 1–2 sentences: what early movers gain
- `p3_late_risk` — 1–2 sentences: what those who wait risk losing
- `p3_final_cta` — compelling final call to action line

---

## Step 3: Build the HTML File

Read `references/html-template.md` — it contains the complete HTML/CSS and component patterns for the output page.

Substitute all `{{PLACEHOLDER}}` tokens with the content you generated. Render multi-item sections (value props, challenges, outcomes, leaders) using the card HTML patterns shown in the template.

**Critical quality checks before saving:**
- `{{PROSPECT_NAME}}` appears in: the page `<title>`, the top bar chip, the eyebrow of section 1, and the Why-section title
- `{{SELLER_NAME}}` appears in: the top bar, the contact block in section 3
- All contact fields (name, email, phone if provided) are correctly placed in the CTA contact block
- Industry-specific language is used throughout — no generic placeholder phrases remain
- The file is fully self-contained (fonts load from Google CDN; no other external dependencies)

Save as: `outreach-[prospect-slug].html`
(where `prospect-slug` = prospect company name, lowercased, spaces → hyphens, e.g. `acme-manufacturing`)

---

## Step 4: Deploy and Generate QR (Optional)

If the user wants to share the page via URL or QR code:

**Deploy with pinme:**
```bash
npx pinme upload ./outreach-[prospect-slug].html
```
This returns a URL like `https://pinme.eth.limo/#/preview/...`

If `npx` or `pinme` isn't available, show the user this command and explain they can run it after downloading the file. You can also suggest alternatives: Netlify Drop (drag-and-drop at netlify.com/drop), or GitHub Pages.

**Generate QR code:**
Once you have the deployed URL, run:
```bash
python scripts/generate_qr.py "<deployed-url>" "qr-[prospect-slug].png"
```
Save the QR PNG alongside the HTML file.

If deployment fails or is skipped, tell the user: *"Download the HTML, deploy it anywhere (e.g. `npx pinme upload ./file.html`), then let me know the URL and I'll generate the QR code."*

---

## Tone and Voice Guide

The copy should feel like it was written by a sharp sales consultant who's done their homework — not a marketing bot. Use:
- **Confident, direct language** — no hedging ("may", "could potentially")
- **Industry-native terms** — if they're in logistics, say "carrier reconciliation", not "data matching"
- **Specificity over vagueness** — "healthcare orgs managing 500+ beds" beats "large organizations"
- **Second-person** — speak directly to the prospect ("your team", "you're probably dealing with")

Avoid:
- Generic superlatives ("world-class", "cutting-edge", "best-in-class")
- Filler phrases ("In today's fast-paced world...")
- Repeating the same opening structure for all 3 value props
