#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2013 Dmitriy A. Perlow <dap.darkness@gmail.com>

# This file is part of Randorator.

# Randorator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# Randorator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

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

        def functionForButton(PlaceWidget, StringToShow):
            QtGui.QMessageBox.information(PlaceWidget, u"Help", StringToShow)

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
            self.Button = QtGui.QPushButton(u"?", PlaceWidget)
            self.Button.setFixedWidth(self.XBonus)
            PlaceWidget.connect(self.Button, QtCore.SIGNAL("clicked()"), QtCore.SLOT(functionForButton(PlaceWidget, ButtonToAdd)))
            self.Layout.addWidget(self.Button)

        self.Edit = QtGui.QLineEdit()
        self.Edit.setFixedWidth(100)
        self.Layout.addWidget(self.Edit)

#==============================|Button_Class|===============================#

class MyPushButton(QtGui.QPushButton):
    def __init__(self,
                 PlaceWidget,
                 PlaceLayout,
                 StringToShow):
        QtGui.QWidget.__init__(self, PlaceWidget)

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

#=============================|Program_Window|==============================#

app = QtGui.QApplication(argv)

WidgetRoot = QtGui.QWidget()
WidgetRoot.setWindowTitle('Randorator')
WidgetRoot.setWindowIcon(QtGui.QIcon(check_icon("gif")))

LayoutRoot = QtGui.QVBoxLayout()

#==================================|Title|==================================#

TextTitle = QtGui.QLabel(locale(u"ui_about"), WidgetRoot)
TextTitle.setAlignment(QtCore.Qt.AlignCenter)
LayoutRoot.addWidget(TextTitle)

#=============================|Text_Data_Input|=============================#

MyLineEditMini  = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_minim"), ["", "+"])
MyLineEditMaxi  = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_maxim"), ["", "+"])
MyLineEditN     = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_quant"))
MyLineEditMean  = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_avera"))
MyLineEditRsd   = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_rsd_p"), ["<", "~"])
MyLineEditRound = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_round"), False, locale(u"ui_ifrnd"))
MyLineEditSortm = MyLineEdit(WidgetRoot, LayoutRoot, locale(u"ui_sortm"), False, locale(u"ui_ifsrt"))

#=================================|Buttons|=================================#

LayoutButtonz = QtGui.QHBoxLayout()
LayoutRoot.addLayout(LayoutButtonz)

MyPushButtonMake = MyPushButton(WidgetRoot, LayoutButtonz, locale(u"ui_gen_b"))

MyPushButtonExit = MyPushButton(WidgetRoot, LayoutButtonz, locale(u"ui_exi_b"))
WidgetRoot.connect(MyPushButtonExit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

#===============================|Check_Boxes|=======s========================#

MyCheckBoxCopy      = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_clipb"), 1)
MyCheckBoxPunctu    = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_punct"), 0)
MyCheckBoxVerbosity = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_error"), 1)
MyCheckBoxAlgorithm = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_truer"), 0)
## Here it is a checkbox to enable true random numbers generation.
## randomdotorg is licenced under GPLv3 and/or any later. The creator is
## Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/
MyCheckBoxRsdA      = MyCheckBox(WidgetRoot, LayoutRoot, locale(u"ui_rsd_a"), 0)
## Here it is a checkbox to configure true RSD value output.
## It isn't activated by default and RSD isn't outputed.

#============================|Text_Data_Output|=============================#

TextOut = QtGui.QTextEdit(WidgetRoot)
TextOut.setFixedWidth(235)
LayoutRoot.addWidget(TextOut)

#=============================|Program_Window|==============================#

WidgetRoot.setLayout(LayoutRoot)
LayoutRoot.setSizeConstraint(QtGui.QLayout.SetFixedSize)
WidgetRoot.show()
app.exec_()
