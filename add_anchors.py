from glyphsLib import GSFont, GSAnchor

def add_mark_anchors(file_path):
    print(f"Adding anchors to marks in {file_path}")
    font = GSFont(file_path)
    
    # name, anchor_name, pos(x,y)
    marks = [
        ('hookabovecomb', '_top', (127, 510)),
        ('dotbelowcomb', '_bottom', (-28, 0)),
        ('horncomb', '_topright', (125, 450))
    ]
    
    for name, a_name, pos in marks:
        if name in font.glyphs:
            glyph = font.glyphs[name]
            for layer in glyph.layers:
                # Clear existing anchors of same name
                layer.anchors = [a for a in layer.anchors if a.name != a_name]
                new_anchor = GSAnchor()
                new_anchor.name = a_name
                new_anchor.position = pos
                layer.anchors.append(new_anchor)
                
    font.save()

add_mark_anchors('sources/duyet-serif/DuyetSerif-Regular.glyphs')
add_mark_anchors('sources/duyet-serif/DuyetSerif-Italic.glyphs')
