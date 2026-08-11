import os
import glob

# Files to update
files = glob.glob('*.html')
exclude = ['dashboard.html', 'login.html', 'signup.html']

mobile_menu_html = """
<!-- Mobile Menu -->
<div id="mobile-menu" class="hidden fixed inset-0 bg-surface/95 dark:bg-inverse-surface/95 z-50 flex-col pt-24 px-8 gap-6 overflow-y-auto backdrop-blur-md">
    <button id="close-menu-btn" class="absolute top-6 right-6 p-2 text-primary focus:outline-none"><span class="material-symbols-outlined text-3xl">close</span></button>
    <a href="index.html" class="text-2xl font-bold text-primary">Home</a>
    <a href="play zone.html" class="text-2xl font-bold text-primary">Play Zone</a>
    <a href="gallery.html" class="text-2xl font-bold text-primary">Gallery</a>
    <a href="membership.html" class="text-2xl font-bold text-primary">Membership</a>
    <a href="package.html" class="text-2xl font-bold text-primary">Package</a>
    <a href="contact.html" class="text-2xl font-bold text-primary">Contact</a>
    <a href="dashboard.html" class="text-2xl font-bold text-primary">Dashboard</a>
    <div class="h-px bg-outline-variant/30 w-full my-2"></div>
    <a href="login.html" class="text-xl font-bold text-on-surface-variant dark:text-[#cbd5e1]">Login</a>
    <a href="signup.html" class="text-xl font-bold text-on-surface-variant dark:text-[#cbd5e1]">Sign Up</a>
</div>
<script>
    document.getElementById('mobile-menu-btn')?.addEventListener('click', () => {
        document.getElementById('mobile-menu').classList.remove('hidden');
        document.getElementById('mobile-menu').classList.add('flex');
    });
    document.getElementById('close-menu-btn')?.addEventListener('click', () => {
        document.getElementById('mobile-menu').classList.add('hidden');
        document.getElementById('mobile-menu').classList.remove('flex');
    });
</script>
"""

hamburger_btn = """
<button id="mobile-menu-btn" class="xl:hidden text-on-surface-variant dark:text-[#cbd5e1] p-2 hover:bg-primary/5 rounded-full transition-colors focus:outline-none">
    <span class="material-symbols-outlined text-3xl">menu</span>
</button>
"""

for f in files:
    if f in exclude:
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'id="mobile-menu"' in content:
        print(f"Skipping {f}, already has mobile menu.")
        continue

    # Update breakpoints
    content = content.replace('class="hidden md:flex items-center gap-2"', 'class="hidden xl:flex items-center gap-2"')
    content = content.replace('class="hidden md:flex gap-2"', 'class="hidden xl:flex gap-2"')
    content = content.replace('class="hidden md:flex items-center gap-4"', 'class="hidden xl:flex items-center gap-4"')
    content = content.replace('class="hidden md:flex items-center gap-6"', 'class="hidden xl:flex items-center gap-6"')
    
    # Inject hamburger button before closing div of navbar inner container
    # The structure is <nav> -> <div> -> ... </div> </nav>
    # Find the closing </nav>
    nav_end_idx = content.find('</nav>')
    if nav_end_idx == -1:
        continue
    
    # We want to put the hamburger btn before the last </div> before </nav>
    # Let's find the last </div> before nav_end_idx
    last_div_idx = content.rfind('</div>', 0, nav_end_idx)
    if last_div_idx != -1:
        content = content[:last_div_idx] + hamburger_btn + content[last_div_idx:]
    
    # Re-find </nav> after insertion
    nav_end_idx = content.find('</nav>')
    
    # Inject mobile menu HTML + script right after </nav>
    content = content[:nav_end_idx + 6] + '\n' + mobile_menu_html + content[nav_end_idx + 6:]
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated {f}")
