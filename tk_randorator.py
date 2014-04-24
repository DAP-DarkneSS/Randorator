#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2014 Dmitriy A. Perlow <dap.darkness@gmail.com>

# This file is part of Randorator.

# Randorator is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.

# Randorator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Randorator.  If not, see
# <http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>.

# You could contact me with e-mail or jabber dap.darkness@gmail.com

#=================================|Import|==================================#

# [ HACK: If not global — SyntaxError: import * is not allowed in function
# 'UserInterface' because it contains a nested function with free variables.

from tkinter import *

# SyntaxError: import * is not allowed in function… End of HACK ].

# [ HACK: If not global — NameError: free variable 'Entry' referenced
# before assignment in enclosing scope.

from tkinter.ttk import Combobox
# Combobox widget module is loaded.
from tkinter import messagebox
# A message box module is loaded to show help window.
from i18n.locator import locale

class MyEntry:
#Класс для уменьшений объёма кода однотипных элементов для ввода параметров.
    def __init__(self, place_class, string_class, DefaultValue, choise_class = False, button_add = False):
#При создании принимается место прикрепления виджета и строковое значение для надписи.
# A string value to add a combobox or a button could be also inputed.

        def button_finfo():
            messagebox.showinfo(locale("ui_iftxt", Settingz["str_langu"]), button_add)
# Here it is a function to show information window.

        self.frame_class = Frame(place_class)
        self.frame_class.pack(side = TOP, fill = BOTH)
#Внутри – рамка для виджетов, растягивается по ширине окна.
        self.label_class = Label(self.frame_class, text = string_class)
        self.label_class.pack(side = LEFT)
#В ней – надписи для описания вводимых значений выровнены по левому краю.
        self.entry_class = Entry(self.frame_class, width = 15)
        self.entry_class.pack(side = RIGHT)
        self.entry_class.insert(0, DefaultValue)
#И элементы для ввода значений шириной в 15 знаков выровнены по правому краю.
        if choise_class:
            self.box_class = Combobox(self.frame_class, values = choise_class, width = 2)
            self.box_class.set(choise_class[0])
            self.box_class.pack(side = RIGHT)
        elif button_add:
            self.button_class = Button(self.frame_class, text = "?", command = button_finfo, width = -1)
            self.button_class.pack(side = RIGHT)
# The combobox widget or the button will be created if it is set.

    def get(self):
        return(self.entry_class.get())
#Метод .get() передаётся от элемента для ввода объекту описываемого класса.
    def getbox(self):
        if self.box_class.get() in ["+", "~"]:
            return(True)
        else:
            return(False)
# Here it is a method to get user decision from a combobox as a logical value.

class MyVCheck:
#Класс для улучшения читаемости кода однотипных элементов чекбоксов.
    def __init__(self, place_class, string_class, logical_class):
#При создании принимается место прикрепления виджета, строковое значение для надписи
#и логическое для установки положения по умолчанию.
        self.frame_class = Frame(place_class)
        self.frame_class.pack(side = TOP, fill = BOTH)
#Внутри – рамка для виджетов, растягивается по ширине окна.
        self.vcheck_class = IntVar()
#Создание переменной для значения чекбокса.
        self.check_class = Checkbutton(self.frame_class, text=string_class, variable=self.vcheck_class, onvalue=1, offvalue=0)
        self.check_class.pack(side = LEFT)
#Собственно чекбокс внутри рамки, выровнен по левому краю.
        if logical_class:
            self.check_class.select()
#Если переданное логическое значение истинно, чекбокс делается активным.
    def get(self):
        return(self.vcheck_class.get())
#Метод .get() передаётся от значения чекбокса объекту описываемого класса.

class MyButton:
#Класс для улучшения читаемости кода однотипных элементов кнопок.
    def __init__(self, place_class, string_class, command_class):
#При создании принимается место прикрепления виджета, строковое значение для надписи
#и строковое для установления команды при нажатии.
        self.button_class = Button(place_class, width = 15, text = string_class, command = command_class)
        self.button_class.pack(side = LEFT)
#Кнопка шириной в 14 пикселей прикрепляется к левому краю.

# NameError: free variable referenced before assignment… End of HACK ].

def UserInterface(Settingz):

    from tkinter.scrolledtext import ScrolledText
#Загружается графическая библиотека и модуль, содержащий текстовый виджет с полосой прокрутки.

    from body import randorator, check_icon, check_windows
# Program kernel module is loaded.
# Program icon existence checking module is loaded.
# Windows platform checking module is loaded.

    def button_fmake():
#Функция для кнопки. Записывается без аргументов!
        text_out.delete(1.0, END)
