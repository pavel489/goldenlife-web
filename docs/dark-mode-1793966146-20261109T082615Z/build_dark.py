from pathlib import Path
from bs4 import BeautifulSoup
import json,re,hashlib
D=Path(__file__).parent;B=Path('/root/workspace/research/css-audit-1793883385');M=json.loads((D/'source-manifest.json').read_text())
VIEWERS={'step3':'pilotni-sablony-offline.html','step4a-hormonal':'hormonal-pracovni-nahled.html','step4b-longevity':'longevity-pracovni-nahled.html','step4c-slim':'slim-pracovni-nahled.html','step4d-collagen-variants':'collagen-varianty-pracovni-nahled.html'}
BG='#19171d';SURFACE='#25212b';RAISED='#302a36';FG='#f4eff4';MUTED='#d3c6d1';BORDER='#9d8e9e';ON='#1b151d';PHOTO='#f5f1f4'
def rgb(s):
 s=s.lstrip('#');s=''.join(x*2 for x in s) if len(s)==3 else s;return tuple(int(s[i:i+2],16) for i in [0,2,4])
def tint(s,white):return '#'+''.join(f'{round(x*(1-white)+255*white):02x}' for x in rgb(s))
changes=[];fixtures=[]
for p in M['products']:
 src=(D/'source'/p['theme']).read_bytes();css=src.decode();theme=re.search(r'data-gl-theme="([^"]+)"',css).group(1);props=dict(re.findall(r'(--[\w-]+)\s*:\s*([^;{}]+);',css));base=props['--gl-color-primary'];accent=tint(base,.62);hover=tint(base,.72);values={}
 for key,val in props.items():
  if key=='--gl-color-primary':value=accent
  elif key=='--gl-color-primary-hover':value=hover
  elif key=='--gl-color-primary-rgb':value=','.join(map(str,rgb(accent)))
  elif key=='--gl-color-bg-light-rgb':value=','.join(map(str,rgb(SURFACE)))
  elif key=='--gl-color-success':value='#93e1b6'
  elif key in ['--gl-color-bg-grey','--gl-color-table-row-alt']:value=RAISED
  elif key in ['--gl-color-bg-light','--gl-color-table-bg']:value=SURFACE
  elif key in ['--gl-color-text-muted','--gl-color-text-subtle','--gl-drink-muted']:value=MUTED
  elif key in ['--gl-paper','--gl-drink-paper']:value=SURFACE
  elif 'note-bg' in key:value='#332a21'
  elif 'note-border' in key:value='#cbb88a'
  elif key=='--gl-icon-filter':value='brightness(0) invert(1)'
  elif 'reg-area-background-image' in key:
   value=re.sub(r'%23(?:e06a6a|bf1818)',lambda m:'%23'+accent[1:],val,flags=re.I)
  elif 'background' in key:
   if 'modal-backdrop' in key:value='rgba(0,0,0,.78)'
   elif 'cta-product-img' in key:value=PHOTO
   elif key.endswith('-2'):value=RAISED
   else:value=SURFACE
  elif 'border' in key:value=BORDER
  elif 'color' in key:
   if any(x in key for x in ['btn-s-color','nad-btn-color','cta-button','latky-plus-color','first-child-th-color','inline-btn-s']):value=ON
   elif 'primary' in val:value='var(--gl-color-primary)'
   else:value=FG
  elif 'shadow' in key:value='rgba(0,0,0,.25)'
  else:continue
  values[key]=value
 root=':where([data-gl-theme="'+theme+'"])'
 # Only palette and colour-role changes; layout, source HTML and scripts remain intact.
 lines=['\n/* GOLDIE SYSTEM DARK START — proposed UI tints; original light palette preserved. */','@media (prefers-color-scheme:dark){',root+'{','  color-scheme:dark;','  color:'+FG+';','  background-color:'+BG+';','  --gl-dark-source-primary:'+base+';','  --gl-dark-bg:'+BG+';','  --gl-dark-surface:'+SURFACE+';','  --gl-dark-raised:'+RAISED+';','  --gl-dark-text:'+FG+';','  --gl-dark-muted:'+MUTED+';','  --gl-dark-border:'+BORDER+';','  --gl-dark-on-accent:'+ON+';']
 lines+=['  '+k+':'+v+';' for k,v in values.items()];lines+=['}']
 # Neutral inherited text on sections that relied on the light shop body's color.
 lines+=[root+' :is(.product-container,.nad-content,.latky-modal-box,.latky,.story-block-text,.cta-text,.gl-faq,.faq-section,.maly-popis){color:var(--gl-dark-text);}',root+' :is(.cta-button,.nad-btn,.btn-s,.latky-plus){color:var(--gl-dark-on-accent)!important;}',root+' :is(.latky-modal-close,.gl-mobile-toggle){border:1px solid var(--gl-dark-border);}',root+' :is(a,button,summary,[tabindex]):focus-visible{outline:3px solid var(--gl-color-primary);outline-offset:3px;box-shadow:0 0 0 3px var(--gl-dark-bg),0 0 0 6px var(--gl-color-primary);}',root+' :is(.cta-availability,.cta-status,.gl-cart-message){color:var(--gl-dark-muted);}',root+' :is(.gl-error,.is-error,[role="alert"]){color:#ffc2c6;}',root+' :is(.cta-product-img,.nad-mol){background-color:'+PHOTO+';border-radius:12px;}',root+' :is(.gl-draft-note,.doza-safety){color:var(--gl-dark-text);}', '}', '/* GOLDIE SYSTEM DARK END */\n']
 footer=lines[-2:];lines=lines[:-2]
 lines += [root+' .nad-banner{background-image:linear-gradient(135deg,var(--gl-dark-surface),var(--gl-dark-raised))!important;color:var(--gl-dark-text);}',root+' .hero-img{background:linear-gradient(145deg,var(--gl-dark-surface),var(--gl-dark-raised))!important;}',root+' .p-icon-card{background:var(--gl-dark-raised)!important;border-color:var(--gl-dark-border);}',root+' .cta-box{background:var(--gl-dark-surface)!important;}',root+' .nad-title{color:var(--gl-color-primary)!important;}',root+' :is(.nad-dose-sub,.nad-dose-label,.nad-feature,.nad-tagline,.nad-info p){color:var(--gl-dark-text)!important;}',root+' :is(th){background-color:var(--gl-color-primary)!important;color:var(--gl-dark-on-accent)!important;}',root+' :is(.cta-button,.nad-btn,.btn-s,.latky-plus){background:var(--gl-color-primary)!important;color:var(--gl-dark-on-accent)!important;}',root+' .gl-history{background:#332a21!important;color:var(--gl-dark-text);}',root+' .gl-history :is(p,span,div,summary){color:var(--gl-dark-text)!important;}']
 lines += [':is(#special-popis,#nad-popis)[data-gl-theme="'+theme+'"] .gl-mobile-toggle{background:var(--gl-dark-surface)!important;color:var(--gl-color-primary)!important;border-color:var(--gl-dark-border)!important;}']
 if p['id']=='168':
  lines += ['@media(max-width:767px){#special-popis[data-gl-product-id="168"][data-gl-theme="slim-extreme-collagen"][data-gl-slim168-mobile-active] .gl-mobile-copy:not(.is-expanded)::after{background:linear-gradient(transparent,var(--gl-dark-bg))!important;}}']
 if p['id'] in ['464','467']:
  lines += [root+' .latky-modal-box{background:var(--gl-dark-surface)!important;color:var(--gl-dark-text);}',root+' .latky-modal-close{background:var(--gl-dark-raised)!important;color:var(--gl-dark-text)!important;border-color:var(--gl-dark-border)!important;}']
 lines+=footer;addition='\n'.join(lines)
 # Keep all dark overrides inside the media block; original source outside it is byte-identical.
 out=D/'out'/p['theme'];out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(src+addition.encode());assert out.read_bytes().split(b'\n/* GOLDIE SYSTEM DARK START')[0]==src
 # Match the exact previously built fixture to current immutable source before injecting only source additions.
 old=(B/p['batch']/'out'/p['theme']).read_bytes();assert src.startswith(old),'Unexpected nonappend source edit: '+p['theme'];delta=(src[len(old):]).decode()+addition
 original=BeautifulSoup((B/p['batch']/'qa'/VIEWERS[p['batch']]).read_text(),'html.parser');data=json.loads(original.select_one('#data').string);f=next(x for x in data['frames'] if x['id']==p['id']);original_html=f['html'];assert '</body>' in original_html
 for state,extra in [('before',src[len(old):].decode()),('after',delta)]:
  html=original_html.replace('</body>','<style>'+extra+'</style></body>');html=re.sub(r'__ASSET_(\d+)__',lambda m:data['assets'][int(m.group(1))],html);dest=D/'fixtures'/(p['id']+'-'+state+'.html');dest.parent.mkdir(exist_ok=True);dest.write_text(html)
 fixtures.append({**p,'theme_id':theme,'before':str(D/'fixtures'/(p['id']+'-before.html')),'after':str(D/'fixtures'/(p['id']+'-after.html'))})
 changes.append({'id':p['id'],'path':p['theme'],'theme':theme,'source_primary':base,'proposed_dark_accent':accent,'base_bytes_preserved':True,'original_sha256':hashlib.sha256(src).hexdigest(),'after_sha256':hashlib.sha256(src+addition.encode()).hexdigest(),'appended_css':addition})
(D/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2));(D/'fixtures.json').write_text(json.dumps(fixtures,ensure_ascii=False,indent=2));print(json.dumps({'product_count':len(changes),'CSS_changed':len(changes),'HTML_changed':0,'shared_framework_changed':False,'photos_generated':False},ensure_ascii=False))
