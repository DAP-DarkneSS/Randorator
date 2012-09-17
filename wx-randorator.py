#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Указывается язык и кодировка.

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

import wx
from body import randorator
# Загружается основной модуль программы и графическая библиотека.
from os import path
# Загрузка модуля получения пути файла.
from platform import system
# Module of defining the operaton system is loaded.
from locale_ru import locale
# Russian locale module is imported.

#===========================|Text_Control_Class|============================#

class MyTextCtrl:
    def __init__(self, place_frame, place_sizer, string_class):
# Принимается frame прикрепления виджета, sizer упаковки и текст надписи.
        self.sizer_class = wx.BoxSizer(wx.HORIZONTAL)
        place_sizer.Add(self.sizer_class)
# Создаётся упаковщик с горизонтальным порядком заполнения и добавляется в переданный упаковщик.
        self.text_class = wx.StaticText(place_frame, label = string_class, size = (130, -1))
        self.control_class = wx.TextCtrl(place_frame, size = (100, -1))
# Описание значения и поле ввода.
        self.sizer_class.Add(self.text_class, flag = wx.ALIGN_CENTER_VERTICAL)
        self.sizer_class.Add(self.control_class)
# Описание (с выравниванием по вертикали) и поле упаковываются в соответствующий упаковщик.
    def GetValue(self):
        return(self.control_class.GetValue())
# Метод передаётся от чекбокса объекту описываемого класса.

#=============================|Check_Box_Class|=============================#

class MyCheckBox:
    def __init__(self, place_frame, place_sizer, string_class, logical_class):
# Принимается frame прикрепления, sizer упаковки, текст надписи и маркер отметки.
        self.check_class = wx.CheckBox(place_frame, label = string_class)
        place_sizer.Add(self.check_class)
# Создаётся и добавляется в переданный упаковщик чекбокс.
        if logical_class:
            self.check_class.SetValue(logical_class)
# Если задано, чекбокс отмечается.
    def IsChecked(self):
        return(self.check_class.IsChecked())
# Метод передаётся от чекбокса объекту описываемого класса.

#==============================|Button_Class|===============================#

class MyButton:
    def __init__(self, place_frame, place_sizer, string_class, command_class):
# Принимается frame прикрепления виджета, sizer упаковки, строковое значение для надписи и функция.
        self.button_class = wx.Button(place_frame, label = string_class, size = (115, -1))
        place_sizer.Add(self.button_class)
        place_frame.Bind(wx.EVT_BUTTON, command_class, self.button_class)
# Создаётся и добавляется в переданный упаковщик кнопка. Присваевается функция для выполнения.

#========================|Generate_Button_Function|=========================#

def button_fmake(event):
# Функция для кнопки генерации. Записывается с аргументом события.
    dict_val = {
    "str_minim": sizer_mini.GetValue(),
    "str_maxim": sizer_maxi.GetValue(),
    "str_quant": sizer_n.GetValue(),
    "str_avera": sizer_mean.GetValue(),
    "str_rsd_p": sizer_rsd.GetValue(),
    "str_round": sizer_round.GetValue(),
    "log_punct": check_punctu.IsChecked(),
    "log_verbo": check_verbosity.IsChecked(),
    "log_algor": check_algorithm.IsChecked()}
# Here it is a dictionary with almost all output values.
    text = randorator(dict_val)
# The output dictionary is transfered to the external function to get text back.
    text_out.SetValue(text)
# Запись текста в поле.
    if check_copy.IsChecked():
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(text))
            wx.TheClipboard.Close()
# Если задано, открывается, заполняется и закрывается буфер обмена.

#==========================|Exit_Button_Function|===========================#

def button_fexit(event):
# Функция для кнопки выхода. Записывается с аргументом события.
    frame_root.Close()
#     app_root.ExitMainLoop()
#     wx.Exit()
# Сразу три способа выйти ^,_,^ Два последних вешают программу под IDLE в Windows.

#=============================|Program_Window|==============================#

app_root = wx.App(0)
# Инициация тулкита. Zero to disable output window creating under windows.

