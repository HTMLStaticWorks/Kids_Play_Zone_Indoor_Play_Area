import glob
import re

files = glob.glob('*.html')

def exact_class(cls):
    return r'(?<=[\s"\'`])' + re.escape(cls) + r'(?=[\s"\'`])'

replacements = {
    exact_class('bg-background'): r'bg-background dark:bg-on-background',
    exact_class('text-on-background'): r'text-on-background dark:text-background',
    exact_class('bg-surface-container-lowest'): r'bg-surface-container-lowest dark:bg-[#122242]',
    exact_class('bg-surface-container-low'): r'bg-surface-container-low dark:bg-[#1a2a4a]',
    exact_class('bg-surface-container'): r'bg-surface-container dark:bg-inverse-surface',
    exact_class('bg-surface-container-high'): r'bg-surface-container-high dark:bg-[#283858]',
    exact_class('bg-surface-container-highest'): r'bg-surface-container-highest dark:bg-[#334155]',
    exact_class('bg-surface'): r'bg-surface dark:bg-on-background',
    exact_class('bg-surface-variant'): r'bg-surface-variant dark:bg-[#213050]',
    exact_class('text-on-surface-variant'): r'text-on-surface-variant dark:text-[#cbd5e1]',
    exact_class('text-on-surface'): r'text-on-surface dark:text-[#f8fafc]',
    exact_class('border-outline-variant/50'): r'border-outline-variant/50 dark:border-[#3f4850]/50',
    exact_class('border-outline-variant'): r'border-outline-variant dark:border-[#3f4850]',
}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied global dark mode classes to all HTML files safely.")
