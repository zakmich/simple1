import PySimpleGUI as sg

layout = [
    [sg.Text('Output', key = "-OUTPUT-")],
    [sg.Input(key = '-INPUT-')],
    [sg.Button('clear', key = '-BUTTON_CLEAR-'), sg.Button('enter', key = '-BUTTON_ENTER-')],
    [sg.Button('7', key = '-BUTTON7-'), sg.Button('8', key = '-BUTTON8-'), sg.Button('9', key = '-BUTTON9-'), sg.Button('*', key = '-BUTTON*-')],
    [sg.Button('4', key = '-BUTTON4-'), sg.Button('5', key = '-BUTTON5-'), sg.Button('6', key = '-BUTTON6-'), sg.Button('/', key = '-BUTTON/-')],
    [sg.Button('1', key = '-BUTTON1-'), sg.Button('2', key = '-BUTTON2-'), sg.Button('3', key = '-BUTTON3-'), sg.Button('+', key = '-BUTTON+-')],
    [sg.Button('0', key = '-BUTTON0-'), sg.Button(',', key = '-BUTTON.-'), sg.Button('-', key = '-BUTTON--')]


]

window = sg.Window("Calculator",layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()