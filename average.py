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

#Функция создаёт список случайных чисел из определённого интервала с заданным средним значением

from random import triangular
#Импорт функции генерирования случайного числа, приближённого к заданному значению.

def average(mini, maxi, n, mean, m, fromzerotom):
#Функция получает верхнюю и нижнюю границу интервала, количество чисел,
#среднее значение и список, соответствующий количеству чисел -1.

    matrix = []
    summ = mean * n
#Создание пустого списка. Расчёт суммы всех чисел.

    maxi = min(maxi, (summ - mini * m))
    mini = max(mini, (summ - maxi * m))
#Немного математики: mini*(n-1)+maxi<=summ. Этим простым неравенством
#можно ограничить верхний интервал. По аналогии ограничиваем и нижний.
#Выбираем между рассчитанным ограничением и введённым значением.

    for i in fromzerotom:
        if (summ / (n - i)) < mean:
            matrix.append(triangular(mini, mean, mean))
        else:
            matrix.append(triangular(mean, maxi, mean))
        summ = summ - matrix[i]
#Заполнение списка случайными числами из интервала от минимума до среднего
#или от среднего до максимума в зависимости от того, куда попадает частное
#оставшейся суммы и количества несгенерированных чисел.
#Вероятность генерирования числа тем выше, чем оно ближе к заданному среднему значению.

    matrix.append(summ)
#Остаток записывается последним значением.

    while matrix[m] > maxi:
        mi = min(matrix)
        increment = (maxi - mi) / 3
        matrix[matrix.index(mi)] += increment
        matrix[m] -= increment
#Пока последнее число больше максимума, оно уменьшается на инкремент,
#рассчитанный из общих соображений. Чтобы не изменилось среднее значение,
#другое число увеличивается на инкремент.
#Такое может произойти, когда среднее значительно удалено от одной из границ.

    while matrix[m] < mini:
        ma = max(matrix)
        increment = (ma - mini) / 3
        matrix[matrix.index(ma)] -= increment
        matrix[m] += increment
#Аналогично, когда последнее число меньше минимума.

    return(matrix)
#Возврат списка.