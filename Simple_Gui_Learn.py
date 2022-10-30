import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'),sg.Spin(['item1', 'item2'])],
    [sg.Button('Button', key = '-BUTTON1-'),],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('Bogato'),sg.Button('Koniec', key = '-BUTTON2-')],

]

window = sg.Window("Converter",layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT-'].update(values['-INPUT-'])

    if event == '-BUTTON2-':
        break

    if event == '-TEXT-':
        print('Text was pressed')

window.close()


















