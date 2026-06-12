# -*- coding: utf-8 -*-
"""產生「進出水平衡計算對照系統」專案進度報告簡報。"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---- 色彩主題 ----
NAVY   = RGBColor(0x0F, 0x2A, 0x4A)   # 主色（深藍）
BLUE   = RGBColor(0x1F, 0x6F, 0xB2)   # 輔色（藍）
TEAL   = RGBColor(0x12, 0x9A, 0x9A)   # 強調（青）
LIGHT  = RGBColor(0xEE, 0xF3, 0xF8)   # 淺底
GREY   = RGBColor(0x55, 0x5F, 0x6B)   # 內文灰
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GOLD   = RGBColor(0xE0, 0x9F, 0x2A)
FONT   = "Microsoft JhengHei"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def slide():
    return prs.slides.add_slide(BLANK)


def rect(s, x, y, w, h, color, line=False):
    from pptx.enum.shapes import MSO_SHAPE
    sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = color
    if line:
        sp.line.color.rgb = color
    else:
        sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def txt(s, x, y, w, h, lines, size=18, color=GREY, bold=False,
        align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font=FONT, space=6):
    """lines: str 或 list[(text, size, color, bold)]"""
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    if isinstance(lines, str):
        lines = [(lines, size, color, bold)]
    for i, item in enumerate(lines):
        t, sz, c, b = item
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space)
        r = p.add_run(); r.text = t
        r.font.size = Pt(sz); r.font.bold = b
        r.font.color.rgb = c; r.font.name = font
    return tb


def header(s, title, idx):
    """內頁標題列。"""
    rect(s, 0, 0, SW, Inches(1.15), NAVY)
    rect(s, 0, Inches(1.15), SW, Pt(4), TEAL)
    txt(s, Inches(0.6), Inches(0.18), Inches(11), Inches(0.8),
        title, size=28, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(12.0), Inches(0.18), Inches(0.9), Inches(0.8),
        f"0{idx}", size=30, color=TEAL, bold=True,
        align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)


def card(s, x, y, w, h, head, body, accent=BLUE):
    rect(s, x, y, w, h, LIGHT)
    rect(s, x, y, Pt(6), h, accent)
    txt(s, x + Inches(0.25), y + Inches(0.15), w - Inches(0.4), Inches(0.5),
        head, size=18, color=NAVY, bold=True)
    txt(s, x + Inches(0.25), y + Inches(0.72), w - Inches(0.4), h - Inches(0.8),
        body, size=14, color=GREY)


# ===================== 1. 封面 =====================
s = slide()
rect(s, 0, 0, SW, SH, NAVY)
rect(s, 0, Inches(4.55), SW, Pt(5), TEAL)
rect(s, Inches(0.0), Inches(0.0), Inches(0.28), SH, TEAL)
txt(s, Inches(0.9), Inches(1.55), Inches(11.5), Inches(0.5),
    "專案進度報告", size=22, color=TEAL, bold=True)
txt(s, Inches(0.9), Inches(2.15), Inches(11.8), Inches(2.0),
    [("進出水平衡計算對照系統", 46, WHITE, True),
     ("Water In/Out Balance Reconciliation System", 20, RGBColor(0xB9,0xC9,0xDA), False)],
    space=14)
txt(s, Inches(0.9), Inches(4.85), Inches(11.5), Inches(1.2),
    [("精確計算蒸發量 ‧ Agent 自動化平衡計算 ‧ 申報資料智慧整理", 18,
      RGBColor(0xCF,0xDB,0xE8), False)])
txt(s, Inches(0.9), Inches(6.45), Inches(7), Inches(0.5),
    "報告日期：2026 年 6 月　|　預計上線：2026 年 10 月", 14,
    RGBColor(0x9F,0xB3,0xC8))

# ===================== 2. 專案目的與說明 =====================
s = slide(); header(s, "專案目的與說明", 2)
txt(s, Inches(0.6), Inches(1.45), Inches(12), Inches(0.6),
    "建立可稽核、可重複、可申報的進出水平衡計算機制，以系統取代人工試算。",
    18, NAVY, True)
cy, cw, ch, gap = Inches(2.25), Inches(3.95), Inches(2.0), Inches(0.25)
card(s, Inches(0.6), cy, cw, ch, "① 水平衡計算",
     "彙整進水、出水與各項用水資料，建立進出水對照基準，確保水量帳務一致且可追溯。", BLUE)
card(s, Inches(0.6)+cw+gap, cy, cw, ch, "② 蒸發量精確計算",
     "以平衡差值反推蒸發量，取代估算，提升環境數據與用水效率分析的準確度。", TEAL)
card(s, Inches(0.6)+2*(cw+gap), cy, cw, ch, "③ Agent 自動化申報",
     "由 Agent 代理執行平衡計算並自動整理後續申報所需資料，降低人工彙整負擔。", GOLD)
rect(s, Inches(0.6), Inches(4.75), Inches(12.1), Inches(1.85), LIGHT)
txt(s, Inches(0.85), Inches(4.92), Inches(11.7), Inches(0.5),
    "為何重要", 16, NAVY, True)
txt(s, Inches(0.85), Inches(5.42), Inches(11.7), Inches(1.1),
    [("‧ 法規申報要求水量數據可佐證、可追溯，人工試算易出錯且難以稽核。", 14, GREY, False),
     ("‧ 蒸發量無法直接量測，需透過進出水平衡推算，計算邏輯一致性至關重要。", 14, GREY, False),
     ("‧ 透過系統與 Agent 標準化流程，建立單一可信數據來源（Single Source of Truth）。", 14, GREY, False)],
    space=5)

# ===================== 3. 專案效益 =====================
s = slide(); header(s, "專案效益", 3)
benefits = [
    ("自動化", "Agent 代理執行平衡計算，減少反覆人工試算與資料搬運，釋放人力投入分析。", TEAL),
    ("準確性", "統一計算邏輯與資料來源，降低人為誤差，蒸發量推算結果可重現、可稽核。", BLUE),
    ("效率提升", "申報資料自動彙整成型，縮短報表與申報前置作業時間。", GOLD),
    ("可追溯／合規", "完整保留計算過程與來源資料，滿足申報佐證與內部稽核需求。", NAVY),
]
bx, bw, bh, bgap = Inches(0.6), Inches(5.95), Inches(2.15), Inches(0.3)
for i, (h, b, c) in enumerate(benefits):
    r, col = divmod(i, 2)
    x = bx + col * (bw + bgap)
    y = Inches(1.55) + r * (bh + bgap)
    rect(s, x, y, bw, bh, LIGHT)
    rect(s, x, y, bw, Inches(0.62), c)
    txt(s, x + Inches(0.3), y + Inches(0.06), bw - Inches(0.5), Inches(0.5),
        h, 20, WHITE, True, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x + Inches(0.3), y + Inches(0.78), bw - Inches(0.6), bh - Inches(0.9),
        b, 15, GREY)

# ===================== 4. 當前進度 =====================
s = slide(); header(s, "當前進度", 4)
txt(s, Inches(0.6), Inches(1.4), Inches(12), Inches(0.5),
    "整體進度：需求釐清與現況盤點階段（約 25%）", 18, NAVY, True)
# 進度條
rect(s, Inches(0.6), Inches(2.05), Inches(12.1), Inches(0.32), RGBColor(0xDD,0xE5,0xEE))
rect(s, Inches(0.6), Inches(2.05), Inches(3.0), Inches(0.32), TEAL)
card(s, Inches(0.6), Inches(2.75), Inches(5.95), Inches(2.0),
     "① AS-IS / TO-BE 流程圖整理（進行中）",
     "盤點現況（AS-IS）人工計算與申報流程，並繪製目標（TO-BE）導入 Agent 後之自動化流程，"
     "界定系統範圍與差異缺口。", TEAL)
card(s, Inches(6.85), Inches(2.75), Inches(5.85), Inches(2.0),
     "② 過往資料盤點與蒐集（進行中）",
     "彙整歷史進出水量、用水紀錄與既有申報報表，確認資料來源、欄位格式與品質，"
     "作為計算邏輯與驗證之基礎。", BLUE)
rect(s, Inches(0.6), Inches(5.0), Inches(12.1), Inches(1.55), LIGHT)
txt(s, Inches(0.85), Inches(5.15), Inches(11.6), Inches(0.5),
    "近期重點 / 待辦", 16, NAVY, True)
txt(s, Inches(0.85), Inches(5.62), Inches(11.6), Inches(0.9),
    [("‧ 完成 TO-BE 流程確認，凍結第一版需求範圍。", 14, GREY, False),
     ("‧ 確認申報所需欄位與計算公式，定義 Agent 計算邏輯規格。", 14, GREY, False)],
    space=4)

# ===================== 5. 專案時間軸 Timeline =====================
s = slide(); header(s, "專案時間軸 Timeline", 5)
txt(s, Inches(0.6), Inches(1.35), Inches(12), Inches(0.5),
    "自 6 月現況盤點起，反向推導至 10 月正式上線", 16, GREY, False)
phases = [
    ("6 月", "現況盤點", ["AS-IS/TO-BE 流程圖", "歷史資料蒐集", "需求範圍界定"], TEAL),
    ("7 月", "需求與設計", ["計算邏輯規格", "Agent 流程設計", "資料模型/介面"], BLUE),
    ("8 月", "系統開發", ["平衡計算引擎", "Agent 代理開發", "申報整理模組"], NAVY),
    ("9 月", "測試與驗證", ["整合測試", "歷史資料對帳驗證", "UAT 使用者驗收"], GOLD),
    ("10 月", "正式上線", ["上線部署", "申報資料產出", "教育訓練/交付"], RGBColor(0xC0,0x53,0x2B)),
]
n = len(phases); x0 = Inches(0.6); span = Inches(12.1)
col_w = Emu(int(span) // n)
line_y = Inches(2.55)
rect(s, x0, line_y, span, Pt(4), BLUE)
for i, (m, name, items, c) in enumerate(phases):
    cx = Emu(int(x0) + i * int(col_w))
    midx = Emu(int(cx) + int(col_w)//2 - int(Inches(0.16)))
    # 節點
    from pptx.enum.shapes import MSO_SHAPE
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, midx, Emu(int(line_y)-int(Inches(0.12))),
                             Inches(0.32), Inches(0.32))
    dot.fill.solid(); dot.fill.fore_color.rgb = c; dot.line.color.rgb = WHITE
    dot.line.width = Pt(2); dot.shadow.inherit = False
    # 月份標籤
    txt(s, cx, Inches(1.95), col_w, Inches(0.45), m, 17, c, True,
        align=PP_ALIGN.CENTER)
    # 卡片
    cardx = Emu(int(cx) + int(Inches(0.1)))
    cardw = Emu(int(col_w) - int(Inches(0.2)))
    rect(s, cardx, Inches(3.05), cardw, Inches(3.2), LIGHT)
    rect(s, cardx, Inches(3.05), cardw, Inches(0.55), c)
    txt(s, cardx, Inches(3.08), cardw, Inches(0.5), name, 15, WHITE, True,
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Emu(int(cardx)+int(Inches(0.18))), Inches(3.75),
        Emu(int(cardw)-int(Inches(0.3))), Inches(2.4),
        [("‧ " + it, 12, GREY, False) for it in items], space=6)
txt(s, Inches(0.6), Inches(6.55), Inches(12.1), Inches(0.6),
    "關鍵里程碑：6/底 需求凍結　▶　7/底 設計定案　▶　8/底 開發完成　▶　9/底 UAT 通過　▶　10 月 正式上線",
    13, NAVY, True, align=PP_ALIGN.CENTER)

# ===================== 6. 結語 / 下一步 =====================
s = slide(); header(s, "結語 / 下一步計畫", 6)
txt(s, Inches(0.6), Inches(1.5), Inches(12), Inches(1.0),
    [("以系統化、可稽核的進出水平衡機制，精準推算蒸發量，", 20, NAVY, True),
     ("並由 Agent 自動產出申報資料，朝 10 月上線目標穩步推進。", 20, NAVY, True)],
    space=6)
nexts = [
    ("即將完成", "確認 TO-BE 流程並凍結第一版需求範圍。"),
    ("近期啟動", "定義平衡計算公式與 Agent 計算邏輯規格。"),
    ("資料準備", "完成歷史資料盤點，作為計算驗證基準。"),
    ("需要協助", "請相關單位協助提供資料來源與申報欄位確認。"),
]
ny = Inches(3.0)
for i, (h, b) in enumerate(nexts):
    y = ny + i * Inches(0.92)
    rect(s, Inches(0.6), y, Inches(2.3), Inches(0.74), BLUE)
    txt(s, Inches(0.6), y, Inches(2.3), Inches(0.74), h, 15, WHITE, True,
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    rect(s, Inches(2.95), y, Inches(9.75), Inches(0.74), LIGHT)
    txt(s, Inches(3.2), y, Inches(9.4), Inches(0.74), b, 15, GREY,
        anchor=MSO_ANCHOR.MIDDLE)

prs.save("進出水平衡計算對照系統_專案進度報告.pptx")
print("OK saved")
