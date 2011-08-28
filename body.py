#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#Основная функция. Производит выбор функции генерерирования. Если требуется, применяют функцию
#уменьшения относительного стандартного отклонения (RSD) и заменяет точки на запятые.

from simple import rando
from average import average
from rsd import relstdev
#Импорт функций создания списка случаных чисел и уменьшения RSD.

def randorator(t_mini, t_maxi, t_n, t_mean, t_rsd, punctuation):
#Функция принимает текстовые значения нижней и верхней границ интервала, количества чисел, среднего значения,
#максимально допустимого RSD и числовое значение, указывающее знак препинания в экспортируемых числах.

    def punctu(txt):
        return(float(txt.replace(",", ".")))
#Функция принимает текстовое значение и возвращает число с точкой. Для обработки введённых данных.

    matrix = []
    text = ""
    mini = punctu(t_mini)
    maxi = punctu(t_maxi)
    n = int(t_n)
    m = n - 1
#Создаётся пустой список и текст. Обработываются границы интервала и количество чисел. Вычисляется удобное число m.

    if t_mean == "":
        matrix = rando(mini, maxi, n)
    else:
        mean = punctu(t_mean)
        matrix = average(mini, maxi, n, mean, m)
#Выбор и применение функции создание списка чисел в зависимости от того, задано ли среднее значение.
        
    if t_rsd != "":
        if t_mean == "":
            mean = sum(matrix) / n
        matrix = relstdev(matrix, n, mean, punctu(t_rsd))
#Если требуется, уменьшается RSD.
    
    for i in xrange(m):
        text += str(matrix[i]) + "\n"
    text +=  str(matrix[m])
#Список преобразуется в строку. Каждое число с красной строки.
    
    if not punctuation:
        text = text.replace(".", ",")
#Если требуется, то точки заменяются запятыми.

    return(text)
#Возврат теста.