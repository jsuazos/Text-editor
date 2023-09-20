import PySimpleGUI as sg

layout = [[]]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

window.close()