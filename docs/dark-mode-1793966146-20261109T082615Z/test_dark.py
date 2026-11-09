from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image,ImageChops
import asyncio,json,io,os,hashlib
D=Path(__file__).parent;F=json.loads((D/'fixtures.json').read_text());ROWS=[];PIXELS=[];NOJS=[];ERRORS=[];REQUESTS=[];CONTRAST=(D/'contrast.js').read_text()
if os.environ.get('RESUME_DARK_QA')=='1':
 prior=json.loads((D/'qa-results.json').read_text());ROWS=prior['scenarios'];PIXELS=prior['light_pixel_checks'];NOJS=prior['no_JS'];ERRORS=prior['JS_errors'];REQUESTS=prior['external_requests']
METRICS='''async () => {const r=document.querySelector('#special-popis,#nad-popis'),s=document.querySelector('.preview-short');let bad=[];for(const c of r.querySelectorAll('td,th')){const b=c.getBoundingClientRect();if(b.width<1)continue;const g=document.createRange();g.selectNodeContents(c);for(const a of g.getClientRects())if(a.width>1&&(a.left<b.left-2||a.right>b.right+2))bad.push(c.innerText)}return {viewport:[innerWidth,innerHeight],dark:matchMedia('(prefers-color-scheme:dark)').matches,rootOverflow:r.scrollWidth-r.clientWidth,shortOverflow:s.scrollWidth-s.clientWidth,tableTextOverflow:[...new Set(bad)],bannerOverflow:[...r.querySelectorAll('.nad-banner')].map(e=>e.scrollWidth-e.clientWidth),rootBG:getComputedStyle(r).backgroundColor,rootColor:getComputedStyle(r).color,photos:await Promise.all([...document.images].filter(i=>!i.closest('.maly-ikony,.custom-grid,.hero-icons-grid,.nad-ico,.p-icon-card,.maly-produkt-info')).map(async i=>({src:Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(i.getAttribute('src')||'')))).map(x=>x.toString(16).padStart(2,'0')).join(''),filter:getComputedStyle(i).filter}))),palette:[...document.querySelectorAll('[data-gl-theme]')].filter(e=>!e.parentElement?.closest('[data-gl-theme]')).map(e=>({bg:getComputedStyle(e).backgroundColor,color:getComputedStyle(e).color,scheme:getComputedStyle(e).colorScheme,primary:getComputedStyle(e).getPropertyValue('--gl-color-primary')}))}}'''
def save():
 (D/'qa-results.json').write_text(json.dumps({'build_manifest_sha256':hashlib.sha256((D/'changes.json').read_bytes()).hexdigest(),'scenarios':ROWS,'light_pixel_checks':PIXELS,'no_JS':NOJS,'JS_errors':ERRORS,'external_requests':REQUESTS,'scope':'Exact Git-derived CSS additions with real cached offline assets, native purchase disabled. Not live shop or physical Safari.'},ensure_ascii=False,indent=2))
