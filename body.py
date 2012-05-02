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
    if (t_mean != ""):
        mean = punctu(t_mean)
    n = set_int_data(t_n, 1)
    rounding = set_int_data(t_round, -1)
    m = n - 1
    fromzeroton = xrange(n)
    fromzerotom = xrange(m)
#Создаётся пустой список и текст. Обрабатываются числовые параметры.
#Вычисляется удобное число m. Создаются удобные списки.

    if mini > maxi:
        maxi, mini = mini, maxi
#Если при вводе были перепутаны границы, то они меняются местами.

    mean_ok = False
    if maxi > mean > mini:
        mean_ok = True
#Проверка среднего значения на принадлежность заданному интервалу.

    if (t_mean != "") and mean_ok:
        matrix = average(mini, maxi, n, mean, m, fromzerotom)
    else:
        matrix = rando(mini, maxi, fromzeroton)
#Выбор и применение функции создание списка чисел в зависимости от того, задано ли среднее значение.
        
    if (t_rsd != "") and (n > 1) and (mini * maxi >= 0):
        rsd = abs(punctu(t_rsd))
        if t_mean == "":
            mean = sum(matrix) / n
        if (mean != 0) and mean_ok and (rsd != 0):
            matrix = relstdev(matrix, n, mean, rsd, fromzeroton)
#Если требуется, уменьшается RSD. Задания на одно число игнорируются.
    
    for i in fromzerotom:
        text += to_text(matrix[i], rounding) + "\n"
    text +=  to_text(matrix[m], rounding)
#Список преобразуется в текст. Каждое число с красной строки. Округление при необходимости.
    
    if not punctuation:
        text = text.replace(".", ",")
#Если требуется, то точки заменяются запятыми.

    return(text)
#Возврат текста.

#================================|Direct_Run|===============================#

if __name__ == '__main__':
# Проверка, запускается ли файл как самостоятельное приложение.

    print u"Продвинутый графический генератор случайных чисел.\n"
    print u"Ввод параметров подтверждайте Enter, пустые параметры разрешены.\n"
    mini = raw_input("Минимально допустимое значение:\t\t")
    maxi = raw_input("Максимально допустимое значение:\t")
    n = raw_input("Количество генерируемых чисел:\t\t")
    mean = raw_input("Среднее значение:\t\t\t")
    rsd = raw_input("Максимальное RSD в %:\t\t\t")
    punctu = raw_input("Разделитель целой и дробной части (. или ,):\t")
    rounding = raw_input("Количество цифер после запятой:\t\t")
# Импорт параметров.

    punctuation = False
    if punctu == ".":
        punctuation = True
# Обработка параметра разделителя.

    while True:
        print u"\nСгенерировано:\n" + randorator(mini, maxi, n, mean, rsd, punctuation, rounding)
# Вход в бесконечный цикл, получение снегерированных данных.

        try:
            raw_input("\nEnter для повторной генерации. Ctrl+C для выхода.")
# При любом вводе цикл возвращается в начало.

        except KeyboardInterrupt:
            print "\n\n\tBye!\n"
            quit()
# В случае клавиатурного прерывания программа завершается.
