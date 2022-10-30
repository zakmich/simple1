import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    layout = [
        [sg.Push(), sg.Image('xmark.png', pad = 0, enable_events = True, key = '-CLOSE-')],
        [sg.VPush()],
        [sg.Text('0.0', font = 'Calibri 50', key = '-TIME-')],
        [
            sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = '-STARTSTOP-'),
            sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = '-LAP-', visible = False)],
        [sg.Column([[]], key = '-LAPS-')],
        [sg.VPush()]
    ]

    return sg.Window('Stopwatch',layout, size =(300,300), no_titlebar = True, element_justification = 'center')

window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible = False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible = True)

    if active:
        current_time = round(time() - start_time, 1)
        window['-TIME-'].update(current_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount),sg.VSeparator(),sg.Text(current_time)]])
        lap_amount += 1



window.close()