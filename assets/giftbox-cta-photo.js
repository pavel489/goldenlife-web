/* Mirror this box's rendered intro image, never an unrelated product. */
(()=>{
  'use strict';
  const root=document.querySelector('#special-popis.gl-box-refined');
  if(!root||root.dataset.glCtaImageBound)return;
  root.dataset.glCtaImageBound='true';
  const targets=[...root.querySelectorAll('.cta-product-img')];
  if(!targets.length)return;
  let hero=null,queued=false;
  const hide=()=>targets.forEach(image=>{image.hidden=true;});
  function safe(value){
    if(!value||/missing_images|\[|\]/i.test(value))return false;
    if(/^data:image\/(png|jpeg|webp|gif);base64,/i.test(value))return true;
    try{const url=new URL(value,document.baseURI);return url.protocol==='https:'&&(url.origin===location.origin||/^(www\.golden-life\.cz|cdn\.myshoptet\.com)$/.test(url.hostname));}catch(error){return false;}
  }
  function sync(){
    queued=false;
    const next=root.querySelector('.heroimg');
    if(next!==hero){
      if(hero){hero.removeEventListener('load',schedule);hero.removeEventListener('error',hide);}
      hero=next;
      if(hero){hero.addEventListener('load',schedule);hero.addEventListener('error',hide);}
    }
    if(!hero||!hero.complete||!hero.naturalWidth){hide();return;}
    const source=hero.currentSrc||hero.getAttribute('src');
    if(!safe(source)){hide();return;}
    targets.forEach(image=>{
      ['srcset','sizes','data-src','data-srcset'].forEach(name=>image.removeAttribute(name));
      if(image.getAttribute('src')!==source)image.setAttribute('src',source);
      if(hero.alt)image.alt=hero.alt;
      image.hidden=false;
    });
  }
  function schedule(){if(!queued){queued=true;requestAnimationFrame(sync);}}
  targets.forEach(image=>{image.dataset.glCtaImage='';image.addEventListener('error',()=>{image.hidden=true;});});
  const observer=new MutationObserver(records=>{
    if(records.some(record=>record.type==='childList'?[...record.addedNodes,...record.removedNodes].some(node=>node.nodeType===1&&(node.matches('.heroimg')||node.querySelector('.heroimg'))):record.target===hero||record.target.matches('.heroimg')))schedule();
  });
  observer.observe(root,{subtree:true,childList:true,attributes:true,attributeFilter:['src','srcset','sizes','data-src','data-srcset']});
  window.addEventListener('resize',schedule,{passive:true});
  schedule();
  window.addEventListener('pagehide',()=>{observer.disconnect();window.removeEventListener('resize',schedule);if(hero){hero.removeEventListener('load',schedule);hero.removeEventListener('error',hide);}},{once:true});
})();
