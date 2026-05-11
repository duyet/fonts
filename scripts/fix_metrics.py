from fontTools.ttLib import TTFont

def fix_metrics(file_path):
    print(f"Fixing metrics for {file_path}")
    font = TTFont(file_path)
    hhea = font['hhea']
    # Set to 120% UPM (assuming 1000 UPM)
    hhea.ascender = 1200
    hhea.descender = -300
    hhea.lineGap = 0
    
    # OS/2 table
    os2 = font['OS/2']
    os2.usWinAscent = 1200
    os2.usWinDescent = 300
    os2.sTypoAscender = 1200
    os2.sTypoDescender = -300
    os2.sTypoLineGap = 0
    
    # Set vendor ID
    os2.achVendID = b'DYET'
    
    font.save(file_path)

fix_metrics('fonts/duyet-serif/ttf/DuyetSerif-Regular.ttf')
fix_metrics('fonts/duyet-serif/ttf/DuyetSerif-Italic.ttf')
