import glob
import re

files = glob.glob('*.html')
exclude = ['dashboard.html', 'login.html', 'signup.html']

standard_brand = """<a class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim" href="index.html">
                <img src="logo.png" alt="Logo" class="h-10 w-10 object-cover rounded-full shadow-sm">
                Play Zone
            </a>"""

for f in files:
    if f in exclude:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to find the brand part in the navbar and replace it.
    # It could be <a ...>PlayZone</a> or <div ...>Play Zone</div>
    # Let's use regex to find it between <div class="flex justify-between items-center ..."> and the first <div class="hidden xl:flex
    
    pattern = r'(<div class="flex justify-between items-center.*?>)\s*(<a[^>]*>.*?</a>|<div[^>]*>.*?Play Zone.*?</div>)\s*(<div class="hidden xl:flex)'
    
    new_content = re.sub(pattern, r'\1\n            ' + standard_brand + r'\n            \3', content, flags=re.DOTALL)
    
    # Let's also ensure px-margin-mobile is present on the flex container
    # find <div class="flex justify-between items-center px-margin-desktop
    # replace with px-margin-mobile md:px-margin-desktop
    new_content = new_content.replace('px-margin-desktop py-4', 'px-margin-mobile md:px-margin-desktop py-4')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated brand/padding in {f}")
    else:
        print(f"No changes for {f}")
