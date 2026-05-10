def inject_mark(file_path, name, unicode_hex, nodes):
    print(f"Injecting {name} into {file_path}")
    with open(file_path, 'r') as f:
        content = f.read()

    if f"glyphname = {name};" in content:
        print(f"Glyph {name} already exists in {file_path}. Skipping.")
        return

    # Glyph template
    glyph_template = f"""{{
glyphname = {name};
unicode = {int(unicode_hex, 16)};
layers = (
{{
layerId = m01;
shapes = (
{{
closed = 1;
nodes = (
{nodes}
);
}}
);
}}
);
}},
"""
    # Find the beginning of the 'glyphs' array. 
    # Usually it looks like: glyphs = ( ... );
    # We'll insert it at the beginning of the list.
    content = content.replace("glyphs = (", f"glyphs = (\n{glyph_template}")

    with open(file_path, 'w') as f:
        f.write(content)

hook_nodes = """(140,669,ls), (121,669,o), (104,664,o), (88,653,cs), (72,642,o), (60,628,o), (51,609,cs), (51,609,ls), (59,616,o), (67,622,o), (76,626,cs), (85,630,o), (94,632,o), (104,632,cs), (117,632,o), (128,628,o), (137,621,cs), (146,613,o), (150,602,o), (150,589,cs), (150,575,o), (144,561,o), (132,547,cs), (120,532,o), (102,519,o), (77,506,cs), (78,506,ls), (121,518,o), (152,533,o), (173,551,cs), (193,569,o), (204,589,o), (204,610,cs), (204,628,o), (198,642,o), (185,653,cs), (173,664,o), (158,669,o), (140,669,cs)"""
dot_nodes = """(-29,-176,ls), (-20,-176,o), (-13,-174,o), (-6,-170,cs), (1,-166,o), (6,-161,o), (10,-154,cs), (14,-148,o), (16,-141,o), (16,-133,cs), (15,-122,o), (11,-112,o), (3,-104,cs), (-6,-95,o), (-16,-91,o), (-28,-91,cs), (-41,-91,o), (-51,-95,o), (-60,-104,cs), (-68,-112,o), (-73,-122,o), (-73,-133,cs), (-72,-145,o), (-68,-155,o), (-60,-163,cs), (-51,-171,o), (-41,-176,o), (-29,-176,cs)"""
horn_nodes = """(216,626,ls), (223,621,o), (229,613,o), (232,604,cs), (235,595,o), (237,583,o), (237,568,cs), (237,552,o), (232,535,o), (221,519,cs), (211,502,o), (195,487,o), (174,476,cs), (152,464,o), (124,458,o), (89,458,cs), (88,458,ls), (127,459,o), (160,461,o), (186,466,cs), (212,471,o), (232,477,o), (247,485,cs), (262,493,o), (273,501,o), (279,511,cs), (285,521,o), (289,531,o), (289,542,cs), (289,563,o), (281,580,o), (267,594,cs), (253,608,o), (236,619,o), (217,626,cs)"""

paths = ['sources/duyet-serif/DuyetSerif-Regular.glyphs', 'sources/duyet-serif/DuyetSerif-Italic.glyphs']
for p in paths:
    inject_mark(p, 'hookabovecomb', '0309', hook_nodes)
    inject_mark(p, 'dotbelowcomb', '0323', dot_nodes)
    inject_mark(p, 'horncomb', '031B', horn_nodes)

