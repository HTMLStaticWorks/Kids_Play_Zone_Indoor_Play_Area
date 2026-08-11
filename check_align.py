import glob, re, os

target_dir = r'd:\project 2\Kids Play Zone & Indoor Play Area'
os.chdir(target_dir)

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'<div class="grid md:grid-cols-2[^>]*>\s*<div class="([^"]*)"', content, re.DOTALL)
    if matches:
        print(f'{filename}: {matches}')
