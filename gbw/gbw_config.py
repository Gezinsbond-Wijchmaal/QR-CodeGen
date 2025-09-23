import os
import PySimpleGUI as sg
from PIL import ImageFont, Image, ImageDraw
import qrcode

# Basisdir altijd relatief aan dit bestand
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Kleuren
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

green_rgb = (0, 152, 68)
green_hex = rgb_to_hex(green_rgb)

# ========== Thema ==========
def create_custom_theme():
    """Voegt het Gezinsbond-thema toe aan PySimpleGUI."""
    Gezinsbond = {
        'BACKGROUND': green_hex,
        'TEXT': 'white',
        'INPUT': 'black',
        'TEXT_INPUT': 'white',
        'SCROLL': green_hex,
        'BUTTON': ('white', green_hex),
        'PROGRESS': ('#01826B', '#D0D0D0'),
        'BORDER': 1,
        'SLIDER_DEPTH': 0,
        'PROGRESS_DEPTH': 0,
    }
    if 'Gezinsbond' not in sg.theme_list():  # dubbel toevoegen vermijden
        sg.theme_add_new('Gezinsbond', Gezinsbond)

# Activeer thema bij import
create_custom_theme()

# ========== Fonts ==========
def get_font_path(name="SourceSansPro-Bold.ttf"):
    """Geeft volledig pad naar een fontbestand (in /gbw/fonts)."""
    return os.path.join(BASE_DIR, "fonts", name)

def get_font(size=16, name="SourceSansPro-Bold.ttf"):
    """Laadt een truetype font op de juiste grootte."""
    return ImageFont.truetype(get_font_path(name), size)

# ========== Afbeeldingen ==========
def get_image(filename):
    """Geeft volledig pad naar een afbeelding in /gbw/pics."""
    return os.path.join(BASE_DIR, "pics", filename)

# ========== Sounds ==========
def get_sound(filename):
    """Geeft volledig pad naar een soundbestand in /gbw/sounds."""
    return os.path.join(BASE_DIR, "sounds", filename)

# ========== Utilities ==========
def add_corners(frame, rad):
    """Maakt hoeken afgerond op een afbeelding."""
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', frame.size, 255)
    w, h = frame.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    frame.putalpha(alpha)
    return frame

# ========== QR-code helper ==========
def generate_qr(data, version=10, box_size=10, border=1,
                fill_color="#009844", back_color="#ffffff"):
    """Genereert een QR code als PIL Image."""
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        version=version,
        border=border,
        box_size=box_size
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    return img
