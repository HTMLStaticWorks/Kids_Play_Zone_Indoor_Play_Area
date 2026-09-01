import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    footer_match = re.search(r'<footer[\s\S]*?</footer>', content)
    if footer_match:
        footer = footer_match.group(0)
        link = re.search(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>[\s\S]*?Play\s*Zone[\s\S]*?</a>', footer, re.IGNORECASE)
        if link:
            print(f, "->", link.group(1))
        else:
            print(f, "-> NO PlayZone BRAND LINK FOUND IN FOOTER")
    else:
        print(f, "-> NO FOOTER")
