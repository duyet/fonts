from fontTools.ttLib import TTFont
from fontTools.pens.basePen import BasePen

def quad_to_cubic(p0, p1, p2):
    # p0 is current point (not passed here, but assumed)
    # Convert quadratic (p0, p1, p2) to cubic (p0, c1, c2, p2)
    c1 = (p0[0] + 2/3 * (p1[0] - p0[0]), p0[1] + 2/3 * (p1[1] - p0[1]))
    c2 = (p2[0] + 2/3 * (p1[0] - p2[0]), p2[1] + 2/3 * (p1[1] - p2[1]))
    return c1, c2, p2

class GlyphsCubicPen(BasePen):
    def __init__(self, glyphset, scale):
        BasePen.__init__(self, glyphset)
        self.nodes = []
        self.scale = scale
        self.curr_pt = (0, 0)

    def _moveTo(self, pt):
        self.nodes.append(f"({pt[0]*self.scale:.0f},{pt[1]*self.scale:.0f},ls)")
        self.curr_pt = pt

    def _lineTo(self, pt):
        self.nodes.append(f"({pt[0]*self.scale:.0f},{pt[1]*self.scale:.0f},ls)")
        self.curr_pt = pt

    def _curveToOne(self, pt1, pt2, pt3):
        self.nodes.append(f"({pt1[0]*self.scale:.0f},{pt1[1]*self.scale:.0f},o)")
        self.nodes.append(f"({pt2[0]*self.scale:.0f},{pt2[1]*self.scale:.0f},o)")
        self.nodes.append(f"({pt3[0]*self.scale:.0f},{pt3[1]*self.scale:.0f},cs)")
        self.curr_pt = pt3

    def _qCurveToOne(self, pt1, pt2):
        c1, c2, c3 = quad_to_cubic(self.curr_pt, pt1, pt2)
        self.nodes.append(f"({c1[0]*self.scale:.0f},{c1[1]*self.scale:.0f},o)")
        self.nodes.append(f"({c2[0]*self.scale:.0f},{c2[1]*self.scale:.0f},o)")
        self.nodes.append(f"({c3[0]*self.scale:.0f},{c3[1]*self.scale:.0f},cs)")
        self.curr_pt = pt2

    def _closePath(self):
        pass

def extract_glyph(font_path, glyph_name, target_scale):
    font = TTFont(font_path)
    glyphset = font.getGlyphSet()
    if glyph_name not in glyphset:
        return None
    
    pen = GlyphsCubicPen(glyphset, target_scale)
    glyphset[glyph_name].draw(pen)
    return pen.nodes

source_font = "/System/Library/Fonts/NewYorkItalic.ttf"
scale = 1000 / 2048

glyphs_to_extract = {
    "hookabovecomb": "hookabovecmb",
    "dotbelowcomb": "dotbelowcmb",
    "horncomb": "horncmb"
}

for name, source_name in glyphs_to_extract.items():
    print(f"--- {name} ---")
    nodes = extract_glyph(source_font, source_name, scale)
    if nodes:
        for node in nodes:
            print(f"  {node},")
