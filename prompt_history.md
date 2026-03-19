<!-- This file is just a prompt history and scratch pad, don't read -->

# Refine

I want to make some changes to the Step-4 and the HTML template. 

Problem:
- The current way of generating the landing page is too rigid: it's just a fixed template with some placeholders. I want to make it more flexible and allow for more customization, that better fits the content and findings from Step-1 and Step-2.

Ask:
- I want you to refactor the Step-4 and the HTML template to generate an adaptive HTML landing page dynamically based on the content and structure of the findings from Step-1 and Step-2.
- Make sure the layout, content, and structure are all adaptive and can be generated dynamically based on the content and structure of the .md files from Step-1 and Step-2.

Things to keep:
- Keep the content rewrite guidelines and output requirements.
- I still like the general structure of sections in the current landing page. 

# Upload and QR
Now add another step to this Skill, to upload the generated landing page to a file hosting service, and generate a QR code for it. Then save the QR code `./qr_codes`

## Tools
- Read this tool called pinme, and understand how it works, I want the skill to use this to deploy the landing page. https://github.com/glitternetwork/pinme?tab=readme-ov-file#for-ai
- Use the `generate_qr.py` script in @refereces folder to generate a QR code for the landing page.

## tasks:
- Update the skill.md, use pinme to upload the site, and then find the url of the uploaded site, I need the site URL, not the preview page URL. Then use the `generate_qr.py` script to generate a QR code for the landing page. Finally, save the QR code `./qr_codes`

# Design improvement

Now I want to make some improvement to the design and generation of the landing page. 

1. Use ui-ux-pro-max skill, to generate a few design theme (i.e color, font, etc.) 
2. Update the prompt in SKILL.md to try pick a design theme based on the design and theme of the prospect's website. If it's not available, then try pick a theme using the seller's brand color and website's primary color. 

Requirements:
- Make a few design theme, and save them in the `design_themes` folder under the `references` folder.
- Make sure the landing_page_template.html can use these design themes to generate the landing page, driven by the updated SKILL.md prompt.
- Pick a default theme for the landing page in case a theme is not picked.

---

# finalise
Help me finalise a few things:
1. Help me publish or package it so that users can use install it using `npx skills add`
2. Write a README.md on how to use @beautifulMention, include how to best prompt it, and choose 

---

# Improve
I want to make the following improvement to the skill:

## Allow more user input:
Users can provide the following input which will be used to generate the prospect research and landing page:
1. Design theme: users can either choose a design theme, or say a few words about the style/design she wants to instruct the agent to pick a theme.
2. Information about the seller and prospect: instead of just providing the URLs, users can also provide the following information:
- linkedin profile URL, company website URL, company or product description, etc.
- when user gave company or product descriptions, the agent should use web search to identify the correct company and prospect, and use the information from web search to supplement the user's input.
3. Auto vs interative modes: users can specify whether they want the agent to ask questions and feedback at different steps, or just run in auto mode. In auto mode, the agent will execute all steps without asking for user feedback once it has enough initial input context. In interactive mode, users can provide feedback at each step to guide the agent's generation.

## Interactive mode: Separate the steps and allow user feedback
(This is only applicable if users choose interactive mode)
Interactive mode allows agent to ask clarifying questions and users to provide feedback at each step.
1. At any steps, if the agent think that it needs more information to produce better results, it should ask the user for clarification or feedback.
2. After Step 1, 2, 3, agent should concisely present the work done so far, and ask the user for feedback before proceeding to the next step. And user's feedback should be used to refine the work done so far.
(Note: In interactive mode, the agent should not ask for feedback after Step 4 and Step 5, as these are the final steps and the agent should have enough information to produce the final result.)
