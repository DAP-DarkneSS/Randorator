#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2013 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

from Tkinter import *
from ScrolledText import ScrolledText
#Загружается графическая библиотека и модуль, содержащий текстовый виджет с полосой прокрутки.
from ttk import Combobox
# Combobox widget module is loaded.
from body import randorator, check_icon, check_windows
# Program kernel module is loaded.
# Program icon existence checking module is loaded.
# Windows platform checking module is loaded.
from locale_ru import locale
# Russian locale module is imported.

windows = check_windows()
# Here it is a value to check if the program is run under windows.

class MyEntry:
#Класс для уменьшений объёма кода однотипных элементов для ввода параметров.
    def __init__(self, place_class, string_class, choise_class = False):
#При создании принимается место прикрепления виджета и строковое значение для надписи.
# A string value to add a combobox could be also inputed.

        self.frame_class = Frame(place_class)
        self.frame_class.pack(side = TOP, fill = BOTH)
#Внутри – рамка для виджетов, растягивается по ширине окна.
        self.label_class = Label(self.frame_class, text = string_class)
        self.label_class.pack(side = LEFT)
#В ней – надписи для описания вводимых значений выровнены по левому краю.
        self.entry_class = Entry(self.frame_class, width = 15)
        self.entry_class.pack(side = RIGHT)
#И элементы для ввода значений шириной в 15 знаков выровнены по правому краю.
        if choise_class:
            self.box_class = Combobox(self.frame_class, values = choise_class, width = 2)
            self.box_class.set(choise_class[0])
            self.box_class.pack(side = RIGHT)
# The combobox widget will be added if it is set.g
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
        self.button_class = Button(place_class, width = 14, text = string_class, command = command_class)
        self.button_class.pack(side = LEFT)
#Кнопка шириной в 14 пикселей прикрепляется к левому краю.

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

root=Tk()
#Создаётся окно приложения.
root.title(locale(u"ui_title"))
#Задаётся заголовок.
root.resizable(False, False)
#Нельзя изменять размер окна.
if windows:
    window_icon = check_icon()
    if window_icon != "":
        root.iconbitmap(default = window_icon)
# Window icon is loaded if the program is run under windows.
# It doesn't work for linux.

label_title = Label(root, text = locale(u"ui_about"))
label_title.pack()
#Надпись с описанием программы.

entry_mini = MyEntry(root, locale(u"ui_minim"), ["", "+"])
entry_maxi = MyEntry(root, locale(u"ui_maxim"), ["", "+"])
entry_n = MyEntry(root, locale(u"ui_quant"))
entry_mean = MyEntry(root, locale(u"ui_avera"))
entry_rsd = MyEntry(root, locale(u"ui_rsd_p"), ["<", "~"])
entry_round = MyEntry(root, locale(u"ui_round"))
entry_sortm = MyEntry(root, locale(u"ui_sortm"))
#Создаётся необходимое количество объектов класса элементов ввода.

frame_buttonz = Frame(root)
frame_buttonz.pack(side = TOP, fill = BOTH)
#Рамка для кнопок. 
button_make = MyButton(frame_buttonz, locale(u"ui_gen_b"), button_fmake)
#Кнопка генерирования.
button_exit = MyButton(frame_buttonz, locale(u"ui_exi_b"), root.destroy)
#Кнопка выхода из приложения.

vcheck_copy = MyVCheck(root, locale(u"ui_clipb"), 1)
#Чекбокс для включения/выключения автоматического копирования значений.
#Активен – копировать.
vcheck_punctuation = MyVCheck(root, locale(u"ui_punct"), 0)
#Чекбокс для переключения между точками и запятыми. Неактивен – запятые.
vcheck_verbosity = MyVCheck(root, locale(u"ui_error"), 1)
#Чекбокс для включения/выключения вывода сообщений об ошибках.
#Активен – выводить.
vcheck_algorithm = MyVCheck(root, locale(u"ui_truer"), 0)
# Here it is a checkbox to enable true random numbers generation.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/
vcheck_rsd_a = MyVCheck(root, locale(u"ui_rsd_a"), 0)
# Here it is a checkbox to configure true RSD value output.
# It isn't activated by default and RSD isn't outputed.

text_out=ScrolledText(root, height = 9, width = 9)
text_out.pack(side = BOTTOM, fill = BOTH)
#Текстовый виджет с полосой прокрутки растянут по ширине окна приложения.

root.mainloop()
#Окончание текста приложения.
