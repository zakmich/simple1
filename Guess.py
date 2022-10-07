import PySimpleGUI as sg
from random import randint

def new_window():
    sg.theme('DarkBlue')
    layout = [
        [sg.VPush(),sg.Text('Guess number from range 1-100', font = 'calibri 14', justification = 'center', expand_x = True)],
        [sg.Button('RESET', font = 'calibri', border_width = 0,  key = '-RESET-'),sg.Input(font = 'calibri 15', key = '-INPUT-', size = (5,10), justification = 'center', expand_x = True),
         sg.Button('CHECK', font = 'calibri', border_width = 0,  key = '-CHECK-')],
        [sg.Text('Result', font = 'calibri 12', key = '-OUTPUT-'), sg.Text('Attempt', font = 'calibri 12', key = '-TRY-', justification = 'right', expand_x = True)],
        [sg.VPush()]
    ]

    return sg.Window("Guess",layout, size = (300,150))

window = new_window()
x = randint(1,100)
print(x)
counter = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-RESET-':
        window = new_window()
    if event == '-CHECK-':
        window['-INPUT-'].update('')
        input_value = int(values['-INPUT-'])
        if x > input_value:
            output_string = 'Too low.'
            counter += 1
        if x < input_value:
            output_string = 'Too high.'
            counter += 1
        if x == input_value:
            output_string = 'You got it!'
            window['-CHECK-'].update(disabled = True)
            counter += 1

        window['-OUTPUT-'].update(output_string)
        window['-TRY-'].update(f'Number of attempts: {counter}')

window.close()