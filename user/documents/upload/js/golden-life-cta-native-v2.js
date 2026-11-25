/* Native CTA bridge: no cart endpoint, credentials, tracking or quantity rewrite. */
(function(){'use strict';
 document.querySelectorAll('[data-gl-cta="native-main-v2"]').forEach(function(box){
  if(box.dataset.glCtaReady)return;box.dataset.glCtaReady='true';
  var id=box.getAttribute('data-gl-product-id'),img=box.querySelector('.gl-cta-v2-image'),price=box.querySelector('[data-gl-cta-price]'),button=box.querySelector('.gl-cta-v2-button'),status=box.querySelector('.gl-cta-v2-status'),fallback=box.getAttribute('data-gl-main-photo'),failed=new Set(),pending=false;
  function text(el,value){if(el&&el.textContent!==value)el.textContent=value;}
  function host(){var f=document.querySelector('form#product-detail-form'),input=f&&f.querySelector('input[name="productId"]');return f&&input&&input.value===id&&!box.contains(f)?f:null;}
  function nativeButton(f){return f&&f.querySelector('button.add-to-cart-button,button[data-testid="buttonAddToCart"],input.add-to-cart-button');}
  function imageURL(){var i=document.querySelector('#main-slider-slide01 img')||document.querySelector('.p-image[data-testid="mainImage"] img,.p-image img');if(!i||box.contains(i)||!i.complete||i.naturalWidth<2)return null;var u=i.currentSrc||i.getAttribute('src');return u&&!failed.has(u)&&!/(?:missing[_-]?images?|no-image|placeholder)/i.test(u)?u:null;}
  function setImage(u){if(!u)return;var canonical;try{canonical=new URL(u,location.href).pathname===new URL(fallback,location.href).pathname;}catch(e){canonical=false;}var fit=canonical?'canonical':'natural';if(img.getAttribute('data-gl-fit')!==fit)img.setAttribute('data-gl-fit',fit);if(img.getAttribute('src')===u)return;['srcset','sizes','data-src','data-srcset','data-lazy'].forEach(function(a){img.removeAttribute(a);});img.setAttribute('src',u);}
  function currentPrice(f){var p=f&&f.querySelector('.p-final-price-wrapper .price-final-holder,.p-final-price-wrapper .price-final');var value=p&&p.textContent.replace(/\s+/g,' ').trim();return value&&/\d/.test(value)?value:null;}
  function sync(){pending=false;if(!box.isConnected){observer.disconnect();return;}var f=host(),b=nativeButton(f),p=currentPrice(f),available=!!(f&&b&&!b.disabled&&b.getAttribute('aria-disabled')!=='true'&&!b.classList.contains('disabled')&&p);setImage(f?(imageURL()||fallback):fallback);text(price,p||'—');if(button.disabled!==!available)button.disabled=!available;box.setAttribute('data-native-ready',String(available));text(status,available?'':f?'Aktuální možnosti nákupu najdete v hlavním nákupním bloku.':'Nákup je dostupný na produktové stránce.');}
  function schedule(){if(!pending){pending=true;queueMicrotask(sync);}}
  img.addEventListener('error',function(){var u=img.getAttribute('src');if(u&&u!==fallback){failed.add(u);setImage(fallback);}});
  button.addEventListener('click',function(e){e.preventDefault();var f=host(),b=nativeButton(f);if(!f||!b||b.disabled||b.getAttribute('aria-disabled')==='true'||b.classList.contains('disabled')||!currentPrice(f)){schedule();if(f)f.scrollIntoView({block:'center',behavior:'smooth'});return;}b.click();});
  var observer=new MutationObserver(schedule);observer.observe(document.documentElement,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['src','srcset','sizes','data-src','value','disabled','aria-disabled','class']});
  document.addEventListener('load',function(e){if(!box.contains(e.target))schedule();},true);document.addEventListener('error',function(e){if(!box.contains(e.target))schedule();},true);document.addEventListener('change',schedule,true);document.addEventListener('input',schedule,true);
  window.addEventListener('pagehide',function(){observer.disconnect();},{once:true});schedule();
 });
})();
