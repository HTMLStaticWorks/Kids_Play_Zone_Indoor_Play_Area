import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    head = content.split("</head>")[0] if "</head>" in content else ""
    theme_scripts = re.findall(r'<script[^>]*>[\s\S]*?</script>', head, re.IGNORECASE)
    print("=== FILE:", f)
    for s in theme_scripts:
        if "theme" in s or "dark" in s or "localStorage" in s:
            print("  ", s.strip())
