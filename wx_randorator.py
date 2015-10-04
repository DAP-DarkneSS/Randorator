#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Указывается язык и кодировка.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2015 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

def UserInterface(Settingz):

    import wx
    from body import randorator, check_icon, check_windows
# Загружается основной модуль программы и графическая библиотека.
# Program icon existence checking module is loaded.
# Windows platform checking module is loaded.
    from i18n.locator import locale

# WxPython version dependent hacks.
    from wxversion import getInstalled
    try:
        if int(getInstalled()[0][0]) < 3:
            WxPython3 = False
        else:
            WxPython3 = True
    except:
# Strange Windows portable issue.
        WxPython3 = True

    windows = check_windows()
# Here it is a value to check if the program is run under windows.

#===========================|Text_Control_Class|============================#

    class MyTextCtrl:
        def __init__(self, place_frame, place_sizer, string_class, DefaultValue, choise_class = False, button_add = False, DefaultSelection = False):
# Принимается frame прикрепления виджета, sizer упаковки и текст надписи.
# A string value to add a combobox or a button could be also inputed.

            def button_finfo(event):
                wx.MessageBox(button_add, locale(u"ui_iftxt", Settingz["str_langu"]), wx.OK | wx.ICON_INFORMATION)
# Here it is a function to show information window.

            if choise_class or button_add:
                x_box = 45
            else:
                x_box = 0
            x_text = 150 - x_box
# The text widget width will be modified if a combobox or a button is enabled.

            self.sizer_class = wx.BoxSizer(wx.HORIZONTAL)
            place_sizer.Add(self.sizer_class)
# Создаётся упаковщик с горизонтальным порядком заполнения и добавляется в переданный упаковщик.
            self.text_class = wx.StaticText(place_frame, label = string_class, size = (x_text, -1))
            if choise_class:
                self.box_class = wx.Choice(place_frame, size = (x_box, -1), choices = choise_class)
            elif button_add:
                self.button_class = wx.Button(place_frame, label = u"?", size = (x_box, -1))
# The combobox widget or the button will be created if it is set.

            self.control_class = wx.TextCtrl(place_frame, size = (90, -1))
            self.control_class.SetValue(DefaultValue)
# Описание значения и поле ввода.
            self.sizer_class.Add(self.text_class, flag = wx.ALIGN_CENTER_VERTICAL)
            if choise_class:
                self.sizer_class.Add(self.box_class)
                self.box_class.SetSelection(DefaultSelection)
            elif button_add:
                self.sizer_class.Add(self.button_class)
                place_frame.Bind(wx.EVT_BUTTON, button_finfo, self.button_class)
# The combobox widget or the button will be shown if it is set.

            self.sizer_class.Add(self.control_class)
# Описание (с выравниванием по вертикали) и поле упаковываются в соответствующий упаковщик.
        def GetValue(self):
            return(self.control_class.GetValue())
# Метод передаётся от чекбокса объекту описываемого класса.
        def GetCurrentSelection(self):
            if self.box_class.GetCurrentSelection() == 1:
                return(True)
            else:
                return(False)
# Here it is a method to get user decision from a combobox as a logical value.

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
        dict_val = {
        "str_langu": Settingz["str_langu"],
        "str_minim": sizer_mini.GetValue(),
        "str_maxim": sizer_maxi.GetValue(),
        "str_quant": sizer_n.GetValue(),
        "str_avera": sizer_mean.GetValue(),
        "str_rsd_p": sizer_rsd.GetValue(),
        "str_round": sizer_round.GetValue(),
        "log_punct": check_punctu.IsChecked(),
        "log_verbo": check_verbosity.IsChecked(),
        "log_algor": check_algorithm.IsChecked(),
        "log_min_v": sizer_mini.GetCurrentSelection(),
        "log_max_v": sizer_maxi.GetCurrentSelection(),
        "log_rsd_a": check_rsd_a.IsChecked(),
        "log_rsd_w": sizer_rsd.GetCurrentSelection(),
        "log_horiz": check_horizontal_output.IsChecked(),
        "str_sortm": sizer_sortm.GetValue()}
