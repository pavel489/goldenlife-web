from pathlib import Path
import json,hashlib,tinycss2
D=Path(__file__).parent;M=json.loads((D/'source-manifest.json').read_text());C=json.loads((D/'changes.json').read_text());QA=json.loads((D/'qa-results.json').read_text());S=json.loads((D/'qa-summary.json').read_text());V=json.loads((D/'visual-verification.json').read_text())
assert QA['build_manifest_sha256']==hashlib.sha256((D/'changes.json').read_bytes()).hexdigest()
assert len(C)==len({x['id'] for x in C})==14;assert len(QA['scenarios'])==len({(x['id'],x['scheme'],tuple(x['viewport'])) for x in QA['scenarios']})==168
assert S['scenario_count']==S['pass_count']==168 and S['no_JS_products']==14 and S['no_JS_pass'] and S['light_unchanged'] and not S['JS_errors'] and not S['external_requests']
errors=[];syntax=[]
def recurse(rules,path):
 for r in rules:
  if r.type=='error':errors.append({'file':path,'line':r.source_line,'error':r.message})
  elif r.type=='at-rule' and r.content is not None:recurse(tinycss2.parse_rule_list(r.content,skip_whitespace=True,skip_comments=True),path)
  elif r.type=='qualified-rule':
   for d in tinycss2.parse_declaration_list(r.content,skip_whitespace=True,skip_comments=True):
    if d.type=='error':errors.append({'file':path,'line':d.source_line,'error':d.message})
for c in C:
 original=(D/'source'/c['path']).read_bytes();out=(D/'out'/c['path']).read_bytes();assert out==original+c['appended_css'].encode();assert hashlib.sha256(out).hexdigest()==c['after_sha256'];assert c['original_sha256']==hashlib.sha256(original).hexdigest()
 rules=tinycss2.parse_stylesheet(c['appended_css'],skip_whitespace=True,skip_comments=True);assert len(rules)==1 and rules[0].type=='at-rule' and rules[0].lower_at_keyword=='media' and tinycss2.serialize(rules[0].prelude).strip()=='(prefers-color-scheme:dark)';recurse(rules,c['path']);syntax.append({'id':c['id'],'path':c['path'],'append_only':True,'only_system_dark_media':True,'source_SHA256':c['original_sha256'],'output_SHA256':c['after_sha256']})
assert not errors
base=[x['contrast'] for x in QA['scenarios'] if x['scheme']=='dark'];states=list(base)
for x in QA['scenarios']:
 if x['scheme']!='dark':continue
 for key in ['dialogs','toggles','details']:states.extend(v['contrast'] for v in x[key])
 if 'hover_contrast' in x:states.append(x['hover_contrast'])
assert all(not x['failures'] for x in states)
photos=[x for x in QA['scenarios'] if x['scheme']=='dark'];assert all(x['photo_sources_unchanged'] and x['photo_no_color_inversion'] for x in photos)
result={'syntax':syntax,'syntax_errors':errors,'original_theme_prefixes_preserved':14,'shared_framework_changed':False,'production_HTML_changed':0,'source_commit':M['source_commit'],'tested_dark_contrast_states':len(states),'dark_text_node_evaluations':sum(x['counts']['text_nodes'] for x in states),'image_backed_text_evaluations_not_photographically_certified':sum(x['counts']['image_backed'] for x in states),'dark_contrast_failures':sum(len(x['failures']) for x in states),'photo_sources_and_no_inversion_cases':len(photos),'actual_light_pixel_checks':sum(x['selector']!='palette after dark→light' for x in QA['light_pixel_checks']),'light_palette_roundtrips':sum(x['selector']=='palette after dark→light' for x in QA['light_pixel_checks']),'all_light_checks_unchanged':S['light_unchanged'],'no_global_leak_to_other_brand':V['other_brand_negative_control'],'scope':'CSS contrast screening with alpha/gradient samples; image-backed text, current shop/Safari and complete WCAG certification remain unverified.'}
(D/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='syntax'},ensure_ascii=False,indent=2))
