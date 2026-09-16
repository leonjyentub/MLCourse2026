"""Download source snapshots by immutable GitHub commit; never execute upstream code."""
from pathlib import Path
import json,urllib.request,hashlib,argparse,time
ROOT=Path(__file__).resolve().parents[1]
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'MLCourse2026 teaching-source-reader'})
 with urllib.request.urlopen(req,timeout=90) as r:return r.read()
def fetch_inventory():
 pins={'ageron/handson-mlp':'47eba45aacc85feae51ba7db68dd1ca66cb25e0a',
       'leonjyentub/MachineLearning2025':'3da2cb56b9efd17d7cd34602589f392554b40603'}
 for repo,commit in pins.items():
  branch='main'
  tree=json.loads(get(f'https://api.github.com/repos/{repo}/git/trees/{commit}?recursive=1'))
  assert not tree.get('truncated'),repo
  folder=ROOT/'upstream'/repo.split('/')[1];folder.mkdir(parents=True,exist_ok=True)
  inventory={'repository':repo,'commit':commit,'default_branch':branch,'files':tree['tree']}
  (folder/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
  print(repo,'commit',commit)
  for f in tree['tree']:
   if f['type']=='blob' and (f['path'].endswith(('.py','.ipynb','.toml','.csv','.md')) or 'LICENSE' in f['path']):print(f['path'],f.get('size'))
if __name__=='__main__':fetch_inventory()
