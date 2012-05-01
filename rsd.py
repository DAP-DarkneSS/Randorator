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

#Функция приводит список чисел к такому, чтобы относительное
#стандартное отклонение (RSD) не превышало заданный максимум.

from math import sqrt
#Импорт функции расчёта квадратного корня.

def relstdev(matrix, n, mean, referance, fromzeroton):
#Функция получает список чисел, их количество, среднее значение,
#максимально возможное RSD и список, соответствующий количеству чисел.

    rsd = referance + 1
    while rsd > referance:
#Изначально RSD задаётся больше допустимого, чтобы программа вошла в цикл.
        
        summ = 0
        for i in fromzeroton:
            summ += ((matrix[i] - mean) ** 2)
        rsd = 100 * (sqrt(summ / (n - 1))) / abs(mean)
#Расчёт и суммирование квадратичных отклонений. Расчёт RSD.

        if rsd > referance:
            maxi = max(matrix)
            mini = min(matrix)
            increment = (maxi - mini) / 3
            matrix[matrix.index(maxi)] -= increment
            matrix[matrix.index(mini)] += increment
#Если рассчитанное значение больше заданного предела,
#то число по позиции с максимальным значением уменьшается на инкремент,
#рассчитанный из общих соображений. Чтобы не изменилось среднее значение,
#число по позиции с минимальным значением увеличивается на инкремент.
#Возвращение в начала цикла.

    return(matrix)
#Возврат списка.