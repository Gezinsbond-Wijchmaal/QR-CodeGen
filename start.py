import PySimpleGUI as start
import subprocess
from PIL import ImageFont

start.theme('Black')

# Voeg hier het pad naar uw lettertypebestand toe
font_path = 'fonts/SourceSansPro-Bold.ttf'
font_size = 16

# Controleer of het lettertype bestaat
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    start.popup_error('Lettertypebestand niet gevonden!', font=(font_path, font_size))
    raise SystemExit('Lettertypebestand niet gevonden!')

# Gebruik de font tuple in uw layout
layout = [
    [start.Text('Welkom bij de Gezinsbondtool', font=(font_path, font_size))],
    [start.Text("Deze tool is gemaakt voor de Gezinsbond.", font=(font_path, font_size))],
    [start.Text("Ben jij een bestuurslid/medewerker van Gezinsbond Wijchmaal?", font=(font_path, font_size))],
    [start.Radio('Ja', 'SR1', key='JA', font=(font_path, font_size)), start.Radio('Nee', 'SR1', default=True, key='NEE', font=(font_path, font_size))],
    [start.Button('Ok', font=(font_path, font_size)), start.Button('Sluiten', font=(font_path, font_size))]
]

window = start.Window('Gezinsbondtool', layout, grab_anywhere=True)

while True:
    try:
        event, values = window.read()
        if event == start.WIN_CLOSED or event == 'Sluiten':
            break

        if values['JA']:
            password = start.popup_get_text("Voer het wachtwoord in:", password_char='*', font=(font_path, font_size))
            if password == "GbW2023":
                start.popup("Geslaagd!", font=(font_path, font_size))
                try:
                    subprocess.run(["python", "gbwmenu.py"])
                except Exception as e:
                    start.popup(f"Er is een fout opgetreden bij het starten van gbwmenu.py: {e}", font=(font_path, font_size))
            else:
                start.popup("Verkeerd wachtwoord.", font=(font_path, font_size))
                try:
                    subprocess.run(["python", "qrgb.py"])
                except Exception as e:
                    start.popup(f"Er is een fout opgetreden bij het starten van qrgb.py: {e}", font=(font_path, font_size))

        if values['NEE']:
            start.popup("Je hebt geen toegang tot deze tool.", font=(font_path, font_size))
            break

    except Exception as e:
        start.popup(f"Een onverwachte fout is opgetreden: {e}", font=(font_path, font_size))

window.close()
