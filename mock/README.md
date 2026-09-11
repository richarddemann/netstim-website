# NetStim website mockup

Open index.html directly in a browser. No installation or build is required. To serve it locally: `python3 -m http.server 8876 --bind 127.0.0.1` from this directory.

## Included

12 complete local routes: Home, Research, Deep Brain Stimulation, People, Publications, Resources, Normative Connectomes, Join Us, Stimu-Latte, Contact, Conference Posters, and Videos & Talks.

- 39 people: 15 current profiles and 24 alumni, with search, group filters and biography dialogs.
- Public Zotero snapshot: 204 records, displayed as 198 entries after repeated links are removed; year filtering, text search, author disclosure, pagination, and undated records.
- 9 connectomes with source citations, download links and available installation/version information.
- 26 conference posters with local display images and original PDF/image destinations.
- 7 video/talk destinations and 8 journal-club sessions.
- Local assets, responsive navigation and grids, keyboard focus states, reduced-motion support and a missing-page state.

External downloads, videos, institutional links and application information remain external destinations. The mock does not submit applications or collect data. It has no analytics, cookies, embedded third-party video or backend.

## Visual revision

Original NetStim logo; white and pale-blue backgrounds; a blue Lead-DBS section; conventional system sans-serif throughout. The revised homepage uses open figure/text rows and section spacing informed by direct visual inspection of Arc's full homepage, plus Notion's sans-serif hierarchy. Team portraits use consistent proportions and unframed names; the PI appears first, with administration and alumni grouped separately.

The supplied component sites are documented in review/design-notes.md. This static mock uses native HTML controls and small CSS/JS interactions, not React packages. No decorative fonts, AI-chat widgets or simulated scientific animation were added.

## Content status

Sources retrieved September 11, 2026. See content-sources.md and ../content-audit.md. The bibliography is a full snapshot of the source library, not a claim to include every publication by every lab member. Original individual biographies can still contain outdated roles; the current Cologne leadership introduction is source-audited. Dates on archived source content are retained. Vacancies and legal information require their responsible owners' review before publication.

## Verification

JavaScript syntax and DOM-based interaction checks pass for all 12 routes, local image paths, internal navigation, profile search/dialogs, publication search/year/pagination, connectome filters, poster search, archives, mobile-menu state, and the missing-page state.

Rendered desktop/mobile appearance, real-browser keyboard behavior and external link availability have not been fully verified. The built-in browser repeatedly returned an admin-policy verification error when opening the local preview. The responsive implementation is present; this is not a visual sign-off.
