#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

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

#=================================|Import|==================================#

#Функция приводит список чисел к такому, чтобы относительное
#стандартное отклонение (RSD) не превышало заданный максимум.

from math import sqrt
#Импорт функции расчёта квадратного корня.

def relstdev(dict_val):
#Функция получает список чисел, их количество, среднее значение,
#максимально возможное RSD и список, соответствующий количеству чисел.

    matrix = dict_val["lst_numbz"]
    referance = dict_val["str_rsd_p"]

    def rsd_calc(fromzeroton, matrix, mean, n):
        summ = 0
        for i in fromzeroton:
            summ += ((matrix[i] - mean) ** 2)
        rsd = 100 * (sqrt(summ / (n - 1))) / abs(mean)
        return(rsd)
#Расчёт и суммирование квадратичных отклонений. Расчёт RSD.

    def rsd_decr(matrix, increment):
        matrix[matrix.index(max(matrix))] -= increment
        matrix[matrix.index(min(matrix))] += increment
#Если рассчитанное значение больше заданного предела,
#то число по позиции с максимальным значением уменьшается на инкремент,
#рассчитанный из общих соображений. Чтобы не изменилось среднее значение,
#число по позиции с минимальным значением увеличивается на инкремент.
        return(matrix)

    if dict_val["log_rsd_w"]:
        rsd_max = dict_val["str_rsd_p"] * 1.1
        rsd_min = dict_val["str_rsd_p"] * 0.9
    else:
        rsd_max = dict_val["str_rsd_p"]
        rsd_min = 0

    k = 3
    rsd = -1
    while (rsd > rsd_max) or (rsd < rsd_min):
        rsd = rsd_calc(dict_val["lst_index"], dict_val["lst_numbz"], dict_val["str_avera"], dict_val["str_quant"])
        
        maxi = max(matrix)
        mini = min(matrix)
        increment = (maxi - mini) / k

        if rsd > rsd_max:
            matrix = rsd_decr(matrix, increment)

        if rsd < rsd_min:
            pass

    dict_out = {
    "lst_matrix": matrix,
    "num_rsd_q": rsd}

    return(dict_out)
# Dictionary with numbers list and rsd value is created and returned.
