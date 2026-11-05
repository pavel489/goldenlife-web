from pathlib import Path
import json, re, requests, time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import tempfile
ROOT=Path(__file__).resolve().parents[1]; REPO=ROOT; OUT=Path(tempfile.mkdtemp(prefix='gl-reader-tables-'))
print('Evidence directory:',OUT,flush=True)
CONFIG=[('slim','golden-life-darkovy-box-collagen-slim'),('beauty','darkovy-box-collagen-beauty'),('hormonal','golden-life-darkovy-box-hormonal-balance'),('longevity','golden-life-darkovy-box-longevity'),('ufirst','ufirst-darkovy-box')]
LOADER=(REPO/'assets/giftbox-detail-loader.js').read_bytes()
RESULTS=[];SOURCES={}
OVERLAYS='''() => {const hide=()=>{document.querySelectorAll('iframe,#cboxOverlay,#colorbox,.newsletter-popup,.cookie-bar,.consents,.smartsupp-widget,#supportBoxWebChat,.supportbox-widget,[id*=supportbox],[id*=supportBox],#heurekaTab,[id*=smartlook]').forEach(e=>e.style.setProperty('display','none','important'));for(const e of document.querySelectorAll('body>*'))if(e.shadowRoot && /cookie|consent|support|chat/i.test(e.id+' '+e.className))e.style.setProperty('display','none','important')};hide();new MutationObserver(hide).observe(document.body,{childList:true,subtree:true});}'''
METRICS='''() => {const h=document.querySelector('[data-gl-reader-content]'),s=h.shadowRoot,r=h.getBoundingClientRect();return {status:document.querySelector('[data-gl-reader-status]').textContent,hostWidth:r.width,overflow:h.scrollWidth-h.clientWidth,text:s.textContent.replace(/\\s+/g,' ').length,forbidden:s.querySelectorAll('script,form,.cta-box,.add-to-cart-button').length,tables:[...s.querySelectorAll('table')].map(t=>({display:getComputedStyle(t).display,width:t.getBoundingClientRect().width,body:t.tBodies[0]?.getBoundingClientRect().width,wrap:t.parentElement.className,scrollWidth:t.parentElement.scrollWidth,clientWidth:t.parentElement.clientWidth,cells:[...t.querySelectorAll('th,td')].map(c=>c.textContent.trim()),outOfHost:t.parentElement.getBoundingClientRect().right-r.right}))}}'''
def wait(p):
 try:
  p.wait_for_function("document.querySelector('[data-gl-reader-content]').shadowRoot?.querySelector('table, p') && !document.querySelector('[data-gl-reader-content]').hasAttribute('aria-busy')",timeout=45000)
 except Exception:
  print(p.evaluate("({status:document.querySelector('[data-gl-reader-status]').textContent,html:document.querySelector('[data-gl-reader-content]').shadowRoot?.innerHTML.slice(0,500),scripts:[...document.scripts].map(s=>({src:s.src,integrity:s.integrity})).filter(s=>/giftbox/.test(s.src))})"),flush=True)
  p.screenshot(path=str(OUT/'failure.png'));raise
