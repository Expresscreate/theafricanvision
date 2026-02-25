import os
import urllib.parse
import re

base_dir = r"c:\Users\LENOVO\Documents\Gabson\patrick maloum\theafricanvision\anyl4psd.org-main"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

link_pattern = re.compile(r'(?:href|src)=[\'"]([^\'"]+)[\'"]')
links = link_pattern.findall(content)

broken_links = set()

for link in links:
    if link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'data:')):
        continue
    
    clean_link = link.split('?')[0].split('#')[0]
    clean_link = urllib.parse.unquote(clean_link)
    
    if clean_link.startswith('/'):
        clean_link = clean_link[1:]
        
    full_path = os.path.join(base_dir, os.path.normpath(clean_link))
    
    if not os.path.exists(full_path):
        broken_links.add(link)

with open("broken_links_utf8.txt", "w", encoding="utf-8") as out:
    out.write("Total unique local links found: {}\n".format(len(set([l for l in links if not l.startswith(('http', 'mailto', 'tel', '#', 'data', 'javascript'))]))))
    out.write("Broken Links/Images ({} found):\n".format(len(broken_links)))
    for bl in sorted(broken_links):
        out.write(bl + "\n")
