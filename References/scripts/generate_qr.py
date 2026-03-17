#!/usr/bin/env python3
"""
generate_qr.py — QR code generator for outreach microsites.

Usage:
    python generate_qr.py "<url>" "<output_path.png>"

Example:
    python generate_qr.py "https://pinme.eth.limo/#/preview/abc123" "qr-acme.png"

Dependencies:
    pip install qrcode[pil] --break-system-packages
"""

import sys
import subprocess

def ensure_deps():
    try:
        import qrcode
        from PIL import Image
    except ImportError:
        print("Installing qrcode[pil]...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]", "--break-system-packages", "-q"])

def generate_qr(url: str, output_path: str):
    ensure_deps()
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    try:
        # Attempt styled render with rounded modules
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            back_color=(255, 255, 255),
            fill_color=(10, 10, 20),
        )
    except Exception:
        # Fallback to simple black-and-white
        img = qr.make_image(fill_color="black", back_color="white")

    img.save(output_path)
    print(f"QR code saved: {output_path}")
    print(f"URL encoded:   {url}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_qr.py <url> <output.png>")
        sys.exit(1)
    generate_qr(sys.argv[1], sys.argv[2])
