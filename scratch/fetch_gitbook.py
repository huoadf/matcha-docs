import urllib.request
import json
import os
import re

site_index_file = r'C:\Users\hayde\.gemini\antigravity\brain\f0a9b400-7b60-496b-a4ff-ebf85cbd14da\.system_generated\steps\1416\content.md'
with open(site_index_file, 'r', encoding='utf-8') as f:
    raw = f.read()

# Extract JSON from line 9
lines = raw.split('\n')
json_line = [l for l in lines if l.strip().startswith('{"version"')][0]
data = json.loads(json_line)

out_dir = r'C:\Users\hayde\.gemini\antigravity\scratch\gitbook_dump'
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0'}

print(f"Found {len(data['pages'])} pages in GitBook.")

for p in data['pages']:
    pathname = p['pathname'] # e.g. /matcha/luau-environment/functions/globals-functions
    slug = pathname.replace('/matcha', '').strip('/') or 'index'
    slug_clean = slug.replace('/', '_')
    
    url = f"https://matcha-latte.gitbook.io{pathname}.md"
    target_file = os.path.join(out_dir, f"{slug_clean}.md")
    
    print(f"Fetching {p['title']} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            with open(target_file, 'w', encoding='utf-8') as out_f:
                out_f.write(content)
            print(f"  -> Saved {len(content)} bytes")
    except Exception as e:
        print(f"  -> Failed: {e}")
