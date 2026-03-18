# Outreach Generator

Generate personalized B2B sales microsites from two URLs — the seller's product website and the prospect's company website. The output is a single, self-contained, mobile-first HTML file with a tailored pitch, value props, competitive insights, and a QR code for easy sharing.

## Installation

You can install this skill into your agent's workspace using:

```bash
npx skills add [YOUR_GITHUB_USERNAME]/snap-reach
```
*(Note: Replace `[YOUR_GITHUB_USERNAME]/snap-reach` with the actual GitHub repository path once published.)*

This will download `SKILL.md` and the `references/` directory into your agent's `.agents/skills/outreach-generator` folder.

## How to use `@outreach-generator`

Once installed, you can trigger the skill in your AI assistant by mentioning it and providing the seller and prospect URLs.

### Standard Prompting
Trigger the skill by simply asking it to create a sales page, providing your website and the prospect's website:

> "@outreach-generator Create a sales page for my meeting with [Prospect Name]. 
> Seller URL: https://www.yourcompany.com
> Prospect URL: https://www.prospect.com"

### Requesting a Specific Design Theme
By default, the skill will try to automatically match a theme to either the prospect's website or your brand's website. However, you can explicitly enforce a theme by including it in your prompt. 

Available themes:
* `midnight_blue` (Default - Dark/Blue: Best for Tech, SaaS, AI, consulting)
* `clean_frost` (Light/Cyan: Best for Modern SaaS, fintech, health)
* `luxury_noir` (Dark/Gold: Best for luxury, fashion, premium brands)
* `corporate_trust` (Light/Navy: Best for enterprise, finance, legal)
* `warm_earth` (Light/Green: Best for wellness, food, organic, retail)
* `vibrant_tech` (Dark/Neon Green: Best for startups, gaming, dev tools)

**Prompt Example:**
> "@outreach-generator I'm visiting [Company] next week — help me prepare something to show them. Make sure to use the **luxury_noir** design theme.
> Seller: https://www.seller.com
> Prospect: https://www.prospect.com"

### Advanced Prompting Tips
* **Add Context:** If you know specific challenges the prospect is facing that aren't obvious on their website, include them in the prompt (e.g., *"Focus on their recent supply chain issues mentioned in the news."*).
* **Define the Outcome:** Specify if you want to push for a specific next step, like a *"Technical Discovery Call"* or a *"Free Audit"*.
* **QR Codes:** The skill automatically deploys the site to IPFS and generates a QR code. Ask the agent for the QR code image path if you want to embed it in a presentation.

---

## Folder Structure

When packaging this for distribution, ensure the following structure is maintained so the agent can find all templates:

```text
├── SKILL.md                          # The core agent instructions
└── references/
    ├── landing_page_template.md      # The component catalog
    ├── prospect_research.md          # Research sub-agent instructions
    ├── scripts/
    │   └── generate_qr.py            # Used for the QR code step
    └── design_themes/                # CSS variable overrides
        ├── clean_frost.md
        ├── corporate_trust.md
        ├── luxury_noir.md
        ├── midnight_blue.md
        ├── vibrant_tech.md
        └── warm_earth.md
```
