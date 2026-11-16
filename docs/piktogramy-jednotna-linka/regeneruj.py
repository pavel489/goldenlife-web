from pathlib import Path
from PIL import Image
import cairosvg,json,io,hashlib
ROOT=Path(__file__).resolve().parents[2]
manifest=json.loads((Path(__file__).parent/'mapovani.json').read_text())
seen=set()
for row in manifest:
 if row['newAsset'] in seen:continue
 seen.add(row['newAsset'])
 source=(ROOT/row['master']).read_text().replace('#25333D',row['color'])
 high=cairosvg.svg2png(bytestring=source.encode(),output_width=512,output_height=512)
 im=Image.open(io.BytesIO(high)).convert('RGBA').resize((256,256),Image.Resampling.LANCZOS)
 out=io.BytesIO();im.save(out,format='PNG');raw=out.getvalue()
 assert hashlib.sha256(raw).hexdigest()==row['newSha256'],row['newAsset']
 (ROOT/row['newAsset']).write_bytes(raw)
print(json.dumps({'regeneratedPng':len(seen),'allHashesMatch':True}))
