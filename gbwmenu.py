import PySimpleGUI as sg
import subprocess
from PIL import ImageFont

# Functies voor het starten van je tools
def start_qr_generator():
    subprocess.run(["python", "qrgbw.py"])
    pass

def start_countdown_timer():
    subprocess.run(["python", "aftelklok.py"])
    # Voorbeeld: subprocess.run(["python", "countdown_timer.py"])
    pass

# RGB naar hexadecimaal
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
green_hex = rgb_to_hex((0, 152, 68))

# Lettertype en grootte
font_path = 'fonts/SourceSansPro-Bold.ttf'
font_size = 16

# Controleer of het lettertype bestaat
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    sg.popup_error('Lettertypebestand niet gevonden!', font=(font_path, font_size))
    raise SystemExit('Lettertypebestand niet gevonden!')

# Definieer het thema en de layout
sg.theme('Black')

# Aangepaste fontinstellingen voor knoppen
button_font = (font_path, font_size, 'bold')  # Verwijder de tekstkleur
button_text_color = green_hex  # Voeg de tekstkleur toe

button_layout = [
    [sg.Button('Start QR Code Generator', key='START_QR', button_color=('white', button_text_color), font=button_font),
     sg.Button('Start Countdown Timer', key='START_TIMER', button_color=('white', button_text_color), font=button_font)],
]

layout = [
    [sg.Text('Welkom bij de Gezinsbond Wijchmaal Tool Selecteerder', justification='center', font=('Helvetica', 16, 'bold'), text_color=button_text_color, pad=(0,10))],  # Verhoog de verticale padding
    [sg.Button('Start QR Code Generator', key='START_QR', button_color=('white', button_text_color), font=button_font),
     sg.Stretch(),
     sg.Button('Start Countdown Timer', key='START_TIMER', button_color=('white', button_text_color), font=button_font)],
    [sg.Stretch(), sg.Button('Sluiten', key='CLOSE', button_color=('white', button_text_color), font=button_font), sg.Stretch()]
]

# Maak het Window
window = sg.Window('Gezinsbond Wijchmaal Selecteerder', layout, size=(600, 200))

# Event Loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'START_QR':
        start_qr_generator()
    elif event == 'START_TIMER':
        start_countdown_timer()

window.close()
