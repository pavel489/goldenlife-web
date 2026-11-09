from pathlib import Path
from bs4 import BeautifulSoup
import json,re,hashlib
D=Path(__file__).parent;M=json.loads((D/'source-manifest.json').read_text());SRC=Path('/root/workspace/research/css-audit-1793883385/step4a-hormonal/qa/hormonal-pracovni-nahled.html')
raw=SRC.read_text();soup=BeautifulSoup(raw,'html.parser');tag=soup.select_one('#data');data=json.loads(tag.string);changes=[]
for product in M['products']:
 pid=product['id'];theme=product['theme'];name='glp1-woman-balance'+('-sacek' if pid=='641' else '')
 old=(D/'source'/theme).read_bytes()
 add=('\n/* Tablet 769–1023 px: stack benefit icons above readable full-width captions. */\n@media (min-width:769px) and (max-width:1023px){\n#special-popis:where([data-gl-theme="'+name+'"]) .nad-feature{flex-direction:column;align-items:center;text-align:center;gap:6px;overflow-wrap:break-word;}\n}\n').encode()
 out=D/'out'/theme;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(old+add);assert out.read_bytes()[:-len(add)]==old
 f=next(x for x in data['frames'] if x['id']==pid);f['html']=f['html'].replace('</body>','<style>'+add.decode()+'</style></body>');assert add.decode() in f['html']
 before=next(x for x in json.loads(tag.string)['frames'] if x['id']==pid);assets=data['assets']
 for mode,frame in [('before',before),('after',f)]:
  html=re.sub(r'__ASSET_(\d+)__',lambda m:assets[int(m.group(1))],frame['html']);(D/(pid+'-'+mode+'.html')).write_text(html)
 changes.append({'id':pid,'path':theme,'added_css':add.decode(),'original_sha256':hashlib.sha256(old).hexdigest(),'after_sha256':hashlib.sha256(old+add).hexdigest(),'original_bytes_preserved':True})
newdata=json.dumps(data,ensure_ascii=False).replace('</','<\\/');start=raw.index('>',raw.index('<script type="application/json" id="data"'))+1;end=raw.index('</script>',start)
viewer=raw[:start]+newdata+raw[end:];(D/'hormonal-tablet-oprava.html').write_text(viewer);(D/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
# Re-run the same whole acceptance matrix, changing only the corrected hormonal viewer input.
qa=(Path('/root/workspace/research/tablet-1793966146/run_audit.py')).read_text()
qa=qa.replace("BASE/'step4a-hormonal/qa/hormonal-pracovni-nahled.html'","Path(__file__).parent/'hormonal-tablet-oprava.html'")
(D/'rerun_matrix.py').write_text(qa)
print(json.dumps(changes,ensure_ascii=False,indent=2))
