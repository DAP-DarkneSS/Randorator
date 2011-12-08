#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#Основная функция. Производит выбор функции генерирования. Если требуется, применяют функцию
#уменьшения относительного стандартного отклонения (RSD), округляет и заменяет точки на запятые.

from simple import rando
from average import average
from rsd import relstdev
#Импорт функций создания списка случайных чисел и уменьшения RSD.

def randorator(t_mini, t_maxi, t_n, t_mean, t_rsd, punctuation, t_round):
#Функция принимает строковые значения нижней и верхней границ интервала, количества чисел,
#среднего значения, максимально допустимого RSD, количество знаков после запятой
#и числовое значение, указывающее знак препинания в экспортируемых числах.

    def punctu(txt):
        return(float(txt.replace(",", ".")))
#Функция принимает строковое значение и возвращает число с точкой. Для обработки введённых данных.

    def set_float_data(in_data):
        out_data = 0
        if in_data != "":
            out_data = punctu(in_data)
        return(out_data)
#Функция принимает строковое значение и возвращает число с точкой или 0,
#если строка пустая. Для обработки введённых данных.

    def set_int_data(in_data, out_data):
        if in_data != "":
            out_data = int(in_data)
        return(out_data)
#Функция принимает строковое значение и число, возвращает целое число
#или второе число, если строка пустая. Для обработки введённых данных.

    def to_text(in_data, rounding):
        if rounding >= 0:
            in_data = round(in_data, rounding)
            out_data = str(in_data)
            out_data += "0" * (rounding - len(out_data) + out_data.find(".") + 1)
        else:
            out_data = str(in_data)
        if rounding == 0:
            out_data = out_data.replace(".0", "")
        return(out_data)
#Число преобразуется в строку, если необходимо, округляется с добавлением нулей.
#У числа, округлённого до целой части, отбрасывается ".0".

    matrix = []
    text = ""
    mini = set_float_data(t_mini)
    maxi = set_float_data(t_maxi)
    n = set_int_data(t_n, 1)
    rounding = set_int_data(t_round, -1)
    m = n - 1
    fromzeroton = xrange(n)
    fromzerotom = xrange(m)
#Создаётся пустой список и текст. Обрабатываются числовые параметры.
#Вычисляется удобное число m. Создаются удобные списки.

    if t_mean == "":
        matrix = rando(mini, maxi, fromzeroton)
    else:
        mean = punctu(t_mean)
        matrix = average(mini, maxi, n, mean, m, fromzerotom)
#Выбор и применение функции создание списка чисел в зависимости от того, задано ли среднее значение.
        
    if (t_rsd != "") and (n > 1):
        if t_mean == "":
            mean = sum(matrix) / n
        matrix = relstdev(matrix, n, mean, punctu(t_rsd), fromzeroton)
#Если требуется, уменьшается RSD.
    
    for i in fromzerotom:
        text += to_text(matrix[i], rounding) + "\n"
    text +=  to_text(matrix[m], rounding)
#Список преобразуется в текст. Каждое число с красной строки. Округление при необходимости.
    
    if not punctuation:
        text = text.replace(".", ",")
#Если требуется, то точки заменяются запятыми.

    return(text)
#Возврат текста.
