#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

import wx
# Импорт тулкита.

#===========================|Text_Control_Class|============================#

class MyTextCtrl:
# Класс для уменьшений объёма кода однотипных элементов для ввода параметров.
    def __init__(self, place_frame, place_sizer, string_class):
# Принимается frame прикрепления виджета, sizer упаковки и строковое значение для надписи.
        self.sizer_class = wx.BoxSizer(wx.HORIZONTAL)
        place_sizer.Add(self.sizer_class)
# Создаётся упаковщик с горизонтальным порядком заполнения и добавляется в переданный упаковщик.
        self.text_class = wx.StaticText(place_frame, label = string_class, size = (140, -1))
        self.control_class = wx.TextCtrl(place_frame, size = (100, -1))
# Описание значения и поле ввода.
        self.sizer_class.Add(self.text_class, flag = wx.ALIGN_CENTER_VERTICAL)
        self.sizer_class.Add(self.control_class)
# Описание (с выравниванием по вертикали) и поле упаковываются в соответствующий упаковщик.

#==============================|Button_Class|===============================#

class MyButton:
# Класс для уменьшений объёма кода однотипных элементов кнопок.
    def __init__(self, place_frame, place_sizer, string_class, command_class):
# Принимается frame прикрепления виджета, sizer упаковки, строковое значение для надписи и функция.
        self.button_class = wx.Button(place_frame, label = string_class, size = (120, -1))
        place_sizer.Add(self.button_class)
        place_frame.Bind(wx.EVT_BUTTON, command_class, self.button_class)
# Создаётся и добавляется в переданный упаковщик кнопка. Присваевается функция для выполнения.

#========================|Generate_Button_Function|=========================#

def button_fmake(event):
# Функция для кнопки генерации. Записывается с аргументом события.
    event.Skip()
# Ничего не делать... пока .__.

#==========================|Exit_Button_Function|===========================#

def button_fexit(event):
# Функция для кнопки выхода. Записывается с аргументом события.
    frame_root.Close()
#     app_root.ExitMainLoop()
#     wx.Exit()
# Сразу три способа выйти ^,_,^ Два последних вешают программу под IDLE в Windows.

#=============================|Program_Window|==============================#

app_root = wx.App()
# Инициация тулкита.

frame_root = wx.Frame(parent = None, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
# Создаётся окно: его можно сворачивать, есть системное меню и кнопка закрытия.

frame_root.SetTitle('Randorator')
# Задаётся заголовок окна.

sizer_root = wx.BoxSizer(wx.VERTICAL)
frame_root.SetSizer(sizer_root, deleteOld=True)
# Создаётся упаковщик с вертикальным порядком заполнения и применяется к окну.

#==============================|Window_Title|===============================#

text_title = wx.StaticText(frame_root, label = u"Продвинутый графический\nгенератор случайных чисел", style = wx.ALIGN_CENTER | wx.EXPAND)
sizer_root.Add(text_title, flag = wx.ALIGN_CENTER)
# Текстовый виджет добавляется в корневой упаковщик.

#=============================|Text_Data_Input|=============================#

sizer_mini = MyTextCtrl(frame_root, sizer_root, u" Минимум:")
sizer_maxi = MyTextCtrl(frame_root, sizer_root, u" Максимум:")
sizer_n = MyTextCtrl(frame_root, sizer_root, u" Количество:")
sizer_mean = MyTextCtrl(frame_root, sizer_root, u" Среднее:")
sizer_rsd = MyTextCtrl(frame_root, sizer_root, u" RSD, %:")
sizer_round = MyTextCtrl(frame_root, sizer_root, u" Округление:")
# Рисуются упаковщики с описаниями значений и полями ввода.

#=================================|Buttons|=================================#

sizer_buttonz = wx.BoxSizer(wx.HORIZONTAL)
sizer_root.Add(sizer_buttonz)
# Создаётся упаковщик для кнопок и добавляется в корневой упаковщик.

button_make = MyButton(frame_root, sizer_buttonz, u"Генерировать!", button_fmake)
button_exit = MyButton(frame_root, sizer_buttonz, u"Выход", button_fexit)
# Создаются кнопки в соответствующем упаковщике.

#=============================|Program_Window|==============================#

frame_root.SetSize(frame_root.GetBestSize())
# Окно подбирает оптимальный размер, для размещения всех виджетов.

frame_root.Show()
# Показать окно.

app_root.MainLoop()
# Окончание графической формы.
