import os
import glob
import re

html_files = glob.glob('*.html')

favicon_tag = '<link rel="icon" type="image/png" href="favicon.png"/>'

logo_div = """<div class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim">
                <img src="logo.png" alt="Logo" class="h-10 w-10 object-cover rounded-full shadow-sm">
                Play Zone
            </div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add favicon
    if 'favicon.png' not in content:
        content = content.replace('<meta charset="utf-8"/>', f'<meta charset="utf-8"/>\n<link rel="icon" type="image/png" href="favicon.png"/>')
    
    # Add logo
    pattern = re.compile(r'<div class="font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim">\s*Play Zone\s*</div>')
    
    if pattern.search(content):
        content = pattern.sub(logo_div, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Done updating HTML files.")
