import re
import sys

def refine(file_path, x_factor=1.0, y_factor=0.85):
    print(f"Refining {file_path}: X*{x_factor}, Y*{y_factor}")
    with open(file_path, 'r') as f:
        content = f.read()

    # Scale nodes (x,y,type)
    def scale_node(match):
        x = int(match.group(1))
        y = int(match.group(2))
        type_ = match.group(3)
        new_x = int(round(x * x_factor))
        new_y = int(round(y * y_factor))
        return f"({new_x},{new_y},{type_})"

    content = re.sub(r'\((\d+),([-]?\d+),(\w+)\)', scale_node, content)

    # Scale horizontal widths
    def scale_width(match):
        prefix = match.group(1)
        w = int(match.group(2))
        new_w = int(round(w * x_factor))
        return f"{prefix}{new_w};"

    content = re.sub(r'(width = )(\d+);', scale_width, content)

    # Scale vertical metrics in customParameters
    def scale_metric(match):
        name = match.group(1)
        val = int(match.group(2))
        # Only scale vertical metrics
        if any(m in name for m in ['Ascender', 'Descender', 'Ascent', 'Descent', 'Height', 'Position']):
            new_val = int(round(val * y_factor))
            return f'name = {name};\nvalue = {new_val};'
        return match.group(0)

    content = re.sub(r'name = ([\w]+);\nvalue = ([-]?\d+);', scale_metric, content)

    with open(file_path, 'w') as f:
        f.write(content)

# We already widened by 1.15 in previous step.
# Now we shorten Y by 0.85. 
# We don't want to re-widen X, so x_factor = 1.0.
refine('sources/duyet-serif/DuyetSerif-Regular.glyphs', x_factor=1.0, y_factor=0.85)
refine('sources/duyet-serif/DuyetSerif-Italic.glyphs', x_factor=1.0, y_factor=0.85)
