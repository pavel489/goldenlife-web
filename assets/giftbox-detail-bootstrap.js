/* Small CMS-safe entry point. The complete, pinned reader loads only on demand. */
(function () {
  'use strict';
  const box=document.querySelector('#special-popis.gl-box-refined');
  if(!box||box.dataset.glBootstrapBound)return;
  box.dataset.glBootstrapBound='true';
  const panel=box.querySelector('[data-gl-reader]'),title=panel.querySelector('[data-gl-reader-title]'),status=panel.querySelector('[data-gl-reader-status]'),host=panel.querySelector('[data-gl-reader-content]'),retry=panel.querySelector('[data-gl-reader-retry]'),buttons=[...box.querySelectorAll('.gl-open-detail')];
  let pending=null,loading=false;
  function ready(){
    if(!box.dataset.glReaderBound||!host.shadowRoot)return false;
    loading=false;
    if(pending){const button=pending;pending=null;button.click();}
    return true;
  }
  function failed(){
    loading=false;
    if(ready()||!pending)return;
    host.removeAttribute('aria-busy');
    status.textContent='Načítání podrobností se nepodařilo spustit. Zkus to prosím znovu; stránku boxu neopouštíš.';
    retry.hidden=false;
  }
  function load(){
    if(ready()||loading)return;
    loading=true;
    const script=document.createElement('script');
    script.src='https://cdn.jsdelivr.net/gh/pavel489/goldenlife-web@912c837872b8ed6b882746590b0b7aaf94f8f44c/assets/giftbox-detail-loader.js';
    script.integrity='sha384-3VsjMF1W22YF/whwckaS38hWgk9eJ9ZhGIXWKVqQH9Xu9bQyjNG3aNf5iRc6XLrx';
    script.crossOrigin='anonymous';
    script.async=true;
    const timeout=setTimeout(failed,15000);
    script.onload=()=>{clearTimeout(timeout);if(!ready())failed();};
    script.onerror=()=>{clearTimeout(timeout);script.remove();failed();};
    document.head.append(script);
  }
  function close(){
    const previous=pending;pending=null;panel.hidden=true;host.removeAttribute('aria-busy');
    buttons.forEach(b=>b.setAttribute('aria-expanded','false'));
    if(previous){previous.scrollIntoView({block:'center',behavior:'auto'});previous.focus({preventScroll:true});}
  }
  function waiting(button){
    pending=button;panel.hidden=false;title.textContent='Podrobně: '+button.dataset.glSourceName;
    buttons.forEach(b=>b.setAttribute('aria-expanded',String(b===button)));
    status.textContent='Načítám podrobnosti produktu…';retry.hidden=true;host.setAttribute('aria-busy','true');
    title.focus({preventScroll:true});panel.scrollIntoView({block:'start',behavior:'auto'});load();
  }
  buttons.forEach(button=>button.addEventListener('click',e=>{
    if(box.dataset.glReaderBound){pending=null;return;}
    e.preventDefault();
    if(pending===button&&!panel.hidden){close();return;}
    waiting(button);
  }));
  panel.querySelectorAll('[data-gl-reader-close]').forEach(button=>button.addEventListener('click',()=>{if(!box.dataset.glReaderBound)close();}));
  panel.addEventListener('keydown',e=>{if(e.key==='Escape'&&!box.dataset.glReaderBound){e.preventDefault();close();}});
  retry.addEventListener('click',e=>{
    if(pending&&box.dataset.glReaderBound){e.stopImmediatePropagation();ready();return;}
    if(!box.dataset.glReaderBound&&pending){e.stopImmediatePropagation();waiting(pending);}
  });
})();
