#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2012 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

#==================================|Icon|===================================#

# Here it is a function to find the icon file location.

def check_icon():

    from os import path
# A module to get file path is loaded.

    icon_file = u"randorator.ico"
    a_icofile = path.dirname(__file__) + u'/' + icon_file
# There are variants of the icon file location. The icon is licenced under
# CC Attribution 3.0 United States (http://creativecommons.org/licenses/by/3.0/us/).
# The author is Aha-Soft (http://www.softicons.com/free-icons/designers/aha-soft)
# http://www.softicons.com/free-icons/toolbar-icons/48x48-free-object-icons-by-aha-soft/dice-icon

    def brute_icon(icon_file):
        try:
            if open(icon_file):
                bi_output = True
        except (IOError, NameError):
            bi_output = False
        return(bi_output)
# Here it is a subfunction to check the icon file existence.

    if brute_icon(icon_file):
        ci_output = icon_file
    elif brute_icon(a_icofile):
        ci_output = a_icofile
    else:
        ci_output = ""
# The correct icon file location is searched.

    if ci_output != "":
        print(ci_output + u" was loaded.")
    else:
        print(u"Icon file wasn't found :(")
# Here it is an announcement of icon file search result.

    return(ci_output)

#=================================|Windows|=================================#

# Here it is a function to check if the program is run under windows.

def check_windows():

    from platform import system
# A module of defining the operation system is loaded.

    system_name = system()
    print('Beam me up, "' + system_name + '"!')
# Here it is an announcement of the system name.

    if system_name.endswith("Windows"):
        cw_output = True
    else:
        cw_output = False
# The function will return True if the program is run under windows.
# Or False — if not.

    return(cw_output)

#=================================|Kernel|==================================#

#Основная функция. Производит выбор функции генерирования. Если требуется, применяют функцию
#уменьшения относительного стандартного отклонения (RSD), округляет и заменяет точки на запятые.

def randorator(dict_val):
# The function gets the dictionary with input values.

    from simple import rando
    from average import average
    from rsd import relstdev
#Импорт функций создания списка случайных чисел и уменьшения RSD.
    from math import log
# Logarithm counting module is loaded.

    if dict_val["log_algor"]:
        from randomwrapper import shuffle
    else:
        from random import shuffle
# Here it is an import of a list shuffling function from the chosen module.

    def punctu(txt):
        try:
            return(float(txt.replace(",", ".")))
        except ValueError:
            return(0)
#Функция принимает строковое значение и возвращает число с точкой. Для обработки введённых данных.

    def set_float_data(in_data):
        out_data = 0
        if in_data != "":
            out_data = punctu(in_data)
        return(out_data)
#Функция принимает строковое значение и возвращает число с точкой или 0,
#если строка пустая. Для обработки введённых данных.

    def set_int_data(in_data, fallback_d):
        if in_data != "":
            try:
                out_data = int(round(abs(punctu(in_data)), 0))
            except TypeError:
                pass
        else:
            out_data = fallback_d
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

    def mean_count(mean_old, quantiny, number_to_count):
        return ((mean_old * quantiny - number_to_count) / (quantiny - 1))
# Here it is a function to correct the mean value
# when a number is set to be included to the output.

    matrix = []
    errorz = []
    text = ""
    mini = set_float_data(dict_val["str_minim"])
    maxi = set_float_data(dict_val["str_maxim"])
    if (dict_val["str_avera"] != ""):
        mean = punctu(dict_val["str_avera"])
    n = set_int_data(dict_val["str_quant"], 1)
    if dict_val["log_min_v"]:
        if (dict_val["str_avera"] != "") and (n > 1):
            mean = mean_count(mean, n, mini)
        n -= 1
    if dict_val["log_max_v"]:
        if (dict_val["str_avera"] != "") and (n > 1):
            mean = mean_count(mean, n, maxi)
        n -= 1
# The numbers quantity and the mean value will be fixed
# when maximum or minimum is set to be included to the output.

    rounding = set_int_data(dict_val["str_round"], -1)
    m = n - 1
    fromzeroton = xrange(n)
    fromzerotom = xrange(m)
#Создаются пустые списки и текст. Обрабатываются числовые параметры.
#Вычисляется удобное число m. Создаются удобные списки.

    if mini > maxi:
        maxi, mini = mini, maxi
        errorz.append(u"Минимальное значение больше максимального!")
#Если при вводе были перепутаны границы, то они меняются местами.
#Запись соответствующего сообщения об ошибке.

    if dict_val["str_avera"] != "":
        if (maxi > mean > mini):
            matrix = average(mini, maxi, n, mean, m, fromzerotom, dict_val["log_algor"])
            average_used = True
            print(u"Average value was selected and randorated.")
        else:
            matrix = rando(mini, maxi, fromzeroton, dict_val["log_algor"])
            errorz.append(u"Среднее значение вне заданного диапазона!")
            average_used = False
            print(u"Average value was selected but couldn't be randorated.")
    else:
        matrix = rando(mini, maxi, fromzeroton, dict_val["log_algor"])
        average_used = False
        print(u"Average value wasn't selected.")
