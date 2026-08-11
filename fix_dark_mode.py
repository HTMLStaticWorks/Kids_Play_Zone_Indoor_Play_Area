import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav block to restrict our changes to the navbar
    nav_start = content.find('<nav')
    nav_end = content.find('</nav>')
    
    if nav_start != -1 and nav_end != -1:
        nav_content = content[nav_start:nav_end + 6]
        
        # 1. Fix nav background
        nav_content = nav_content.replace(
            'class="bg-surface/80 dark:bg-surface-dim/80 backdrop-blur-md shadow-sm dark:bg-surface-container-high fixed top-0 w-full z-50"',
            'class="bg-surface/80 dark:bg-inverse-surface/90 backdrop-blur-md shadow-sm fixed top-0 w-full z-50"'
        )
        
        # 2. Fix inactive link text color (currently text-on-surface-variant dark:text-on-surface-variant)
        nav_content = nav_content.replace(
            'text-on-surface-variant dark:text-on-surface-variant',
            'text-on-surface-variant dark:text-inverse-on-surface'
        )
        
        # 3. Fix active link border color
        nav_content = nav_content.replace(
            'border-b-2 border-primary font-bold',
            'border-b-2 border-primary dark:border-primary-fixed font-bold'
        )
        
        # 4. Fix buttons text color (currently text-on-surface-variant)
        # To avoid replacing the ones we already fixed in step 2:
        nav_content = re.sub(
            r'class="text-on-surface-variant([^"]*?hidden md:block)',
            r'class="text-on-surface-variant dark:text-inverse-on-surface\1',
            nav_content
        )

        content = content[:nav_start] + nav_content + content[nav_end + 6:]
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Done fixing dark mode menu in HTML files.")
