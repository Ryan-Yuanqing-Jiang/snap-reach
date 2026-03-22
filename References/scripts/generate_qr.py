#!/usr/bin/env python3
"""
generate_qr.py — Designed QR code generator for outreach microsites.

Usage:
    python generate_qr.py "<url>" "<output_path.png>" [--title "Title"] [--prospect "Prospect Name"] [--seller "Seller Name"]
"""

import sys
import argparse
import subprocess

def ensure_deps():
    try:
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Installing qrcode[pil] and pillow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]", "pillow", "--break-system-packages", "-q"])

ensure_deps()
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image, ImageDraw, ImageFont

def get_font(size, force_bold=False):
    # Try common Mac fonts
    paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    for path in paths:
        try:
            index = 1 if force_bold and "Helvetica.ttc" in path else 0
            return ImageFont.truetype(path, size, index=index)
        except Exception:
            continue
    return ImageFont.load_default()

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        # Check width. ImageFont getbbox signature: (left, top, right, bottom)
        bbox = font.getbbox(" ".join(current_line))
        w = bbox[2] - bbox[0]
        if w > max_width and len(current_line) > 1:
            current_line.pop()
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def generate_qr(url: str, output_path: str, title: str, prospect: str, seller: str):
    # Base QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    try:
        qr_img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            back_color="white",
            fill_color=(13, 17, 32), # #0d1120
        ).convert("RGBA")
    except Exception:
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # Dimensions
    canvas_w = 800
    canvas_h = 2000
    bg_color = (13, 17, 32)
    text_color = (255, 255, 255)
    accent_color = (79, 110, 247)

    canvas = Image.new("RGBA", (canvas_w, canvas_h), bg_color)
    draw = ImageDraw.Draw(canvas)

    title_font = get_font(48, force_bold=True)
    subtitle_font = get_font(28)
    label_font = get_font(20, force_bold=True)

    curr_y = 100

    if title:
        title_lines = wrap_text(title, title_font, canvas_w - 100)
        for line in title_lines:
            bbox = draw.textbbox((0, 0), line, font=title_font)
            line_w = bbox[2] - bbox[0]
            draw.text(((canvas_w - line_w)/2, curr_y), line, font=title_font, fill=text_color)
            curr_y += (bbox[3] - bbox[1]) + 15
    
    curr_y += 50

    if prospect:
        line1 = "PREPARED FOR:"
        bbox1 = draw.textbbox((0,0), line1, font=label_font)
        w1 = bbox1[2] - bbox1[0]
        draw.text(((canvas_w - w1)/2, curr_y), line1, font=label_font, fill=accent_color)
        curr_y += 35

        bbox2 = draw.textbbox((0,0), prospect, font=subtitle_font)
        w2 = bbox2[2] - bbox2[0]
        draw.text(((canvas_w - w2)/2, curr_y), prospect, font=subtitle_font, fill=text_color)
        curr_y += 70

    qr_w, qr_h = qr_img.size
    qr_x = (canvas_w - qr_w) // 2
    
    # White rounded background
    padding = 20
    qr_bg_rect = [qr_x - padding, curr_y - padding, qr_x + qr_w + padding, curr_y + qr_h + padding]
    draw.rounded_rectangle(qr_bg_rect, radius=24, fill="white")
    canvas.paste(qr_img, (qr_x, curr_y), qr_img)
    curr_y += qr_h + 80

    if seller:
        line1 = "PREPARED BY:"
        bbox1 = draw.textbbox((0,0), line1, font=label_font)
        w1 = bbox1[2] - bbox1[0]
        draw.text(((canvas_w - w1)/2, curr_y), line1, font=label_font, fill=accent_color)
        curr_y += 35

        bbox2 = draw.textbbox((0,0), seller, font=subtitle_font)
        w2 = bbox2[2] - bbox2[0]
        draw.text(((canvas_w - w2)/2, curr_y), seller, font=subtitle_font, fill=(241,245,249))
        curr_y += (bbox2[3] - bbox2[1])

    # Crop to actual height used
    bottom_padding = 100
    canvas = canvas.crop((0, 0, canvas_w, curr_y + bottom_padding))

    canvas.save(output_path)
    print(f"Designed QR code saved: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Designed QR Code")
    parser.add_argument("url", help="URL to encode")
    parser.add_argument("output", help="Output file path")
    parser.add_argument("--title", default="Your message")
    parser.add_argument("--prospect", default="")
    parser.add_argument("--seller", default="")
    args = parser.parse_args()

    generate_qr(args.url, args.output, args.title, args.prospect, args.seller)
