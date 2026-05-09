from fontTools.ttLib import TTFont

fonts = [
    "/System/Library/Fonts/NewYorkItalic.ttf",
    "/System/Library/Fonts/Supplemental/Baskerville.ttc",
    "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
]

glyphs_to_check = {
    "hookabovecomb": 0x0309,
    "dotbelowcomb": 0x0323,
    "horncomb": 0x031B
}

for font_path in fonts:
    print(f"\nChecking {font_path}...")
    try:
        if font_path.endswith(".ttc"):
            from fontTools.ttLib import TTCollection
            collection = TTCollection(font_path)
            font = collection[0]
        else:
            font = TTFont(font_path)
        
        cmap = font.getBestCmap()
        for name, unicode_val in glyphs_to_check.items():
            if unicode_val in cmap:
                print(f"  {name} (U+{unicode_val:04X}) found as {cmap[unicode_val]}")
            else:
                print(f"  {name} (U+{unicode_val:04X}) NOT found")
    except Exception as e:
        print(f"  Error: {e}")
