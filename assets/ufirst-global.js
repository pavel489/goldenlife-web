/* UFIRST appearance only. One shared stylesheet for the shop and same-origin SupportBox.
   Root-relative CSS paths belong to the SHOP origin, never to the rewritten CDN script origin. */
(()=>{'use strict';
const script=document.currentScript,revision='ufirst-2';
const paths=new Set(['/ufirst-darkovy-box/','/ufirst-all-in-one-drink-/','/ufirst-sample-pack/','/ufirst-all-in-one-drink-sacek-tropical/','/ufirst-all-in-one-drink-sacek-malina/','/ufirst-all-in-one-drink-sacek-jablko/','/ufirst-trio/','/vitality-complex/','/maca-triple-complex/','/care-free/','/brain-focus/','/ashwagandha-ksm-66/','/magnesium-triple-blend/','/lahev-ufirst/','/ufirstlab/','/znacka/u-first/']);
const html=document.documentElement,path=location.pathname.replace(/\/+$/,'')+'/';
const marked=html.dataset.glSiteBrand==='ufirst'||!!document.querySelector('[data-gl-page-brand="ufirst"]');
if(!marked&&!paths.has(path))return;
if(html.dataset.glUfirstGlobalVersion===revision)return;
let cssUrl;try{const url=new URL(script?.dataset.ufirstCss||'/user/documents/upload/css/ufirst-global.css',location.href);if(!/^https?:$/.test(url.protocol))return;if(!url.searchParams.has('v'))url.searchParams.set('v',revision);cssUrl=url.href}catch(error){return}
html.dataset.glSiteBrand='ufirst';html.dataset.glUfirstGlobalBound='true';html.dataset.glUfirstGlobalVersion=revision;
function style(doc){
 if(!doc?.documentElement)return;
 doc.documentElement.dataset.glSiteBrand='ufirst';
 let link=doc.getElementById('gl-ufirst-global-css');
 if(!link){link=doc.createElement('link');link.id='gl-ufirst-global-css';link.rel='stylesheet';link.href=cssUrl;(doc.head||doc.documentElement).append(link)}
 else if(link.href!==cssUrl)link.href=cssUrl;
}
style(document);
const frames=new WeakSet(),documents=new WeakSet();let queued=false;
function paint(frame){
 let doc;try{doc=frame.contentDocument}catch(error){return}
 if(!doc?.documentElement)return;
 style(doc);
 if(!documents.has(doc)){documents.add(doc);new MutationObserver(()=>style(doc)).observe(doc.documentElement,{childList:true,subtree:true})}
}
function scan(){queued=false;const frame=document.getElementById('supportBox-iframe');if(!frame||frame.tagName!=='IFRAME')return;if(!frames.has(frame)){frames.add(frame);frame.addEventListener('load',()=>paint(frame))}paint(frame)}
function schedule(){if(!queued){queued=true;queueMicrotask(scan)}}
new MutationObserver(schedule).observe(html,{childList:true,subtree:true});scan();
})();
