from pathlib import Path
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio, json, re, hashlib, time

BASE=Path('/root/workspace/research/css-audit-1793883385')
OUT=Path(__file__).parent
FILES=[BASE/'step3/qa/pilotni-sablony-offline.html',Path(__file__).parent/'hormonal-tablet-oprava.html',BASE/'step4b-longevity/qa/longevity-pracovni-nahled.html',BASE/'step4c-slim/qa/slim-pracovni-nahled.html',BASE/'step4d-collagen-variants/qa/collagen-varianty-pracovni-nahled.html']
ROWS=[];ROUNDTRIPS=[];ERRORS=[];REQUESTS=[];SOURCES=[];CAPTURES=[]
METRICS='''() => {
const r=document.querySelector('#special-popis,#nad-popis'),s=document.querySelector('.preview-short');
const bad=[];for(const c of r.querySelectorAll('td,th')){const b=c.getBoundingClientRect();if(b.width<1)continue;const range=document.createRange();range.selectNodeContents(c);for(const a of range.getClientRects())if(a.width>1&&(a.left<b.left-2||a.right>b.right+2))bad.push(c.innerText)}
const banners=[...r.querySelectorAll('.nad-banner')].map(e=>({width:e.clientWidth,overflow:e.scrollWidth-e.clientWidth}));
const shortLabels=[...s.querySelectorAll('p,span,strong')].filter(e=>e.children.length===0&&e.checkVisibility({checkOpacity:true,checkVisibilityCSS:true})).filter(e=>e.scrollWidth>e.clientWidth+2&&getComputedStyle(e).display!=='inline').map(e=>e.textContent.trim());
const colors=[document.documentElement,document.body,r,r.querySelector('.nad-banner'),r.querySelector('.product-container p'),r.querySelector('.latky-teaser')].filter(Boolean).map(e=>({bg:getComputedStyle(e).backgroundColor,color:getComputedStyle(e).color,image:getComputedStyle(e).backgroundImage}));
return {viewport:[innerWidth,innerHeight],systemDark:matchMedia('(prefers-color-scheme:dark)').matches,rootOverflow:r.scrollWidth-r.clientWidth,shortOverflow:s.scrollWidth-s.clientWidth,shortWidth:s.clientWidth,tableTextOverflow:[...new Set(bad)],banners,shortLabelOverflow:shortLabels,palette:colors,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')?.slice(0,160)),mobileToggles:[...r.querySelectorAll('.gl-mobile-toggle')].map(e=>({text:e.textContent,visible:e.checkVisibility(),expanded:e.getAttribute('aria-expanded')}))};}'''
def save():
 (OUT/'results.json').write_text(json.dumps({'sources':SOURCES,'scenarios':ROWS,'roundtrips':ROUNDTRIPS,'errors':ERRORS,'external_request_events':REQUESTS,'captures':CAPTURES,'scope':'Previously delivered local offline snapshots; not current Git/main, live shop or physical iPad. No production changes.'},ensure_ascii=False,indent=2))
