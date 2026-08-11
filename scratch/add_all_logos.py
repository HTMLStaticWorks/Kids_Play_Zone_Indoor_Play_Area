import glob

files = glob.glob('*.html')

logo_html = """<div class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim">
                <img src="logo.png" alt="Logo" class="h-10 w-10 object-cover rounded-full shadow-sm">
                Play Zone
            </div>"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # If the file already has the logo, skip it
    if 'src="logo.png"' in content and '<nav' in content: # Just to be safe, don't double add
        pass
    
    # We want to replace the text-only Play Zone logo with the image one in the navbar
    old_logo_html_1 = """<div class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary">
                Play Zone
            </div>"""
    
    old_logo_html_2 = """<div class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim">
                Play Zone
            </div>"""
            
    if old_logo_html_1 in content:
        content = content.replace(old_logo_html_1, logo_html)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Added logo to {f}")
    elif old_logo_html_2 in content:
        content = content.replace(old_logo_html_2, logo_html)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Added logo to {f}")
