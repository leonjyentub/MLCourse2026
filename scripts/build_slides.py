"""Export reviewed Marp sources only when PDF and/or HTML is explicitly requested."""
from pathlib import Path
import argparse
import base64
import html
import mimetypes
import os
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def embed_local_images(body, source):
    """Keep exported HTML usable when moved away from the source asset folders."""
    def replace(match):
        url = html.unescape(match.group(2))
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        asset = (source.parent / unquote(parsed.path)).resolve()
        if not asset.is_file():
            raise FileNotFoundError(f'{source.name}: missing HTML asset {url}')
        mime = mimetypes.guess_type(asset.name)[0] or 'application/octet-stream'
        encoded = base64.b64encode(asset.read_bytes()).decode('ascii')
        return f'{match.group(1)}data:{mime};base64,{encoded}{match.group(3)}'
    return re.sub(r'(<img\b[^>]*?\bsrc=["\'])([^"\']+)(["\'])', replace, body)


def embed_marp_resources(body, marp):
    # Use native Unicode for emoji instead of requiring Twemoji's remote images.
    body = re.sub(r'<img\b(?=[^>]*\bdata-marp-twemoji\b)[^>]*>',
                  lambda m: re.search(r'\balt="([^"]*)"', m.group(0))[1], body)
    # The installed CLI's matching KaTeX fonts are also needed for offline math.
    package = next((p / 'node_modules/katex' for p in Path(marp).resolve().parents
                    if (p / 'node_modules/katex/dist/fonts').is_dir()), None)
    if package is None:
        raise FileNotFoundError('找不到 Marp 使用的 KaTeX 字型，無法建立離線 HTML。')
    def font(match):
        asset = package / 'dist/fonts' / match.group(1)
        mime = mimetypes.guess_type(asset.name)[0] or 'application/octet-stream'
        return 'data:' + mime + ';base64,' + base64.b64encode(asset.read_bytes()).decode('ascii')
    body = re.sub(r'https://cdn\.jsdelivr\.net/npm/katex@[^/]+/dist/fonts/([^\s\)"\']+)', font, body)
    license_text = (package / 'LICENSE').read_text(encoding='utf-8')
    return body + '\n<!-- KaTeX license\n' + license_text.replace('--', '- -') + '\n-->\n'


def make_index():
    rows = []
    for output in sorted((ROOT / 'output/html').glob('[0-9][0-9]_*.html')):
        title = html.escape(output.stem.replace('_', '｜', 1))
        filename = html.escape(output.name, quote=True)
        pdf = ROOT / 'output/pdf' / f'{output.stem}.pdf'
        pdf_link = f'<a href="../pdf/{html.escape(pdf.name, quote=True)}">PDF</a>' if pdf.exists() else ''
        rows.append(f'<tr><td>{title}</td><td><a href="{filename}">播放 HTML</a></td><td>{pdf_link}</td></tr>')
    body = '''<!doctype html><html lang="zh-Hant"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>機器學習投影片</title>
<style>body{font-family:system-ui,sans-serif;max-width:1000px;margin:40px auto;padding:0 24px;line-height:1.7;color:#24364b}table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #ddd;padding:10px;text-align:left}a{color:#116b70}</style>
<h1>機器學習投影片</h1><p>由目前 Marp 投影片內容匯出；HTML 可用方向鍵翻頁，PDF 適合註記與列印。HTML 已內嵌本地圖片。</p>
<p><a href="../../programs/outputs/html/index.html">Notebook：程式與執行結果閱讀版</a></p>
<table><thead><tr><th>章節</th><th>投影片</th><th>講義</th></tr></thead><tbody>'''
    (ROOT / 'output/html/index.html').write_text(body + ''.join(rows) + '</tbody></table></html>', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', action='store_true', help='明確輸出 PDF')
    parser.add_argument('--html', action='store_true', help='明確輸出內嵌圖片的 HTML 投影片')
    parser.add_argument('--extended', action='store_true', help='只輸出第 4–11 週')
    parser.add_argument('--weeks', nargs='+', type=int, help='只輸出指定週次')
    args = parser.parse_args()
    if not (args.pdf or args.html):
        parser.error('請在確認 Marp 內容後，明確加入 --pdf 或 --html。')
    marp = shutil.which('marp')
    if not marp:
        raise SystemExit('找不到 marp CLI，請先安裝 @marp-team/marp-cli。')
    chrome = os.environ.get('ML_COURSE_CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    sources = sorted((ROOT / 'slides').glob('[0-9][0-9]_*.md'))
    if args.extended:
        sources = [s for s in sources if 4 <= int(s.name[:2]) <= 11]
    if args.weeks:
        sources = [s for s in sources if int(s.name[:2]) in args.weeks]
    elif not args.extended:
        sources = [s for s in sources if int(s.name[:2]) <= 3]
    if not sources:
        parser.error('沒有符合指定週次的投影片。')
    for src in sources:
        base = [marp, str(src), '--theme-set', str(ROOT / 'slides/theme.css'), '--html']
        if args.pdf:
            target = ROOT / 'output/pdf' / f'{src.stem}.pdf'
            target.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(base + ['--pdf', '--pdf-outlines', '--browser', 'chrome', '--browser-path', chrome,
                                  '--allow-local-files', '-o', str(target)], check=True)
        if args.html:
            target = ROOT / 'output/html' / f'{src.stem}.html'
            target.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(base + ['-o', str(target)], check=True)
            body = embed_local_images(target.read_text(encoding='utf-8'), src)
            target.write_text(embed_marp_resources(body, marp), encoding='utf-8')
        print(f'完成：{src.stem}', flush=True)
    if args.html:
        make_index()


if __name__ == '__main__':
    main()