#Выбор и применение функции создание списка чисел в зависимости от того, задано ли среднее значение.
#Запись соответствующего сообщения об ошибке.

    if dict_val["str_rsd_p"] != "":
        if (not dict_val["log_max_v"]) and (not dict_val["log_min_v"]):
# RSD adjustment with maximum or minimum included to the output isn't implemented.

            if n > 1:
                if (mini * maxi >= 0):
                    rsd = punctu(dict_val["str_rsd_p"])
                    if not average_used:
                        mean = sum(matrix) / n
                    if mean != 0:
                            if rsd > 0:
                                matrix = relstdev(matrix, n, mean, rsd, fromzeroton)
                            else:
                                errorz.append(u"RSD должно быть больше 0!")
                else:
                    errorz.append(u"RSD не может быть рассчитано для интервала, включающего 0!")
            else:
                errorz.append(u"RSD не может быть рассчитано менее чем для двух чисел!")

        else:
            errorz.append(u"Оптимизация по RSD отключена при добавлении границы интервала!")
#Если требуется, уменьшается RSD. Задания на одно число игнорируются.
#Запись соответствующих сообщений об ошибке.

    if dict_val["log_min_v"]:
        matrix.append(mini)
    if dict_val["log_max_v"]:
        matrix.append(maxi)
# Selected numbers are included to the output.

    if not (mini == maxi == 0):
        mini = abs(mini)
        maxi = abs(maxi)
        if mini > maxi:
            maxi, mini = mini, maxi
        if mini == 0:
            mini = maxi / 10
        elif maxi == 0:
            maxi = mini * 10
# Logarithm of nonpositive numbers couldn't be calculated!

        log_mini = log(mini, 10)
        if (log_mini > 11) or (log(maxi, 10) < -4):
            if rounding != -1:
                errorz.append(u"Округление больших и маленьких чисел не поддерживается!")
                rounding = -1
# Rounding of small and big numbers doesn't work.

        else:
            round_max = (-1 * log_mini) + 11
            if rounding > round_max:
                rounding = int(round_max)
                errorz.append(u"Не более " + str(rounding) + u" цифер после запятой!")
# If rounding is set more than the maximum value
# that could be applied the rounding is truncated.

    else:
        errorz.append(u"Кого бы поделить на ноль?")
        rounding = 0
# Here it is an easter egg ^,,^

    if dict_val["log_verbo"] and (errorz != []):
        for i in xrange(len(errorz)):
            text += errorz[i] + "\n"
#Если задано, и ошибки есть, они переносятся в текст.

    if matrix != []:
        n = len(matrix)
        m = n - 1
        fromzerotom = xrange(m)
# Proper values are restored.

        if n > 2:
            shuffle(matrix)
        for i in fromzerotom:
                text += to_text(matrix[i], rounding) + "\n"
        if m >= 0:
                text += to_text(matrix[m], rounding)
#Cписок c количеством элементов больше 3 перемешивается и преобразуется в текст.
#Каждое число с красной строки. Округление при необходимости.
    
    if not dict_val["log_punct"]:
        text = text.replace(".", ",")
#Если требуется, то точки заменяются запятыми.

    return(text)
#Возврат текста.

#================================|Direct_Run|===============================#

if __name__ == '__main__':
# Проверка, запускается ли файл как самостоятельное приложение.

    def my_input(string):
        print string
        return(raw_input())

    dict_val = {
    "str_minim": "",
    "str_maxim": "",
    "str_quant": "",
    "str_avera": "",
    "str_rsd_p": "",
    "str_round": "",
    "log_punct": False,
    "log_verbo": True,
    "log_algor": False,
    "log_min_v": False,
    "log_max_v": False}
# Here it is a blank dictionary with almost all output values.
        
    print u"Продвинутый графический генератор случайных чисел.\n"
    print u"Ввод параметров подтверждайте Enter, пустые параметры разрешены.\n"
    dict_val["str_minim"] = my_input(u"Минимально допустимое значение:")
    dict_val["str_maxim"] = my_input(u"Максимально допустимое значение:")
    dict_val["str_quant"] = my_input(u"Количество генерируемых чисел:")
    dict_val["str_avera"] = my_input(u"Среднее значение:")
    dict_val["str_rsd_p"] = my_input(u"Максимальное RSD в %:")
    punctu = my_input(u"Разделитель целой и дробной части (. или ,):")
    dict_val["str_round"] = my_input(u"Количество цифер после запятой:")
    algorithm = my_input(u"Истинно случайные числа через интернет, медленно (True[1]/False[0], 0 is default):")
# Импорт параметров.

    if punctu == ".":
        dict_val["log_punct"] = True
    if (algorithm == "True") or (algorithm == "1"):
        dict_val["log_algor"] = True
# Logical data are refined.

    while True:
        print u"\nСгенерировано:\n" + randorator(dict_val)
# Вход в бесконечный цикл, получение снегерированных данных.

        try:
            my_input(u"\nEnter для повторной генерации. Ctrl+C для выхода.")
# При любом вводе цикл возвращается в начало.

        except KeyboardInterrupt:
            print "\n\n\tBye!\n"
            quit()
# В случае клавиатурного прерывания программа завершается.
