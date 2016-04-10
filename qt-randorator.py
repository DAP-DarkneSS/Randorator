#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2016 Dmitriy A. Perlow <dap.darkness@gmail.com>

# This file is part of Randorator.

# Randorator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# Randorator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Randorator.  If not, see
# <http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>.

# You could contact me with e-mail or jabber dap.darkness@gmail.com

#=================================|Import|==================================#

from sys import argv
from PyQt4 import QtCore, QtGui

from body import randorator, check_icon
# Program the main module is loaded.
# Program icon existence checking module is loaded.

from i18n.locator import locale
# Russian locale module is imported.

#===========================|Text_Control_Class|============================#

class MyLineEdit:
    def __init__(self,
                 PlaceWidget,
                 PlaceLayout,
                 StringToShow,
                 ComboBoxToAdd = False,
                 ButtonToAdd = False):

        class MyAnotherButton(QtGui.QPushButton):
            def __init__(self,
                         PlaceWidget,
                         PlaceLayout,
                         XBonus,
                         StringToShow):
                QtGui.QWidget.__init__(self, PlaceWidget)

                self.StringToShow = StringToShow
                self.clicked.connect(self.functionForButton)
# Connects only method only without arguments only in init.

                self.setText(u"?")
                self.setFixedWidth(XBonus)
                PlaceLayout.addWidget(self)

            def functionForButton(self):
                QtGui.QMessageBox.information(self, u"Help", self.StringToShow)

        if ComboBoxToAdd or ButtonToAdd:
            self.XBonus = 35
        else:
            self.XBonus = 0
        self.XText = 130 - self.XBonus
# The text widget width will be modified if a combobox or a button is enabled.

        self.Layout = QtGui.QHBoxLayout()
        PlaceLayout.addLayout(self.Layout)

        self.Label = QtGui.QLabel(StringToShow, PlaceWidget)
        self.Label.setFixedWidth(self.XText)
        self.Layout.addWidget(self.Label)

        if ComboBoxToAdd:
            self.ComboBox = QtGui.QComboBox(PlaceWidget)
            self.ComboBox.addItems(ComboBoxToAdd)
            self.ComboBox.setFixedWidth(self.XBonus)
            self.Layout.addWidget(self.ComboBox)

        if ButtonToAdd:
            self.Button = MyAnotherButton(PlaceWidget, self.Layout, self.XBonus, ButtonToAdd)

        self.LineEdit = QtGui.QLineEdit()
        self.LineEdit.setFixedWidth(100)
        self.Layout.addWidget(self.LineEdit)

    def text(self):
        return(self.LineEdit.text())

    def currentIndex(self):
        return(self.ComboBox.currentIndex())
# Here it is a method to get user decision from a combobox as a logical value.

#==============================|Button_Class|===============================#

class MyPushButton(QtGui.QPushButton):
    def __init__(self,
                 PlaceWidget,
                 PlaceLayout,
                 StringToShow,
                 DictToGet = False):
        QtGui.QWidget.__init__(self, PlaceWidget)

        if not DictToGet:
            self.clicked.connect(quit)

        self.setText(StringToShow)
        self.setFixedWidth(115)
        PlaceLayout.addWidget(self)

#=============================|Check_Box_Class|=============================#

class MyCheckBox:
    def __init__(self,
                 PlaceWidget,
                 PlaceLayout,
                 StringToShow,
                 LogicalToSet):

        self.CheckBox = QtGui.QCheckBox(StringToShow, PlaceWidget)
        PlaceLayout.addWidget(self.CheckBox)

        if LogicalToSet:
            self.CheckBox.setCheckState(QtCore.Qt.Checked)

    def checkStateSet(self):
        return(self.CheckBox.checkStateSet())

#=============================|Program_Window|==============================#

app = QtGui.QApplication(argv)

WidgetRoot = QtGui.QWidget()
WidgetRoot.setWindowTitle('Randorator')
WidgetRoot.setWindowIcon(QtGui.QIcon(check_icon("gif")))

LayoutRoot = QtGui.QVBoxLayout()

#==================================|Title|==================================#

TextTitle = QtGui.QLabel(locale(u"ui_about", "en"), WidgetRoot)
TextTitle.setAlignment(QtCore.Qt.AlignCenter)
LayoutRoot.addWidget(TextTitle)

#=============================|Text_Data_Input|=============================#

MyLineEditMini  = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_minim", "en"), ["", "+"])
MyLineEditMaxi  = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_maxim", "en"), ["", "+"])
MyLineEditN     = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_quant", "en"))
MyLineEditMean  = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_avera", "en"))
MyLineEditRsd   = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_rsd_p", "en"), ["<", "~"])
MyLineEditRound = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_round", "en"), False, locale(u"ui_ifrnd", "en"))
MyLineEditSortm = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_sortm", "en"), False, locale(u"ui_ifsrt", "en"))

#=================================|Buttons|=================================#

LayoutButtonz = QtGui.QHBoxLayout()
LayoutRoot.addLayout(LayoutButtonz)

MyPushButtonMake = MyPushButton(WidgetRoot, LayoutButtonz, locale(u"ui_gen_b", "en"), DictToGet = {})
MyPushButtonMake.setDisabled(True)

MyPushButtonExit = MyPushButton(WidgetRoot, LayoutButtonz, locale(u"ui_exi_b", "en"))

#===============================|Check_Boxes|=======s========================#

MyCheckBoxCopy      = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_clipb", "en"), 1)
MyCheckBoxPunctu    = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_punct", "en"), 0)
MyCheckBoxVerbosity = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_error", "en"), 1)
MyCheckBoxAlgorithm = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_truer", "en"), 0)
## Here it is a checkbox to enable true random numbers generation.
## randomdotorg is licenced under GPLv3 and/or any later. The creator is
## Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/
MyCheckBoxRsdA      = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_rsd_a", "en"), 0)
## Here it is a checkbox to configure true RSD value output.
## It isn't activated by default and RSD isn't outputed.

#DictToGet = {
            #"str_minim": MyLineEditMini.text(),
            #"str_maxim": MyLineEditMaxi.text(),
            #"str_quant": MyLineEditN.text(),
            #"str_avera": MyLineEditMean.text(),
            #"str_rsd_p": MyLineEditRsd.text(),
            #"str_round": MyLineEditRound.text(),
            #"log_punct": MyCheckBoxPunctu.checkStateSet(),
            #"log_verbo": MyCheckBoxVerbosity.checkStateSet(),
            #"log_algor": MyCheckBoxAlgorithm.checkStateSet(),
            #"log_min_v": MyLineEditMini.currentIndex(),
            #"log_max_v": MyLineEditMaxi.currentIndex(),
            #"log_rsd_a": MyCheckBoxRsdA.checkStateSet(),
            #"log_rsd_w": MyLineEditRsd.currentIndex(),
            #"str_sortm": MyLineEditSortm.text()}

#============================|Text_Data_Output|=============================#

TextOut = QtGui.QTextEdit(WidgetRoot)
TextOut.setFixedWidth(235)
LayoutRoot.addWidget(TextOut)

#=============================|Program_Window|==============================#

WidgetRoot.setLayout(LayoutRoot)
LayoutRoot.setSizeConstraint(QtGui.QLayout.SetFixedSize)
WidgetRoot.show()
app.exec_()
