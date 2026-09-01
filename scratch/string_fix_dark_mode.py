import glob

bad_block = """<script>
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        document.documentElement.classList.remove('dark');
    } else {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
    }
</script>"""

good_block = """<script>
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
</script>"""

for f in sorted(glob.glob("*.html")):
    content = open(f, "r", encoding="utf-8").read()
    if "document.documentElement.classList.remove('dark');" in content:
        # Replace inside the if block
        fixed_content = content.replace(
            "document.documentElement.classList.add('dark');\n        document.documentElement.classList.remove('dark');",
            "document.documentElement.classList.add('dark');"
        ).replace(
            "document.documentElement.classList.add('dark');\n    document.documentElement.classList.remove('dark');",
            "document.documentElement.classList.add('dark');"
        )
        with open(f, "w", encoding="utf-8") as out:
            out.write(fixed_content)
        print("REPLACED:", f)
    else:
        print("ALREADY CLEAN:", f)
