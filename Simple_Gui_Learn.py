import PySimpleGUI as sg

layout = [
    [sg.Text('Text'),sg.Spin(['item1', 'item2'])],
    [sg.Button('Button')],
    [sg.Input()],
    [sg.Text('Bogato'),sg.Button('Koniec')],

]

window = sg.Window("Converter",layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


















