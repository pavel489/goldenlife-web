/* Gift-box intro beside six benefit pictograms: sixth native gallery photo.
   CTA keeps the original main photo; packaging keeps the second photo. */
(()=>{
  'use strict';
  const root=document.querySelector('#special-popis.gl-box-refined');
  if(!root||root.dataset.glSixthPhotoBound)return;
  const image=root.querySelector('.heroimg');
  const expected=image&&image.dataset.glGalleryProductId||root.dataset.glProductId;
  if(!image||!expected)return;
  root.dataset.glSixthPhotoBound='true';
  let timer=0;
  function photo(value){
    try{
      const url=new URL(value,document.baseURI);
      if(url.protocol!=='https:'||url.username||url.password||!['www.golden-life.cz','golden-life.cz','cdn.myshoptet.com'].includes(url.hostname))return null;
      if(url.hostname==='cdn.myshoptet.com'&&!url.pathname.startsWith('/usr/www.golden-life.cz/'))return null;
      if(!/\/user\/shop\/(big|orig|detail|related)\/[^/]+\.(jpe?g|png|webp|avif|gif)$/i.test(url.pathname)||/missing_images/i.test(url.pathname))return null;
      return {url:url.href,key:url.pathname.replace(/\/shop\/(big|orig|detail|related)\//,'/shop/')};
    }catch{return null;}
  }
  function hide(){image.hidden=true;}
  function sync(){
    const form=document.getElementById('product-detail-form');
    // Standalone preview retains only the verified same-SKU sixth-photo snapshot.
    if(!form||root.contains(form))return;
    const identity=form.querySelector('input[name="productId"]');
    if(!identity||identity.value!==expected){hide();return;}
    let links=[...form.querySelectorAll('.p-thumbnail[href]')].filter(a=>!root.contains(a)&&!a.closest('.is-clone,.splide__slide--clone'));
    if(!links.length)links=[...form.querySelectorAll('.p-image-wrapper a.cbox-gal[data-gallery][href]')].filter(a=>!root.contains(a)&&!a.closest('.is-clone,.splide__slide--clone'));
    const seen=new Set(),photos=[];
    for(const link of links){
      const entry=photo(link.getAttribute('href'));
      if(!entry||seen.has(entry.key))continue;
      seen.add(entry.key);photos.push(entry);
    }
    const sixth=photos[5];
    if(!sixth){hide();return;}
    ['srcset','sizes','data-src','data-srcset'].forEach(name=>image.removeAttribute(name));
    if(image.getAttribute('src')!==sixth.url){image.hidden=true;image.src=sixth.url;}
    else image.hidden=!(image.complete&&image.naturalWidth);
    image.dataset.glGalleryPhotoIndex='6';
  }
  image.addEventListener('load',sync);
  image.addEventListener('error',hide);
  function schedule(){clearTimeout(timer);timer=setTimeout(sync,40);}
  const observer=new MutationObserver(records=>{
    if(records.some(record=>!root.contains(record.target)))schedule();
  });
  function start(){sync();observer.observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['href','src','srcset','class','value']});}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
  window.addEventListener('pagehide',()=>{observer.disconnect();clearTimeout(timer);},{once:true});
})();