def capture(p,name):
 p.add_style_tag(content='html,body,*{scroll-behavior:auto!important}.siteCookies,[id^="hw-"]{display:none!important}')
 p.evaluate("document.querySelectorAll('body *').forEach(e=>{if(getComputedStyle(e).position==='fixed'&&!e.closest('.basic-description'))e.style.setProperty('display','none','important')})")
 p.locator('[data-gl-reader-content]').locator('table').first.screenshot(path=str(OUT/name),timeout=15000)
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,args=['--no-sandbox'])
 for key,slug in CONFIG:
  url=f'https://www.golden-life.cz/{slug}/'
  resp=requests.get(url,timeout=45);resp.raise_for_status();(OUT/(key+'-live.html')).write_text(resp.text)
  soup=BeautifulSoup(resp.text,'html.parser');area=soup.select_one('.basic-description');assert area
  original=area.decode_contents();delivered=(REPO/'shoptet'/f'{key}.html').read_text()
  # Whole public parent retained; only long-description field is overridden for tests.
  area.clear();area.append(BeautifulSoup(delivered,'html.parser'));testhtml=str(soup)
  ctx=browser.new_context(viewport={'width':1440,'height':1000},device_scale_factor=1)
  def route(r):
   u=r.request.url
   if u==url and r.request.resource_type=='document':return r.fulfill(status=200,content_type='text/html',body=testhtml)
   if '/assets/giftbox-detail-loader.js' in u:return r.fulfill(status=200,content_type='application/javascript',headers={'Access-Control-Allow-Origin':'*'},body=LOADER)
   if any(x in u for x in ['clarity.ms','googletagmanager','google-analytics','facebook','supportbox','smartsupp','lhinsights','seznam','bing.com','heureka','productwidgets','dklab','additional-sale','openai.com','ecmtr','partner.golden','shop-factory','fvstudio','honzabartos']):return r.abort()
   return r.continue_()
  ctx.route('**/*',route);p=ctx.new_page();p.goto(url,wait_until='domcontentloaded',timeout=60000);p.evaluate(OVERLAYS)
  buttons=p.locator('[data-gl-source-url]');assert buttons.count()==5
  for width in [1440,390,320]:
   p.set_viewport_size({'width':width,'height':1000});p.wait_for_timeout(250)
   for i in range(5):
    b=buttons.nth(i);identity=b.get_attribute('data-gl-source-id');b.click(timeout=15000);wait(p)
    assert b.get_attribute('aria-expanded')=='true'
    m=p.evaluate(METRICS);m.update(box=key,width=width,id=identity,button=i)
    source_url=b.get_attribute('data-gl-source-url')
    if source_url not in SOURCES:
     source=requests.get(source_url,timeout=45);source.raise_for_status();(OUT/f'source-{identity}.html').write_text(source.text)
     src=BeautifulSoup(source.text,'html.parser').select_one('.basic-description')
     SOURCES[source_url]=[[c.get_text().strip() for c in t.select('th,td')] for t in src.select('table')]
    assert [t['cells'] for t in m['tables']]==SOURCES[source_url],('table values changed',key,identity)
    # Recreate the former TABLE display:block treatment only in the test DOM.
    p.evaluate("document.querySelector('[data-gl-reader-content]').shadowRoot.querySelectorAll('.gl-reader-table').forEach(w=>{const t=w.firstElementChild;w.replaceWith(t);t.classList.add('gl-reader-table')})")
    old=p.evaluate(METRICS)
    if key=='slim' and identity=='464' and width==1440:capture(p,'pred-opravou-1440.png')
    p.evaluate("document.querySelector('[data-gl-reader-content]').shadowRoot.querySelectorAll('table.gl-reader-table').forEach(t=>{t.classList.remove('gl-reader-table');const w=document.createElement('div');w.className='gl-reader-table';w.tabIndex=0;w.setAttribute('role','region');w.setAttribute('aria-label','Tabulka produktu – lze posouvat');t.before(w);w.append(t)})")
    m['previousOverflow']=old['overflow'];m['previousTableWidths']=[{'width':t['width'],'body':t['body']} for t in old['tables']]
    assert m['overflow']<=old['overflow']+2,('new horizontal overflow',m)
    assert 'Podrobnosti ze stránky' in m['status'], m
    assert m['forbidden']==0,m
    for t in m['tables']:
     assert t['display']=='table',m
     assert t['wrap']=='gl-reader-table',m
     assert abs(t['width']-t['body'])<6,m
     assert t['outOfHost']<=2,m
    RESULTS.append(m);(OUT/'results.json').write_text(json.dumps(RESULTS,ensure_ascii=False,indent=2))
    if key=='slim' and identity=='464' and width in [1440,390]:capture(p,f'po-oprave-{width}.png')
   # Close, reopen (cached), close via Escape. Real pointer buttons.
   p.locator('[data-gl-reader-close]').first.click();assert p.locator('[data-gl-reader]').is_hidden()
   buttons.first.click();wait(p);assert buttons.first.get_attribute('aria-expanded')=='true'
   p.locator('[data-gl-reader-title]').press('Escape');assert p.locator('[data-gl-reader]').is_hidden()
  ctx.close();print(key,'OK',flush=True)
 browser.close()
print(json.dumps({'cases':len(RESULTS),'tables':sum(len(x['tables']) for x in RESULTS),'boxes':len(CONFIG),'widths':[1440,390,320]},indent=2))
