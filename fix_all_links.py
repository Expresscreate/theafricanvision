import os
import re

base_dir = r"c:\Users\LENOVO\Documents\Gabson\patrick maloum\theafricanvision\anyl4psd.org-main"

def fix_html_content(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Calculate relative prefix to site root
    rel_depth = os.path.relpath(base_dir, os.path.dirname(file_path))
    if rel_depth == ".":
        prefix = ""
    else:
        prefix = rel_depth.replace("\\", "/") + "/"

    # 1. External Resources Replacements (Facebook, YouTube, Google)
    # HTTrack often adds ../ before these if they were caught as external but not downloaded
    content = content.replace('href="../connect.facebook.net', 'href="https://connect.facebook.net')
    content = content.replace('src="../connect.facebook.net', 'src="https://connect.facebook.net')
    content = content.replace('href="../img.youtube.com', 'href="https://img.youtube.com')
    content = content.replace('src="../img.youtube.com', 'src="https://img.youtube.com')
    content = content.replace('href="../www.google.com', 'href="https://www.google.com')
    content = content.replace('src="../www.google.com', 'src="https://www.google.com')

    # 2. Internal Image Paths (Convert absolute anyl4psd.org to relative)
    # We target wp-content, wp-includes, etc.
    patterns = [
        'https://anyl4psd.org/',
        'http://anyl4psd.org/',
        '//anyl4psd.org/'
    ]
    
    for pattern in patterns:
        content = content.replace(pattern + 'wp-content/', prefix + 'wp-content/')
        content = content.replace(pattern + 'wp-includes/', prefix + 'wp-includes/')

    with open(file_path, "w", encoding="utf-8", errors="ignore") as f:
        f.write(content)

def main():
    html_count = 0
    for root, dirs, files in os.walk(base_dir):
        # Skip wp-content as it mostly contains assets, not the site wrapper html usually
        # But we should scan everywhere just in case for subpages
        for file in files:
            if file.lower().endswith(".html"):
                file_path = os.path.join(root, file)
                fix_html_content(file_path)
                html_count += 1
    
    print(f"Processed {html_count} HTML files.")

if __name__ == "__main__":
    main()
