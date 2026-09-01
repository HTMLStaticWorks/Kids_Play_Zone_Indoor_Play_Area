import glob, re

target_script = """<script>
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
</script>"""

pattern = r'<script>\s*if\s*\([^)]*localStorage\.theme\s*===\s*[\'\"]dark[\'\"][\s\S]*?</script>'

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    if re.search(pattern, content):
        new_content = re.sub(pattern, target_script, content, count=1)
        with open(f, "w", encoding="utf-8") as out:
            out.write(new_content)
        print("FIXED:", f)
    else:
        print("NO MATCH:", f)
