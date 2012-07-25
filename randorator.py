#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2012 Dmitriy A. Perlow <dap.darkness@gmail.com>

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
from body import randorator
from platform import system
#Загружается основной модуль программы и модуль определения операционной системы.
from locale_ru import locale
# Russian locale module is imported.

class MyEntry:
#Класс для уменьшений объёма кода однотипных элементов для ввода параметров.
    def __init__(self, place_class, string_class):
#При создании принимается место прикрепления виджета и строковое значение для надписи.
        self.frame_class = Frame(place_class)
        self.frame_class.pack(side = TOP, fill = BOTH)
#Внутри – рамка для виджетов, растягивается по ширине окна.
        self.label_class = Label(self.frame_class, text = string_class)
        self.label_class.pack(side = LEFT)
#В ней – надписи для описания вводимых значений выровнены по левому краю.
        self.entry_class = Entry(self.frame_class, width = 15)
        self.entry_class.pack(side = RIGHT)
#И элементы для ввода значений шириной в 15 знаков выровнены по правому краю.
    def get(self):
        return(self.entry_class.get())
#Метод .get() передаётся от элемента для ввода объекту описываемого класса.

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
    text = randorator(entry_mini.get(), entry_maxi.get(), entry_n.get(), entry_mean.get(), entry_rsd.get(), vcheck_punctuation.get(), entry_round.get(), vcheck_verbosity.get(), vcheck_algorithm.get())     
    text_out.insert(END, text)
#Передача внешней функции большинства параметров. Получение теста и передача его в поле.
    if vcheck_copy.get():
        root.clipboard_clear()
        root.clipboard_append(text)
#Если не указано иное, очищается буфер обмена, копируются полученные значения.

root=Tk()
#Создаётся окно приложения.
root.title(locale(u"ui_title"))
#Задаётся заголовок.
root.resizable(False, False)
#Нельзя изменять размер окна.
if system().endswith("Windows"):
    from os import path
#Загрузка модуля получения пути файла.
    root.iconbitmap(default=path.dirname(__file__) + '/randorator.ico')
#Для windows загружается иконка окна из папки с запускаемым файлом.
#Под linux не работает. Лицензия иконки: CC Attribution 3.0 United States
#(http://creativecommons.org/licenses/by/3.0/us/).
#Автор — Aha-Soft (http://www.softicons.com/free-icons/designers/aha-soft)
#http://www.softicons.com/free-icons/toolbar-icons/48x48-free-object-icons-by-aha-soft/dice-icon

label_title = Label(root, text = locale(u"ui_about"))
label_title.pack()
#Надпись с описанием программы.

entry_mini = MyEntry(root, locale(u"ui_minim"))
entry_maxi = MyEntry(root, locale(u"ui_maxim"))
entry_n = MyEntry(root, locale(u"ui_quant"))
entry_mean = MyEntry(root, locale(u"ui_avera"))
entry_rsd = MyEntry(root, locale(u"ui_rsd_p"))
entry_round = MyEntry(root, locale(u"ui_round"))
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

text_out=ScrolledText(root, height = 9, width = 9)
text_out.pack(side = BOTTOM, fill = BOTH)
#Текстовый виджет с полосой прокрутки растянут по ширине окна приложения.

root.mainloop()
#Окончание текста приложения.
