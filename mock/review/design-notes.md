# Visual references and implementation

## Visually inspected

- Arc Institute, https://arcinstitute.org/: homepage viewed from introduction through research, model, recruitment, newsletter and footer. Open research rows with thin dividers, scientific images given their own space, broad blue sections. Implemented related row/section geometry; retained sans-serif instead of Arc's serif and monospaced accents.
- Notion, https://www.notion.com/: homepage viewed from hero through feature panels, testimonials and footer. Clear sans-serif size hierarchy, consistent gutters, restrained control shapes. Applied these to typography and controls without adding marketing claims or illustrated AI interface content.
- Chang Lab, https://changlab.ucsf.edu/: hero only. Browser failed before further scrolling; not treated as a fully inspected reference.

## User-supplied component references

- Beautiful UI: https://www.beautifului.dev/ — text catalogue reviewed; search, filter and disclosure primitives are relevant to the archives. AI chat, reasoning and streaming controls are not used.
- beUI: https://beui.dev/ — text catalogue reviewed; used as an interaction reference, with restrained transitions implemented locally.
- Rare UI: https://www.rareui.com/ — text catalogue reviewed; no decorative effects imported into the lab site.
- Transitions: https://transitions.dev/ — text catalogue reviewed; the route change uses a short opacity/5px entrance with reduced-motion opt-out.
- shadcn/ui: https://ui.shadcn.com/ — browser inspection attempted but blocked. Native search, select, dialog and filter controls are styled consistently. No claim of visually reproducing its current site or importing its React components.

These are reference relationships, not claims that the libraries were installed. The user requested a standalone working HTML mock. All page text and controls remain native HTML/CSS/JavaScript; anatomical figures are existing NetStim assets.

## Needs rendered review

The IAB policy check failed for the mock URL, including the final retry. Do not describe this revision as visually validated. Check all routes at desktop and 390px mobile, including header wrapping, portrait crops, bibliography pagination, dialog scrolling and poster loading, once browser access works.

## Follow-up review

Removed generic added slogans such as “Open tools. Shared progress.” and “Mapping the connections that matter.” They departed from the user's request to preserve the lab's voice and made the redesign feel like a generic marketing site. Replaced them with descriptive research headings.

Changed mobile scientific-focus rows to full-width images followed by text, rather than squeezing them into 100px thumbnails beside a narrow text column. Added an earlier tablet navigation collapse at 860px to preserve readable labels. Detail pages now highlight their parent navigation section.

Confirmed the local server had stalled and returned empty responses. Restarted it and verified HTTP200. This fixed the serving failure, but IAB still returned its policy-verification error. A full rendered review remains outstanding; no screenshot comparison is claimed.