# Here it is a dictionary with almost all output values.
        dict_out = randorator(dict_val)
# The output dictionary is transfered to the external function to get text back.
        text_out.SetValue(dict_out["str_infoz"] + dict_out["str_numbz"])
# Запись текста в поле.
        if check_copy.IsChecked():
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(wx.TextDataObject(dict_out["str_numbz"]))
                wx.TheClipboard.Close()
# Если задано, открывается, заполняется и закрывается буфер обмена.

#==========================|Exit_Button_Function|===========================#

    def button_fexit(event):
# Функция для кнопки выхода. Записывается с аргументом события.
        frame_root.Close()
#         app_root.ExitMainLoop()
#         wx.Exit()
# Сразу три способа выйти ^,_,^ Два последних вешают программу под IDLE в Windows.

#=============================|Program_Window|==============================#

    app_root = wx.App(0)
# Инициация тулкита. Zero to disable output window creating under windows.

    frame_root = wx.Frame(parent = None, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
# Создаётся окно: его можно сворачивать, есть системное меню и кнопка закрытия.
    if Settingz["log_ontop"]:
        frame_root.SetWindowStyleFlag(wx.STAY_ON_TOP)
# Window always on top behavior if configured.
    frame_root.SetTitle(locale(u"ui_title", Settingz["str_langu"]))
# Задаётся заголовок окна.
    window_icon = check_icon("ico")
    if window_icon != "":
        frame_root.SetIcon(wx.Icon(window_icon, type = wx.BITMAP_TYPE_ICO))
# Window icon is loaded.

    panel_root = wx.Panel(frame_root, style = wx.TAB_TRAVERSAL)
# На корневой фрейм добавляется корневая панель,
# чтобы можно было переключаться между элементами по нажатию кнопки Tab.
# Применяется соответствующий стиль, хотя работает и без него.
    if not WxPython3:
        panel_root.SetBackgroundColour(wx.NullColor)
# Окно заливается цветом по умолчанию для корректной отрисовки под windows.

    sizer_root = wx.BoxSizer(wx.VERTICAL)
    panel_root.SetSizer(sizer_root, deleteOld=True)
# Создаётся упаковщик с вертикальным порядком заполнения и применяется к окну.

#==================================|Title|==================================#

    text_title = wx.StaticText(panel_root, style = wx.ALIGN_CENTER | wx.EXPAND)
# Текстовый виджет c выравниванием по центру, растянут по ширине.
    text_title.SetLabel(locale(u"ui_about", Settingz["str_langu"]))
# Задаётся текст виджета.

    sizer_root.Add(text_title, flag = wx.ALIGN_CENTER)
# Текстовый виджет добавляется в корневой упаковщик.

#=============================|Text_Data_Input|=============================#

    sizer_mini = MyTextCtrl(panel_root, sizer_root, locale(u"ui_minim", Settingz["str_langu"]), Settingz["str_minim"], ["", "+"], False, Settingz["log_min_v"])

    sizer_maxi = MyTextCtrl(panel_root, sizer_root, locale(u"ui_maxim", Settingz["str_langu"]), Settingz["str_maxim"], ["", "+"], False, Settingz["log_max_v"])

    sizer_n = MyTextCtrl(panel_root, sizer_root, locale(u"ui_quant", Settingz["str_langu"]), Settingz["str_quant"])

    sizer_mean = MyTextCtrl(panel_root, sizer_root, locale(u"ui_avera", Settingz["str_langu"]),  Settingz["str_avera"])

    sizer_rsd = MyTextCtrl(panel_root, sizer_root, locale(u"ui_rsd_p", Settingz["str_langu"]), Settingz["str_rsd_p"], ["<", "~"], False, Settingz["log_rsd_w"])

    sizer_round = MyTextCtrl(panel_root, sizer_root, locale(u"ui_round", Settingz["str_langu"]), Settingz["str_round"], False, locale(u"ui_ifrnd", Settingz["str_langu"]))

    sizer_sortm = MyTextCtrl(panel_root, sizer_root, locale(u"ui_sortm", Settingz["str_langu"]), Settingz["str_sortm"], False, locale(u"ui_ifsrt", Settingz["str_langu"]))
# Рисуются упаковщики с описаниями значений и полями ввода.

#=================================|Buttons|=================================#

    sizer_buttonz = wx.BoxSizer(wx.HORIZONTAL)
    sizer_root.Add(sizer_buttonz)
# Создаётся упаковщик для кнопок и добавляется в корневой упаковщик.

    button_make = MyButton(panel_root, sizer_buttonz, locale(u"ui_gen_b", Settingz["str_langu"]), button_fmake)
# Кнопка запуска генерирования.
    button_exit = MyButton(panel_root, sizer_buttonz, locale(u"ui_exi_b", Settingz["str_langu"]), button_fexit)
# Кнопка выхода из приложения.

#===============================|Check_Boxes|===============================#

    check_copy = MyCheckBox(panel_root, sizer_root, locale(u"ui_clipb", Settingz["str_langu"]), Settingz["log_clipb"])
# Чекбокс для включения/выключения автоматического копирования значений.
# Активен — копировать.

    check_punctu = MyCheckBox(panel_root, sizer_root, locale(u"ui_punct", Settingz["str_langu"]), Settingz["log_punct"])
# Чекбокс для переключения между точками и запятыми. Неактивен – запятые.
    check_verbosity = MyCheckBox(panel_root, sizer_root, locale(u"ui_error", Settingz["str_langu"]), Settingz["log_verbo"])
# Чекбокс для включения/выключения вывода сообщений об ошибках.
# Активен – выводить.
    if ((not WxPython3) and windows):
        check_algorithm = MyCheckBox(panel_root, sizer_root, locale(u"ui_true1", Settingz["str_langu"]), Settingz["log_algor"])
    else:
        check_algorithm = MyCheckBox(panel_root, sizer_root, locale(u"ui_truer", Settingz["str_langu"]), Settingz["log_algor"])
# Here it is a checkbox to enable true random numbers generation.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/
# wx.CheckBox under windows doesn't suppoth the newline symbol:
# see more at http://trac.wxwidgets.org/ticket/9495
    check_rsd_a = MyCheckBox(panel_root, sizer_root, locale(u"ui_rsd_a", Settingz["str_langu"]), Settingz["log_rsd_a"])
# Here it is a checkbox to configure true RSD value output.
# It isn't activated by default and RSD isn't outputed.
    check_horizontal_output = MyCheckBox(panel_root, sizer_root, locale(u"ui_horiz", Settingz["str_langu"]), Settingz["log_horiz"])
# Horizontal (default&True) / vertical numbers output checkbox.

#============================|Text_Data_Output|=============================#

    text_out = wx.TextCtrl(panel_root, style = wx.EXPAND | wx.TE_MULTILINE, size = (-1, 150))
# Текстовый виджет c выравниванием по центру, растянут по ширине.
    sizer_root.Add(text_out, flag = wx.EXPAND)
# Текстовый виджет добавляется в корневой упаковщик.

#=============================|Program_Window|==============================#

    window_size = panel_root.GetBestSize()
    if ((not WxPython3) and windows):
        window_size[0] += ((235 - 230) + 1)
        window_size[1] += ((400 - 377) + 1)
# Size should be enlaged to fix wx/windows bug.
    frame_root.SetSize(window_size)
# Окно подбирает оптимальный размер, для размещения всех виджетов.
    frame_root.Show()
# Показать окно.
    app_root.MainLoop()
# Окончание графической формы.

#================================|Direct_Run|===============================#

if __name__ == '__main__':

    from randorator import Settingz

    UserInterface(Settingz)
