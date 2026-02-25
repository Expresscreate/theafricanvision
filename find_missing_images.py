import os
import urllib.parse
import re

base_dir = r"c:\Users\LENOVO\Documents\Gabson\patrick maloum\theafricanvision\anyl4psd.org-main"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Expanded regex to catch images in various attributes and CSS
# srcs, hrefs, data-*, srcset, url()
patterns = [
    r'src=[\'"]([^\'"]+)[\'"]',
    r'href=[\'"]([^\'"]+)[\'"]',
    r'data-[a-z-]+=[\'"]([^\'"]+)[\'"]',
    r'url\([\'"]?([^\'"()]+)[\'"]?\)',
    r'content=[\'"]([^\'"]+)[\'"]' # for social tags
]

candidates = set()
for p in patterns:
    candidates.update(re.findall(p, content, re.IGNORECASE))

# Special handling for srcset
srcset_pattern = re.compile(r'srcset=[\'"]([^\'"]+)[\'"]', re.IGNORECASE)
for match in srcset_pattern.findall(content):
    parts = match.split(',')
    for part in parts:
        url = part.strip().split(' ')[0]
        candidates.add(url)

missing_images = []
image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp')

for url in candidates:
    clean_url = url.replace('&amp;', '&')
    clean_url = clean_url.split('?')[0].split('#')[0].strip()
    
    if any(clean_url.lower().endswith(ext) for ext in image_exts):
        if clean_url.startswith('data:'):
            continue
            
        is_missing = False
        reason = ""
        
        if clean_url.startswith(('http://', 'https://')):
            # It's an absolute URL. Usually HTTrack should have converted it.
            # If it's still absolute, it's "missing" from the local copy.
            is_missing = True
            reason = "Absolute external URL"
        elif clean_url.startswith('//'):
            is_missing = True
            reason = "Protocol-relative URL"
        else:
            # Local path
            relative_path = clean_url
            if relative_path.startswith('/'):
                relative_path = relative_path[1:]
            
            full_path = os.path.join(base_dir, os.path.normpath(relative_path))
            if not os.path.exists(full_path):
                is_missing = True
                reason = "File not found locally"
        
        if is_missing:
            missing_images.append((url, reason))

with open("missing_images_utf8.txt", "w", encoding="utf-8") as out:
    out.write(f"Found {len(missing_images)} missing or external image links:\n")
    for img, reason in sorted(missing_images):
        out.write(f"{reason}: {img}\n")

print(f"Refined script found {len(missing_images)} issues. Results in missing_images_utf8.txt")
