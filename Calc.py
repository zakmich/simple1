import PySimpleGUI as sg


sg.theme('Python')
sg.set_options(font = 'Calibri 13', button_element_size = (6,3))
button_size = (6,3)

layout = [
    [sg.Text('', key = '-TEXT-', font = 'Calibri 25', justification = 'right', expand_x = True, pad = (5,20), background_color = 'white')],
    [sg.Button('clear', expand_x = True), sg.Button('enter', expand_x = True)],
    [sg.Button('7', size = button_size), sg.Button('8', size = button_size), sg.Button('9', size = button_size), sg.Button('*', size = button_size)],
    [sg.Button('4', size = button_size), sg.Button('5', size = button_size), sg.Button('6', size = button_size), sg.Button('/', size = button_size)],
    [sg.Button('1', size = button_size), sg.Button('2',size = button_size), sg.Button('3', size = button_size), sg.Button('+', size = button_size)],
    [sg.Button('0', expand_x = True), sg.Button('.', size = button_size), sg.Button('-', size = button_size)]

]
window = sg.Window("Calculator",layout)

current_number = []
operation = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_number.append(event)
        join_number = ''.join(current_number)
        window['-TEXT-'].update(join_number)

    if event in ['+', '-', '/', '*' ]:
        operation.append(''.join(current_number))
        current_number = []
        operation.append(event)
        window['-TEXT-'].update('')

    if event == 'enter':
        operation.append(''.join(current_number))
        result = eval(''.join(operation))
        window['-TEXT-'].update(result)
        operation = []

    if event == 'clear':
        current_number = []
        operation = []
        window['-TEXT-'].update('')


window.close()