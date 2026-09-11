from pathlib import Path
from bs4 import BeautifulSoup
import re,json,html,difflib
from editorial_revision import REFERENCES

root=Path(__file__).parent
old=json.loads((root/'findings.json').read_text())
def blocks(name):
    soup=BeautifulSoup((root/'source-snapshots'/f'{name}.html').read_text(),'html.parser')
    return [re.sub(r'\s+',' ',x.get_text()).strip() for x in soup.select_one('#main').select('h1,h2,h3,p') if x.get_text(strip=True)]
home=blocks('home');people=blocks('about-us_about-us');andy=blocks('about-us_about-us_andreashorn');jobs=blocks('about-us_jobs');dbs=blocks('research-interests_deep-brain-stimulation');book=blocks('research-interests_the-book');club=blocks('research-interests_stimu-latte');conn=blocks('research-interests_normative-connectomes')
entries=[]
def add(ids,title,before,after,note=''):
    row=old[ids[0]-1]
    entries.append(dict(ids=ids,title=title,before=before,after=after,note=note or row['why'],url=row['url'],references=row.get('references',[])))

# The compared scope is identical on both sides: complete affected paragraphs.
add([2],'Home · Introduction','\n\n'.join(home[1:6]),old[1]['after'].split('\n\nTogether with collaborators')[0], 'Optional rewrite of the introduction. The software paragraph is compared separately below; no surrounding text is silently omitted from the proposed passage.')
add([1],'Site-wide · Page title','Network Stimulation Laboratory','NetStim — Institute for Network Stimulation','Formal site name only; individual page prefixes remain unchanged.')
add([4],'Home · Past funding',home[17],home[17].replace('the Foundation for OCD research (FFOR), the German Research Council and','the Foundation for OCD research (FFOR) and'),'Remove only the repeated funder. Current grant status still needs confirmation.')
add([5],'People · Andreas’s opening',people[8],old[4]['after'].split('\n\n[')[0]+'\n\n'+people[8],'Insert the current appointment before the existing history. No training history or personal details are removed. Continuing Berlin affiliations still need confirmation.')
add([10,11],'Andreas page · Scientific focus',andy[6],re.sub(r'Andreas has spent the last five years including a PhD on developing and improving methods to analyse brain stimulation sites and how their whole brain effects are mediated via distributed structural and functional networks\.',old[9]['after'],andy[6]).replace(' and is used by over one thousand scientists on all continents (>7000 downloads)',''),'Replace the relative time window and remove undated usage numbers; preserve the development history and awards.')
add([14],'Jobs · Unsolicited applications',jobs[3],old[13]['after'].split('\n\n',1)[1],'Proposed wording, pending confirmation of hosting capacity, application contact and any continuing Berlin programme arrangements.')
add([16],'DBS · Introduction',dbs[2],old[15]['after']+'\n\n'+dbs[2][dbs[2].index('In DBS,'):],'The alternative replaces the research-scope sentences and retains the procedure explanation and figure caption. The change in emphasis is editorial, not a claim that the former conditions are no longer studied.')
add([17],'DBS · Undated statistics',dbs[8],'','Delete this paragraph. Keep the download link, contributor link and preceding awards paragraph.')
add([22],'Connectomes · Applications',conn[10],old[21]['after']+' This often includes clinical applications such as:','Retain the following application list. Its separate statement about postoperative MRI still needs clinical review.')
add([25],'Book · Opening',book[1],old[24]['after']+' The book is available from the publisher (Academic Press) and Amazon.','Keep the existing publisher and retailer links on their names and retain the contributor paragraphs below.')
add([28],'Stimu-Latte · Introduction',club[2],old[27]['after'],'The organiser should confirm the schedule. Keep the location and session list below; this comparison covers the introduction only.')
add([34],'People · Benjamin’s repeated paragraphs','\n\n'.join(people[68:72]),people[68],'The repeated paragraphs are in the retrieved live HTML and local mock. Remove the extra copies while keeping the first complete research and hobbies paragraph. This corrects the earlier claim that the duplication was local only.')
# Lead-DBS was included in the previous proposed introduction but absent from its comparison scope.
add([2],'Home · Lead-DBS paragraph',home[7],old[1]['after'].split('\n\n')[-1],'Separate comparison of the existing software paragraph. The normative-connectome paragraph that follows is retained.')

covered={i for e in entries for i in e['ids']}
notes=[]
for i,r in enumerate(old,1):
    if i in covered:continue
    r=dict(r)
    if i==31:
        r.update(before=blocks('internal_onboarding')[1],after='No location edit needed. The directly retrieved page already says Cologne.',why='The previous finding came from older web retrieval. Superseded by the direct page snapshot.',status='Keep')
    notes.append((i,r))

def diff(a,b):
    aa=re.findall(r'\s+|[^\s]+',a);bb=re.findall(r'\s+|[^\s]+',b)
    left=[];right=[]
    for op,i,j,k,l in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
        x=html.escape(''.join(aa[i:j]));y=html.escape(''.join(bb[k:l]))
        left.append(x if op=='equal' else ('<del>'+x+'</del>' if x else ''))
        right.append(y if op=='equal' else ('<ins>'+y+'</ins>' if y else ''))
    return ''.join(left),''.join(right)
