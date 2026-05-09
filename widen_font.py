import re
import sys

def widen(file_path, factor=1.2):
    print(f"Widening {file_path} by {factor}...")
    with open(file_path, 'r') as f:
        content = f.read()

    # Regex to find (x,y,type) and scale x
    # Format: (224,0,ls)
    def scale_node(match):
        x = int(match.group(1))
        y = match.group(2)
        type_ = match.group(3)
        new_x = int(round(x * factor))
        return f"({new_x},{y},{type_})"

    content = re.sub(r'\((\d+),([-]?\d+),(\w+)\)', scale_node, content)

    # Regex to find width = XXX; and scale it
    def scale_width(match):
        prefix = match.group(1)
        w = int(match.group(2))
        new_w = int(round(w * factor))
        return f"{prefix}{new_w};"

    content = re.sub(r'(width = )(\d+);', scale_width, content)

    with open(file_path, 'w') as f:
        f.write(content)

widen('sources/duyet-serif/DuyetSerif-Regular.glyphs', 1.15)
widen('sources/duyet-serif/DuyetSerif-Italic.glyphs', 1.15)
