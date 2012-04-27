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
    gui.Close(True)
    root.ExitMainLoop()
    wx.Exit()
# Сразу три способа выйти ^,_,^

root = wx.App()

gui = wx.Frame(parent = None, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title = 'Randorator')
# Окно можно сворачивать, с системным меню, с заголовком и кнопкой закрытия.
# Задаётся заголовок.
 
button_make = wx.Button(gui, label=u"Генерировать!", pos=(0, 0), size=(110, 25))
button_exit = wx.Button(gui, label=u"Выход", pos=(111, 0), size=(110, 25))
# Кнопки.

gui.Bind(wx.EVT_BUTTON, button_fmake, button_make)
gui.Bind(wx.EVT_BUTTON, button_fexit, button_exit)
# Присваиваем кнопкам соответствующие функцию.

gui.Show()
# Показать форму.

root.MainLoop()
# Окончание формы.