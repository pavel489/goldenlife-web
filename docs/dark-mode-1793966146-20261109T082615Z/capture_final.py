from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image,ImageDraw,ImageFont,ImageOps
import asyncio,json
D=Path(__file__).parent;F=json.loads((D/'fixtures.json').read_text());OUT=D/'visual';OUT.mkdir(exist_ok=True)
async def main():
 records=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox']);c=await b.new_context(viewport={'width':820,'height':1180},has_touch=True,color_scheme='light');await c.route('**/*',lambda r:r.abort() if r.request.url.startswith(('http:','https:')) else r.continue_())
  for f in F:
   page=await c.new_page();await page.goto(Path(f['after']).as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(150);selector=next(s for s,count in [(s,await page.locator(s).count()) for s in ['.nad-banner','.reg-banner','.hero-img']] if count)
   for mode in ['light','dark']:
    await page.emulate_media(color_scheme=mode);await page.wait_for_timeout(100);path=OUT/(f['id']+'-'+mode+'.png');await page.locator(selector).screenshot(path=str(path));records.append({'id':f['id'],'mode':mode,'selector':selector,'path':str(path)})
   if f['id'] in ['635','467']:
    link=page.locator('.latky-plus').last;href=await link.get_attribute('href');await link.click();await page.locator(href).wait_for(state='visible');await page.locator(href+' .latky-modal-box').screenshot(path=str(OUT/(f['id']+'-dark-dialog.png')));await page.locator(href+' .latky-modal-close').click()
   if f['id']=='168':
    await page.set_viewport_size({'width':390,'height':844});await page.wait_for_timeout(180);fade=await page.locator('.gl-mobile-copy').first.evaluate('(e)=>getComputedStyle(e,"::after").backgroundImage');assert '255, 255, 255' not in fade;records.append({'id':'168','mobile_fade':fade})
   await page.close()
  # Negative control: all new CSS loaded, but no allowed product root.
  page=await c.new_page();await page.emulate_media(color_scheme='dark');styles='\n'.join(x['appended_css'] for x in json.loads((D/'changes.json').read_text()));await page.set_content('<!doctype html><style>'+styles+'</style><div id="sentinel" data-gl-theme="ufirst">Nedotčená jiná řada</div>');control=await page.locator('#sentinel').evaluate('(e)=>({color:getComputedStyle(e).color,bg:getComputedStyle(e).backgroundColor,bodyBg:getComputedStyle(document.body).backgroundColor,bodyScheme:getComputedStyle(document.body).colorScheme})');assert control=={'color':'rgb(0, 0, 0)','bg':'rgba(0, 0, 0, 0)','bodyBg':'rgba(0, 0, 0, 0)','bodyScheme':'normal'};await b.close()
 font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',24);small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
 for pid in ['383','635','550']:
  a=Image.open(OUT/(pid+'-light.png')).convert('RGB');z=Image.open(OUT/(pid+'-dark.png')).convert('RGB');canvas=Image.new('RGB',(a.width+z.width+32,max(a.height,z.height)+62),'#eeeeee');draw=ImageDraw.Draw(canvas);draw.text((8,12),'SVĚTLÝ REŽIM · ID'+pid,font=font,fill='#29212b');draw.text((a.width+24,12),'TMAVÝ REŽIM · podle systému',font=font,fill='#29212b');canvas.paste(a,(8,54));canvas.paste(z,(a.width+24,54));canvas.save(OUT/(pid+'-light-dark.png'))
 # Overview is visual evidence only; original individual captures stay available for detail.
 tiles=[]
 for f in F:
  im=Image.open(OUT/(f['id']+'-dark.png')).convert('RGB');im.thumbnail((470,430));tile=Image.new('RGB',(490,474),'#eeeeee');draw=ImageDraw.Draw(tile);draw.text((10,8),'ID'+f['id']+' · '+f['theme_id'][:30],font=small,fill='#222222');tile.paste(im,((490-im.width)//2,40));tiles.append(tile)
 sheets=[]
 for start in [0,6,12]:
  group=tiles[start:start+6];sheet=Image.new('RGB',(980,474*((len(group)+1)//2)),'#eeeeee')
  for i,im in enumerate(group):sheet.paste(im,((i%2)*490,(i//2)*474))
  path=OUT/('prehled-dark-'+str(start//6+1)+'.jpg');sheet.save(path,quality=92);sheets.append(str(path))
 (D/'visual-verification.json').write_text(json.dumps({'captures':records,'other_brand_negative_control':control,'overview_sheets':sheets,'source': 'Final delivered-theme additions with exact original cached preview assets; unavailable assets not synthesized.'},ensure_ascii=False,indent=2));print(json.dumps({'captured_products':len(F),'captures':len(records),'negative_control':'PASS','sheets':sheets},ensure_ascii=False,indent=2))
asyncio.run(main())
