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

#=============================|Program_Window|==============================#

app = QtGui.QApplication(argv)

WidgetRoot = QtGui.QWidget()
WidgetRoot.setWindowTitle('Randorator')
WidgetRoot.setWindowIcon(QtGui.QIcon(check_icon("gif")))

LayoutRoot = QtGui.QVBoxLayout()

TextTitle = QtGui.QLabel(locale(u"ui_about"), WidgetRoot)
LayoutRoot.addWidget(TextTitle)

LayoutMini = QtGui.QHBoxLayout()
LayoutRoot.addLayout(LayoutMini)

LabelMini = QtGui.QLabel(locale(u"ui_minim"), WidgetRoot)
LayoutMini.addWidget(LabelMini)

EditMini = QtGui.QLineEdit()
LayoutMini.addWidget(EditMini)

LayoutButtonz = QtGui.QHBoxLayout()
LayoutRoot.addLayout(LayoutButtonz)

ButtonMake = QtGui.QPushButton(locale(u"ui_gen_b"), WidgetRoot)
LayoutButtonz.addWidget(ButtonMake)

ButtonExit = QtGui.QPushButton(locale(u"ui_exi_b"), WidgetRoot)
LayoutButtonz.addWidget(ButtonExit)

WidgetRoot.setLayout(LayoutRoot)
WidgetRoot.show()

app.exec_()
