import glob

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    lines = content.splitlines()[:25]
    print("=== FILE:", f)
    for l in lines:
        if "script" in l or "dark" in l or "theme" in l or "head" in l or "class=" in l:
            print("  ", l)
