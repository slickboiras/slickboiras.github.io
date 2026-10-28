import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Build: inline the pfp + images (as data URIs) so the page is one self-contained file.
import base64, re
from PIL import Image
s = open('template.html').read()
def uri(p): return 'data:image/jpeg;base64,' + base64.b64encode(open(p,'rb').read()).decode()
s = s.replace('__PFP__', uri('pfp.jpg'))
def img(m): return uri(f'img/{m.group(1)}.jpg')
def ratio(m):
    w,h = Image.open(f'img/{m.group(1)}.jpg').size; return f'{w/h:.4f}'
s = re.sub(r'__IMG:(\w+)__', img, s)
s = re.sub(r'__R:(\w+)__', ratio, s)

# Standalone website version (GitHub Pages): add the document shell the artifact host normally provides.
head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Farras Raihan Akbar Firmansyah: graphic designer and computer engineering student at BINUS University. Posters, documentation, and hardware projects.">
<meta name="theme-color" content="#121a10">
<meta property="og:title" content="Farras · Portfolio">
<meta property="og:description" content="Half designer, half engineer. An interactive portfolio built like a design app.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%239ccc87'/%3E%3Ctext x='16' y='24' font-family='Arial Black,Arial' font-weight='900' font-size='22' text-anchor='middle' fill='%2310180e'%3EF%3C/text%3E%3C/svg%3E">
<style>*,*::before,*::after{box-sizing:border-box}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
"""
page = s.replace('<title>Farras Artboard</title>', '<title>Farras · Portfolio</title>', 1)
open('../index.html','w').write(head + page.replace('<style>', '</head>\n<body>\n<style>', 0) + '\n</body>\n</html>\n')
print('built index.html')
