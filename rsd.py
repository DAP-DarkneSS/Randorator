#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

from math import sqrt
#Импорт модуля квадратного корня.

def relstdev(matrix, n, referance):
    rsd = referance + 1
    mean = sum(matrix) / n
    while rsd > referance:
#Изначально rsd задаётся больше допустимого, чтобы программа вошла в цикл.
        
        dev = []
        for i in xrange(0,n):
            dev.append((matrix[i] - mean) ** 2)
        rsd = 100 * (sqrt(sum(dev) / (n - 1))) / mean
#Рассчёт среднего значения.
#Рассчёт квадратичных отклонений, которые записываются в список, потому что пригодятся далее.
#Рассчёт относительного стандартного отклонения.

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
#из интервала между вычисленными максимумом и минимумом. Возвращение в начала цикла.

    return(matrix)
#Вывод значений.