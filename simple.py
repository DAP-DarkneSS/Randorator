#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#=================================|Copying|=================================#

# Copyright (C) 2011-2012 Dmitriy A. Perlow <dap.darkness@gmail.com>

# This file is part of Randorator.

# Randorator is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Randorator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Randorator.  If not, see <http://www.gnu.org/licenses/>.

#=================================|Import|==================================#

#Функция создаёт список случайных чисел из определённого интервала.

from random import uniform
#Импорт функции генерирования случайного числа.

def rando(mini, maxi, fromzeroton):
#Функция получает верхнюю и нижнюю границу интервала и список, соответствующий количеству чисел.

    matrix = []
    for i in fromzeroton:
        matrix.append(uniform(mini, maxi))
#Создаётся пустой список, заполняется определённым количеством случайных значений из выбранного интервала.

    return(matrix)
#Возврат списка.