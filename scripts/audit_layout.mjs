// Visual-layout audit of the rendered Marp HTML. Requires Playwright and local Chrome.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require=createRequire(import.meta.url);
const runtime=process.env.ML_COURSE_NODE_MODULES || '/Users/leonjye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const {chromium}=require(path.join(runtime,'playwright'));
const root=path.resolve(import.meta.dirname,'..');
const htmlDir=process.env.ML_COURSE_QA_HTML_DIR||path.join(root,'.build/qa/html');
const htmlSuffix=process.env.ML_COURSE_QA_HTML_SUFFIX||'.html';
const screenshotDir=process.env.ML_COURSE_QA_SCREENSHOT_DIR;
const screenshotFiles=new Set((process.env.ML_COURSE_QA_SCREENSHOT_FILES||'').split(',').filter(Boolean));
const onlySlide=Number(process.env.ML_COURSE_QA_ONLY_SLIDE)||null;
if(screenshotDir)fs.mkdirSync(screenshotDir,{recursive:true});
const browser=await chromium.launch({executablePath:process.env.ML_COURSE_CHROME||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage({viewport:{width:1400,height:900},deviceScaleFactor:1});
const report=[];
for(const file of fs.readdirSync(htmlDir).filter(x=>x.endsWith(htmlSuffix)).sort()){
 await page.goto('file://'+path.join(htmlDir,file));
 await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
 const data=await page.evaluate(()=>[...document.querySelectorAll('section')].map((section,i)=>{
  const s=section.getBoundingClientRect();const scale=s.width/1280;
  const elems=[...section.querySelectorAll(':scope > h1,:scope > h2,:scope > p,:scope > table,:scope > ul,:scope > ol,:scope > blockquote,:scope > div,.columns > div > p,.columns > div > ul,.columns > div > ol')];
  const bad=[];
  for(const e of elems){const r=e.getBoundingClientRect();if(r.width===0||r.height===0)continue;
   if(r.left<s.left-1||r.right>s.right+1||r.bottom>s.top+660*scale+1||r.top<s.top-1)bad.push({element:e.tagName,text:e.innerText?.slice(0,100),x:(r.left-s.left)/scale,y:(r.top-s.top)/scale,bottom:(r.bottom-s.top)/scale,width:r.width/scale});
  }
  return {slide:i+1,title:section.querySelector('h1,h2')?.innerText,width:s.width,height:s.height,scrollHeight:section.scrollHeight,bad,broken:[...section.querySelectorAll('img')].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')),mathErrors:[...section.querySelectorAll('.katex-error')].map(e=>e.innerText),rawMarkdown:section.innerText.includes('**')};
 }));
 report.push({file,slides:data});
 if(screenshotDir&&data.length>=3&&(!screenshotFiles.size||screenshotFiles.has(file.slice(0,2)))){
  await page.keyboard.press('ArrowRight');
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(100);
  const box=await page.locator('section').nth(2).boundingBox();
  if(box)await page.screenshot({path:path.join(screenshotDir,file.replace(/\.qa\.html$|\.html$/,'.png')),clip:box});
 }
 console.log(file,data.length,'slides',data.filter(s=>(!onlySlide||s.slide===onlySlide)&&(s.bad.length||s.broken.length||s.mathErrors.length||s.rawMarkdown)).map(s=>({slide:s.slide,bad:s.bad,broken:s.broken,mathErrors:s.mathErrors})));
}
fs.writeFileSync(path.join(root,'.build/qa/layout_report.json'),JSON.stringify(report,null,2));
await browser.close();
if(report.some(d=>d.slides.some(s=>(!onlySlide||s.slide===onlySlide)&&(s.bad.length||s.broken.length||s.mathErrors.length||s.rawMarkdown))))process.exitCode=1;
