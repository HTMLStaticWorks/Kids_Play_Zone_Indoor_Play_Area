import glob
import re

files = glob.glob('*.html')

scroll_button_code = """
<!-- Scroll to Top Button -->
<button id="scrollToTopBtn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="fixed bottom-8 right-8 bg-primary text-on-primary p-3 rounded-full shadow-lg hover:scale-110 transition-all duration-300 z-50 opacity-0 pointer-events-none translate-y-4 flex items-center justify-center">
    <span class="material-symbols-outlined">arrow_upward</span>
</button>
<script>
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollToTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
            scrollToTopBtn.classList.add('opacity-100', 'translate-y-0');
        } else {
            scrollToTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
            scrollToTopBtn.classList.remove('opacity-100', 'translate-y-0');
        }
    });
</script>
</body>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'scrollToTopBtn' not in content:
        content = content.replace('</body>', scroll_button_code)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Scroll to top button added to all HTML files.")
