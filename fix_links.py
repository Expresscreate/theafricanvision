import os

base_dir = r"c:\Users\LENOVO\Documents\Gabson\patrick maloum\theafricanvision\anyl4psd.org-main"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Replacements
content = content.replace('href="../connect.facebook.net', 'href="https://connect.facebook.net')
content = content.replace('src="../connect.facebook.net', 'src="https://connect.facebook.net')

content = content.replace('href="../img.youtube.com', 'href="https://img.youtube.com')
content = content.replace('src="../img.youtube.com', 'src="https://img.youtube.com')

content = content.replace('href="../www.google.com', 'href="https://www.google.com')
content = content.replace('src="../www.google.com', 'src="https://www.google.com')

with open(index_path, "w", encoding="utf-8", errors="ignore") as f:
    f.write(content)

print(f"Successfully replaced external URLs in {index_path}")
