import re
from glyphsLib import GSFont, GSAnchor

def fix_font(file_path):
    print(f"Fixing VI alignment in {file_path}")
    font = GSFont(file_path)
    
    # name, new_anchor_x, shift_x, width
    marks = {
        'hookabovecomb': {'anchor': (0, 0), 'shift': -127, 'width': 0},
        'dotbelowcomb':  {'anchor': (0, 0), 'shift': 28,  'width': 0},
        'horncomb':      {'anchor': (0, 0), 'shift': -125, 'width': 0}
    }
    
    for name, config in marks.items():
        if name in font.glyphs:
            glyph = font.glyphs[name]
            for layer in glyph.layers:
                layer.width = config['width']
                # Shift all nodes
                for shape in layer.shapes:
                    if hasattr(shape, 'nodes'):
                        for node in shape.nodes:
                            pos = list(node.position)
                            pos[0] += config['shift']
                            node.position = tuple(pos)
                
                # Set anchor
                a_name = '_top' if 'hook' in name else '_bottom' if 'dot' in name else '_topright'
                layer.anchors = [a for a in layer.anchors if a.name != a_name]
                new_anchor = GSAnchor()
                new_anchor.name = a_name
                new_anchor.position = config['anchor']
                layer.anchors.append(new_anchor)
                
    # Also ensure base vowels have correct 'topright' for horn
    for name in ['o', 'u', 'O', 'U']:
        if name in font.glyphs:
            glyph = font.glyphs[name]
            for layer in glyph.layers:
                if name.lower() == 'o':
                    horn_pos = (layer.width - 20, 450)
                else:
                    horn_pos = (layer.width - 30, 450)
                    
                layer.anchors = [a for a in layer.anchors if a.name != 'topright']
                new_anchor = GSAnchor()
                new_anchor.name = 'topright'
                new_anchor.position = horn_pos
                layer.anchors.append(new_anchor)

    font.save()

fix_font('sources/duyet-serif/DuyetSerif-Regular.glyphs')
fix_font('sources/duyet-serif/DuyetSerif-Italic.glyphs')
