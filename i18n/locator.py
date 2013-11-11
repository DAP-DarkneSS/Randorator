#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2013 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

#=============================|Locale_Import|===============================#

from locale import getdefaultlocale

CurrentLocale = getdefaultlocale()
print("Current locale is " + CurrentLocale[0] + ". Current encoding is " + CurrentLocale[1] + ".")
# Here it is an announcement of the current locale & encoding.

if "ru" in CurrentLocale[0].lower():
    print("Let's speak Russian.")
    from ru import dict_str
else:
    print("Let's speak English.")
    from en import dict_str
# If "ru" isn't a country or a language, English will be chosen.

#============================|Locale_Function|==============================#

def locale(str_in):
    if str_in in dict_str:
        return(dict_str[str_in])
# If the key exists the corresponding value will be returned.

    else:
        return(dict_str[u"ui_lcerr"])
# Else the error message will be returned.
