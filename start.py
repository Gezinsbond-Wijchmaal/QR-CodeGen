import PySimpleGUI as start, gbw, gb
import qrcode
import PIL
import os
from PIL import Image, ImageDraw, ImageFont
from tkinter import messagebox
import os.path

start.theme('Black')
layout =    [   [start.Text('Welkom bij de Gezinsbondtool')],
                [start.Text('Deze tool is gemaakt voor de Gezinsbond.')],
                [start.Text('Ben jij een bestuurslid/medewerker van Gezinsbond Wijchmaal?')],
                [start.Radio('Ja','SR1', key='JA'), start.Radio('Nee','SR1', default=True, key='NEE')],
                [start.Button('Ok'), start.Button('Sluiten')]
            ] 
window = start.Window('Gezinsbondtool', layout, no_titlebar=True, grab_anywhere=True)

while True:
    event, values = window.read()
    if event == start.WIN_CLOSED or event == 'Sluiten': # if user closes window or clicks cancel
        break
    
# Check voor 'Ja' keuze
    if values['JA']:
        # Popup voor wachtwoord
        password = start.popup_get_text('Voer het wachtwoord in:', password_char='*')
        
        if password == "GbW2023":
            start.popup('Geslaagd!')
            # Voeg hier de code toe om het 'Geslaagd' script te starten
            
            
        else:
            start.popup('Verkeerd wachtwoord.')
            # Voeg hier de code toe om het 'QR-gewoon' script te starten
    if values['NEE']:
        # Voeg hier de code toe om het 'QR-gewoon' script te starten
        start.popup('Je hebt geen toegang tot deze tool.')
        break

window.close()