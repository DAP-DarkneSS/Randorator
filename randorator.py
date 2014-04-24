#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2014 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

from configparser import SafeConfigParser
from body import check_icon
# Configuration file parser and existence checker are imported.

#=================================|Parser|==================================#

def parseIt(Config, Section, Value, FallBack, Type = "str"):

    try:
        if Type == "bool":
            OutPut = Config.getboolean(Section, Value)
# Logical values are parsed by special method.
        else:
            OutPut = Config.get(Section, Value)
    except:
        OutPut = FallBack
# If any exception is rised fallback value will be returned.

    return(OutPut)

#==================================|Input|==================================#

Confirator = SafeConfigParser()
Confirator.read(check_icon("ini"))

#=================================|Defaults|================================#

Settingz = {
    "str_usint": "wx",
    "str_langu": "en",
    "str_minim": "",
    "str_maxim": "",
    "str_quant": "",
    "str_avera": "",
    "str_rsd_p": "",
    "str_round": "",
    "log_clipb": True,
    "log_punct": True,
    "log_verbo": True,
    "log_algor": False,
    "log_min_v": False,
    "log_max_v": False,
    "log_rsd_a": False,
    "log_rsd_w": False,
    "str_sortm": ""}

#====================================|UI|===================================#
Interfacez = []

if __name__ == '__main__':

    try:
        from wx import App
        Interfacez.append("wx")
    except:
        print("WxWidgets (WxPython) user interface isn't available.")

    try:
        from tkinter import Tk
        Interfacez.append("tk")
    except:
        print("Tcl/Tk (Tkinter) user interface isn't available.")

    Interfacez.append("cl")

    try:
        from PyQt4 import QtCore
        Interfacez.append("qt")
    except:
        print("Qt4 (PyQt) user interface isn't available.")

    InterfaceConf = (parseIt(Confirator, "Interface", "str_usint", "")).lower()

    if InterfaceConf in Interfacez:
        print(InterfaceConf + " user interface will be used.")
        Settingz["str_usint"] = InterfaceConf

#=================================|Language|================================#

LanguageConf = (parseIt(Confirator, "Interface", "str_langu", "")).lower()

if LanguageConf in ["en", "ru"]:
    print("Let's speak " + LanguageConf + ".")
    Settingz["str_langu"] = LanguageConf

else:
    from locale import getdefaultlocale
    CurrentLocale = getdefaultlocale()
    print("Current locale is " + CurrentLocale[0] + ". Current encoding is " + CurrentLocale[1] + ".")
    if "ru" in CurrentLocale[0].lower():
        Settingz["str_langu"] = "ru"
# If interface language isn't configured system settings will be parsed.

#===============================|Decimal_Mark|==============================#

DecimalMarkConf = parseIt(Confirator, "Variables", "str_punct", "")

if not (DecimalMarkConf in [".", ","]):
    from locale import localeconv
    DecimalMarkConf = localeconv()["decimal_point"]

if DecimalMarkConf == ",":
    Settingz["log_punct"] = False
# If decimal mark isn't configured system settings will be parsed.

#==================================|Setup|==================================#

for i in ["log_clipb", "log_verbo", "log_algor", "log_min_v", "log_max_v", "log_rsd_a", "log_rsd_w"]:
    Settingz[i] = parseIt(Confirator, "Variables", i, Settingz[i], "bool")

for i in ["str_minim", "str_maxim", "str_quant", "str_avera", "str_rsd_p", "str_round", "str_sortm"]:
    Settingz[i] = parseIt(Confirator, "Variables", i, "")

#================================|Direct_Run|===============================#

if __name__ == '__main__':

    if Settingz["str_usint"] == "tk":
        from tk_randorator import UserInterface
    elif Settingz["str_usint"] == "cl":
        from body import UserInterface
    elif Settingz["str_usint"] == "qt":
        from qt_randorator import UserInterface
    else:
        from wx_randorator import UserInterface

    UserInterface(Settingz)
