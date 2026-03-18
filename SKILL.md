---
name: outreach-generator
description: Generate a personalized B2B sales microsite from two URLs — the seller's product website and the prospect's company website. The output is a single, self-contained, mobile-first HTML file with 3 sections (intro, challenges, industry trend) plus an optional QR code PNG. Use this skill whenever a salesperson asks to create a personalized pitch page, sales microsite, outreach landing page, or "something to show a prospect" — even if they don't say "microsite". Trigger phrases: "create a sales page for [company]", "make a personalized pitch for [prospect URL]", "generate outreach materials for my meeting with [company]", "build a page I can share with [prospect]", "I'm visiting [company] next week — help me prepare something to show them", "make a QR code page for [prospect]". Also trigger when the user provides any combination of: their own website URL + a prospect's website URL + intent to meet, pitch, or share materials.
---

# Role: 
You are an expert Go-To-Market (GTM) Strategist and Sales Enablement 
You are building a personalized B2B sales microsite — a single HTML file a salesperson can deploy, share via URL, or present as a QR code at an in-person meeting. The page is dark-themed, mobile-first, and has three scrollable sections connected by a bottom tab bar.

## What You'll Produce

**Primary output**: `outreach-[prospect-slug].html` — a self-contained HTML file with:
- **Section 1 – Intro**: Personalized hero headline, seller value props.
- **Section 2 – Challenge**: Industry-specific pain points + how the product reshapes things + outcome metrics
- **Section 3 – Trends**: Industry movement narrative + who's leading + early/late adopter gap + seller's contact CTA

**Optional output**: `qr-[prospect-slug].png` — QR code for the deployed URL

# Input: 
The salesperson will provide their own business URL {seller_url} and a Prospect’s URL/LinkedIn {prospect_url}.
*Optional*: The salesperson may explicitly request a specific design theme from `./references/design_themes/` to be used for the page. 

# Steps
These are the steps you should follow:
1. Understand the context of the Seller and the Prospect, by studying the provided URLs, use browser automation tools to extract the information.
2. Use sub-agent to identify prospect's challenges and pain points.
3. Generate the markdown sales collateral.
4. Generate a personalised landing page from the markdown collateral.
5. Upload the landing page to IPFS via pinme and generate a QR code for the live site URL.

Note:
- If files for any steps are already generated, don't bother regenerating them, just use the existing files and go to the next step.

# Step-1: Understand the seller and prospect:
You must first understand the context of the Seller and the Prospect, by studying the provided URLs, use browser automation tools to extract the information.

You should strive to understand the following about the Seller:
- What is the Seller's product/service?
- What is the Seller's target industry?
- What is the Seller's market positioning?
- What is the Seller's unique value proposition?
- What is the Seller's competitive edge?

Then study the prospect and understand the following:
- What is the Prospect's industry/sector?
- What is the Prospect's core business model?

You should also learn about the latest trends in the Prospect's industry and how the Seller's product/service can help the Prospect stay ahead of the curve.

## Note:
- You can use up to 5 sub-agents to help you understand the context of the Seller and the Prospect, and their industry. Each sub-agent can use browser automation tools to extract information from the provided URLs.

# Step-2: Identify prospect's challenges and pain points:
Use a sub-agent to identify prospect's challenges and pain points:
1. Ask it to follow the instructions in the {./references/prospect_research.md} file. And give it the research and context you've learned in Step-1.
2. Once you get the result from the sub-agent, you should review it and make sure it is accurate and comprehensive. If not, you should ask the sub-agent to refine it.
3. Then save the result in a file named {./Steps/prospect_challenges.md}.

# Step-3: Generate the markdown sales collateral
With the deep understanding of the Seller and the Prospect, you can now generate the markdown sales collateral.

- Use markdown templates provided below to generate the markdown sales collateral.

Checklist:
- The output should be 3 markdown files.
- The files must be generated and saved under the `./md_files/[prospect-slug]/` directory.
- Each markdown file should be concise enough to fit on a single A4 page.
- Each markdown file should be personalized to the Seller and the Prospect.

