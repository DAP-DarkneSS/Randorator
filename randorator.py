#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

from Tkinter import *
from ScrolledText import ScrolledText
from body import randorator
#Загружается основной модуль программы, графическая библиотека
#и модуль, содержащий текстовый виджет с полосой прокрутки.

class MyEntry:
#Класс для уменьшений объёма кода однотипных элементов для ввода параметров.
    def __init__(self, place_class, string_class):
#При создании принимается место прикрепления виджета и строковое значение для надписи.
        self.frame_class = Frame(place_class)
        self.frame_class.pack(side = TOP, fill = BOTH)
#Внутри – рамка для виджетов, растягивается по ширине окна.
        self.label_class = Label(self.frame_class, text = string_class)
        self.label_class.pack(side = LEFT)
        self.entry_class = Entry(self.frame_class, width = 15)
        self.entry_class.pack(side = RIGHT)
#В ней – надписи (для описания вводимых значений, выровнены по левому краю) и
#элементы для ввода значений (шириной в 15 знаков, выровнены по правому краю).
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
#Очистка текстового поля
    text = randorator(entry_mini.get(), entry_maxi.get(), entry_n.get(), entry_mean.get(), entry_rsd.get(), vcheck_punctuation.get(), entry_round.get())     
    text_out.insert(END, text)
#Передача внешней функции большинства параметров. Получение теста и передача его в поле.
    if vcheck_copy.get():
        root.clipboard_clear()
        root.clipboard_append(text)
#Если не указано иное, очищается буфер обмена, копируются полученные значения.

root=Tk()
root.title(u"Рандоратор")
#Создаётся окно приложения, задаётся заголовок.
root.resizable(False, False)
#Нельзя изменять размер окна.

label_title = Label(root, text = u"Продвинутый графический\nгенератор случайных чисел")
label_title.pack()
#Надпись с описанием программы.

entry_mini = MyEntry(root, u"Минимум:")
entry_maxi = MyEntry(root, "Максимум:")
entry_n = MyEntry(root, u"Количество:")
entry_mean = MyEntry(root, u"Среднее:")
entry_rsd = MyEntry(root, u"RSD, %:")
entry_round = MyEntry(root, u"Округление:")
#Создаётся необходимое количество объектов класса элементов ввода.

frame_buttonz = Frame(root)
frame_buttonz.pack(side = TOP, fill = BOTH)
#Рамка для кнопок. 
button_make = MyButton(frame_buttonz, u"Генерировать!", button_fmake)
#Кнопка генерирования.
button_exit = MyButton(frame_buttonz, u"Выход", root.destroy)
#Кнопка выхода из приложения.

vcheck_copy = MyVCheck(root, u"Автоматически копировать", 1)
#Чекбокс для включения/выключения автоматического копирования значений.
#Активен – копировать.
vcheck_punctuation = MyVCheck(root, u'Числа с "." ("," по умолчанию)', 0)
#Чекбокс для переключения между точками и запятыми. Неактивен – запятые.

text_out=ScrolledText(root, height = 9, width = 9)
text_out.pack(side = BOTTOM, fill = BOTH)
#Текстовый виджет с полосой прокрутки растянут по ширине окна приложения.

root.mainloop()
#Окончание текста приложения.
