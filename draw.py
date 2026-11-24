import os
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def wrap_text(draw, text, font, max_width):
    """Wrap text into lines using font.getlength() to ensure no clipping."""
    words = text.split()
    if not words:
        return []
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        if hasattr(font, "getlength"):
            w = font.getlength(test_line)
        else:
            w = draw.textlength(test_line, font=font)
        if w <= max_width or not current_line:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def draw_emblem(draw, x, y, w, h, kind):
    """Draw a refined flat bold pictorial emblem inside box (x, y, w, h)."""
    cx = x + w // 2
    cy = y + h // 2
    
    if kind == "cop31":
        # Cracked globe & sun rays
        r = min(w, h) // 3
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#1E3A8A", outline="#FFFFFF", width=3)
        # Sun rays / arc
        draw.arc([cx - r - 10, cy - r - 10, cx + r + 10, cy + r + 10], start=195, end=345, fill="#F59E0B", width=5)
        # Crack line with jagged segments
        draw.line([cx - r//2, cy - r, cx, cy - r//4], fill="#EF4444", width=4)
        draw.line([cx, cy - r//4, cx - r//4, cy + r//3], fill="#EF4444", width=4)
        draw.line([cx - r//4, cy + r//3, cx + r//3, cy + r], fill="#EF4444", width=4)
        
    elif kind == "indonesia":
        # Factory & vibrant flames
        fw, fh = int(w * 0.65), int(h * 0.55)
        fx, fy = cx - fw // 2, cy - fh // 2 + 12
        # Factory body
        draw.rectangle([fx, fy + 12, fx + fw, fy + fh], fill="#4B5563", outline="#1F2937", width=2)
        # Smokestacks
        draw.rectangle([fx + 12, fy - 18, fx + 28, fy + 12], fill="#6B7280")
        draw.rectangle([fx + fw - 36, fy - 30, fx + fw - 20, fy + 12], fill="#6B7280")
        # Flames (layered for depth)
        draw.polygon([fx + 10, fy - 18, fx + 2, fy - 40, fx + 22, fy - 28], fill="#DC2626")
        draw.polygon([fx + 14, fy - 22, fx + 10, fy - 48, fx + 26, fy - 32], fill="#F59E0B")
        draw.polygon([fx + fw - 32, fy - 30, fx + fw - 24, fy - 58, fx + fw - 12, fy - 36], fill="#DC2626")
        draw.polygon([fx + fw - 28, fy - 35, fx + fw - 20, fy - 65, fx + fw - 8, fy - 40], fill="#F59E0B")
        
    elif kind == "estonia":
        # Border barrier & prominent warning triangle
        bw = int(w * 0.65)
        bx = cx - bw // 2
        by = cy - 8
        # Barrier arm (striped red/white)
        draw.rectangle([bx, by, bx + bw, by + 14], fill="#DC2626", outline="#111827", width=2)
        draw.rectangle([bx + 12, by, bx + 36, by + 14], fill="#F9FAFB")
        draw.rectangle([bx + 60, by, bx + 84, by + 14], fill="#F9FAFB")
        # Warning triangle above
        tw = 46
        th = 40
        tx1, ty1 = cx, cy - 42
        tx2, ty2 = cx - tw//2, cy - 2
        tx3, ty3 = cx + tw//2, cy - 2
        draw.polygon([tx1, ty1, tx2, ty2, tx3, ty3], fill="#F59E0B", outline="#111827", width=2)
        draw.text((cx - 5, ty1 + 10), "!", fill="#111827", font=None)
        
    elif kind == "sparta":
        # Burning ship on waves with smoke
        sw, sh = int(w * 0.7), int(h * 0.38)
        sx, sy = cx - sw // 2, cy + 2
        # Hull
        draw.polygon([sx, sy, sx + sw, sy, sx + int(sw*0.82), sy + sh, sx + int(sw*0.18), sy + sh], fill="#1F2937")
        # Cabin superstructure
        draw.rectangle([cx - 20, sy - 14, cx + 20, sy], fill="#4B5563")
        # Fire & smoke
        draw.ellipse([cx - 18, sy - 30, cx + 18, sy - 10], fill="#DC2626")
        draw.ellipse([cx - 12, sy - 45, cx + 12, sy - 22], fill="#F59E0B")
        draw.ellipse([cx - 8, sy - 58, cx + 8, sy - 40], fill="#9CA3AF") # smoke
        # Waves
        draw.arc([cx - 35, sy + sh - 4, cx + 5, sy + sh + 16], start=0, end=180, fill="#2563EB", width=4)
        draw.arc([cx - 5, sy + sh - 4, cx + 35, sy + sh + 16], start=0, end=180, fill="#2563EB", width=4)
        
    elif kind == "nepal":
        # Mountains & help bridge/hands
        mw = int(w * 0.65)
        mx = cx - mw // 2
        my = cy + 12
        # Mountain peaks (multiple)
        draw.polygon([mx, my, mx + mw//3, my - 50, mx + int(mw*0.6), my], fill="#6B7280")
        draw.polygon([mx + int(mw*0.3), my, mx + int(mw*0.7), my - 60, mx + mw, my], fill="#4B5563")
        # Snow caps
        draw.polygon([mx + mw//3 - 12, my - 32, mx + mw//3, my - 50, mx + mw//3 + 12, my - 32], fill="#FFFFFF")
        draw.polygon([mx + int(mw*0.7) - 14, my - 38, mx + int(mw*0.7), my - 60, mx + int(mw*0.7) + 14, my - 38], fill="#FFFFFF")
        # Solid support line (aid pledge)
        draw.line([mx - 15, my + 8, mx + mw + 15, my + 8], fill="#059669", width=5)
        
    elif kind == "alcaraz":
        # Trophy & tennis ball
        tw, th = 34, 38
        tx, ty = cx - 28, cy - 16
        draw.rectangle([tx, ty, tx + tw, ty + th], fill="#F59E0B", outline="#B45309", width=2)
        # Handles
        draw.arc([tx - 12, ty, tx, ty + th//2], start=90, end=270, fill="#F59E0B", width=4)
        draw.arc([tx + tw, ty, tx + tw + 12, ty + th//2], start=270, end=90, fill="#F59E0B", width=4)
        # Stem & base
        draw.rectangle([cx - 4, ty + th, cx + 4, ty + th + 10], fill="#B45309")
        draw.rectangle([cx - 18, ty + th + 10, cx + 18, ty + th + 16], fill="#B45309")
        # Tennis ball
        bx, by, br = cx + 28, cy + 6, 15
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill="#84CC16", outline="#65A30D", width=2)
        draw.arc([bx - br, by - br, bx + br, by + br], start=35, end=145, fill="#FFFFFF", width=2)

def generate_poster():
    width, height = 1024, 1024
    image = Image.new("RGB", (width, height), "#F8FAFC") # Crisp light background
    draw = ImageDraw.Draw(image)
    
    try:
        font_date = ImageFont.truetype(FONT_PATH, 28)
        font_lead_head = ImageFont.truetype(FONT_PATH, 32)
        font_lead_cap = ImageFont.truetype(FONT_PATH, 20)
        font_grid_head = ImageFont.truetype(FONT_PATH, 20)
        font_grid_cap = ImageFont.truetype(FONT_PATH, 15)
    except Exception as e:
        print(f"Font loading error: {e}")
        font_date = ImageFont.load_default()
        font_lead_head = ImageFont.load_default()
        font_lead_cap = ImageFont.load_default()
        font_grid_head = ImageFont.load_default()
        font_grid_cap = ImageFont.load_default()

    # 1. Masthead Banner Across Top
    banner_h = 90
    draw.rectangle([0, 0, width, banner_h], fill="#0F172A") # Deep slate/navy
    draw.text((24, 16), "GLOBAL CHRONICLE • SPECIAL EDITION", fill="#94A3B8", font=font_grid_cap)
    date_text = "TUESDAY 24 NOVEMBER 2026"
    draw.text((24, 38), date_text, fill="#FFFFFF", font=font_date)
    
    # Red accent bar
    draw.rectangle([0, banner_h, width, banner_h + 4], fill="#EF4444")

    margin = 16
    y_cursor = banner_h + 16
    
    # 2. Lead Panel (COP31 Collapse)
    lead_h = 300
    lead_w = width - (2 * margin)
    lead_x = margin
    lead_y = y_cursor
    
    draw.rectangle([lead_x, lead_y, lead_x + lead_w, lead_y + lead_h], fill="#FFFFFF", outline="#CBD5E1", width=2)
    draw.rectangle([lead_x, lead_y, lead_x + lead_w, lead_y + 36], fill="#1E293B")
    draw.text((lead_x + 12, lead_y + 8), "TOP STORY • INTERNATIONAL CLIMATE DIPLOMACY", fill="#F1F5F9", font=font_grid_cap)
    
    emblem_w = 260
    draw_emblem(draw, lead_x + 16, lead_y + 52, emblem_w, lead_h - 68, "cop31")
    
    text_x = lead_x + emblem_w + 32
    text_w = lead_w - emblem_w - 48
    
    lead_headline = "COP31 CLIMATE SUMMIT COLLAPSES"
    lead_caption = "Antalya talks fail with no deal; UN chief deeply disappointed."
    
    head_lines = wrap_text(draw, lead_headline, font_lead_head, text_w)
    ty = lead_y + 54
    for line in head_lines:
        draw.text((text_x, ty), line, fill="#0F172A", font=font_lead_head)
        ty += 38
        
    ty += 12
    cap_lines = wrap_text(draw, lead_caption, font_lead_cap, text_w)
    for line in cap_lines:
        draw.text((text_x, ty), line, fill="#475569", font=font_lead_cap)
        ty += 26

    y_cursor += lead_h + 16

    # 3. Grid of Smaller Panels (5 panels total)
    grid_y1 = y_cursor
    grid_h1 = 260
    
    panels_row1 = [
        {"kind": "indonesia", "head": "INDONESIA CANDY FACTORY FIRE", "cap": "Banten blaze kills 24 people; thirty still missing."},
        {"kind": "estonia", "head": "RUSSIA WARNS ESTONIA", "cap": "Moscow cites border closure threat on verge of war."},
        {"kind": "sparta", "head": "SPARTA II HIT BY DRONES", "cap": "Russian cargo ship catches fire in Gulf of Finland."}
    ]
    
    num_cols1 = 3
    total_gaps1 = (num_cols1 + 1) * margin
    col_w1 = (width - total_gaps1) // num_cols1
    
    for i, p in enumerate(panels_row1):
        px = margin + i * (col_w1 + margin)
        py = grid_y1
        draw.rectangle([px, py, px + col_w1, py + grid_h1], fill="#FFFFFF", outline="#CBD5E1", width=2)
        draw_emblem(draw, px + 12, py + 12, col_w1 - 24, 90, p["kind"])
        
        tx = px + 12
        ty = py + 112
        tw = col_w1 - 24
        
        h_lines = wrap_text(draw, p["head"], font_grid_head, tw)
        for line in h_lines[:2]:
            draw.text((tx, ty), line, fill="#0F172A", font=font_grid_head)
            ty += 22
            
        ty += 6
        c_lines = wrap_text(draw, p["cap"], font_grid_cap, tw)
        for line in c_lines[:2]:
            draw.text((tx, ty), line, fill="#475569", font=font_grid_cap)
            ty += 18

    y_cursor += grid_h1 + 16
    
    # Row 2 (2 panels)
    grid_y2 = y_cursor
    grid_h2 = 260
    
    panels_row2 = [
        {"kind": "nepal", "head": "INDIA PLEDGES 1.6B FOR NEPAL", "cap": "Aid helps Nepal rebuild after severe devastating floods."},
        {"kind": "alcaraz", "head": "ALCARAZ WINS ATP FINALS", "cap": "Spaniard beats Alexander Zverev to claim first title."}
    ]
    
    num_cols2 = 2
    total_gaps2 = (num_cols2 + 1) * margin
    col_w2 = (width - total_gaps2) // num_cols2
    
    for i, p in enumerate(panels_row2):
        px = margin + i * (col_w2 + margin)
        py = grid_y2
        draw.rectangle([px, py, px + col_w2, py + grid_h2], fill="#FFFFFF", outline="#CBD5E1", width=2)
        draw_emblem(draw, px + 12, py + 12, col_w2 - 24, 90, p["kind"])
        
        tx = px + 12
        ty = py + 112
        tw = col_w2 - 24
        
        h_lines = wrap_text(draw, p["head"], font_grid_head, tw)
        for line in h_lines[:2]:
            draw.text((tx, ty), line, fill="#0F172A", font=font_grid_head)
            ty += 22
            
        ty += 6
        c_lines = wrap_text(draw, p["cap"], font_grid_cap, tw)
        for line in c_lines[:2]:
            draw.text((tx, ty), line, fill="#475569", font=font_grid_cap)
            ty += 18

    out_path = "entry.png"
    image.save(out_path, "PNG")
    print(f"Successfully generated {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    generate_poster()