frame_root = wx.Frame(parent = None, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
# Создаётся окно: его можно сворачивать, есть системное меню и кнопка закрытия.
frame_root.SetTitle(locale(u"ui_title"))
# Задаётся заголовок окна.
try:
    frame_root.SetIcon(wx.Icon(path.dirname(__file__) + '/randorator.ico', type = wx.BITMAP_TYPE_ICO))
except NameError:
    frame_root.SetIcon(wx.Icon('randorator.ico', type = wx.BITMAP_TYPE_ICO))
# Загружается иконка окна из папки с запускаемым файлом. Лицензия иконки:
# CC Attribution 3.0 United States (http://creativecommons.org/licenses/by/3.0/us/).
# Автор — Aha-Soft (http://www.softicons.com/free-icons/designers/aha-soft)
# http://www.softicons.com/free-icons/toolbar-icons/48x48-free-object-icons-by-aha-soft/dice-icon

panel_root = wx.Panel(frame_root, style = wx.TAB_TRAVERSAL)
# На корневой фрейм добавляется корневая панель,
# чтобы можно было переключаться между элементами по нажатию кнопки Tab.
# Применяется соответствующий стиль, хотя работает и без него.
panel_root.SetBackgroundColour(wx.NullColor)
# Окно заливается цветом по умолчанию для корректной отрисовки под windows.

sizer_root = wx.BoxSizer(wx.VERTICAL)
panel_root.SetSizer(sizer_root, deleteOld=True)
# Создаётся упаковщик с вертикальным порядком заполнения и применяется к окну.

#==================================|Title|==================================#

text_title = wx.StaticText(panel_root, style = wx.ALIGN_CENTER | wx.EXPAND)
# Текстовый виджет c выравниванием по центру, растянут по ширине.
text_title.SetLabel(locale(u"ui_about"))
# Задаётся текст виджета.

sizer_root.Add(text_title, flag = wx.ALIGN_CENTER)
# Текстовый виджет добавляется в корневой упаковщик.

#=============================|Text_Data_Input|=============================#

sizer_mini = MyTextCtrl(panel_root, sizer_root, locale(u"ui_minim"))
sizer_maxi = MyTextCtrl(panel_root, sizer_root, locale(u"ui_maxim"))
sizer_n = MyTextCtrl(panel_root, sizer_root, locale(u"ui_quant"))
sizer_mean = MyTextCtrl(panel_root, sizer_root, locale(u"ui_avera"))
sizer_rsd = MyTextCtrl(panel_root, sizer_root, locale(u"ui_rsd_p"))
sizer_round = MyTextCtrl(panel_root, sizer_root, locale(u"ui_round"))
# Рисуются упаковщики с описаниями значений и полями ввода.

#=================================|Buttons|=================================#

sizer_buttonz = wx.BoxSizer(wx.HORIZONTAL)
sizer_root.Add(sizer_buttonz)
# Создаётся упаковщик для кнопок и добавляется в корневой упаковщик.

button_make = MyButton(panel_root, sizer_buttonz, locale(u"ui_gen_b"), button_fmake)
# Кнопка запуска генерирования.
button_exit = MyButton(panel_root, sizer_buttonz, locale(u"ui_exi_b"), button_fexit)
# Кнопка выхода из приложения.

#===============================|Check_Boxes|===============================#

check_copy = MyCheckBox(panel_root, sizer_root, locale(u"ui_clipb"), 1)
# Чекбокс для включения/выключения автоматического копирования значений.
# Активен — копировать.
check_punctu = MyCheckBox(panel_root, sizer_root, locale(u"ui_punct"), 0)
# Чекбокс для переключения между точками и запятыми. Неактивен – запятые.
check_verbosity = MyCheckBox(panel_root, sizer_root, locale(u"ui_error"), 1)
# Чекбокс для включения/выключения вывода сообщений об ошибках.
# Активен – выводить.
if system().endswith("Windows"):
    check_algorithm = MyCheckBox(panel_root, sizer_root, u"Истинно случайные, медленно", 0)
else:
    check_algorithm = MyCheckBox(panel_root, sizer_root, locale(u"ui_truer"), 0)
# Here it is a checkbox to enable true random numbers generation.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/
# wx.CheckBox under windows doesn't suppoth the newline symbol:
# see more at http://trac.wxwidgets.org/ticket/9495

#============================|Text_Data_Output|=============================#

text_out = wx.TextCtrl(panel_root, style = wx.EXPAND | wx.TE_MULTILINE, size = (-1, 150))
# Текстовый виджет c выравниванием по центру, растянут по ширине.
sizer_root.Add(text_out, flag = wx.EXPAND)
# Текстовый виджет добавляется в корневой упаковщик.

#=============================|Program_Window|==============================#

frame_root.SetSize(panel_root.GetBestSize())
# Окно подбирает оптимальный размер, для размещения всех виджетов.
frame_root.Show()
# Показать окно.
app_root.MainLoop()
# Окончание графической формы.