#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

from random import triangular

def average(mini, maxi, n, mean):

#ввод верхней и нижней границ интервала генерирования.
#Ввод среднего значения.

    matrix = []
    summ = mean * n
#Создание пустого списка. Расчёт суммы всех чисел.

    if mini > maxi:
        maxi, mini = mini, maxi
#Если при вводе были перепутаны границы, то они меняются местами.

    m = n - 1
    maxi = min(maxi, (summ - mini * m))
    mini = max(mini, (summ - maxi * m))
#Немного математики: mini*(n-1)+maxi<=summ. Этим простым неравенством
#можно ограничить верхний интервал. По аналогии ограничиваем и нижний.
#Выбираем между рассчитанным ограничением и введённым значением.

    for i in xrange(0, m):
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
#Вывод разделителя и значений.