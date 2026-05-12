import re

# Paths
index_path = '/Users/meeragupta/Downloads/MyPortfolio/index.html'
graphic_path = '/Users/meeragupta/Downloads/MyPortfolio/src/correct_graphic_base64.txt'
toolbar_path = '/Users/meeragupta/Downloads/MyPortfolio/src/toolbar_base64.txt'

# Read high-fidelity assets
with open(graphic_path, 'r') as f:
    graphic_base64 = f.read().strip()
    if not graphic_base64.startswith('data:'):
        graphic_base64 = 'data:image/png;base64,' + graphic_base64

with open(toolbar_path, 'r') as f:
    toolbar_base64 = f.read().strip()
    if not toolbar_base64.startswith('data:'):
        toolbar_base64 = 'data:image/png;base64,' + toolbar_base64

# Read current HTML
with open(index_path, 'r') as f:
    html = f.read()

# 1. Inject Main Graphic (torn-wrap)
graphic_pattern = re.compile(r'(<div class="torn-wrap">\s*<img[^>]*src=")([^"]*)(")', re.DOTALL)
html = graphic_pattern.sub(r'\1' + graphic_base64 + r'\3', html)

# 2. Inject Toolbar Graphic (toolbar)
toolbar_pattern = re.compile(r'(<div class="toolbar">\s*<img[^>]*src=")([^"]*)(")', re.DOTALL)
html = toolbar_pattern.sub(r'\1' + toolbar_base64 + r'\3', html)

# Write back
with open(index_path, 'w') as f:
    f.write(html)

print("Successfully injected high-fidelity graphic and toolbar.")
