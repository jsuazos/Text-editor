import PySimpleGUI as sg

smileys = [
    'happy',[':)','xD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word count']],
    ['Add', smileys]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline()]
]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

window.close()