parts=[];md=['# NetStim — actual text comparison','','Left: text extracted from the public HTML. Whitespace is normalised; wording is preserved. Right: proposed text. Review notes are separate.','','']
for n,e in enumerate(entries,1):
    left,right=diff(e['before'],e['after'])
    refs=''.join(f' · <a href="{html.escape(x[1])}">{html.escape(x[0])}</a>' for x in e['references'])
    parts.append(f'''<article><h2>{n:02d} · {html.escape(e['title'])}</h2><div class="cols"><section><h3>Current text</h3><div class="copy">{left}</div></section><section><h3>Proposed text</h3><div class="copy">{right or '<em class="empty">Paragraph removed; no replacement text.</em>'}</div></section></div><footer>{html.escape(e['note'])}<p><a href="{e['url']}">Original page</a>{refs}</p></footer></article>''')
    md += [f'## {e["title"]}','','```diff',*difflib.unified_diff(e['before'].splitlines(),e['after'].splitlines(),fromfile='Current',tofile='Proposed',lineterm=''),'```','',e['note'],f'[Source]({e["url"]})','']
notes_html=''
for i,r in notes:
    excerpt=''
    if i==6:excerpt=people[18]+'\n\n'+people[20]
    if i==13:excerpt=jobs[1]
    if i==15:excerpt=jobs[5]+'\n\n'+jobs[7]
    if i==31:excerpt=r['before']
    notes_html+=f'<div class="note"><h3>{html.escape(r["page"]+" · "+r["title"])}</h3>'+(f'<blockquote>{html.escape(excerpt)}</blockquote>' if excerpt else '')+f'<p>{html.escape(r["after"])}</p><small>{html.escape(r["why"])}</small> <a href="{r["url"]}">Source</a></div>'
    md += [f'### Review note: {r["page"]} — {r["title"]}','',r['after'],r['why'],'']
style='''*{box-sizing:border-box}body{margin:0;background:#f7f7f5;color:#253039;font:16px/1.65 system-ui,sans-serif}main{max-width:1350px;margin:auto;padding:36px 28px}h1{font-size:32px;line-height:1.2}h2{font-size:19px;padding:16px 22px;margin:0}h3{font-size:13px;margin:0 0 14px;color:#5b656c}article{background:white;border:1px solid #ccd2d6;border-radius:6px;margin:26px 0;overflow:hidden}.cols{display:grid;grid-template-columns:1fr 1fr}.cols section{padding:20px 24px;border-top:1px solid #dce0e2}.cols section+section{border-left:1px solid #dce0e2}.copy{white-space:pre-wrap}del{background:#ffdad7;text-decoration:line-through;text-decoration-color:#a33329}ins{background:#d5f0dc;text-decoration:none;border-bottom:1px solid #42985c}.empty{color:#6d747a}footer{border-top:1px solid #dce0e2;padding:14px 22px;font-size:14px;color:#59656d}footer p{margin:6px 0 0}a{color:#175978}.toolbar{display:flex;gap:10px;margin:20px 0;position:sticky;top:0;background:#f7f7f5;padding:10px 0}input,button{padding:10px;font:inherit;border:1px solid #bdc7cd;border-radius:4px;background:white}input{flex:1}.note{border-bottom:1px solid #ccd2d6;padding:20px 0}.note h3{font-size:17px;margin:0}.note p{margin:8px 0}blockquote{white-space:pre-wrap;margin:12px 0;padding:12px 18px;border-left:3px solid #bbc5ca;background:white}small{color:#59656d}details{margin:24px 0}summary{cursor:pointer;font-weight:600}.plain del,.plain ins{background:transparent;text-decoration:none;border:0}@media(max-width:750px){main{padding:20px 12px}.cols{grid-template-columns:1fr}.cols section+section{border-left:0}.toolbar{position:static;flex-wrap:wrap}}@media print{.toolbar{display:none}article{break-inside:avoid}main{padding:0}body{background:white}}'''
document='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NetStim — actual text diff</title><style>'+style+'</style><main><h1>Current text → proposed text</h1><p>Original passages on the left; their alternatives on the right. <del>Removed words</del> and <ins>added words</ins> are highlighted. Unchanged wording stays unmarked.</p><p><small>Original wording extracted directly from the public page HTML; whitespace normalised. The comparisons cover the complete affected paragraphs, not summaries. Nothing has been published.</small></p><div class="toolbar"><input id="search" placeholder="Find a page or passage…" aria-label="Find a page or passage"><button id="toggle">Hide highlights</button><button onclick="print()">Print / save PDF</button></div>'+''.join(parts)+f'<details><summary>Review notes — {len(notes)} items without a proposed text change</summary><p>These are checks or decisions, not text replacements. No invented copy is presented as an alternative.</p>'+notes_html+'</details><details><summary>Writing references</summary><ul>'+''.join(f'<li><a href="{u}">{html.escape(n)}</a> — {html.escape(t)}</li>' for n,u,t in REFERENCES)+'</ul></details></main><script>document.querySelector("#toggle").onclick=function(){document.body.classList.toggle("plain");this.textContent=document.body.classList.contains("plain")?"Show highlights":"Hide highlights"};document.querySelector("#search").oninput=function(){for(const a of document.querySelectorAll("article"))a.hidden=!a.textContent.toLowerCase().includes(this.value.toLowerCase())};</script></html>'
(root/'netstim-content-diff.html').write_text(document)
(root/'netstim-content-diff.md').write_text('\n'.join(md))
(root/'exact-comparisons.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
assert len(covered)+len(notes)==35
for e in entries:
    l,r=diff(e['before'],e['after'])
    assert html.unescape(re.sub(r'</?(?:del|ins)>', '', l))==e['before']
    assert html.unescape(re.sub(r'</?(?:del|ins)>', '', r))==e['after']
print(f'{len(entries)} actual text diffs; {len(notes)} separate notes; all 35 original items accounted for. Word-diff reconstruction verified.')
