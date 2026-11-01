// Inspect actual browser-computed text/outline colors and clipping in a local SVG.
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {runtime} from './mermaid_runtime.mjs';

let browser;
try {
  const {require} = await runtime(process.argv[2]);
  const puppeteer = require('puppeteer');
  const style = JSON.parse(readFileSync(process.argv[4], 'utf8'));
  const options = process.argv[5] ? JSON.parse(readFileSync(process.argv[5], 'utf8')) : {};
  browser = await puppeteer.launch({...options, headless:true});
  const page = await browser.newPage();
  await page.setViewport({width:1600,height:1000,deviceScaleFactor:1});
  await page.goto(pathToFileURL(process.argv[3]).href, {waitUntil:'load',timeout:30000});
  const result = await page.evaluate(style => {
    const svg=document.querySelector('svg'), errors=[], colors=new Set();
    if (!svg) return {passed:false,errors:['SVG did not load.']};
    const bounds=svg.getBoundingClientRect();
    const hex = value => {
      if (/^#[\da-f]{6}$/i.test(value)) return value.toUpperCase();
      const m=value.match(/^rgba?\((\d+)[, ]+\s*(\d+)[, ]+\s*(\d+)/);
      return m?'#'+m.slice(1).map(v=>Number(v).toString(16).padStart(2,'0')).join('').toUpperCase():null;
    };
    const contrast=(a,b)=>{
      const lum=value=>[1,3,5].map(i=>parseInt(value.slice(i,i+2),16)/255).map(v=>v<=0.04045?v/12.92:((v+0.055)/1.055)**2.4).reduce((s,v,i)=>s+v*[0.2126,0.7152,0.0722][i],0);
      const values=[lum(a),lum(b)].sort((x,y)=>x-y);return(values[1]+0.05)/(values[0]+0.05);
    };
    const visible=element=>{
      for(let e=element;e&&e!==svg.parentElement;e=e.parentElement){const c=getComputedStyle(e);if(c.display==='none'||c.visibility==='hidden'||Number(c.opacity)===0)return false;}
      const b=element.getBoundingClientRect();return b.width>0&&b.height>0;
    };
    const contains=(box,x,y)=>x>=box.left&&x<=box.right&&y>=box.top&&y<=box.bottom;
    let textCount=0;
    for(const element of svg.querySelectorAll('text,tspan,foreignObject span,foreignObject p')) {
      const own=[...element.childNodes].filter(n=>n.nodeType===Node.TEXT_NODE).map(n=>n.textContent).join('').trim();
      if(!own||!visible(element))continue;
      const c=getComputedStyle(element), box=element.getBoundingClientRect();
      const foreground=hex(element.namespaceURI==='http://www.w3.org/2000/svg'?c.fill:c.color);
      let background=style.canvas.background;
      const container=element.closest('.node,.cluster,.note');
      if(container)for(const shape of container.querySelectorAll('rect,path,polygon,circle,ellipse')) {
        const paint=getComputedStyle(shape), color=hex(paint.fill), r=shape.getBoundingClientRect();
        if(color&&Number(paint.fillOpacity)!==0&&contains(r,box.left+box.width/2,box.top+box.height/2)){background=color;break;}
      }
      textCount++;
      if(foreground)colors.add(foreground);
      if(!foreground||contrast(foreground,background)<style.minimum_text_contrast)errors.push('Insufficient computed text contrast: '+own);
      if(foreground&&![style.text,style.stroke].map(v=>v.toUpperCase()).includes(foreground))errors.push('Text is outside the shared palette: '+own+' ('+foreground+')');
      if(box.left<bounds.left-1||box.top<bounds.top-1||box.right>bounds.right+1||box.bottom>bounds.bottom+1)errors.push('Clipped text: '+own);
    }
    const allowed=new Set([style.canvas.background,style.stroke,style.text,...Object.values(style.roles).map(r=>r.fill)].map(v=>v.toUpperCase()));
    for(const shape of svg.querySelectorAll('#technical-writer-content rect,#technical-writer-content path,#technical-writer-content polygon,#technical-writer-content circle,#technical-writer-content ellipse,#technical-writer-content line')) {
      if(!visible(shape))continue;
      const c=getComputedStyle(shape), fill=hex(c.fill), stroke=hex(c.stroke);
      if(fill&&Number(c.fillOpacity)!==0&&!allowed.has(fill))errors.push('Shape fill is outside the shared palette: '+fill);
      if(stroke&&Number(c.strokeOpacity)!==0&&parseFloat(c.strokeWidth)>0&&contrast(stroke,fill&&fill!==stroke?fill:style.canvas.background)<style.minimum_graphic_contrast)errors.push('Insufficient computed outline contrast: '+JSON.stringify({shape:shape.tagName,group:shape.parentElement.getAttribute('class'),fill,stroke}));
    }
    if(!textCount)errors.push('No visible diagram text.');
    return {passed:errors.length===0,errors,text_count:textCount,text_colors:[...colors].sort()};
  },style);
  if(process.argv[6])await page.screenshot({path:process.argv[6],fullPage:true});
  process.stdout.write(JSON.stringify({kind:'browser_observation',browser:await browser.version(),...result}));
  process.exitCode=result.passed?0:1;
} catch(error) {
  process.stdout.write(JSON.stringify({passed:false,errors:[String(error)]}));process.exitCode=2;
} finally {
  if(browser)await browser.close();
}
