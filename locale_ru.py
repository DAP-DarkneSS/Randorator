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

#===========================|Locale_Dictionary|=============================#

# Here it is a russian locale module.

dict_str = {
    u"ui_title": u"Randorator",
    u"ui_about": u"Продвинутый графический\nгенератор случайных чисел",
    u"ui_minim": u" Минимум:",
    u"ui_maxim": u" Максимум:",
    u"ui_quant": u" Количество:",
    u"ui_avera": u" Среднее:",
    u"ui_rsd_p": u" RSD, %:",
    u"ui_round": u" Округление:",
    u"ui_gen_b": u"Генерировать!",
    u"ui_exi_b": u"Выход",
    u"ui_clipb": u"Автоматически копировать",
    u"ui_punct": u'Числа с "." ("," по умолчанию)',
    u"ui_error": u"Сообщения об ошибках",
    u"ui_truer": u"Истинно случайные числа\nчерез интернет, медленно",
    u"ui_rsd_a": u"Отображение реального RSD",
    u"ui_sortm": u" Сортировка:"}
# There are lists of locale keys and values.

#============================|Locale_Function|==============================#

def locale(str_in):
    if str_in in dict_str:
        return(dict_str[str_in])
# If the key exists the corresponding value will be returned.

    else:
        return(u"Неверный идентификатор перевода!")
# Else the error message will be returned.