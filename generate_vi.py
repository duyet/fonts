import sys
from glyphsLib import GSFont, GSGlyph, GSComponent

def add_vi(file_path):
    print(f"Generating Vietnamese for {file_path}")
    font = GSFont(file_path)
    
    # Mapping of VI characters to components
    # Format: (name, unicode, [base, mark1, mark2...])
    vi_set = [
        # a
        ('aacute', '00E1', ['a', 'acutecomb']),
        ('agrave', '00E0', ['a', 'gravecomb']),
        ('ahookabove', '1EA3', ['a', 'hookabovecomb']),
        ('atilde', '00E3', ['a', 'tildecomb']),
        ('adotbelow', '1EA1', ['a', 'dotbelowcomb']),
        ('abreve', '0103', ['a', 'brevecomb']),
        ('abreveacute', '1EAF', ['a', 'brevecomb', 'acutecomb']),
        ('abrevegrave', '1EB1', ['a', 'brevecomb', 'gravecomb']),
        ('abrevehookabove', '1EB3', ['a', 'brevecomb', 'hookabovecomb']),
        ('abrevetilde', '1EB5', ['a', 'brevecomb', 'tildecomb']),
        ('abrevedotbelow', '1EB7', ['a', 'brevecomb', 'dotbelowcomb']),
        ('acircumflex', '00E2', ['a', 'circumflexcomb']),
        ('acircumflexacute', '1EA5', ['a', 'circumflexcomb', 'acutecomb']),
        ('acircumflexgrave', '1EA7', ['a', 'circumflexcomb', 'gravecomb']),
        ('acircumflexhookabove', '1EA9', ['a', 'circumflexcomb', 'hookabovecomb']),
        ('acircumflextilde', '1EAB', ['a', 'circumflexcomb', 'tildecomb']),
        ('acircumflexdotbelow', '1EAD', ['a', 'circumflexcomb', 'dotbelowcomb']),
        # e
        ('eacute', '00E9', ['e', 'acutecomb']),
        ('egrave', '00E8', ['e', 'gravecomb']),
        ('ehookabove', '1EBB', ['e', 'hookabovecomb']),
        ('etilde', '1EBD', ['e', 'tildecomb']),
        ('edotbelow', '1EB9', ['e', 'dotbelowcomb']),
        ('ecircumflex', '00EA', ['e', 'circumflexcomb']),
        ('ecircumflexacute', '1EBF', ['e', 'circumflexcomb', 'acutecomb']),
        ('ecircumflexgrave', '1EC1', ['e', 'circumflexcomb', 'gravecomb']),
        ('ecircumflexhookabove', '1EC3', ['e', 'circumflexcomb', 'hookabovecomb']),
        ('ecircumflextilde', '1EC5', ['e', 'circumflexcomb', 'tildecomb']),
        ('ecircumflexdotbelow', '1EC7', ['e', 'circumflexcomb', 'dotbelowcomb']),
        # i
        ('iacute', '00ED', ['i', 'acutecomb']),
        ('igrave', '00EC', ['i', 'gravecomb']),
        ('ihookabove', '1EC9', ['i', 'hookabovecomb']),
        ('itilde', '0129', ['i', 'tildecomb']),
        ('idotbelow', '1ECB', ['i', 'dotbelowcomb']),
        # o
        ('oacute', '00F3', ['o', 'acutecomb']),
        ('ograve', '00F2', ['o', 'gravecomb']),
        ('ohookabove', '1ECD', ['o', 'hookabovecomb']),
        ('otilde', '00F5', ['o', 'tildecomb']),
        ('odotbelow', '1ECF', ['o', 'dotbelowcomb']),
        ('ocircumflex', '00F4', ['o', 'circumflexcomb']),
        ('ocircumflexacute', '1ED1', ['o', 'circumflexcomb', 'acutecomb']),
        ('ocircumflexgrave', '1ED3', ['o', 'circumflexcomb', 'gravecomb']),
        ('ocircumflexhookabove', '1ED5', ['o', 'circumflexcomb', 'hookabovecomb']),
        ('ocircumflextilde', '1ED7', ['o', 'circumflexcomb', 'tildecomb']),
        ('ocircumflexdotbelow', '1ED9', ['o', 'circumflexcomb', 'dotbelowcomb']),
        ('ohorn', '01A1', ['o', 'horncomb']),
        ('ohornacute', '1EDB', ['o', 'horncomb', 'acutecomb']),
        ('ohorngrave', '1EDD', ['o', 'horncomb', 'gravecomb']),
        ('ohornhookabove', '1EDF', ['o', 'horncomb', 'hookabovecomb']),
        ('ohorntilde', '1EE1', ['o', 'horncomb', 'tildecomb']),
        ('ohorndotbelow', '1EE3', ['o', 'horncomb', 'dotbelowcomb']),
        # u
        ('uacute', '00FA', ['u', 'acutecomb']),
        ('ugrave', '00F9', ['u', 'gravecomb']),
        ('uhookabove', '1EE7', ['u', 'hookabovecomb']),
        ('utilde', '0169', ['u', 'tildecomb']),
        ('udotbelow', '1EE5', ['u', 'dotbelowcomb']),
        ('uhorn', '01B0', ['u', 'horncomb']),
        ('uhornacute', '1EE9', ['u', 'horncomb', 'acutecomb']),
        ('uhorngrave', '1EEB', ['u', 'horncomb', 'gravecomb']),
        ('uhornhookabove', '1EED', ['u', 'horncomb', 'hookabovecomb']),
        ('uhorntilde', '1EEF', ['u', 'horncomb', 'tildecomb']),
        ('uhorndotbelow', '1EF1', ['u', 'horncomb', 'dotbelowcomb']),
        # y
        ('yacute', '00FD', ['y', 'acutecomb']),
        ('ygrave', '1EF3', ['y', 'gravecomb']),
        ('yhookabove', '1EF7', ['y', 'hookabovecomb']),
        ('ytilde', '1EF9', ['y', 'tildecomb']),
        ('ydotbelow', '1EF5', ['y', 'dotbelowcomb']),
        # Caps
        ('Aacute', '00C1', ['A', 'acutecomb']),
        ('Agrave', '00C0', ['A', 'gravecomb']),
        ('Ahookabove', '1EA2', ['A', 'hookabovecomb']),
        ('Atilde', '00C3', ['A', 'tildecomb']),
        ('Adotbelow', '1EA0', ['A', 'dotbelowcomb']),
        ('Abreve', '0102', ['A', 'brevecomb']),
        ('Abreveacute', '1EAE', ['A', 'brevecomb', 'acutecomb']),
        ('Abrevegrave', '1EB0', ['A', 'brevecomb', 'gravecomb']),
        ('Abrevehookabove', '1EB2', ['A', 'brevecomb', 'hookabovecomb']),
        ('Abrevetilde', '1EB4', ['A', 'brevecomb', 'tildecomb']),
        ('Abrevedotbelow', '1EB6', ['A', 'brevecomb', 'dotbelowcomb']),
        ('Acircumflex', '00C2', ['A', 'circumflexcomb']),
        ('Acircumflexacute', '1EA4', ['A', 'circumflexcomb', 'acutecomb']),
        ('Acircumflexgrave', '1EA6', ['A', 'circumflexcomb', 'gravecomb']),
        ('Acircumflexhookabove', '1EA8', ['A', 'circumflexcomb', 'hookabovecomb']),
        ('Acircumflextilde', '1EAA', ['A', 'circumflexcomb', 'tildecomb']),
        ('Acircumflexdotbelow', '1EAC', ['A', 'circumflexcomb', 'dotbelowcomb']),
        # E
        ('Eacute', '00C9', ['E', 'acutecomb']),
        ('Egrave', '00C8', ['E', 'gravecomb']),
        ('Ehookabove', '1EBA', ['E', 'hookabovecomb']),
        ('Etilde', '1EBC', ['E', 'hookabovecomb']),
        ('Edotbelow', '1EB8', ['E', 'dotbelowcomb']),
        ('Ecircumflex', '00CA', ['E', 'circumflexcomb']),
        ('Ecircumflexacute', '1EBE', ['E', 'circumflexcomb', 'acutecomb']),
        ('Ecircumflexgrave', '1EC0', ['E', 'circumflexcomb', 'gravecomb']),
        ('Ecircumflexhookabove', '1EC2', ['E', 'circumflexcomb', 'hookabovecomb']),
        ('Ecircumflextilde', '1EC4', ['E', 'circumflexcomb', 'tildecomb']),
        ('Ecircumflexdotbelow', '1EC6', ['E', 'circumflexcomb', 'dotbelowcomb']),
        # I
        ('Iacute', '00CD', ['I', 'acutecomb']),
        ('Igrave', '00CC', ['I', 'gravecomb']),
        ('Ihookabove', '1EC8', ['I', 'hookabovecomb']),
        ('Itilde', '0128', ['I', 'tildecomb']),
        ('Idotbelow', '1ECA', ['I', 'dotbelowcomb']),
        # O
        ('Oacute', '00D3', ['O', 'acutecomb']),
        ('Ograve', '00D2', ['O', 'gravecomb']),
        ('Ohookabove', '1ECC', ['O', 'hookabovecomb']),
        ('Otilde', '00D5', ['O', 'tildecomb']),
        ('Odotbelow', '1ECE', ['O', 'dotbelowcomb']),
        ('Ocircumflex', '00D4', ['O', 'circumflexcomb']),
        ('Ocircumflexacute', '1ED0', ['O', 'circumflexcomb', 'acutecomb']),
        ('Ocircumflexgrave', '1ED2', ['O', 'circumflexcomb', 'gravecomb']),
        ('Ocircumflexhookabove', '1ED4', ['O', 'circumflexcomb', 'hookabovecomb']),
        ('Ocircumflextilde', '1ED6', ['O', 'circumflexcomb', 'tildecomb']),
        ('Ocircumflexdotbelow', '1ED8', ['O', 'circumflexcomb', 'dotbelowcomb']),
        ('Ohorn', '01A0', ['O', 'horncomb']),
        ('Ohornacute', '1EDA', ['O', 'horncomb', 'acutecomb']),
        ('Ohorngrave', '1EDC', ['O', 'horncomb', 'gravecomb']),
        ('Ohornhookabove', '1EDE', ['O', 'horncomb', 'hookabovecomb']),
        ('Ohorntilde', '1EE0', ['O', 'horncomb', 'tildecomb']),
        ('Ohorndotbelow', '1EE2', ['O', 'horncomb', 'dotbelowcomb']),
        # U
        ('Uacute', '00DA', ['U', 'acutecomb']),
        ('Ugrave', '00D9', ['U', 'gravecomb']),
        ('Uhookabove', '1EE6', ['U', 'hookabovecomb']),
        ('Utilde', '0168', ['U', 'tildecomb']),
        ('Udotbelow', '1EE4', ['U', 'dotbelowcomb']),
        ('Uhorn', '01AF', ['U', 'horncomb']),
        ('Uhornacute', '1EE8', ['U', 'horncomb', 'acutecomb']),
        ('Uhorngrave', '1EEA', ['U', 'horncomb', 'gravecomb']),
        ('Uhornhookabove', '1EEC', ['U', 'horncomb', 'hookabovecomb']),
        ('Uhorntilde', '1EEE', ['U', 'horncomb', 'tildecomb']),
        ('Uhorndotbelow', '1EF0', ['U', 'horncomb', 'dotbelowcomb']),
        # Y
        ('Yacute', '00DD', ['Y', 'acutecomb']),
        ('Ygrave', '1EF2', ['Y', 'gravecomb']),
        ('Yhookabove', '1EF6', ['Y', 'hookabovecomb']),
        ('Ytilde', '1EF8', ['Y', 'tildecomb']),
        ('Ydotbelow', '1EF4', ['Y', 'dotbelowcomb']),
    ]

    for name, uni, comps in vi_set:
        if name in font.glyphs:
            glyph = font.glyphs[name]
        else:
            glyph = GSGlyph(name)
            font.glyphs.append(glyph)
        
        glyph.unicode = uni
        
        for layer in glyph.layers:
            layer.components = []
            for c_name in comps:
                layer.components.append(GSComponent(c_name))
            
    font.save()

add_vi('sources/duyet-serif/DuyetSerif-Regular.glyphs')
add_vi('sources/duyet-serif/DuyetSerif-Italic.glyphs')
