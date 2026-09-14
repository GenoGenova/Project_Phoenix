from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[3]
im = Image.open(Path(__file__).with_name('numen-favicon-master-v1.png'))
im.save(root / 'web/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
for size, name in [(32, 'numen-favicon-32.png'), (180, 'numen-apple-touch-icon.png')]:
    im.resize((size, size), Image.Resampling.LANCZOS).save(root / 'web/assets' / name)
p = root / 'web/index.html'
s = p.read_text(encoding='utf-8')
if 'numen-favicon-32.png' not in s:
    s = s.replace('<title>', '<link rel="icon" href="favicon.ico" sizes="16x16 32x32 48x48"><link rel="icon" type="image/png" sizes="32x32" href="assets/numen-favicon-32.png"><link rel="apple-touch-icon" sizes="180x180" href="assets/numen-apple-touch-icon.png"><title>', 1)
    p.write_text(s, encoding='utf-8')
assert Image.open(root / 'web/favicon.ico').ico.sizes() == {(16,16), (32,32), (48,48)}
print('Favicon sizes and website references verified.')
