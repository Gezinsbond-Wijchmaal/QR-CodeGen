import PySimpleGUI as sg
import time
import threading
from PIL import Image, ImageFont
import pygame  # Voor geluidsbeheer

# Geluidssysteem initialiseren
pygame.mixer.init()

# RGB naar hexadecimaal
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

green_hex = rgb_to_hex((0, 152, 68))

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
    sg.theme_add_new('MyCustomTheme', Gezinsbond)

# Creëer en gebruik aangepast thema
create_custom_theme()
sg.theme('Gezinsbond')

# Lettertype en grootte
font_path = 'fonts/sspb.ttf'
font_size = 16

# Controleer of het lettertype bestaat
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    sg.popup_error('Lettertypebestand niet gevonden!', font=(font_path, font_size))
    raise SystemExit('Lettertypebestand niet gevonden!')

# Aanpassingen voor timer tekst font
timer_font_large = (font_path, 300, 'bold')
timer_font_small = (font_path, 20, 'bold')

def update_timer_text(graph, text_id, text, location, font, color='#FF0000'):
    """Update tekst in de graph."""
    graph.delete_figure(text_id)
    return graph.draw_text(text, location, font=font, color=color, text_location='center')

def show_timer_window(hrs, mins, secs):
    # Open afbeelding en bepaal afmetingen
    img = Image.open('pics/GB_Transparant.png')
    img_width, img_height = img.size

    # Maak een graph element met dezelfde afmetingen als de afbeelding
    graph_layout = sg.Graph(
        canvas_size=(img_width, img_height),
        graph_bottom_left=(0, 0),
        graph_top_right=(img_width, img_height),
        key='-GRAPH-',
        background_color='black',
        enable_events=True  # Klikbare events inschakelen
    )

    layout = [
        [graph_layout]
    ]

    window = sg.Window('Timer', layout, no_titlebar=True, keep_on_top=True, resizable=True, element_justification='center', background_color='black').Finalize()
    window.Maximize()

    # Voeg de afbeelding toe aan de graph
    graph = window['-GRAPH-']
    graph.draw_image('pics/GB_Transparant.png', location=(0, img_height))

    # Locaties voor grote en kleine klokken
    large_clock_location = (img_width // 2, img_height // 2)
    small_clock_location = (img_width - 150, 50)

    # Voeg eerste teksten toe
    large_text_id = graph.draw_text("00:00:00", large_clock_location, font=timer_font_large, color='#FF0000', text_location='center')
    small_text_id = graph.draw_text(f'{hrs:02d}:{mins:02d}:{secs:02d}', small_clock_location, font=timer_font_small, color='#777777', text_location='center')

    return window, graph, large_text_id, small_text_id, img_width, img_height, large_clock_location, small_clock_location

def start_timer(graph, large_text_id, large_clock_location, stop_event, countdown_finished_event):
    elapsed_seconds = 0
    # Kleurenlijst voor de optelklok
    colors = ['#FFFFFF', '#FF0000', '#0000FF', '#00FFFF', '#FFFF00', '#FF9900', '#0099FF', '#00FF99']
    color_index = 0  # Start met de eerste kleur

    while not stop_event.is_set():
        if countdown_finished_event.is_set():
            break  # Stop als de countdown klaar is

        hrs_elapsed, mins_elapsed = divmod(elapsed_seconds, 3600)
        mins_elapsed, secs_elapsed = divmod(mins_elapsed, 60)

        # Verander kleur elke 10 seconden
        if elapsed_seconds % 10 == 0:
            color_index = (color_index + 1) % len(colors)  # Ga naar de volgende kleur
        current_color = colors[color_index]

        # Update de grote optelklok
        text = f'{hrs_elapsed:02d}:{mins_elapsed:02d}:{secs_elapsed:02d}'
        large_text_id = update_timer_text(graph, large_text_id, text, large_clock_location, font=timer_font_large, color=current_color)
        
        elapsed_seconds += 1
        time.sleep(1)

def countdown_timer(hrs, mins, secs, graph, small_text_id, small_clock_location, stop_event, countdown_finished_event):
    total_seconds = hrs * 3600 + mins * 60 + secs
    last_displayed_time = None  # Houd de laatste tijd bij die weergegeven werd

    while total_seconds > 0 and not stop_event.is_set():
        time.sleep(1)
        total_seconds -= 1
        hrs, mins = divmod(total_seconds, 3600)
        mins, secs = divmod(mins, 60)

        # Update de kleine aftelklok enkel als de tijd verandert
        current_time = f'{hrs:02d}:{mins:02d}:{secs:02d}'
        if current_time != last_displayed_time:
            small_text_id = update_timer_text(graph, small_text_id, current_time, small_clock_location, font=timer_font_small, color='#777777')
            last_displayed_time = current_time  # Update de laatste weergegeven tijd

    if not stop_event.is_set():  # Speel geluid alleen af als de klok niet is gestopt
        countdown_finished_event.set()
        pygame.mixer.music.load('sounds/horn.wav')
        pygame.mixer.music.play(-1)  # Herhaal het geluid totdat je het stopt

sg.theme('Black')

hours = [f'{i:02d}' for i in range(24)]
minutes = [f'{i:02d}' for i in range(60)]
seconds = [f'{i:02d}' for i in range(60)]

uur_kolom = [
    [sg.Text('Uren', font=(font_path, font_size), justification='center')],
    [sg.Combo(hours, size=(15, 1), key='-HRS-', font=(font_path, font_size))]
]

minuut_kolom = [
    [sg.Text('Minuten', font=(font_path, font_size), justification='center')],
    [sg.Combo(minutes, size=(15, 1), key='-MINS-', font=(font_path, font_size))]
]

seconde_kolom = [
    [sg.Text('Seconden', font=(font_path, font_size), justification='center')],
    [sg.Combo(seconds, size=(15, 1), key='-SECS-', font=(font_path, font_size))]
]

knoppen_rij = [
    [sg.Button('Starten', font=(font_path, font_size), button_color=('white', green_hex)),
     sg.Push(),
     sg.Button('Sluiten', font=(font_path, font_size), button_color=('white', green_hex))]
]

layout = [
    [sg.Column(uur_kolom), sg.Column(minuut_kolom), sg.Column(seconde_kolom)],
    [sg.Text(' ')],
    knoppen_rij
]

window = sg.Window('Aftelklok', layout, size=(670, 200))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sluiten':
        break
    if event == 'Starten':
        try:
            hrs = int(values['-HRS-'])
            mins = int(values['-MINS-'])
            secs = int(values['-SECS-'])

            timer_window, graph, large_text_id, small_text_id, img_width, img_height, large_clock_location, small_clock_location = show_timer_window(hrs, mins, secs)

            stop_event = threading.Event()
            countdown_finished_event = threading.Event()

            threading.Thread(target=start_timer, args=(graph, large_text_id, large_clock_location, stop_event, countdown_finished_event), daemon=True).start()
            threading.Thread(target=countdown_timer, args=(hrs, mins, secs, graph, small_text_id, small_clock_location, stop_event, countdown_finished_event), daemon=True).start()

            while True:
                event, _ = timer_window.read(timeout=10)
                if event == '-GRAPH-':
                    stop_event.set()
                    pygame.mixer.music.stop()  # Stop het geluid
                    timer_window.close()
                    break

        except ValueError:
            sg.popup('Voer geldige getallen in voor uren, minuten en seconden.')

window.close()
