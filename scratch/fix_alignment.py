import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's fix the brand first: Play Zone -> <span class="whitespace-nowrap">Play Zone</span>
    # Or just add whitespace-nowrap to the <a> tag.
    
    # Let's add whitespace-nowrap to the brand a tag
    content = content.replace('class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim"', 'class="flex items-center gap-2 font-headline-md text-headline-md font-extrabold text-primary dark:text-primary-fixed-dim whitespace-nowrap"')
    
    # We will replace all px-4 py-2 in the navbar links to px-2 py-2 to save space
    # And add whitespace-nowrap to ALL of them
    
    # We can just do a regex for the navbar links
    # But it's easier to just find the block from <div class="hidden xl:flex items-center gap-2">
    # up to </nav>
    
    start_idx = content.find('<nav')
    end_idx = content.find('</nav>')
    
    if start_idx != -1 and end_idx != -1:
        nav_part = content[start_idx:end_idx]
        
        # Replace px-4 with px-2 for the links
        nav_part = nav_part.replace('px-4 py-2', 'px-2 py-2 whitespace-nowrap')
        
        # Sign up button has px-6
        nav_part = nav_part.replace('px-6 py-2', 'px-4 py-2 whitespace-nowrap')
        
        content = content[:start_idx] + nav_part + content[end_idx:]
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Fixed alignment issues in navbars")
