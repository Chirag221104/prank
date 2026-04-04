import re
with open('d:/Projects/spam link/audio_b64.txt', 'r') as f:
    b64 = f.read().strip()

with open('d:/Projects/spam link/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r"const audioBase64 = '[^']+';", f"const audioBase64 = '{b64}';", html)

with open('d:/Projects/spam link/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
