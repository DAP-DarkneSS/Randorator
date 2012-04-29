#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

import wx
from body import randorator
#Загружается основной модуль программы и графическая библиотека.

#===========================|Text_Control_Class|============================#

class MyTextCtrl:
    def __init__(self, place_frame, place_sizer, string_class):
# Принимается frame прикрепления виджета, sizer упаковки и текст надписи.
        self.sizer_class = wx.BoxSizer(wx.HORIZONTAL)
        place_sizer.Add(self.sizer_class)
# Создаётся упаковщик с горизонтальным порядком заполнения и добавляется в переданный упаковщик.
        self.text_class = wx.StaticText(place_frame, label = string_class, size = (140, -1))
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
        self.button_class = wx.Button(place_frame, label = string_class, size = (120, -1))
        place_sizer.Add(self.button_class)
        place_frame.Bind(wx.EVT_BUTTON, command_class, self.button_class)
# Создаётся и добавляется в переданный упаковщик кнопка. Присваевается функция для выполнения.

#========================|Generate_Button_Function|=========================#

def button_fmake(event):
# Функция для кнопки генерации. Записывается с аргументом события.
    text = randorator(sizer_mini.GetValue(), sizer_maxi.GetValue(), sizer_n.GetValue(), sizer_mean.GetValue(), sizer_rsd.GetValue(), check_punctu.IsChecked(), sizer_round.GetValue())
# Передача внешней функции большинства параметров и получение теста.
    text_out.SetValue(text)
# Запись текста в поле.
    if check_copy.IsChecked():
        pass
        #cb = wx.Clipboard()
        #if cb.Open():
            #tdo = wx.TextDataObject("123")
            #cb.SetData(tdo)
            #cb.Close()
# Начало работы над буфером обмена. Epic fail! =(

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

#==================================|Title|==================================#

text_title = wx.StaticText(frame_root, style = wx.ALIGN_CENTER | wx.EXPAND)
# Текстовый виджет c выравниванием по центру, растянут по ширине.
text_title.SetLabel(u"Продвинутый графический\nгенератор случайных чисел")
# Задаётся текст виджета.

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
# Кнопка запуска генерирования.
button_exit = MyButton(frame_root, sizer_buttonz, u"Выход", button_fexit)
# Кнопка выхода из приложения.

#===============================|Check_Boxes|===============================#

check_copy = MyCheckBox(frame_root, sizer_root, u"Автоматически копировать", 1)
# Чекбокс для включения/выключения автоматического копирования значений. Активен — копировать
check_punctu = MyCheckBox(frame_root, sizer_root, u'Числа с "." ("," по умолчанию)', 0)
# Чекбокс для переключения между точками и запятыми. Неактивен – запятые.

#============================|Text_Data_Output|=============================#

text_out = wx.TextCtrl(frame_root, style = wx.EXPAND | wx.TE_MULTILINE, size = (-1, 150))
# Текстовый виджет c выравниванием по центру, растянут по ширине.
sizer_root.Add(text_out, flag = wx.EXPAND)
# Текстовый виджет добавляется в корневой упаковщик.

#=============================|Program_Window|==============================#

frame_root.SetSize(frame_root.GetBestSize())
# Окно подбирает оптимальный размер, для размещения всех виджетов.
frame_root.Show()
# Показать окно.
app_root.MainLoop()
# Окончание графической формы.
