import sys
import re

# Read the correct base64 graphic
with open('/Users/meeragupta/Downloads/MyPortfolio/src/correct_graphic_base64.txt', 'r') as f:
    correct_base64 = f.read().strip()

# Read the current index.html
with open('/Users/meeragupta/Downloads/MyPortfolio/index.html', 'r') as f:
    html = f.read()

# The pattern to replace is the <img> tag inside <div class="torn-wrap">
pattern = re.compile(r'(<div class="torn-wrap">\s*<img[^>]*src=")([^"]*)(")', re.DOTALL)
new_html = pattern.sub(r'\1' + correct_base64 + r'\3', html)

with open('/Users/meeragupta/Downloads/MyPortfolio/index.html', 'w') as f:
    f.write(new_html)

print("Restored the high-fidelity graphic into index.html")
