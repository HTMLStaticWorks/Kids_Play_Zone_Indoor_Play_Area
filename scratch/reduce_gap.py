import glob

files = glob.glob('*.html')
exclude = ['dashboard.html', 'login.html', 'signup.html']

for f in files:
    if f in exclude:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace gap-6 with gap-4 in the mobile menu container
    # The container starts with: <div id="mobile-menu" class="hidden fixed inset-0 bg-surface/95 dark:bg-inverse-surface/95 z-50 flex-col pt-24 px-8 gap-6 overflow-y-auto backdrop-blur-md">
    
    old_class = 'id="mobile-menu" class="hidden fixed inset-0 bg-surface/95 dark:bg-inverse-surface/95 z-50 flex-col pt-24 px-8 gap-6 overflow-y-auto backdrop-blur-md"'
    new_class = 'id="mobile-menu" class="hidden fixed inset-0 bg-surface/95 dark:bg-inverse-surface/95 z-50 flex-col pt-24 px-8 gap-3 overflow-y-auto backdrop-blur-md"'
    
    if old_class in content:
        content = content.replace(old_class, new_class)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Reduced gap in {f}")
    else:
        # Try a more general regex replacement if exact string doesn't match
        import re
        new_content = re.sub(r'(id="mobile-menu".*?)gap-6', r'\1gap-3', content)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Reduced gap in {f} using regex")
        else:
            print(f"No match for {f}")
