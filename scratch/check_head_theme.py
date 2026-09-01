import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    head = content.split("</head>")[0] if "</head>" in content else ""
    theme_script = re.search(r'<script[^>]*>[\s\S]*?localStorage[\s\S]*?</script>', head, re.IGNORECASE)
    print(f, "-> IN HEAD:" if theme_script else "-> MISSING IN HEAD")
