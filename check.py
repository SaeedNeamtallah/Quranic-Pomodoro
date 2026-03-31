import re
with open('static/script.js', encoding='utf-8') as f:
    script = f.read()

ids_in_script = set(re.findall(r"\$\('([^']+)'\)", script))

with open('static/index.html', encoding='utf-8') as f:
    html = f.read()

ids_in_html = set(re.findall(r'id="([^"]+)"', html))

missing = ids_in_script - ids_in_html
print('Missing IDs in HTML:', missing)
