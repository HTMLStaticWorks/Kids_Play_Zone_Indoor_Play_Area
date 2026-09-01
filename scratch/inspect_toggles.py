import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    toggles = re.findall(r'<button[^>]*dark_mode[^>]*>[\s\S]*?</button>', content, re.IGNORECASE)
    toggles += re.findall(r'document\.documentElement\.classList\.toggle\([^\)]+\)', content, re.IGNORECASE)
    print("=== FILE:", f)
    for t in set(toggles):
        print("  ", t.strip())
