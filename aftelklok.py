import PySimpleGUI as sg
import time
import threading
from playsound import playsound
from PIL import Image

def show_countdown_window(hrs, mins, secs):
    # Afmetingen van de afbeelding bepalen
    img = Image.open('pics/GB_Transparant.png')
    img_width, img_height = img.size

    # Maak een graph element met dezelfde afmetingen als de afbeelding
    graph_layout = sg.Graph(
        canvas_size=(img_width, img_height),
        graph_bottom_left=(0, 0),
        graph_top_right=(img_width, img_height),
        key='-GRAPH-',
        background_color='black'
    )

    layout = [
        [graph_layout]
    ]

    window = sg.Window('Timer', layout, no_titlebar=True, keep_on_top=True, resizable=True, element_justification='center', background_color='black').Finalize()
    window.Maximize()

    # Voeg de afbeelding en tekst toe aan het graph element
    graph = window['-GRAPH-']
    graph.draw_image('pics/GB_Transparant.png', location=(0, img_height))
    text_location = (img_width // 2, img_height // 2)
    font = ('Helvetica', 300, 'bold')
    text_id = graph.draw_text(f'{hrs:02d}:{mins:02d}:{secs:02d}', text_location, font=font, color='#FFFFFF', text_location='center')

    return window, text_id

def countdown_timer(hrs, mins, secs, window, graph, text_id):
    total_seconds = hrs * 3600 + mins * 60 + secs
    img_width, img_height = graph.CanvasSize
    font = ('Helvetica', 300, 'bold')

    while total_seconds > 0:
        time.sleep(1)
        total_seconds -= 1
        hrs, mins = divmod(total_seconds, 3600)
        mins, secs = divmod(mins, 60)

        # Update de timer tekst
        graph.delete_figure(text_id)
        text_location = (img_width // 2, img_height // 2)
        text_id = graph.draw_text(f'{hrs:02d}:{mins:02d}:{secs:02d}', text_location, font=font, color='#FFFFFF', text_location='center')

    playsound('sounds/Horn.wav')
    window.close()


sg.theme('Black')

hours = [f'{i:02d}' for i in range(24)]
minutes = [f'{i:02d}' for i in range(60)]
seconds = [f'{i:02d}' for i in range(60)]

layout = [
    [sg.Text('Uren'), sg.Combo(hours, size=(5, 1), key='-HRS-'), sg.Text('Minuten'), sg.Combo(minutes, size=(5, 1), key='-MINS-'), sg.Text('Seconden'), sg.Combo(seconds, size=(5, 1), key='-SECS-')],
    [sg.Button('Starten'), sg.Button('Sluiten')]
]

# Creëer het hoofdvenster
window = sg.Window('Aftelklok', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sluiten':
        break
    if event == 'Starten':
        try:
            hrs = int(values['-HRS-'])
            mins = int(values['-MINS-'])
            secs = int(values['-SECS-'])
            # Toewijzen van returnwaarden van show_countdown_window
            countdown_window, text_id = show_countdown_window(hrs, mins, secs)
            graph = countdown_window['-GRAPH-'] # Haal het graph-element op
            threading.Thread(target=countdown_timer, args=(hrs, mins, secs, countdown_window, graph, text_id), daemon=True).start()
        except ValueError:
            sg.popup('Voer geldige getallen in voor uren, minuten en seconden.')



window.close()
