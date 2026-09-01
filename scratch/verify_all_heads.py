import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    head = content.split("</head>")[0]
    script_match = re.search(r'<script>([\s\S]*?)</script>', head)
    if script_match:
        script = script_match.group(1).strip()
        print("=== FILE:", f)
        print(script)
