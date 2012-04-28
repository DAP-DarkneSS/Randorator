#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

import wx
# Импорт тулкита.

def button_fmake(event):
# Функция для кнопки генерации. Записывается с аргументом события.
    event.Skip()
# Ничего не делать... пока .__.

def button_fexit(event):
# Функция для кнопки выхода. Записывается с аргументом события.
    frame_root.Close()
#     app_root.ExitMainLoop()
#     wx.Exit()
# Сразу три способа выйти ^,_,^ Два последних вешают программу под IDLE в Windows.

app_root = wx.App()
# Инициация тулкита.

frame_root = wx.Frame(parent = None, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title = 'Randorator', size = (230, 250))
# Окно можно сворачивать, с системным меню, с заголовком и кнопкой закрытия.
# Задаётся заголовок и размер.

sizer_root = wx.BoxSizer(wx.VERTICAL)
frame_root.SetSizer(sizer_root, deleteOld=True)
# Создаётся упаковщик с вертикальным порядком заполнения и применяется к окну.

text_title = wx.StaticText(frame_root, label = u"Продвинутый графический\nгенератор случайных чисел", style = wx.ALIGN_CENTER | wx.EXPAND)
sizer_root.Add(text_title, flag = wx.ALIGN_CENTER)
# Текстовый виджет добавляется в корневой упаковщик.

sizer_buttonz = wx.BoxSizer(wx.HORIZONTAL)
sizer_root.Add(sizer_buttonz)
# Создаётся упаковщик с горизонтальным порядком заполнения и добавляется в корневой упаковщик.

button_make = wx.Button(frame_root, label = u"Генерировать!", size = (110, 25))
button_exit = wx.Button(frame_root, label = u"Выход", size = (110, 25))
# Создаются кнопки.

sizer_buttonz.Add(button_make)
sizer_buttonz.Add(button_exit)
# Кнопки упаковываются в соответствующий упаковщик.

frame_root.Bind(wx.EVT_BUTTON, button_fmake, button_make)
frame_root.Bind(wx.EVT_BUTTON, button_fexit, button_exit)
# Присваиваем кнопкам соответствующие функции.

frame_root.Show()
# Показать окно.

app_root.MainLoop()
# Окончание графической формы.
