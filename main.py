import PySimpleGUI as sg

smileys = [
    'happy',[':)','xD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
]

smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word count']],
    ['Add', smileys]
]

sg.theme('GrayGrayGray')

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline(
        no_scrollbar = True, 
        size = (50, 30), 
        key = '-TEXTBOX-')]
]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Word count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'Palabras: {word_count}\nCaracteres: {char_count}')
        

window.close()