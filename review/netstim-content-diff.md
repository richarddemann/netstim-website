# NetStim — actual text comparison

Left: text extracted from the public HTML. Whitespace is normalised; wording is preserved. Right: proposed text. Review notes are separate.


## Home · Introduction

```diff
--- Current
+++ Proposed
@@ -1,9 +1,3 @@
-DEAR READER,
+Institute for Network Stimulation
 
-Welcome to the website of the Institute for Network Stimulation – which is based at the University Hospital Cologne.
-
-We are a scientific group with interest in neuroimaging, methods development, movement disorders and invasive brain stimulation.
-
-The goal of our research is to analyse and modulate brain networks to improve clinical treatment in neurological and psychiatric brain disorders.
-
-The primary tools we use to pursue these goals are structural imaging and noninvasive connectivity measures derived from functional and diffusion weighted MRI.
+We study how brain networks respond to stimulation and how these responses relate to neurological and psychiatric symptoms. Our group is based at University Hospital Cologne. We use structural and functional MRI, diffusion imaging and computational modelling to investigate these questions.
```

Optional rewrite of the introduction. The software paragraph is compared separately below; no surrounding text is silently omitted from the proposed passage.
[Source](https://www.netstim.org/)

## Site-wide · Page title

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-Network Stimulation Laboratory
+NetStim — Institute for Network Stimulation
```

Formal site name only; individual page prefixes remain unchanged.
[Source](https://www.netstim.org/)

## Home · Past funding

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-Past funding includes grants from the German Research Council, the Dystonia Research Foundation, the Berlin Institute of Health, Stiftung Charite, the Thiemann Foundation for Parkinson’s Disease Research, the Foundation for OCD research (FFOR), the German Research Council and the EU Joint Programme – Neurodegenerative Disease Research (JPND).
+Past funding includes grants from the German Research Council, the Dystonia Research Foundation, the Berlin Institute of Health, Stiftung Charite, the Thiemann Foundation for Parkinson’s Disease Research, the Foundation for OCD research (FFOR) and the EU Joint Programme – Neurodegenerative Disease Research (JPND).
```

Remove only the repeated funder. Current grant status still needs confirmation.
[Source](https://www.netstim.org/)

## People · Andreas’s opening

```diff
--- Current
+++ Proposed
@@ -1 +1,3 @@
+Andreas is Schilling Professor for Computational Neurology at the University of Cologne, where he took up his appointment in May 2025. His research focuses on brain connectivity and deep brain stimulation.
+
 Before bringing to life the NetStim Lab in April 2019, Andreas worked as a postdoc at the Laboratory for Brain Network Imaging and Modulation headed by Prof. Michael Fox at Harvard. Prior to that, he completed an MD/PhD with Prof. Andrea Kühn in the Movement Disorders and Neuromodulation Section at Charité Berlin, conjointly with a scientific appointment at the laboratory of Prof. Felix Blankenburg (Bernstein Center for Computational Neuroscience / Max Planck Institute for Human Development). Andreas also holds a Dr. med., which he obtained under the guidance of Prof. Cornelius Weiller in Freiburg. As a PI he is affiliated with the PhD program of the Einstein Center for Neurosciences Berlin and the International Graduate Program Medical Neurosciences at Charité Berlin, and teaches medical as well as postgraduate-level courses.
```

Insert the current appointment before the existing history. No training history or personal details are removed. Continuing Berlin affiliations still need confirmation.
[Source](https://www.netstim.org/about-us/about-us/)

## Andreas page · Scientific focus

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-Andreas has spent the last five years including a PhD on developing and improving methods to analyse brain stimulation sites and how their whole brain effects are mediated via distributed structural and functional networks. To facilitate this work, he developed an openly available software toolbox to localise deep brain stimulation electrode placement based on postoperative imaging (lead-dbs.org / leadsuite.io). The software is now developed by a multi-institutional team and is used by over one thousand scientists on all continents (>7000 downloads). The software was awarded by the Max Rubner Prize of Stiftung Charité, the Robert Koch Prize of Charité Berlin and an Academic Ventures grant of Harvard Radcliffe Institute for Advanced Studies.
+Andreas develops methods to reconstruct brain stimulation sites and study their structural and functional connections with the rest of the brain. To facilitate this work, he developed an openly available software toolbox to localise deep brain stimulation electrode placement based on postoperative imaging (lead-dbs.org / leadsuite.io). The software is now developed by a multi-institutional team. The software was awarded by the Max Rubner Prize of Stiftung Charité, the Robert Koch Prize of Charité Berlin and an Academic Ventures grant of Harvard Radcliffe Institute for Advanced Studies.
```

Replace the relative time window and remove undated usage numbers; preserve the development history and awards.
[Source](https://www.netstim.org/about-us/about-us/andreashorn/)

## Jobs · Unsolicited applications

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-We are always open for unsolicited applications if you’d like to join our team e.g. with a personal grant or other types of funding. For instance, Andreas Horn is PI at the Einstein Center for Neurosciences and the Medical Neurosciences PhD programs in Berlin that offer the possibility to apply for funding. Just contact us and we may find a good way.
+If you would like to join the lab with your own fellowship or other funding, please get in touch to discuss a possible project in Cologne.
```

Proposed wording, pending confirmation of hosting capacity, application contact and any continuing Berlin programme arrangements.
[Source](https://www.netstim.org/about-us/jobs/)

## DBS · Introduction

```diff
--- Current
+++ Proposed
@@ -1 +1,5 @@
-The main focus of our work is deep brain stimulation (DBS) – predominantly in movement disorders such as Parkinson’s Disease, Essential Tremor or Dystonia – more rarely in cognitive disorders such as Depression or Alzheimer’s Disease. In DBS, electrodes are surgically implanted into deep (subcortical) areas of the brain and – using an implanted impulse generator – these structures are stimulated chronically. The figure below shows a reconstruction of two DBS leads implanted with target subthalamic nucleus (orange) to treat Parkinson’s Disease.
+We investigate how the location of deep brain stimulation and its connections to other brain regions relate to clinical outcomes. We reconstruct electrode locations from postoperative imaging and use structural and functional connectivity to study the networks associated with improvement in symptoms.
+
+Our work also asks how stimulation of a small brain region affects activity across a wider network.
+
+In DBS, electrodes are surgically implanted into deep (subcortical) areas of the brain and – using an implanted impulse generator – these structures are stimulated chronically. The figure below shows a reconstruction of two DBS leads implanted with target subthalamic nucleus (orange) to treat Parkinson’s Disease.
```

The alternative replaces the research-scope sentences and retains the procedure explanation and figure caption. The change in emphasis is editorial, not a claim that the former conditions are no longer studied.
[Source](https://www.netstim.org/research-interests/deep-brain-stimulation/)

## DBS · Undated statistics

```diff
--- Current
+++ Proposed
@@ -1 +0,0 @@
-At the time of writing, Lead-DBS was downloaded over 65,000 times by researchers world-wide and currently, groups from over 20 institutions contributed to Lead-DBS code & content.
```

Delete this paragraph. Keep the download link, contributor link and preceding awards paragraph.
[Source](https://www.netstim.org/research-interests/deep-brain-stimulation/)

## Connectomes · Applications

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-Normative connectomes cannot replace patient/subject-specific connectivity information but are useful in scenarios where subject-specific data is not available and cannot be acquired. This often includes clinical applications such as:
+Normative connectomes describe connectivity in a group of subjects. We use them when individual connectivity data are unavailable, while recognising that they do not capture the connectivity of a particular patient. This often includes clinical applications such as:
```

Retain the following application list. Its separate statement about postoperative MRI still needs clinical review.
[Source](https://www.netstim.org/research-interests/normative-connectomes/)

## Book · Opening

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-We are excited that our book on connectomic deep brain stimulation can now be ordered from the publisher (Academic Press) and/or Amazon etc.
+Our book, Connectomic Deep Brain Stimulation, covers electrode localisation, stimulation modelling and brain connectivity, with chapters contributed by researchers working in these areas. The book is available from the publisher (Academic Press) and Amazon.
```

Keep the existing publisher and retailer links on their names and retain the contributor paragraphs below.
[Source](https://www.netstim.org/research-interests/the-book/)

## Stimu-Latte · Introduction

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-We are proud to present our new in-person journal club series: Stimu-latte! This post-doc-run journal club takes place once a month on Wednesdays at 4:00 PM. We will gather in a friendly environment and discuss the latest developments on neuromodulation over a cup of coffee. Neuromodulation enthusiasts from all career levels are welcome! On this page, you can find upcoming and previous sessions. Looking forward to stimulating discussions!
+Stimu-Latte is our monthly journal club in Cologne. We meet to discuss papers on neuromodulation over coffee. Everyone with an interest in the topic is welcome. Sign up to the mailing list for session announcements.
```

The organiser should confirm the schedule. Keep the location and session list below; this comparison covers the introduction only.
[Source](https://www.netstim.org/research-interests/stimu-latte/)

## People · Benjamin’s repeated paragraphs

```diff
--- Current
+++ Proposed
@@ -1,7 +1 @@
 At the Institute for Network Stimulation, his research is supported by DFG funding, giving him the opportunity to focus on his main area of interest, the development of personalized protocols in TMS. He is interested in how individualized brain mapping and circuit dynamics can guide stimulation targeting and improve treatment response. Benjamin has played tennis since the age of four, competed in teams for years and trained as a coach, though he makes it onto the court only occasionally these days. He also enjoys reading other than scientific articles, or listening to audiobooks and podcasts. He particularly enjoys traveling to France and generally to the sea. Occasionally, he tries to recall his childhood piano lessons, only to give up in frustration.
-
-At the Institute for Network Stimulation, his research is supported by DFG funding, giving him the opportunity to focus on his main area of interest, the development of personalized protocols in TMS. He is interested in how individualized brain mapping and circuit dynamics can guide stimulation targeting and improve treatment response.
-
-Benjamin has played tennis since the age of four, competed in teams for years and trained as a coach, though he makes it onto the court only occasionally these days. He also enjoys reading other than scientific articles, or listening to audiobooks and podcasts. He particularly enjoys traveling to France and generally to the sea. Occasionally, he tries to recall his childhood piano lessons, only to give up in frustration.
-
-Benjamin has played tennis since the age of four, competed in teams for years and trained as a coach, though he makes it onto the court only occasionally these days. He also enjoys reading other than scientific articles, or listening to audiobooks and podcasts. He particularly enjoys traveling to France and generally to the sea. Occasionally, he tries to recall his childhood piano lessons, only to give up in frustration.
```

The repeated paragraphs are in the retrieved live HTML and local mock. Remove the extra copies while keeping the first complete research and hobbies paragraph. This corrects the earlier claim that the duplication was local only.
[Source](https://www.netstim.org/about-us/about-us/)

## Home · Lead-DBS paragraph

```diff
--- Current
+++ Proposed
@@ -1 +1 @@
-As a methodological “backbone” of our work, together with others, we develop an open-source software called Lead-DBS. Lead-DBS is a toolbox facilitating Deep Brain Stimulation electrode reconstructions and computer simulations based on postoperative MRI & CT imaging.
+Together with collaborators, we develop Lead-DBS, an open-source toolbox for reconstructing DBS electrodes and modelling stimulation from postoperative MRI and CT images.
```

Separate comparison of the existing software paragraph. The normative-connectome paragraph that follows is retained.
[Source](https://www.netstim.org/)

### Review note: Home — Publication highlights

Keep the heading “Publications”. Add a small selection of papers above the full list, with authors, title, journal and year. Label preprints. The journal list can be shortened once the papers are in place.
The problem is that readers cannot readily see the work. There is no need to replace the section with promotional summaries.

### Review note: People — Aysu: conflicting career stages

Ask Aysu to confirm the opening sentence and the passages about completing her PhD. Then correct those passages together; leave the research description and personal paragraph intact.
The page gives incompatible career stages. A polished workaround would hide the problem rather than resolve it.

### Review note: People — Helen: location and project stage

Ask Helen whether the Boston affiliation, thesis description and degree information are still current. Update only the passages that have changed.
A 2023 arrival date is valid history. The unresolved issue is the present-tense description.

### Review note: People — Short biographies

Keep the short entries. Add a research sentence if each person wants one; confirm Michael’s role.
A short biography is not an outdated biography. Equal paragraph lengths are unnecessary.

### Review note: People — Remaining roster

Keep the current biographies and alumni list. Correct individual roles when members report a change.
Preserve personal details, including Pepsi. Do not rewrite the whole roster into a standard template.

### Review note: Andreas page — Duplicate biography and profile links

Update this page alongside the People biography. Check the CV and profile links, and ask Andreas which contact link he wants displayed.
A separate detailed biography can be useful. It does not have to be removed merely because a shorter biography exists.

### Review note: Jobs — Vacancy status

Confirm whether there are open positions. If there are none, keep the existing sentence. If there are, replace it with the position titles and application links.
The wording itself is fine; the vacancy status needs checking.

### Review note: Jobs — Culture and software expectations

Keep the description of code, documentation, testing and teaching contributions. Ask whether the expectation still applies to every role. Explain “teal organization” only if it remains a useful description of how the lab works.
Specific expectations are more useful than a newly invented culture paragraph.

### Review note: DBS — Release narrative

Keep “Lead-DBS 3.0” as a dated release story. Add a link to current release information and, separately, the 2026 Lead-DBS 4.0 poster.
A conference poster is evidence of work on that version, not confirmation of a public stable release.

### Review note: DBS — Awards and methods

Keep the dated awards and methods papers. Add recent methods where they belong in the account of the research.
Do not rename everything “Earlier milestones” or imply that an older method is obsolete.

### Review note: Connectomes — Catalogue currency

Keep the dataset list, citations and download links.
The list already contains newer resources. It needs maintenance, not a rewritten introduction.

### Review note: Connectomes — Version and installation guidance

Check each version label and installation instruction against its dataset repository. Add missing information about template space, licence or citation where users need it.
Keep this as a resource-maintenance task, not proposed website prose.

### Review note: Publications — Bibliography visibility

Check that the bibliography loads in a browser and includes the intended recent papers. Keep a direct link to the source library if the embedded list fails.
The text retrieval did not establish that the widget is broken. Fix a confirmed display problem before redesigning the bibliography.

### Review note: Posters — 2026 work

Keep the 2026 posters and their original affiliations. Add a journal-paper link when a corresponding paper is available.
Preserve the distinction between conference work and published articles.

### Review note: Videos & Talks — Archive framing

Keep “Videos & Talks” and the dates. Add newer recordings when available.
There is no reason to call the section an archive just because its recordings are older.

### Review note: Videos & Talks — Conflicting event date

Check the recording or programme and correct the conflicting year.
Do not guess whether the date or event label is wrong.

### Review note: Stimu-Latte — Weekday consistency

Ask the organisers whether the two Tuesday dates were exceptions or errors. Correct the dates or the recurring weekday description accordingly.
Retain the session history.

### Review note: Updates — Latest-news freshness

Keep “Updates” and the dated posts. Ask the team which developments since September 2025 should be added.
The news list needs attention, but its age does not justify a compulsory rename to “News archive”.

### Review note: Onboarding — Current location

No location edit needed. The directly retrieved page already says Cologne.
The previous finding came from older web retrieval. Superseded by the direct page snapshot.

### Review note: Site-wide — Legacy destinations

Check the old-domain links and update destinations where needed. Keep working redirects.
A link using netstim.berlin may still work.

### Review note: Privacy — Policy and cookie descriptions

Ask the site owner to check that the privacy text and cookie list describe the services actually in use, and remove duplicate entries.
No replacement legal text is proposed.

### Review note: Local mock — Selected papers versus full coverage

Keep the prototype’s selected papers labelled as a selection. Restore links to the full bibliography, posters, book, talks and updates when developing the site further.
The mock should not accidentally drop the lab’s existing material.
