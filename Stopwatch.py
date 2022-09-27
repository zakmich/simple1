import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Push(), sg.Image('xmark.png', pad = 0, enable_events = True, key = '-CLOSE-')],
    [sg.VPush()],
    [sg.Text('Time', font = 'Calibri 25')],
    [
        sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width = 0),
        sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width = 0)],
    [sg.VPush()]
]

window = sg.Window('Stopwatch',layout, size =(300,300), no_titlebar = True, element_justification = 'center')

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

window.close()