#Очистка текстового поля.
        dict_val = {
        "str_minim": entry_mini.get(),
        "str_maxim": entry_maxi.get(),
        "str_quant": entry_n.get(),
        "str_avera": entry_mean.get(),
        "str_rsd_p": entry_rsd.get(),
        "str_round": entry_round.get(),
        "log_punct": vcheck_punctuation.get(),
        "log_verbo": vcheck_verbosity.get(),
        "log_algor": vcheck_algorithm.get(),
        "log_min_v": entry_mini.getbox(),
        "log_max_v": entry_maxi.getbox(),
        "log_rsd_a": vcheck_rsd_a.get(),
        "log_rsd_w": entry_rsd.getbox(),
        "str_sortm": entry_sortm.get()}
# Here it is a dictionary with almost all output values.
        dict_out = randorator(dict_val)
# The output dictionary is transfered to the external function to get text back.
        text_out.insert(END, dict_out["str_infoz"] + dict_out["str_numbz"])
# The text is put into the field.
        if vcheck_copy.get():
            root.clipboard_clear()
            root.clipboard_append(dict_out["str_numbz"])
#Если не указано иное, очищается буфер обмена, копируются полученные значения.

    windows = check_windows()
# Here it is a value to check if the program is run under windows.

    if windows:
        from tkinter.ttk import Button, Entry
# Let tkinter GUI at windows be less ugly. It doesn't look natively at Linux.

    root=Tk()
#Создаётся окно приложения.
    root.title(locale("ui_title", Settingz["str_langu"]))
#Задаётся заголовок.
    root.resizable(False, False)
#Нельзя изменять размер окна.
    root.call('wm', 'iconphoto', root._w, PhotoImage(file = check_icon("gif")))
# Window icon is loaded.

    label_title = Label(root, text = locale("ui_about", Settingz["str_langu"]))
    label_title.pack()
#Надпись с описанием программы.

    entry_mini = MyEntry(root, locale("ui_minim", Settingz["str_langu"]), Settingz["str_minim"], ["", "+"])

    entry_maxi = MyEntry(root, locale("ui_maxim", Settingz["str_langu"]), Settingz["str_maxim"], ["", "+"])

    entry_n = MyEntry(root, locale("ui_quant", Settingz["str_langu"]), Settingz["str_quant"])

    entry_mean = MyEntry(root, locale("ui_avera", Settingz["str_langu"]),  Settingz["str_avera"])

    entry_rsd = MyEntry(root, locale("ui_rsd_p", Settingz["str_langu"]), Settingz["str_rsd_p"], ["<", "~"])

    entry_round = MyEntry(root, locale("ui_round", Settingz["str_langu"]), Settingz["str_round"], False, locale("ui_ifrnd", Settingz["str_langu"]))

    entry_sortm = MyEntry(root, locale("ui_sortm", Settingz["str_langu"]), Settingz["str_sortm"], False, locale("ui_ifsrt", Settingz["str_langu"]))
#Создаётся необходимое количество объектов класса элементов ввода.

    frame_buttonz = Frame(root)
    frame_buttonz.pack(side = TOP, fill = BOTH)
#Рамка для кнопок. 
    button_make = MyButton(frame_buttonz, locale("ui_gen_b", Settingz["str_langu"]), button_fmake)
#Кнопка генерирования.
    button_exit = MyButton(frame_buttonz, locale("ui_exi_b", Settingz["str_langu"]), root.destroy)
#Кнопка выхода из приложения.

    vcheck_copy = MyVCheck(root, locale("ui_clipb", Settingz["str_langu"]), Settingz["log_clipb"])
#Чекбокс для включения/выключения автоматического копирования значений.
#Активен – копировать.
    vcheck_punctuation = MyVCheck(root, locale("ui_punct", Settingz["str_langu"]), Settingz["log_punct"])
#Чекбокс для переключения между точками и запятыми. Неактивен – запятые.
    vcheck_verbosity = MyVCheck(root, locale("ui_error", Settingz["str_langu"]), Settingz["log_verbo"])
#Чекбокс для включения/выключения вывода сообщений об ошибках.
#Активен – выводить.
    vcheck_algorithm = MyVCheck(root, locale("ui_truer", Settingz["str_langu"]), Settingz["log_algor"])
# Here it is a checkbox to enable true random numbers generation.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/
    vcheck_rsd_a = MyVCheck(root, locale("ui_rsd_a", Settingz["str_langu"]), Settingz["log_rsd_a"])
# Here it is a checkbox to configure true RSD value output.
# It isn't activated by default and RSD isn't outputed.

    text_out = ScrolledText(root, height = 9, width = 9)
    text_out.pack(side = BOTTOM, fill = BOTH)
#Текстовый виджет с полосой прокрутки растянут по ширине окна приложения.

    root.mainloop()
#Окончание текста приложения.

#================================|Direct_Run|===============================#

if __name__ == '__main__':

    from randorator import Settingz

    UserInterface(Settingz)
