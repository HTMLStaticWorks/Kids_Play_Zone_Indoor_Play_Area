import glob
import re

files = glob.glob('*.html')
exclude = ['dashboard.html', 'login.html', 'signup.html']

for f in files:
    if f in exclude:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to insert "Home 2" right after "Home" in both desktop and mobile menus
    
    # 1. Desktop Menu
    # Find: <a class="[classes]" href="index.html">Home</a>
    # We need to capture the exact classes used for the link to replicate them, but they might differ based on which page is active.
    # We'll use a regex to find the Home link and inject Home 2 after it.
    
    pattern_desktop = r'(<a\s+class="[^"]+"\s+href="index\.html">\s*Home\s*</a>)'
    
    # But wait, in index.html, the Home link might be active, so its classes are different. 
    # It's better to just extract the full <a> tag for Home, clone it, change href and text, and insert it.
    
    def replace_desktop(match):
        home_tag = match.group(1)
        # make it inactive if it's active
        home2_tag = home_tag.replace('href="index.html"', 'href="home2.html"').replace('>Home<', '>Home 2<')
        
        # If this is index.html, the home tag might be active (border-b-2). 
        # For home2, we should use the inactive classes if we are in index.html, or active if we are in home2.html
        if f == 'home2.html':
            # Home2 is active
            home2_tag = home2_tag.replace('text-on-surface-variant dark:text-[#cbd5e1] dark:text-inverse-on-surface hover:text-primary dark:hover:text-primary-fixed transition-colors hover:bg-primary/5 dark:hover:bg-primary-fixed/10 rounded-full', 'text-primary dark:text-primary-fixed border-b-2 border-primary dark:border-primary-fixed font-bold hover:scale-105 transition-transform duration-200')
            # Home is inactive
            home_tag = home_tag.replace('text-primary dark:text-primary-fixed border-b-2 border-primary dark:border-primary-fixed font-bold hover:scale-105 transition-transform duration-200', 'text-on-surface-variant dark:text-[#cbd5e1] dark:text-inverse-on-surface hover:text-primary dark:hover:text-primary-fixed transition-colors hover:bg-primary/5 dark:hover:bg-primary-fixed/10 rounded-full')
        elif f == 'index.html':
            # Home is active, Home2 should be inactive
            home2_tag = home2_tag.replace('text-primary dark:text-primary-fixed border-b-2 border-primary dark:border-primary-fixed font-bold hover:scale-105 transition-transform duration-200', 'text-on-surface-variant dark:text-[#cbd5e1] dark:text-inverse-on-surface hover:text-primary dark:hover:text-primary-fixed transition-colors hover:bg-primary/5 dark:hover:bg-primary-fixed/10 rounded-full')
            
        return home_tag + '\n' + home2_tag

    new_content = re.sub(pattern_desktop, replace_desktop, content)
    
    # 2. Mobile Menu
    pattern_mobile = r'(<a href="index\.html" class="text-2xl font-bold text-primary">\s*Home\s*</a>)'
    new_content = re.sub(pattern_mobile, r'\1\n    <a href="home2.html" class="text-2xl font-bold text-primary">Home 2</a>', new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Added Home 2 link to {f}")
    else:
        print(f"Could not add Home 2 link to {f}")
