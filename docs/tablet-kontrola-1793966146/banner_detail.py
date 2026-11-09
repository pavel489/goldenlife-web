from pathlib import Path
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio,json,re
D=Path(__file__).parent
SRC=Path('/root/workspace/research/css-audit-1793883385/step4a-hormonal/qa/hormonal-pracovni-nahled.html')
async def main():
 data=json.loads(BeautifulSoup(SRC.read_text(),'html.parser').select_one('#data').string)
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell',args=['--no-sandbox'])
  c=await b.new_context(viewport={'width':820,'height':1180},has_touch=True)
  await c.route('**/*',lambda r:r.abort() if r.request.url.startswith(('https:','http:')) else r.continue_())
  results=[]
  for item in data['frames']:
   if item['id'] not in ['635','641']:continue
   html=re.sub(r'__ASSET_(\d+)__',lambda m:data['assets'][int(m.group(1))],item['html']);f=D/(item['id']+'-tablet.html');f.write_text(html)
   page=await c.new_page();await page.goto(f.as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(250)
   banner=page.locator('.nad-banner');await banner.screenshot(path=str(D/(item['id']+'-banner-820.png')))
   metrics=await banner.evaluate('''r=>{const b=r.getBoundingClientRect();return {banner:{x:b.x,y:b.y,width:b.width,scrollWidth:r.scrollWidth,clientWidth:r.clientWidth,overflow:getComputedStyle(r).overflow},outside:[...r.querySelectorAll('*')].filter(e=>{const t=e.getBoundingClientRect();return t.width>0&&(t.left<b.left-1||t.right>b.right+1)}).map(e=>({tag:e.tagName,cls:e.className,text:e.textContent.trim().slice(0,150),x:e.getBoundingClientRect().x,right:e.getBoundingClientRect().right,width:e.getBoundingClientRect().width,font:getComputedStyle(e).fontSize}))}}''')
   results.append({'id':item['id'],'metrics':metrics,'detail':await banner.evaluate('''r=>({pseudo:['::before','::after'].map(p=>{let s=getComputedStyle(r,p);return {p,content:s.content,width:s.width,left:s.left,right:s.right,position:s.position,transform:s.transform}}),wide:[...r.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+2&&e.clientWidth>0).map(e=>({tag:e.tagName,cls:e.className,text:e.textContent.trim().slice(0,120),clientWidth:e.clientWidth,scrollWidth:e.scrollWidth,transform:getComputedStyle(e).transform}))})''')});await page.close()
  (D/'banner-detail.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False,indent=2));await b.close()
asyncio.run(main())
