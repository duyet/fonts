from glyphsLib import GSFont

def refine_anchors(file_path):
    print(f"Refining anchors in {file_path}")
    font = GSFont(file_path)
    
    # Adjust dotbelowcomb horizontal anchor to center it better under 'e'
    # Current dotbelowcomb _bottom is at (-28, 0). 
    # Let's shift it slightly.
    if 'dotbelowcomb' in font.glyphs:
        glyph = font.glyphs['dotbelowcomb']
        for layer in glyph.layers:
            for anchor in layer.anchors:
                if anchor.name == '_bottom':
                    anchor.position = (-10, 0) # Shifted right from -28
    
    font.save()

refine_anchors('sources/duyet-serif/DuyetSerif-Regular.glyphs')
refine_anchors('sources/duyet-serif/DuyetSerif-Italic.glyphs')
