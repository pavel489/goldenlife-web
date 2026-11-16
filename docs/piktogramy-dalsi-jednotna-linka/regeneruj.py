"""Re-export the real delivered PNGs from their editable SVG masters.
Run from the repository root with Pillow and CairoSVG installed.
"""
from pathlib import Path
import json,io,hashlib
from PIL import Image
import cairosvg
ROOT=Path(__file__).resolve().parents[2]
records=json.loads((Path(__file__).parent/'mapovani.json').read_text())
checked=set()
for rec in records:
 target=ROOT/rec['newAsset']
 if str(target) in checked:continue
 svg=(ROOT/rec['master']).read_text().replace('stroke="#25333D"','stroke="'+rec['color']+'"')
 im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=1024,output_height=1024))).convert('RGBA').resize((256,256),Image.Resampling.LANCZOS)
 buf=io.BytesIO();im.save(buf,format='PNG');data=buf.getvalue()
 assert hashlib.sha256(data).hexdigest()==rec['newSha256'],str(target)
 target.write_bytes(data);checked.add(str(target))
print(json.dumps({'regeneratedVerifiedPngs':len(checked),'allExpectedHashesMatch':True}))