def passed(m):
 return m['rootOverflow']<=2 and m['shortOverflow']<=2 and not m['tableTextOverflow'] and not any(x['overflow']>2 for x in m['banners'])
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox'])
  for src in FILES:
   raw=src.read_bytes();data=json.loads(BeautifulSoup(raw,'html.parser').select_one('#data').string)
   SOURCES.append({'file':str(src),'sha256':hashlib.sha256(raw).hexdigest(),'ids':[x['id'] for x in data['frames']]});save()
   context=await b.new_context(viewport={'width':1500,'height':1300},color_scheme='light',has_touch=True)
   await context.route('**/*',lambda route:route.abort() if route.request.url.startswith(('https:','http:')) else route.continue_())
   page=await context.new_page();page.on('pageerror',lambda e:ERRORS.append(str(e)));page.on('request',lambda r:REQUESTS.append(r.url) if r.url.startswith(('https:','http:')) else None)
   await page.goto(src.as_uri());await page.evaluate('document.fonts.ready')
   async def resize(w,h):
    await page.locator('#frame').evaluate('(f,s)=>{f.style.boxSizing="content-box";f.style.width=s[0]+"px";f.style.height=s[1]+"px"}',[w,h]);await page.wait_for_timeout(180)
    frame=page.frames[1];await frame.evaluate('document.fonts.ready');return frame
   for index,item in enumerate(data['frames']):
    await page.locator('#product').select_option(index=index);await page.wait_for_timeout(200)
    for w,h in [(768,1024),(820,1180),(1024,768),(767,1024)]:
     row={'id':item['id'],'name':item['name'],'scheme':'light','viewport':[w,h],'dialogs':[]}
     try:
      f=await resize(w,h);root=f.locator('#special-popis,#nad-popis');await root.wait_for(state='visible')
      for link in await root.locator('.latky-plus').all():
       href=await link.get_attribute('href');await link.click(timeout=5000);modal=f.locator(href);await modal.wait_for(state='visible',timeout=5000)
       opened=await modal.evaluate('(e)=>e.checkVisibility({checkOpacity:true,checkVisibilityCSS:true})');text=await modal.inner_text();await modal.locator('.latky-modal-close').click(timeout=5000);await modal.wait_for(state='hidden',timeout=5000)
       row['dialogs'].append({'href':href,'pointer_open_close':opened and len(text.strip())>0})
      row['metrics']=await f.evaluate(METRICS);row['pass']=passed(row['metrics']) and row['metrics']['viewport']==[w,h] and bool(row['dialogs']) and all(x['pointer_open_close'] for x in row['dialogs'])
     except Exception as e:row['pass']=False;row['error']=str(e)[:1000]
     ROWS.append(row);save();print(item['id'],w,'PASS' if row['pass'] else 'FAIL',flush=True)
    trip={'id':item['id'],'stages':[]}
    for w,h in [(390,844),(768,1024),(1440,1000),(820,1180)]:
     try:
      f=await resize(w,h);m=await f.evaluate(METRICS);trip['stages'].append({'viewport':[w,h],'pass':passed(m),'metrics':m})
     except Exception as e:trip['stages'].append({'viewport':[w,h],'pass':False,'error':str(e)[:400]})
    trip['pass']=all(x['pass'] for x in trip['stages']);ROUNDTRIPS.append(trip);save()
    await page.emulate_media(color_scheme='dark');f=await resize(820,1180);m=await f.evaluate(METRICS)
    light=next(x for x in ROWS if x['id']==item['id'] and x['scheme']=='light' and x['viewport']==[820,1180])
    ROWS.append({'id':item['id'],'name':item['name'],'scheme':'dark','viewport':[820,1180],'metrics':m,'pass':passed(m),'palette_changed':m['palette']!=light.get('metrics',{}).get('palette')});save();await page.emulate_media(color_scheme='light')
    if item['id'] in ['351','550','416']:
     # Use direct documents to avoid iframe screenshot clipping. Exact embedded source assets only.
     html=re.sub(r'__ASSET_(\d+)__',lambda m:data['assets'][int(m.group(1))],item['html'])
     path=OUT/(item['id']+'-tablet.html');path.write_text(html)
     cap=await context.new_page();await cap.set_viewport_size({'width':820,'height':1180});await cap.goto(path.as_uri());await cap.evaluate('document.fonts.ready');await cap.wait_for_timeout(250)
     shot=OUT/(item['id']+'-tablet-820.png');await cap.screenshot(path=str(shot),full_page=False);CAPTURES.append(str(shot));await cap.close();save()
   await context.close()
  await b.close()
 ids=sorted({x['id'] for x in ROWS},key=int);assert len(ids)==14
 summary={'products':len(ids),'ids':ids,'light_scenarios':sum(x['scheme']=='light' for x in ROWS),'light_pass':sum(x['scheme']=='light' and x['pass'] for x in ROWS),'dark_scenarios':sum(x['scheme']=='dark' for x in ROWS),'dark_palette_changed':sum(x['scheme']=='dark' and x['palette_changed'] for x in ROWS),'roundtrip_products':len(ROUNDTRIPS),'roundtrip_pass':sum(x['pass'] for x in ROUNDTRIPS),'pointer_dialogs':sum(len(x.get('dialogs',[])) for x in ROWS),'pointer_dialog_pass':sum(y['pointer_open_close'] for x in ROWS for y in x.get('dialogs',[])),'js_errors':len(ERRORS),'external_request_events':len(REQUESTS),'failed':[{k:x.get(k) for k in ['id','scheme','viewport','error','metrics']}for x in ROWS if not x['pass']]}
 (OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False,indent=2))
asyncio.run(main())
