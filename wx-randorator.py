#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

import wx

def button_fmake(event):
# Функция для кнопки генерации. Записывается с аргументом события.
    event.Skip()
# Ничего не делать... пока .__.

def button_fexit(event):
# Функция для кнопки выхода. Записывается с аргументом события.
    frame_root.Close()
#     app_root.ExitMainLoop()
#     wx.Exit()
# Сразу три способа выйти ^,_,^ Два последних вешаются под Windows.

app_root = wx.App()

frame_root = wx.Frame(parent = None, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title = 'Randorator')
# Окно можно сворачивать, с системным меню, с заголовком и кнопкой закрытия.
# Задаётся заголовок.

sizer_root = wx.BoxSizer(wx.HORIZONTAL)
 
button_make = wx.Button(frame_root, wx.NewId(), label=u"Генерировать!", size=(110, 25))
button_exit = wx.Button(frame_root, wx.NewId(), label=u"Выход", size=(110, 25))
# Кнопки.

sizer_root.Add(button_make)
sizer_root.Add(button_exit)

frame_root.Bind(wx.EVT_BUTTON, button_fmake, button_make)
frame_root.Bind(wx.EVT_BUTTON, button_fexit, button_exit)
# Присваиваем кнопкам соответствующие функцию.

frame_root.SetSizer(sizer_root, deleteOld=True)

frame_root.Show()
# Показать форму.

app_root.MainLoop()
# Окончание формы.
