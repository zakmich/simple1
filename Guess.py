import PySimpleGUI as sg
from random import randint

sg.theme('DarkBlue')

layout = [
    [sg.Text('Guess number from range 1-100', font = 'calibri 20', justification = 'center', expand_x = True)],
    [sg.Input(font = 'calibri 15', key = '-INPUT-'), sg.Button('CHECK', font = 'calibri', border_width = 0,  key = '-CHECK-')],
    [sg.Text('Result', font = 'calibri 15', key = '-OUTPUT-'), sg.Text('Attempt', font = 'calibri 15', key = '-TRY-', justification = 'right', expand_x = True)]
]

window = sg.Window("Guess",layout)

x = randint(1,100)
number = 0
print(x)
counter = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CHECK-':
        input_value = int(values['-INPUT-'])
        if x > input_value:
            output_string = 'Too low.'
            counter += 1
        if x < input_value:
            output_string = 'Too high.'
            counter += 1
        if x == input_value:
            output_string = 'You got it!'
            counter += 1

        window['-OUTPUT-'].update(output_string)
        window['-TRY-'].update(f'Number of attempts: {counter}')

window.close()