## Tone & Style: 
- Professional, succinct, and data-driven. Avoid fluff. Focus on "Problem/Solution" and "Value/Outcome." Each document must be concise enough to fit on a single A4 page.

Phase 1: Research & Synthesis
Analyze Seller: Identify the product/service, target industry, market positioning, unique attributes, and competitive edge.

Analyze Prospect: Identify their industry/sector, core business model, and the likely daily operational challenges or "margin-burners" they face.

Phase 2: Output Generation
Generate the following three markdown files using the exact templates provided below.

---
# Markdown templates for sales collateral

## Template 1: Personalized Value Proposition
File Name: `./md_files/[prospect-slug]/01_Value_Proposition.md`
Objective: A succinct description of the seller’s service, pivoted specifically to the prospect’s industry.

```

# [Seller Name] x [Prospect Name]: Strategic Value Overview

### Product/Service Positioning
[2-3 sentences defining what the product is within the context of the Prospect's industry.]

### Market Fit & Category
* **Core Category:** [e.g., Enterprise SaaS / AI-Driven Logistics]
* **Targeted Industry Segment:** [Specific sector of the prospect]

### Unique Attributes & Competitive Edge
* **[Attribute 1]:** [How it beats the status quo for a company like Prospect Name]
* **[Attribute 2]:** [Technical or operational advantage]

{{IF: seller is a service based company}}

### Engagement process for [Prospect Name]

* **[Step 1]:** [Description of the first step in the engagement process]
* **[Step 2]:** [Description of the second step in the engagement process]
* **[Step 3]:** [Description of the third step in the engagement process]
{{add more steps if the engagement process is long}}
{{ENDIF}}

{{IF: seller is a product based company}}

### Key Features for [Prospect Name]
* **[Feature A]:** [Direct impact on Prospect's specific business model]
* **[Feature B]:** [Efficiency or revenue gain]

{{ENDIF}}

```

## Template 2: Challenge & Solution Fit
File Name: `./md_files/[prospect-slug]/02_Solution_Fit.md`
Objective: Map specific pains to the seller's solutions. Focus on "Pain vs. Gain."

```
# [Prospect Name] + [Seller Name]: Strategic Partnership & Solution Fit

## 1. The Executive Gap (Status Quo vs. Future State)
[2-3 sentences summarizing the gap between the Prospect's current operational state and where they need to be to stay competitive or preserve margins. Highlight the cost of doing nothing.]

## 2. Core Operational Pains & The [Seller Name] Solution

### Challenge 1: [Name of the biggest operational headache, e.g., Supply Chain Bottlenecks]
* **The Pain:** [Describe the specific root cause and how it burns margin or slows growth for the prospect.]
* **The Solution:** [How the Seller's product/service directly intercepts and solves this specific pain.]
* **Expected ROI:** [Quantifiable metric, e.g., "X% reduction in turnaround time" or "Immediate recovery of $Y in operational costs."]

### Challenge 2: [Name of secondary operational bottleneck]
* **The Pain:** [Describe the specific bottleneck or inefficiency.]
* **The Solution:** [Explain the specific Seller capability that eliminates this bottleneck.]
* **Expected ROI:** [Quantifiable metric or competitive advantage gained.]

### Challenge 3: [Name of tertiary challenge, if applicable]
* **The Pain:** [Describe the challenge.]
* **The Solution:** [Explain the Seller's solution.]
* **Expected ROI:** [Quantifiable metric.]

## 3. Why [Seller Name]? Why Now?
* **Strategic Advantage:** [One sentence on why this Seller is uniquely positioned to solve these exact problems.]
* **Cost of Inaction:** [What the prospect stands to lose (in revenue, market share, or operational waste) by delaying a decision over the next 6-12 months.]

## 4. Recommended Next Steps
* [Actionable Next Step 1, e.g., "Custom ROI Workshop" or "Deep-dive technical discovery call."]
* [Actionable Next Step 2, e.g., "Review of pilot program parameters."]
```

