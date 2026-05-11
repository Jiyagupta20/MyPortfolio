import re

with open("index.html", "r") as f:
    html = f.read()

with open("src/portfolio_base64.html", "r") as f:
    img_tag = f.read().strip()

pattern = re.compile(r'(<div class="torn-wrap">\s*)<!-- purple FOLIO behind -->.*?<!-- SVG torn paper mask on top -->.*?</svg>\s*(</div>)', re.DOTALL)

img_tag_styled = img_tag.replace('<img ', '<img style="width: 100%; height: 100%; object-fit: contain;" ')

new_html, count = pattern.subn(r'\1' + img_tag_styled + r'\n    \2', html)

if count > 0:
    with open("index.html", "w") as f:
        f.write(new_html)
    print(f"Success! Replaced {count} instance(s).")
else:
    print("Failed to find pattern to replace.")

