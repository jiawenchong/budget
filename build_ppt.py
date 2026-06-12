# -*- coding: utf-8 -*-
"""產生「進出水平衡計算對照系統」一頁式專案進度報告（單張投影片）。"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

NAVY  = RGBColor(0x0F, 0x2A, 0x4A)
BLUE  = RGBColor(0x1F, 0x6F, 0xB2)
TEAL  = RGBColor(0x12, 0x9A, 0x9A)
LIGHT = RGBColor(0xEE, 0xF3, 0xF8)
GREY  = RGBColor(0x44, 0x4F, 0x5B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GOLD  = RGBColor(0xE0, 0x9F, 0x2A)
RUST  = RGBColor(0xC0, 0x53, 0x2B)
FONT  = "Microsoft JhengHei"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
s = prs.slides.add_slide(prs.slide_layouts[6])


def rect(x, y, w, h, color, line=None):
    sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = color
    if line: sp.line.color.rgb = line; sp.line.width = Pt(1)
    else: sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def txt(x, y, w, h, lines, size=14, color=GREY, bold=False,
        align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space=3):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_top = 0; tf.margin_bottom = 0
    if isinstance(lines, str): lines = [(lines, size, color, bold)]
    for i, (t, sz, c, b) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space); p.space_before = Pt(0)
        r = p.add_run(); r.text = t
        r.font.size = Pt(sz); r.font.bold = b; r.font.color.rgb = c; r.font.name = FONT
    return tb


def panel(x, y, w, h, title, tcolor):
    rect(x, y, w, h, LIGHT)
    rect(x, y, w, Inches(0.42), tcolor)
    txt(x + Inches(0.18), y, w - Inches(0.3), Inches(0.42), title, 14, WHITE, True,
        anchor=MSO_ANCHOR.MIDDLE)


# ===== 標題列 =====
rect(0, 0, SW, Inches(1.0), NAVY)
rect(0, Inches(1.0), SW, Pt(4), TEAL)
rect(0, 0, Inches(0.22), Inches(1.0), TEAL)
txt(Inches(0.5), Inches(0.12), Inches(9.5), Inches(0.8),
    [("進出水平衡計算對照系統 ‧ 專案進度報告", 25, WHITE, True),
     ("精確計算蒸發量 ‧ Agent 自動化平衡計算與申報整理", 13, RGBColor(0xC4,0xD2,0xE2), False)],
    space=2, anchor=MSO_ANCHOR.MIDDLE)
txt(Inches(9.9), Inches(0.12), Inches(3.0), Inches(0.8),
    [("預計上線：2026 / 10", 14, GOLD, True),
     ("報告日期：2026 / 06　進度約 25%", 11, RGBColor(0xC4,0xD2,0xE2), False)],
    space=2, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

# ===== 左上：專案目的 =====
M = Inches(0.45)
panel(M, Inches(1.25), Inches(6.05), Inches(1.95), "專案目的", BLUE)
txt(M + Inches(0.2), Inches(1.78), Inches(5.7), Inches(1.4),
    [("‧ 水平衡計算：彙整進／出水資料，建立可稽核的進出水對照基準。", 12.5, GREY, False),
     ("‧ 蒸發量推算：以平衡差值精確反推蒸發量，取代人工估算。", 12.5, GREY, False),
     ("‧ Agent 自動化：代理執行平衡計算並整理後續申報所需資料。", 12.5, GREY, False)],
    space=6)

# ===== 右上：專案效益 =====
panel(Inches(6.85), Inches(1.25), Inches(6.05), Inches(1.95), "專案效益", TEAL)
bx = Inches(6.85); by = Inches(1.78); bw = Inches(2.9); bh = Inches(0.6)
bens = [("自動化", "減少人工試算與資料搬運", TEAL),
        ("準確性", "統一邏輯、結果可重現可稽核", BLUE),
        ("效率提升", "申報資料自動彙整成型", GOLD),
        ("可追溯／合規", "保留計算過程滿足申報佐證", NAVY)]
for i, (h, d, c) in enumerate(bens):
    r, col = divmod(i, 2)
    x = bx + Inches(0.18) + col * (bw + Inches(0.05))
    y = by + r * (bh + Inches(0.12))
    rect(x, y, Inches(0.1), bh, c)
    txt(x + Inches(0.2), y, bw - Inches(0.2), bh,
        [(h, 13, NAVY, True), (d, 10.5, GREY, False)], space=1,
        anchor=MSO_ANCHOR.MIDDLE)

# ===== 中段：當前進度 =====
panel(M, Inches(3.4), Inches(12.45), Inches(1.35), "當前進度", NAVY)
rect(M + Inches(0.2), Inches(3.95), Inches(6.0), Inches(0.22), RGBColor(0xDD,0xE5,0xEE))
rect(M + Inches(0.2), Inches(3.95), Inches(1.5), Inches(0.22), TEAL)
txt(M + Inches(6.35), Inches(3.9), Inches(1.2), Inches(0.32), "約 25%", 12, TEAL, True,
    anchor=MSO_ANCHOR.MIDDLE)
txt(M + Inches(0.2), Inches(4.28), Inches(12.0), Inches(0.5),
    [("‧ AS-IS / TO-BE 流程圖整理（進行中）　　‧ 過往相關資料盤點與蒐集（進行中）", 12.5, GREY, False),
     ("‧ 近期重點：凍結第一版需求範圍、確認申報欄位與 Agent 計算邏輯規格", 12.5, GREY, False)],
    space=4)

# ===== 下段：時間軸 Timeline =====
panel(M, Inches(4.95), Inches(12.45), Inches(2.35), "專案時間軸 Timeline（6 月 → 10 月上線）", GOLD)
phases = [("6 月", "現況盤點", "流程圖整理／資料蒐集", TEAL, "需求凍結"),
          ("7 月", "需求與設計", "計算邏輯／Agent 設計", BLUE, "設計定案"),
          ("8 月", "系統開發", "計算引擎／Agent 開發", NAVY, "開發完成"),
          ("9 月", "測試驗證", "整合測試／資料對帳／UAT", GOLD, "UAT 通過"),
          ("10 月", "正式上線", "部署／申報產出／訓練", RUST, "正式上線")]
x0 = M + Inches(0.25); span = Inches(11.95); n = len(phases)
col_w = Emu(int(span)//n); line_y = Inches(5.75)
rect(x0, line_y, span, Pt(3), BLUE)
for i, (m, name, det, c, ms) in enumerate(phases):
    cx = Emu(int(x0) + i*int(col_w))
    midx = Emu(int(cx) + int(col_w)//2 - int(Inches(0.12)))
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, midx, Emu(int(line_y)-int(Inches(0.09))),
                             Inches(0.26), Inches(0.26))
    dot.fill.solid(); dot.fill.fore_color.rgb = c
    dot.line.color.rgb = WHITE; dot.line.width = Pt(1.5); dot.shadow.inherit = False
    txt(cx, Inches(5.42), col_w, Inches(0.3), m, 13, c, True, align=PP_ALIGN.CENTER)
    cardx = Emu(int(cx)+int(Inches(0.08))); cardw = Emu(int(col_w)-int(Inches(0.16)))
    rect(cardx, Inches(6.12), cardw, Inches(1.05), WHITE, line=RGBColor(0xD5,0xDE,0xE8))
    rect(cardx, Inches(6.12), cardw, Pt(4), c)
    txt(cardx, Inches(6.2), cardw, Inches(0.6),
        [(name, 11.5, NAVY, True), (det, 9, GREY, False)], space=2,
        align=PP_ALIGN.CENTER)
    txt(cardx, Inches(6.86), cardw, Inches(0.28), "◆ " + ms, 9, c, True,
        align=PP_ALIGN.CENTER)

# ===== 頁尾：下一步 =====
txt(M, Inches(7.2), Inches(12.45), Inches(0.28),
    "下一步：確認 TO-BE 流程並凍結需求 ▶ 定義計算公式與 Agent 規格 ▶ 完成歷史資料盤點（需相關單位協助提供資料來源與申報欄位）",
    10.5, NAVY, True, align=PP_ALIGN.CENTER)

prs.save("進出水平衡計算對照系統_專案進度報告.pptx")
print("OK saved", len(prs.slides.__iter__.__self__._sldIdLst), "slide(s)")
