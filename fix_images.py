import os

base_dir = r"c:\Users\LENOVO\Documents\Gabson\patrick maloum\theafricanvision\anyl4psd.org-main"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Fix absolute and protocol-relative links for wp-content
replacements = [
    ('https://anyl4psd.org/wp-content/', 'wp-content/'),
    ('http://anyl4psd.org/wp-content/', 'wp-content/'),
    ('//anyl4psd.org/wp-content/', 'wp-content/'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(index_path, "w", encoding="utf-8", errors="ignore") as f:
    f.write(content)

print(f"Successfully fixed image links in {index_path}")
