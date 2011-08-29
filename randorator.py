#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from ScrolledText import *
from body import randorator
#Загружается модуль случайных чисел, графическая библиотека
#и модуль, содержащий текстовый виджет с полосой прокрутки.

root=Tk()
root.title(u"Рандоратор")
root.resizable(False, False)
#Создаётся окно приложения, задаётся заголовок.
#Нельзя изменять размер окна.

label_title = Label(root, text = u"Продвинутый графический\nгенератор случайных чисел")
label_title.pack()
#Надпись с описанием программы.

frame_mini = Frame(root)
frame_mini.pack(fill=BOTH)
frame_maxi = Frame(root)
frame_maxi.pack(fill=BOTH)
frame_n = Frame(root)
frame_n.pack(fill=BOTH)
frame_mean = Frame(root)
frame_mean.pack(fill=BOTH)
frame_rsd = Frame(root)
frame_rsd.pack(fill=BOTH)
#Создаётся три рамки для виджетов. Рамки растягиваются по ширине окна.

label_mini = Label(frame_mini, text = u"*Минимум:")
label_mini.pack(side=LEFT)
entry_mini = Entry(frame_mini, width=15)
entry_mini.pack(side=RIGHT)
label_maxi = Label(frame_maxi, text = u"*Максимум:")
label_maxi.pack(side=LEFT)
entry_maxi = Entry(frame_maxi, width=15)
entry_maxi.pack(side=RIGHT)
label_n = Label(frame_n, text = u"*Количество:")
label_n.pack(side=LEFT)
entry_n = Entry(frame_n, width=15)
entry_n.pack(side=RIGHT)
label_mean = Label(frame_mean, text = u"Среднее:")
label_mean.pack(side=LEFT)
entry_mean = Entry(frame_mean, width=15)
entry_mean.pack(side=RIGHT)
label_rsd = Label(frame_rsd, text = u"RSD, %:")
label_rsd.pack(side=LEFT)
entry_rsd = Entry(frame_rsd, width=15)
entry_rsd.pack(side=RIGHT)
#Надписи, описывающие вводимые значения, выровнены по левому краю.
#Элементы для ввода значений шириной в 15 знаков выровнены по правому краю.

def button_fmake():
#Функция для кнопки. Записывается без аргументов!

    text_out.delete(1.0, END)
#Очистка текстового поля

    text = randorator(entry_mini.get(), entry_maxi.get(), entry_n.get(), entry_mean.get(), entry_rsd.get(), vcheck_punctuation.get())     
    text_out.insert(END, text)
#Передача внешней функции большинства параметров. Получение теста и передача его в поле.

    if vcheck_copy.get():
        root.clipboard_clear()
        root.clipboard_append(text)
#Если не указано иное, очищается буфер обмена, копируются полученные значения.

frame_buttonz = Frame(root)
frame_buttonz.pack(fill=BOTH)
button_make = Button(frame_buttonz, width=14, text=u"Генерировать!", command=button_fmake)
button_make.pack(side=LEFT)
button_exit = Button(frame_buttonz, width=14, text=u"Выход", command=root.destroy)
button_exit.pack(side=LEFT)
#Рамка для кнопок. Кнопка генерирования и выхода из приложения.

frame_checkz = Frame(root)
frame_checkz.pack(fill=BOTH)
frame_copy = Frame(frame_checkz)
frame_copy.pack(fill=BOTH)
frame_punctuation = Frame(frame_checkz)
frame_punctuation.pack(fill=BOTH)
vcheck_copy=IntVar()
vcheck_punctuation=IntVar()
#Рамки для чекбоксов и создание переменных для значений чекбоксов.

check_copy=Checkbutton(frame_copy,text=u"Автоматически копировать",variable=vcheck_copy,onvalue=1,offvalue=0)
check_copy.pack(side=LEFT)
check_copy.select()
#Чекбокс для включения/выключения автоматического копирования значений.
#Активен по умолчанию и означает "копировать".

check_punctuation=Checkbutton(frame_punctuation,text=u'Числа с "." ("," по умолчанию)',variable=vcheck_punctuation,onvalue=1,offvalue=0)
check_punctuation.pack(side=LEFT)
#Чекбокс для переключения между точками и запятыми.
#Неактивен по умолчанию и определяет вывод с запятыми.

text_out=ScrolledText(root, height=9, width=9)
text_out.pack(fill=BOTH)
#Текстовый виджет с полосой прокрутки растянут по ширине окна приложения.

label_star = Label(root, text = u'* — обязательно для заполнения')
label_star.pack(side=LEFT)
#Надпись с пояснением звёздочки.

root.mainloop()
#Окончание текста приложения.
