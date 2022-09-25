import PySimpleGUI as sg

layout = [
    [sg.Input(key = '-INPUT-'),sg.Spin(['km to mile', 'kg to pound'], key = '-UNITS-'), sg.Button('Convert', key = '-CONVERT-')],
    [sg.Text('Output', key = '-OUTPUT-')]

]

window = sg.Window("Converter",layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f'{input_value} km is equal to {output} miles'

            window['-OUTPUT-'].update(output_string)


window.close()


















