() => {
 const active=document.querySelector('.latky-modal:target');
 const roots=active?[active]:[...document.querySelectorAll('[data-gl-theme]')].filter(e=>!e.parentElement?.closest('[data-gl-theme]'));
 const rgba=s=>{let v=(s.match(/[\d.]+/g)||[]).map(Number);return [v[0]||0,v[1]||0,v[2]||0,v.length>3?v[3]:1]};
 const over=(a,b)=>[a[0]*a[3]+b[0]*(1-a[3]),a[1]*a[3]+b[1]*(1-a[3]),a[2]*a[3]+b[2]*(1-a[3]),1];
 const lum=a=>a.slice(0,3).map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4}).reduce((n,x,i)=>n+x*[.2126,.7152,.0722][i],0);
 const ratio=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
 function backgrounds(e){let nodes=[];for(let n=e;n;n=n.parentElement)nodes.unshift(n);let pool=[[255,255,255,1]],image=false;
  for(const n of nodes){const s=getComputedStyle(n);const bg=rgba(s.backgroundColor);pool=pool.map(b=>over(bg,b));if(s.backgroundImage!=='none'){
    if(s.backgroundImage.includes('url('))image=true;
    const colors=[...s.backgroundImage.matchAll(/rgba?\([^)]+\)/g)].map(m=>rgba(m[0]));
    if(colors.length){let samples=[...colors];for(let i=0;i<colors.length-1;i++)for(let t of [.25,.5,.75])samples.push(colors[i].map((v,k)=>v*(1-t)+colors[i+1][k]*t));pool=pool.flatMap(b=>samples.map(a=>over(a,b))).slice(-64);}
   }}return {pool,image};}
 const failures=[],imageBacked=[],counts={text_nodes:0,AA_pass:0,image_backed:0},details=[];
 for(const root of roots){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
  while(n=w.nextNode()){
   if(!n.textContent.trim())continue;const e=n.parentElement;if(['SCRIPT','STYLE','NOSCRIPT'].includes(e.tagName))continue;
   if(!e.checkVisibility({checkOpacity:true,checkVisibilityCSS:true}))continue;
   let range=document.createRange();range.selectNodeContents(n);let rect=range.getBoundingClientRect();if(rect.width<1||rect.height<1)continue;
   let left=rect.left,right=rect.right,top=rect.top,bottom=rect.bottom,alpha=1;
   for(let a=e;a;a=a.parentElement){const z=getComputedStyle(a),b=a.getBoundingClientRect();alpha*=parseFloat(z.opacity);if(['hidden','clip'].includes(z.overflowX)){left=Math.max(left,b.left);right=Math.min(right,b.right)}if(['hidden','clip'].includes(z.overflowY)){top=Math.max(top,b.top);bottom=Math.min(bottom,b.bottom)}}
   if(right<=left||bottom<=top||alpha===0)continue;
   const s=getComputedStyle(e),color=rgba(s.color);color[3]*=alpha;const bg=backgrounds(e);const icon=s.fontFamily.includes('Material Symbols');const fs=parseFloat(s.fontSize),weight=parseFloat(s.fontWeight)||400;const threshold=icon||fs>=24||(fs>=18.66&&weight>=700)?3:4.5;
   const minimum=Math.min(...bg.pool.map(b=>ratio(over(color,b),b)));counts.text_nodes++;if(minimum+0.01>=threshold)counts.AA_pass++;if(bg.image)counts.image_backed++;
   const item={tag:e.tagName,cls:typeof e.className==='string'?e.className:'',text:n.textContent.trim().slice(0,120),color:s.color,fontSize:s.fontSize,weight:s.fontWeight,ratio:+minimum.toFixed(3),threshold,bgCandidates:bg.pool.slice(0,4).map(x=>x.slice(0,3).map(Math.round)),imageBacked:bg.image};
   if(minimum+0.01<threshold)failures.push(item);if(bg.image)imageBacked.push(item);
  }
 }
 return {counts,failures,imageBacked};
}
