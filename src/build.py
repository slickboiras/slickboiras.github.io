"""Build: inline the images from src/img/ into src/page.html and write ../index.html (one self-contained file)."""
import base64, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = open('page.html', encoding='utf-8').read()
def uri(m):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(f'img/{m.group(1)}.jpg', 'rb').read()).decode()
s = re.sub(r'__IMG:(\w+)__', uri, s)
open('../index.html', 'w', encoding='utf-8').write(s)
print('built index.html', len(s) // 1024, 'KB')