def geometry(m):return m['rootOverflow']<=2 and m['shortOverflow']<=2 and not m['tableTextOverflow'] and all(x<=2 for x in m['bannerOverflow'])
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox']);c=await b.new_context(has_touch=True,color_scheme='light');await c.route('**/*',lambda r:r.abort() if r.request.url.startswith(('http:','https:')) else r.continue_())
  for f in F:
   existing=[x for x in ROWS if x['id']==f['id']]
   if len(existing)==12 and all(x['pass'] for x in existing):continue
   if existing:ROWS[:]=[x for x in ROWS if x['id']!=f['id']];PIXELS[:]=[x for x in PIXELS if x['id']!=f['id']];NOJS[:]=[x for x in NOJS if x['id']!=f['id']]
   page=await c.new_page();page.on('pageerror',lambda e:ERRORS.append(str(e)));page.on('request',lambda r:REQUESTS.append(r.url) if r.url.startswith(('http:','https:')) else None)
   await page.set_viewport_size({'width':820,'height':1180});await page.goto(Path(f['after']).as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(150)
   # Actual light-mode banner/short pixel equality, not an inference from the media query alone.
   old=await c.new_page();await old.set_viewport_size({'width':820,'height':1180});await old.goto(Path(f['before']).as_uri());await old.evaluate('document.fonts.ready');await old.wait_for_timeout(150)
   bannerSelector=next(selector for selector,count in [(s,await page.locator(s).count()) for s in ['.nad-banner','.reg-banner','.hero-img']] if count)
   for selector in [bannerSelector,'.preview-short']:
    a=Image.open(io.BytesIO(await old.locator(selector).screenshot())).convert('RGB');z=Image.open(io.BytesIO(await page.locator(selector).screenshot())).convert('RGB');PIXELS.append({'id':f['id'],'selector':selector,'viewport':[820,1180],'unchanged':a.size==z.size and ImageChops.difference(a,z).getbbox() is None})
   beforePhotos=await old.evaluate(METRICS);await old.close()
   for scheme in ['light','dark']:
    await page.emulate_media(color_scheme=scheme)
    for width,height in [(390,844),(767,1024),(768,1024),(820,1180),(1024,768),(1440,1000)]:
     row={'id':f['id'],'scheme':scheme,'viewport':[width,height],'dialogs':[],'toggles':[],'details':[]}
     try:
      await page.set_viewport_size({'width':width,'height':height});await page.evaluate('document.fonts.ready');await page.wait_for_timeout(180);root=page.locator('#special-popis,#nad-popis')
      row['metrics']=await page.evaluate(METRICS);check=await page.evaluate(CONTRAST);row['contrast']=check
      row['geometry_pass']=geometry(row['metrics']);assert row['metrics']['viewport']==[width,height]
      if scheme=='dark':
       assert row['metrics']['dark'] and row['metrics']['rootBG']=='rgb(25, 23, 29)'
       row['photo_sources_unchanged']=[i['src'] for i in row['metrics']['photos']]==[i['src'] for i in beforePhotos['photos']]
       row['photo_no_color_inversion']=all(not any(x in i['filter'] for x in ['invert','hue-rotate','saturate','brightness','contrast']) for i in row['metrics']['photos'])
      if width in [390,820]:
       for link in await root.locator('.latky-plus').all():
        href=await link.get_attribute('href');await link.click(timeout=5000);modal=page.locator(href);await modal.wait_for(state='visible',timeout=5000);assert (await modal.inner_text()).strip();mc=await page.evaluate(CONTRAST);row['dialogs'].append({'href':href,'pointer_open_close':True,'contrast':mc});await modal.locator('.latky-modal-close').click(timeout=5000);await modal.wait_for(state='hidden',timeout=5000)
       for toggle in await root.locator('.gl-mobile-toggle').all():
        if not await toggle.is_visible():continue
        initial=await toggle.get_attribute('aria-expanded');await toggle.click(timeout=5000);await page.wait_for_timeout(60);expanded=await toggle.get_attribute('aria-expanded');tc=await page.evaluate(CONTRAST);await toggle.click(timeout=5000);row['toggles'].append({'changed':initial!=expanded,'returned':await toggle.get_attribute('aria-expanded')==initial,'contrast':tc})
       # Open native FAQ/history summaries that are actually painted; test the real pointer.
       for summary in await page.locator('[data-gl-theme] details > summary').all():
        if not await summary.evaluate('(e)=>e.checkVisibility({checkOpacity:true,checkVisibilityCSS:true})'):continue
        await summary.click(timeout=5000);await page.wait_for_timeout(50);dc=await page.evaluate(CONTRAST);opened=await summary.evaluate('(e)=>e.parentElement.open');await summary.click(timeout=5000);row['details'].append({'opened':opened,'closed':not await summary.evaluate('(e)=>e.parentElement.open'),'contrast':dc})
       # Focus-visible uses a real keyboard input, while hover uses the pointer; no purchase is submitted.
       if scheme=='dark' and width==820:
        await page.evaluate('window.scrollTo(0,0);document.activeElement?.blur()');await page.keyboard.press('Tab');row['keyboard_focus']=await page.evaluate('''() => {let e=document.activeElement,s=getComputedStyle(e);return {tag:e.tagName,cls:e.className,focusVisible:e.matches(':focus-visible'),outline:s.outline,outlineWidth:s.outlineWidth}}''')
        btn=page.locator('[data-gl-theme] .btn-s,[data-gl-theme] .cta-button').first
        if await btn.count() and await btn.is_visible():await btn.hover(timeout=5000);row['hover_contrast']=await page.evaluate(CONTRAST)
      contrast_states=[row['contrast']]+[d['contrast'] for d in row['dialogs']]+[d['contrast'] for d in row['toggles']]+[d['contrast'] for d in row['details']]+([row['hover_contrast']] if 'hover_contrast' in row else [])
      row['dark_contrast_pass']=scheme!='dark' or all(not q['failures'] for q in contrast_states)
      row['pass']=row['geometry_pass'] and row['dark_contrast_pass'] and row.get('photo_sources_unchanged',True) and row.get('photo_no_color_inversion',True) and all(x['changed'] and x['returned'] for x in row['toggles']) and all(x['opened'] and x['closed'] for x in row['details'])
     except Exception as e:row['pass']=False;row['error']=str(e)[:1200]
     ROWS.append(row);save();print(f['id'],scheme,width,'PASS' if row['pass'] else 'FAIL',flush=True)
   # Same page: dark to light restores exact palette and exact light banner/short pixels.
   await page.emulate_media(color_scheme='light');await page.set_viewport_size({'width':820,'height':1180});await page.evaluate('window.scrollTo(0,0)');await page.mouse.move(0,0);await page.wait_for_timeout(200)
   restored=await page.evaluate(METRICS);PIXELS.append({'id':f['id'],'selector':'palette after dark→light','unchanged':restored['palette']==beforePhotos['palette']});await page.close();save()
  await c.close()
  no=await b.new_context(java_script_enabled=False,color_scheme='dark',viewport={'width':390,'height':844},has_touch=True);await no.route('**/*',lambda r:r.abort() if r.request.url.startswith(('http:','https:')) else r.continue_())
  for f in F:
   if any(x['id']==f['id'] for x in NOJS):continue
   page=await no.new_page();await page.goto(Path(f['after']).as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(120);metrics=await page.evaluate(METRICS);contrast=await page.evaluate(CONTRAST);link=page.locator('.latky-plus').first;await link.click(timeout=5000);modal=page.locator(await link.get_attribute('href'));await modal.wait_for(state='visible',timeout=5000);await modal.locator('.latky-modal-close').click(timeout=5000);await modal.wait_for(state='hidden',timeout=5000);NOJS.append({'id':f['id'],'geometry_pass':geometry(metrics),'contrast':contrast,'CSS_dialog_pointer':True});await page.close();save()
  await b.close()
 summary={'products':len(F),'scenario_count':len(ROWS),'pass_count':sum(x['pass'] for x in ROWS),'dark_contrast_scenarios':sum(x['scheme']=='dark' and x.get('dark_contrast_pass',False) for x in ROWS),'geometry_pass_count':sum(x.get('geometry_pass',False) for x in ROWS),'pointer_dialogs':sum(len(x['dialogs']) for x in ROWS),'toggle_cycles':sum(len(x['toggles']) for x in ROWS),'native_detail_cycles':sum(len(x['details']) for x in ROWS),'light_pixel_and_palette_checks':len(PIXELS),'light_unchanged':all(x['unchanged'] for x in PIXELS),'no_JS_products':len(NOJS),'no_JS_pass':all(x['geometry_pass'] and not x['contrast']['failures'] and x['CSS_dialog_pointer'] for x in NOJS),'JS_errors':ERRORS,'external_requests':REQUESTS,'failures':[{k:x.get(k) for k in ['id','scheme','viewport','error','geometry_pass','dark_contrast_pass']} for x in ROWS if not x['pass']]}
 (D/'qa-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False,indent=2))
asyncio.run(main())
