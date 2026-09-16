"""Render reviewed Marp sources to PDF only. Requires marp-cli and Chrome."""
from pathlib import Path
import subprocess,shutil,argparse,os
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--pdf',action='store_true',help='在確認 Marp 內容後，明確輸出 PDF');p.add_argument('--extended',action='store_true',help='只輸出新增第 4–11 週');p.add_argument('--weeks',nargs='+',type=int,help='只輸出指定週次');args=p.parse_args()
if not args.pdf:raise SystemExit('此腳本只在投影片確認後輸出 PDF；請明確加入 --pdf。')
marp=shutil.which('marp')
if not marp:raise SystemExit('找不到 marp CLI，請先安裝 @marp-team/marp-cli。')
chrome=os.environ.get('ML_COURSE_CHROME','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
(ROOT/'output/pdf').mkdir(parents=True,exist_ok=True)
sources=sorted((ROOT/'slides').glob('*.md')) if args.extended or args.weeks else sorted((ROOT/'slides').glob('0[0-3]_*.md'))
if args.extended:sources=[s for s in sources if s.name[:2].isdigit() and 4<=int(s.name[:2])<=11]
if args.weeks:sources=[s for s in sources if s.name[:2].isdigit() and int(s.name[:2]) in args.weeks]
for src in sources:
 base=[marp,str(src),'--theme-set',str(ROOT/'slides/theme.css'),'--html']
 subprocess.run(base+['--pdf','--pdf-outlines','--browser','chrome','--browser-path',chrome,'--allow-local-files','-o',str(ROOT/'output/pdf'/(src.stem+'.pdf'))],check=True)
print('完成：output/pdf')
