import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('/Users/leonjye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root='/Users/leonjye/Documents/MacProject/MLCourse2026';
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1});
await page.route(/^https?:\/\//,route=>route.abort());
const results=[];
for(const name of fs.readdirSync(root+'/programs/outputs/html').filter(n=>n.endsWith('.html')).sort()) {
 await page.goto('file://'+root+'/programs/outputs/html/'+name,{waitUntil:'domcontentloaded'});
 await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(x=>x.decode().catch(()=>{})));});
 const state=await page.evaluate(()=>({title:document.querySelector('h1')?.textContent,images:document.images.length,
   brokenImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.getAttribute('src')?.slice(0,70)),
   width:document.documentElement.scrollWidth,viewport:innerWidth,codeCells:document.querySelectorAll('.jp-CodeCell').length,
   headings:document.querySelectorAll('h1,h2').length}));
 results.push({name,...state});
 if(name.startsWith('04')||name.startsWith('07')||name==='index.html')await page.screenshot({path:root+'/.build/program_qa/'+name.replace('.html','_top.png')});
 if(name.startsWith('04')){
  await page.getByRole('heading',{name:'5. 最終測試與 RMSE 信賴區間',exact:false}).scrollIntoViewIfNeeded();
  await page.screenshot({path:root+'/.build/program_qa/04_evaluation.png'});
 }
}
fs.writeFileSync(root+'/.build/program_qa/html_audit.json',JSON.stringify(results,null,2));
console.log(JSON.stringify(results,null,2));
await browser.close();
if(results.some(r=>r.brokenImages.length||r.width>r.viewport+2))process.exitCode=1;
