import glob, os

target_dir = r'd:\project 2\Kids Play Zone & Indoor Play Area'
os.chdir(target_dir)

def make_responsive(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for common patterns of uncentered headings or text that should be centered on mobile
    
    # In package.html, there's a pricing section maybe? Let's check it.
    if 'package.html' in filename:
        pass # Actually package.html has <div class="text-center mb-16"> for its headers
        
    # Let's apply a general fix for all instances of "text-left" without "text-center md:text-left"
    # Wait, usually the issue is lack of ANY text alignment, defaulting to left.
    # The fix we did for contact and gallery covers the main hero and split sections that were left aligned.
    
    pass

