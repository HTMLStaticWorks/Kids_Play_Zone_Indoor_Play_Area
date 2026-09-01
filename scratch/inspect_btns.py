import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    btns = re.findall(r'<button[^>]*dark_mode[^>]*>[\s\S]*?</button>', content, re.IGNORECASE)
    print("=== FILE:", f)
    for b in btns:
        print("  ", b.strip())
