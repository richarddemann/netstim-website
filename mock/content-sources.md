# Content provenance — 11 September 2026

`publications-data.js` is a complete snapshot of all 204 top-level records in the public **Netstim Publications** Zotero group (ID 5249585), the group referenced by the original NetStim publications page. It contains 202 journalArticle records and two preprint records. It is not an independent audit of all publications by every lab member.

- Lab source: https://www.netstim.org/research-interests/publications/
- Public library: https://www.zotero.org/groups/5249585/netstim_publications
- API: https://api.zotero.org/groups/5249585/items/top?format=json&limit=100&sort=date&direction=desc
- Retrieved pages at start=0, 100 and 200. API `total-results` was 204; 204 unique item keys retrieved.
- Six pairs share the same DOI; six records have no date. These source metadata irregularities are retained. Render a missing year as “Undated”, never “null”. Do not describe the source records as 204 distinct papers.
- Titles, authors, journal names, dates and DOI/item links are source metadata. Preprints retain their item type. Displaying “et al.” can shorten long author lists while full names remain searchable.

`content-data.js` contains:

- All nine currently listed connectome entries, including source download/repository/citation links, from https://www.netstim.org/research-interests/normative-connectomes/ . Download targets are preserved; archives were not downloaded or validated. Population and space constraints remain in descriptions.
- Research overview and DBS methods adapted from https://www.netstim.org/research-interests/ and https://www.netstim.org/research-interests/deep-brain-stimulation/ . The old undated download count and institution count are omitted. The book, atlases, methods, posters and talks remain accessible in resources.
- Journal-club location, 4 PM schedule, signup link and all eight dated past-session entries from https://www.netstim.org/research-interests/stimu-latte/ . The page’s early October/November 2025 dates are retained exactly despite its general Wednesday description. Do not infer future dates from this archive.
- Jobs wording based on https://www.netstim.org/about-us/jobs/ . Its “Currently no open posts” status is reported as the live page’s statement, not independent vacancy confirmation. The potentially stale Berlin funding-program suggestion is omitted, pending confirmation.

Existing local people data and photos are managed separately. Current membership and roles still require institutional confirmation before publication. This is a local review mockup, not a deployment.

The content snapshot also includes all **26 poster entries** (titles, presenter/conference labels, full image links and PDF links where supplied) from https://www.netstim.org/research-interests/posters/ and all **seven video/talk entries** with the original YouTube/Vimeo URLs from https://www.netstim.org/research-interests/videos-talks/ . Poster affiliations and long reference lists remain in the linked original poster files rather than being duplicated in the browsing list. Videos are linked directly, avoiding automatic third-party embeds. One source date reads 07.09.2021 beside a 2019 workshop; it is retained and should be checked before publication. Original poster HTML contains duplicate anchor IDs; the mock should use local array indexes/unique slugs instead of copying those IDs.
