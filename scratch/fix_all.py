import glob
import re
import os

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix footer
    content = content.replace(
        'dark:bg-surface-container-lowest border-t border-outline-variant/50 dark:border-[#3f4850]/50 pt-16 pb-8 mt-20">',
        'border-t border-outline-variant/50 dark:border-[#3f4850]/50 pt-16 pb-8 mt-20">'
    )

    if f == 'index.html':
        # Fix nav active classes
        content = content.replace(
            '<a class="text-primary dark:text-primary-fixed border-b-2 border-primary dark:border-primary-fixed font-bold font-label-md text-label-md hover:scale-105 transition-transform duration-200 px-2 py-2 whitespace-nowrap" href="home2.html">Home 2</a>',
            '<a class="text-on-surface-variant dark:text-[#cbd5e1] dark:text-inverse-on-surface hover:text-primary dark:hover:text-primary-fixed transition-colors font-label-md text-label-md hover:bg-primary/5 dark:hover:bg-primary-fixed/10 rounded-full px-2 py-2 whitespace-nowrap" href="home2.html">Home 2</a>'
        )
        # Fix hero colors
        content = content.replace(
            '<h1 class="font-headline-xl text-headline-xl text-primary mb-6 max-w-4xl drop-shadow-sm">Where Little Adventures Begin Every Day</h1>',
            '<h1 class="font-headline-xl text-headline-xl text-primary dark:text-primary-fixed mb-6 max-w-4xl drop-shadow-sm">Where Little Adventures Begin Every Day</h1>'
        )
        content = content.replace(
            '<p class="font-body-lg text-body-lg text-on-surface-variant dark:text-[#cbd5e1] max-w-2xl mb-10">Experience a world of safe, clean, and imaginative play designed for children of all ages to explore, learn, and grow.</p>',
            '<p class="font-body-lg text-body-lg text-on-surface-variant dark:text-inverse-on-surface max-w-2xl mb-10">Experience a world of safe, clean, and imaginative play designed for children of all ages to explore, learn, and grow.</p>'
        )
        content = content.replace(
            '<button class="bg-primary text-on-primary px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform duration-150 shadow-md">Explore Play Zones</button>',
            '<button class="bg-primary text-on-primary dark:bg-primary-fixed dark:text-on-primary-fixed px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform duration-150 shadow-md">Explore Play Zones</button>'
        )
        content = content.replace(
            '<button class="border-2 border-primary text-primary px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform duration-150 shadow-md">Reserve a Slot</button>',
            '<button class="border-2 border-primary text-primary dark:border-primary-fixed dark:text-primary-fixed px-8 py-4 rounded-full font-label-md text-label-md hover:scale-95 transition-transform duration-150 shadow-md">Reserve a Slot</button>'
        )

    if f == 'home2.html':
        content = content.replace(
            '<a class="text-primary dark:text-primary-fixed border-b-2 border-primary dark:border-primary-fixed font-bold font-label-md text-label-md hover:scale-105 transition-transform duration-200 px-2 py-2 whitespace-nowrap" href="index.html">Home</a>',
            '<a class="text-on-surface-variant dark:text-[#cbd5e1] dark:text-inverse-on-surface hover:text-primary dark:hover:text-primary-fixed transition-colors font-label-md text-label-md hover:bg-primary/5 dark:hover:bg-primary-fixed/10 rounded-full px-2 py-2 whitespace-nowrap" href="index.html">Home</a>'
        )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
