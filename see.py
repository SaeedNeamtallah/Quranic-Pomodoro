
import re
with open('static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

res = re.search(r'<div class=\
timer-section\>[\s\S]*?<main', html)
if res:
    print(res.group(0)[:1000])

