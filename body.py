#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#Основная функция. Производит выбор функции генерирования. Если требуется, применяют функцию
#уменьшения относительного стандартного отклонения (RSD) и заменяет точки на запятые.

from simple import rando
from average import average
from rsd import relstdev
#Импорт функций создания списка случайных чисел и уменьшения RSD.

def randorator(t_mini, t_maxi, t_n, t_mean, t_rsd, punctuation, t_round):
#Функция принимает текстовые значения нижней и верхней границ интервала, количества чисел,
#среднего значения, максимально допустимого RSD, количество знаков после запятой
#и числовое значение, указывающее знак препинания в экспортируемых числах.

    def punctu(txt):
        return(float(txt.replace(",", ".")))
#Функция принимает текстовое значение и возвращает число с точкой. Для обработки введённых данных.

    matrix = []
    text = ""
    if t_mini == "":
        mini = 0
    else:
        mini = punctu(t_mini)
    if t_maxi == "":
        maxi = 0
    else:
        maxi = punctu(t_maxi)
    if t_n == "":
        n = 1
    else:
        n = int(t_n)
    m = n - 1
    fromzeroton = xrange(n)
    fromzerotom = xrange(m)
    if t_round == "":
        rounding = -1
    else:
        rounding = int(t_round)
#Создаётся пустой список и текст. Обрабатываются числовые параметры.
#Вычисляется удобное число m. Создаются удобные списки.

    if t_mean == "":
        matrix = rando(mini, maxi, fromzeroton)
    else:
        mean = punctu(t_mean)
        matrix = average(mini, maxi, n, mean, m, fromzerotom)
#Выбор и применение функции создание списка чисел в зависимости от того, задано ли среднее значение.
        
    if t_rsd != "":
        if t_mean == "":
            mean = sum(matrix) / n
        matrix = relstdev(matrix, n, mean, punctu(t_rsd), fromzeroton)
#Если требуется, уменьшается RSD.
    
    for i in fromzerotom:
        if rounding != -1:
            matrix[i] = round(matrix[i], rounding)
        text += str(matrix[i]) + "\n"
    if rounding != -1:
        matrix[m] = round(matrix[m], rounding)
    text +=  str(matrix[m])
#Список преобразуется в строку. Каждое число с красной строки. Округление при необходимости.
    
    if not punctuation:
        text = text.replace(".", ",")
#Если требуется, то точки заменяются запятыми.

    return(text)
#Возврат теста.
