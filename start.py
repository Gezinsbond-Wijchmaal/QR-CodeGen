import PySimpleGUI as start
import subprocess

start.theme('Black')
layout =    [   [start.Text('Welkom bij de Gezinsbondtool')],
                [start.Text("Deze tool is gemaakt voor de Gezinsbond.")],
                [start.Text("Ben jij een bestuurslid/medewerker van Gezinsbond Wijchmaal?")],
                [start.Radio('Ja','SR1', key='JA'), start.Radio('Nee','SR1', default=True, key='NEE')],
                [start.Button('Ok'), start.Button('Sluiten')]
            ]
window = start.Window('Gezinsbondtool', layout, grab_anywhere=True)

while True:
    try:
        event, values = window.read()
        if event == start.WIN_CLOSED or event == 'Sluiten':
            break

        if values['JA']:
            password = start.popup_get_text("Voer het wachtwoord in:", password_char='*')
            if password == "GbW2023":
                start.popup("Geslaagd!")
                try:
                    subprocess.run(["python", "gbwmenu.py"])
                except Exception as e:
                    start.popup(f"Er is een fout opgetreden bij het starten van qrgbw.py: {e}")
            else:
                start.popup("Verkeerd wachtwoord.")
                try:
                    subprocess.run(["python", "qrgb.py"])
                except Exception as e:
                    start.popup(f"Er is een fout opgetreden bij het starten van qrgbw.py: {e}")

        if values['NEE']:
            try:
                subprocess.run(["python", "qrgb.py"])
            except Exception as e:
                start.popup("Je hebt geen toegang tot deze tool.")
            break

    except Exception as e:
        start.popup(f"Een onverwachte fout is opgetreden: {e}")

window.close()