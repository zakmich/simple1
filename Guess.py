import PySimpleGUI as sg
from random import randint

layout = [
    [sg.Text('Guess number from range 1-100')],
    [sg.Input(key = '-INPUT-'), sg.Button('CHECK', key = '-CHECK-')],
    [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window("Guess",layout)

x = randint(1,100)
number = 0
print(x)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CHECK-':
        input_value = int(values['-INPUT-'])
        if x > input_value:
            output_string = 'Too low'
        if x < input_value:
            output_string = 'Too high'
        if x == input_value:
            output_string = 'Score!'

    window['-OUTPUT-'].update(output_string)

window.close()