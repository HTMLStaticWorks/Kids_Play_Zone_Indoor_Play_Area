import glob, re, os

target_dir = r'd:\project 2\Kids Play Zone & Indoor Play Area'
os.chdir(target_dir)

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for object-cover
    new_content = re.sub(r'class="([^"]*object-cover[^"]*)"', lambda m: m.group(0) if 'object-center' in m.group(1) else f'class="{m.group(1)} object-center"', content)
    
    # For text centering, we look at divs that are first children of grid md:grid-cols-2
    # Specifically in contact.html and others
    if 'contact.html' in filename:
        new_content = new_content.replace('<div class="z-10 relative">', '<div class="z-10 relative text-center md:text-left flex flex-col items-center md:items-start mx-auto md:mx-0">')
        new_content = new_content.replace('<div class="space-y-8">', '<div class="space-y-8 text-center md:text-left flex flex-col items-center md:items-start mx-auto md:mx-0">')
        # Fix the flex items inside space-y-8 that might now look weird if they are flex row
        # Specifically: <div class="flex items-start gap-4">
        # In contact.html these are contact details. If the parent is items-center, they might stretch or look weird.
        # So we also make them flex-col md:flex-row items-center md:items-start text-center md:text-left
        new_content = new_content.replace('<div class="flex items-start gap-4">', '<div class="flex flex-col md:flex-row items-center md:items-start gap-4 text-center md:text-left">')
        
        # also inquiry section
        new_content = new_content.replace('<div class="md:w-1/3 p-8 md:p-12 text-on-primary-container flex flex-col justify-center">', '<div class="md:w-1/3 p-8 md:p-12 text-on-primary-container flex flex-col justify-center items-center md:items-start text-center md:text-left">')

    if 'gallery.html' in filename:
        new_content = new_content.replace('<div class="flex justify-between items-end mb-12">', '<div class="flex flex-col md:flex-row justify-center md:justify-between items-center md:items-end mb-12 text-center md:text-left gap-6 md:gap-0">')
        
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filename}')
