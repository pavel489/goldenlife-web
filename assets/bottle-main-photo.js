/* Mirror the loaded main gallery only on bottle product 597. No cart writes. */
(()=>{
 'use strict';
 const r=document.querySelector('#special-popis.gl-bottle[data-gl-product-id="597"]');
 if(!r||r.dataset.glbPhotoBound)return;
 r.dataset.glbPhotoBound='true';
 const photo=r.querySelector('[data-gl-bottle-photo]'),fallback=r.querySelector('.glb-photo-fallback');
 if(!photo||!fallback)return;
 const known=photo.getAttribute('src'),failed=new Set();
 let queued=false;
 const show=()=>{const ok=photo.complete&&photo.naturalWidth>1;photo.hidden=!ok;fallback.hidden=ok;};
 const set=url=>{
  if(!url)return;
  ['srcset','sizes','data-src','data-srcset','data-lazy'].forEach(a=>photo.removeAttribute(a));
  if(photo.getAttribute('src')===url){if(photo.complete)show();return;}
  photo.hidden=true;fallback.hidden=false;
  photo.src=url;
  if(photo.complete)show();
 };
 const sync=()=>{
  queued=false;
  if(!r.isConnected){observer.disconnect();document.removeEventListener('load',schedule,true);document.removeEventListener('error',schedule,true);return;}
  const form=document.querySelector('#product-detail-form');
  const pid=form&&(form.querySelector('input[name="productId"]')?.value||form.querySelector('[itemprop="productID"]')?.getAttribute('content'));
  if(pid!=='597'){set(known);return;}
  const img=document.querySelector('#main-slider-slide01 img')||document.querySelector('.p-main-image img');
  const url=img&&(img.currentSrc||img.getAttribute('src'));
  if(!img||failed.has(url)||r.contains(img)||!img.complete||img.naturalWidth<=1||!url||/missing_images|missing-image|no-image/i.test(url)){set(known);return;}
  set(url);
 };
 function schedule(){if(!queued){queued=true;queueMicrotask(sync);}}
 photo.addEventListener('load',show);
 photo.addEventListener('error',()=>{const bad=photo.getAttribute('src');if(bad!==known){failed.add(bad);set(known);}else show();});
 const observer=new MutationObserver(schedule);
 observer.observe(document.documentElement,{childList:true,subtree:true,attributes:true,attributeFilter:['src','srcset','sizes','value','content','id']});
 document.addEventListener('load',schedule,true);document.addEventListener('error',schedule,true);
 if(photo.complete)show();
 schedule();
})();