## Template 3: Industry Trends & Benchmarking
File Name: `./md_files/[prospect-slug]/03_Industry_Trends.md`
Objective: Use social proof and market trends to advocate for adoption.

# The [Relevant Technology] Shift in [Prospect Industry]

## 1. The Market Reality
* **The Trend:** [1 concise sentence on the major trend disrupting the industry.]
* **The Threat:** [1 concise sentence on the risk to companies that fail to adapt.]

## 2. Setting the New Standard
* **How Leaders Win:** [1 sentence on how top competitors are using this tech/service to pull ahead.]
* **The [Seller Name] Edge:** [1 short sentence on what makes the Seller the best vehicle for this transition.]

## 3. Strategic Recommendation
**Adopt [Seller Solution] to:**
* [Benefit 1, e.g., Protect profit margins.]
* [Benefit 2, e.g., Scale without adding headcount.]
* [Benefit 3, e.g., Future-proof operations.]

---
*Prepared for [Prospect Representative] by [Salesperson Name]*

# Step-4: Generate personalised landing page
With the markdown files from Steps 1-3 now complete, generate a mobile-first, sales-oriented HTML landing page that a prospect can read and understand in under 3 minutes.

Unlike a static template, the page structure should **adapt to the content**. Use the Design System Reference at `{./references/landing_page_template.md}` as a component catalog — not a fill-in-the-blanks template.

## Phase 1 — Analyse the content
Read all available markdown files and inventory their structure:
- `./md_files/[prospect-slug]/01_Value_Proposition.md` — note how many unique attributes, engagement steps or key features exist, and whether the seller is service-based or product-based.
- `./md_files/[prospect-slug]/02_Solution_Fit.md` — count the number of challenges; note which have quantitative vs qualitative ROI; note the number of recommended next steps.
- `./md_files/[prospect-slug]/03_Industry_Trends.md` — note the number of recommendation bullets; check for multiple trends or a single one.
- `Steps/prospect_challenges.md` — check for any additional operational insights that weren't captured in the 3 files above.

## Phase 1.5 — Select Design Theme
Pick a design theme from `./references/design_themes/` using this priority:

1. **Explicit Request** — if the user explicitly asked for a specific design theme in their prompt (e.g., "Use the luxury_noir theme"), use that theme.
2. **Match the prospect's website** — if you visited the prospect's URL in Step-1, identify the dominant visual tone (dark/light mode, accent colour family, industry feel) and compare it against the **Best-for Keywords** in each theme file. Select the closest match.
3. **Match the seller's brand** — if the prospect's website design is not available or not distinctive enough to match confidently, use the seller's primary brand colour and website aesthetic to pick the theme whose accent colours and mood are closest.
4. **Default** — if neither signal is available, use `midnight_blue.md`.

Record the chosen theme name in your Phase 2 plan. You will apply its CSS variables, Google Fonts link, and Component Overrides when composing the HTML in Phase 3.

## Phase 2 — Plan the page layout
Based on the inventory above, decide the page sections and sub-components:
- **Default structure**: 3 sections (Value · Fit · Trends) — this is the recommended baseline, but you may split, merge, or reorder sections if the content warrants it (e.g. if there are many challenges, consider giving them a dedicated expanded section).
- **Component selection**: For each section, choose components from the **Component Catalog** in the Design System Reference. Match component types to content — e.g. use `.engage-card` for service engagement steps, but `.vp-card` style for product features. Use as many or as few of each component as the content requires.
- **Bottom nav & section IDs**: Assign section IDs and nav tab labels based on the sections you planned. The 3-tab nav (Value / Fit / Trends) is the default; adjust if you changed the section structure.

