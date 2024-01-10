import os
# Импорт этой библиотеки позволяет обращаться
# напрямую к операционной системе
# (os - operational system (операционная система))

import subprocess
# Импорт этой библиотеки позволяет запускать
# параллельные процессы, чтобы не мешать
# основному процессу)
import PySimpleGUI as sg
# Уже знакомый Вам импорт
# графической библиотеки
import sys
# Тут пока будет не понятно, но этот
# модуль добавляем, чтобы иметь возможность
#нам пользоваться в коде временной папкой _MEIPASS,
#которая содержится в модуле sys

#---------------------------------------

#Код, расположенный ниже нужен для того, чтобы после
#компиляции вашего проекта система не "ошибалась",
#а искала файлы, входящие в проект именно там,
#где нужно. Этот код мы разберём обязательно,
#но сильно позже

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# Уже знакомая Вам тема оформления
sg.theme('LightGreen')
# Декоративные отступы
sg.set_options(element_padding=(0, 0))

# ------ Здесь расположены названия кнопок меню ------ #
menu_def = [['Файл', ['Открыть', 'Выход']],
['Свой пункт', ['Свой вложенный пункт', 'Ещё один вложенный пункт', 'Отмена'], ],
['Excel',['Открыть Excel']],
['Word',['Открыть Word']],
['Chrome',['Открыть Chrome']],
['Калькулятор',['Открыть калькулятор']],
['Командная строка',['Открыть командную строку']],
['Площади фигур',['Площадь прямоугольника']],

]

# ------ GUI  ------ #
layout = [
    [sg.Menu(menu_def, )],
    [sg.Output(size=(100, 20))]
]

window = sg.Window("Образец окна с меню", layout, default_element_size=(12, 1), auto_size_text=False,
                   auto_size_buttons=False,
                   default_button_element_size=(12, 1))

# ------ Логика работы кнопок меню ------ #
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    print('Button = ', event)

    # ------ Основное меню ------ #

    if event == 'Открыть':
        filename = sg.popup_get_file('file to open', no_window=True)
        os.startfile(filename)

    elif event == 'Открыть Excel':
        os.startfile(resource_path("./Start.xlsx"))

    elif event == 'Открыть Word':
        os.startfile(resource_path("./Start.docx"))

    elif event == 'Открыть калькулятор':
        #os.startfile(".\launch.bat")
        subprocess.Popen(resource_path("./launch.bat"))

    elif event == 'Открыть Chrome':
        subprocess.Popen(resource_path("./launch_chrome.bat"))

    elif event == 'Площадь прямоугольника':
        os.startfile(resource_path("./rectangle.exe"))
        #from subprocess import call
        #call["python", "resource_path[(./Rectangle/rectangle.py)]"]

    elif event == 'Открыть командную строку':
        os.startfile(resource_path("C:/Windows/system32/cmd.exe" ))













