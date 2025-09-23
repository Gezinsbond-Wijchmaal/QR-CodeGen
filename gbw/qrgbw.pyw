import PySimpleGUI as gbw
from PIL import Image, ImageDraw
import os
from gbw_config import (
    green_hex,
    get_font,
    get_font_path,
    get_image,
    add_corners,
    generate_qr
)

# Definieer eigen thema
def create_custom_theme():
    Gezinsbond = {
        'BACKGROUND': 'black',
        'TEXT': green_hex,
        'INPUT': green_hex,
        'TEXT_INPUT': green_hex,
        'SCROLL': green_hex,
        'BUTTON': ('white', green_hex),
        'PROGRESS': ('#01826B', '#D0D0D0'),
        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
    }
    gbw.theme_add_new('MyCustomTheme', Gezinsbond)

create_custom_theme()
gbw.theme('Gezinsbond')

# Fonts
font_path = get_font_path("SourceSansPro-Bold.ttf")
font_size = 16

# Layout
layout = [
    [gbw.Text('Selecteer de map waar het moet opgeslagen worden', font=(font_path, font_size))],
    [gbw.In(key='Mapje'), gbw.FolderBrowse()],
    [gbw.Text('Vul hier de URL in', font=(font_path, font_size))],
    [gbw.InputText(key='URL')],
    [gbw.Text('Vul hier de naam van het bestand in (in 1 woord)', font=(font_path, font_size))],
    [gbw.InputText(key='Bestand')],
    [gbw.Text('Welke tekst wil je onder Gezinsbond hebben staan onder de QR-Code?', font=(font_path, font_size))],
    [gbw.InputText(key='Subtekst')],
    [gbw.Checkbox(key='geenpopup', text='Geen popup na aanmaken van het bestand', default=False, font=(font_path, font_size))],
    [gbw.Button('Ok', font=(font_path, font_size)), gbw.Button('Sluiten', font=(font_path, font_size))]
]

window = gbw.Window('QR code generator', layout, grab_anywhere=True)

# Event loop
while True:
    event, values = window.read()
    if event == gbw.WIN_CLOSED or event == 'Sluiten':
        break

    url = values['URL']
    word = values['Bestand']
    mapje = values['Mapje']
    subtext = values['Subtekst']
    filename = f"{word}.png"
    bestand = os.path.join(mapje, filename)

    # Achtergrondframe
    frame = Image.new(mode="RGB", size=(700, 900), color=(0, 152, 68))
    frame = add_corners(frame, 45)

    # Tekst "Gezinsbond" + subtekst
    draw = ImageDraw.Draw(frame)
    font_main = get_font(120)
    draw.text((32, 609), "Gezinsbond", font=font_main, fill=(255, 255, 255))

    font_sub = get_font(120)
    ratiox = draw.textlength(subtext, font=font_sub) / frame.size[0]
    if ratiox > 0.8:
        new_size = int(font_sub.size * 0.8 / ratiox)
        font_sub = get_font(new_size)

    text_ws = draw.textlength(subtext, font=font_sub)
    text_hs = font_sub.size
    text_xs = (frame.size[0] - text_ws) // 2
    text_ys = frame.size[1] - text_hs - 30
    draw.text((text_xs, text_ys), subtext, font=font_sub, fill=(255, 255, 255))

    # Logo "GB" + afdeling
    gbz = Image.open(get_image("GB.png"))
    afdeling = "Wijchmaal"
    drawtje = ImageDraw.Draw(gbz)
    font_afdeling = get_font(120)
    ratioj = drawtje.textlength(afdeling, font=font_afdeling) / gbz.size[0]
    if ratioj > 0.8:
        new_size = int(font_afdeling.size * 0.8 / ratioj)
        font_afdeling = get_font(new_size)
    text_w = drawtje.textlength(afdeling, font=font_afdeling)
    text_h = font_afdeling.size
    text_x = (gbz.size[0] - text_w) // 2
    text_y = gbz.size[1] - text_h - 10
    drawtje.text((text_x, text_y), afdeling, font=font_afdeling, fill=(0, 152, 68))

    # QR code genereren
    qrtje = generate_qr(url, version=10, border=1)
    posqr = ((qrtje.size[0] - gbz.size[0]) // 2, (qrtje.size[1] - gbz.size[1]) // 2)
    posimg = (54, 22)

    # QR + GB-logo + achtergrond combineren
    qrtje.paste(gbz, posqr)
    frame.paste(qrtje, posimg)
    frame.save(bestand)

    # Popup tonen indien gewenst
    if not values['geenpopup']:
        message = f"Het bestand {bestand} is aangemaakt.\n\nWil je ook nog de QR code zien?"
        antwoord = gbw.popup_yes_no(message, title="Gelukt", font=(font_path, font_size))
        if antwoord == 'Yes':
            frame.show()
    break

window.close()