## Phase 3 — Compose the HTML
Build the final HTML file using the **Page Scaffold**, **Section Shell**, and **Component Catalog** from the Design System Reference:
1. Start with the Page Scaffold (doctype, head, CSS variables, top bar, bottom nav, JS). **Apply the chosen theme** by replacing the `:root` block and Google Fonts `<link>` with the values from the selected theme file, and appending any Component Overrides CSS from the theme.
2. For each planned section, use the Section Shell pattern and fill it with chosen components.
3. Populate each component with content rewritten from the markdown files (see Content Guidelines below).
4. Save the final output as `./pages/landing_page_[prospect-slug].html` in the project root.

## Content Guidelines
- **Headlines**: Derive punchy, 6-10 word headlines from the markdown content — do not use the markdown headers verbatim.
- **Body copy**: Rewrite for scannability. Use short sentences, no jargon, and active voice.
- **Challenges section**: Each challenge card must include Pain, Solution, and ROI rows. Rewrite for scannability.
- **Outcomes**: Extract quantifiable metrics from the Expected ROI values. If the markdown uses qualitative language (e.g. "measurable reduction"), infer a reasonable metric. Keep the copy concise and scannable.
- **CTAs**: Each section should end with a contextual call-to-action that leads the reader forward.

## Output Requirements
- The output must be a **single self-contained HTML file** with all CSS and JS inline (no external dependencies except Google Fonts).
- The page must render correctly on mobile (375px width) and desktop.
- The bottom navigation must highlight the active section on scroll.
- All `.r` (reveal) elements must animate in on scroll.

## Checklist
- [ ] Design theme selected and applied (`:root` variables + fonts + component overrides)
- [ ] Page loads and renders correctly with the chosen theme
- [ ] Bottom nav correctly highlights active section and switches on scroll
- [ ] All cards are populated with personalised content (no placeholder tokens remain)
- [ ] Contact section has correct email (and phone if provided)
- [ ] Page is readable in under 3 minutes

# Step-5: Upload landing page & generate QR code
With the landing page HTML generated in Step-4, deploy it to IPFS using pinme CLI and create a QR code that links directly to the live site.

## Phase 1 — Deploy with pinme:
```bash
npx pinme upload ./pages/landing_page_[prospect-slug].html
```
This returns a URL like `https://pinme.eth.limo/#/preview/...`

If `npx` or `pinme` isn't available, show the user this command and explain they can run it after downloading the file. You can also suggest alternatives: Netlify Drop (drag-and-drop at netlify.com/drop), or GitHub Pages.

## Phase 2 — Extract URL
1. Capture the **full terminal output** from the upload command.
2. **Extract the site URL** — this is the direct site URL that renders the page (e.g. `https://*.pinit.eth.limo` or similar gateway URL shown in the output). **Do NOT use the preview page URL** (`https://pinme.eth.limo/#/preview/...`) — the user needs the direct site URL.
   - Look for the live site URL/link in the upload CLI output.
   - If site URL is not present, use a sub-agent (with cheaper model like Haiku or Minimax) to extract the live site URL by using agent-browser to browse the preview URL and extract the live site URL (look for "site link" in the preview page).

## Phase 4 — Generate QR code
1. Create the `./qr_codes` directory if it does not exist.
2. Run the QR code generation script:
   ```
   python3 ./references/scripts/generate_qr.py "<site_url>" "./qr_codes/qr-<prospect-slug>.png"
   ```
   Replace `<site_url>` with the direct site URL extracted in Phase 3, and `<prospect-slug>` with the prospect's slug used throughout the skill.

## Phase 5 — Report results
Return the following to the user:
- **Live site URL** (the direct site URL)
- **QR code file path** (`./qr_codes/qr-<prospect-slug>.png`)

## Checklist
- [ ] pinme CLI working
- [ ] landing page is generated at `./pages/landing_page_[prospect-slug].html`
- [ ] `pinme upload` completes successfully
- [ ] Direct site URL (not preview URL) is extracted from the output
- [ ] QR code PNG is saved to `./qr_codes/qr-<prospect-slug>.png`
- [ ] User is shown the live site URL and QR code path