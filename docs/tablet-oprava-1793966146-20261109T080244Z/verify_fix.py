from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image,ImageChops,ImageDraw,ImageFont
import asyncio,json,io
D=Path(__file__).parent
async def main():
 rows=[];errors=[];requests=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox'])
  c=await b.new_context(has_touch=True,color_scheme='light');await c.route('**/*',lambda r:r.abort() if r.request.url.startswith(('http:','https:')) else r.continue_())
  for pid in ['635','641']:
   for width,height in [(390,844),(767,1024),(768,1024),(769,1024),(780,1024),(800,1180),(820,1180),(900,1180),(1023,768),(1024,768),(1440,1000)]:
    variants={};pictures={}
    for state in ['before','after']:
     page=await c.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url) if r.url.startswith(('http:','https:')) else None)
     await page.set_viewport_size({'width':width,'height':height});await page.goto((D/(pid+'-'+state+'.html')).as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(300)
     metrics=await page.locator('.nad-banner').evaluate('''r=>({overflow:r.scrollWidth-r.clientWidth,features:[...r.querySelectorAll('.nad-feature')].map(e=>{const b=e.getBoundingClientRect();let bad=[];for(const n of e.childNodes){if(n.nodeType!==Node.TEXT_NODE||!n.textContent.trim())continue;const t=document.createRange();t.selectNodeContents(n);for(const x of t.getClientRects())if(x.width>0&&(x.left<b.left-1||x.right>b.right+1))bad.push(n.textContent.trim())}return {overflow:e.scrollWidth-e.clientWidth,badText:bad,wrap:getComputedStyle(e).overflowWrap}})})''')
     variants[state]=metrics
     png=await page.locator('.nad-banner').screenshot();pictures[state]=png
     if width==820:(D/(pid+'-820-'+state+'.png')).write_bytes(png)
     await page.close()
    after=variants['after'];row={'id':pid,'viewport':[width,height],'before':variants['before'],'after':after,'pass':after['overflow']<=2 and all(x['overflow']<=2 and not x['badText'] for x in after['features'])}
    if width in [390,767,768,1024,1440]:
     a=Image.open(io.BytesIO(pictures['before'])).convert('RGB');z=Image.open(io.BytesIO(pictures['after'])).convert('RGB');row['pixels_unchanged']=a.size==z.size and ImageChops.difference(a,z).getbbox() is None;assert row['pixels_unchanged'],row
    rows.append(row);assert row['pass'],row
  await c.close();await b.close()
 assert not errors and not requests
 out={'scenarios':rows,'scenario_count':len(rows),'pass_count':sum(x['pass'] for x in rows),'unchanged_outside_tablet_pixel_cases':sum(x.get('pixels_unchanged',False) for x in rows),'JS_errors':errors,'external_requests':requests,'scope':'Exact original offline docs + exact CSS additions from output themes. Source current-main verified byte-identical before patch. Not live shop/Safari.'}
 (D/'extended-tests.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='scenarios'},ensure_ascii=False,indent=2))
 for pid in ['635','641']:
  a=Image.open(D/(pid+'-820-before.png')).convert('RGB');z=Image.open(D/(pid+'-820-after.png')).convert('RGB');canvas=Image.new('RGB',(a.width+z.width+32,max(a.height,z.height)+68),'#ffffff');draw=ImageDraw.Draw(canvas);font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
  draw.text((8,10),'PŘED · ID'+pid+' · tablet 820 px',font=font,fill='#333333');draw.text((a.width+24,10),'PO OPRAVĚ · zalomení textu',font=font,fill='#333333');canvas.paste(a,(8,56));canvas.paste(z,(a.width+24,56));canvas.save(D/(pid+'-tablet-srovnani.png'))
asyncio.run(main())
