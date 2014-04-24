#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Указывается язык и кодировка.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2014 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

def check_icon(extension):

    from os import path
# A module to get file path is loaded.

    icon_file = "randorator." + extension
# The icon is licenced under
# CC Attribution 3.0 United States (http://creativecommons.org/licenses/by/3.0/us/).
# The author is Aha-Soft (http://www.softicons.com/free-icons/designers/aha-soft)
# http://www.softicons.com/free-icons/toolbar-icons/48x48-free-object-icons-by-aha-soft/dice-icon
    try:
        a_icofile = path.dirname(__file__) + '/' + icon_file
    except UnicodeDecodeError:
        a_icofile = ""
# There are variants of the icon file location. We have not to use
# unicode strings and we should handle an exception because of
# error with directories with non-Latin symbols in the names.

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
    elif (a_icofile != "") and (brute_icon(a_icofile)):
        ci_output = a_icofile
    else:
        ci_output = ""
# The correct icon file location is searched.

    if ci_output != "":
        try:
            message = ci_output + " was loaded."
        except UnicodeDecodeError:
            message = icon_file + " was loaded from directory with non-Latin symbols in the name."
    else:
        message = icon_file + " wasn't found :("

    print(message)
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
    from rsd import randorateGauss, relstdev, rsd_calc
# Modules to generate random numbers list are loaded.
# RSD adjusting and calculating modules are loaded.
    from math import log, copysign
# Logarithm counting and sign copy functions are loaded.

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

    def check_limits(limits_add, str_avera, n, mini, maxi, mean):
        dict_check = {}
        limits_n = len(limits_add)
        dict_check["log_avera"] = False
        if str_avera != "":
            if n > limits_n:
                mean = ((mean * n) - sum(limits_add)) / (n - limits_n)
# The mean value should be corrected.

                dict_check["num_avera"] = mean
                if maxi > mean > mini:
                    dict_check["log_avera"] = True
                    dict_check["str_error"] = u""
# New average value should be checked.

            if not dict_check["log_avera"]:
                dict_check["str_error"] = u"Несовместимые параметры: количество, среднее, включение интервалов!"
        dict_check["num_quant"] = max(0, (n - limits_n))
        return(dict_check)
# Here it is a funcion to transform input value in according
# to correspond with interval limit(s) marked to be added.

    def parse_sortm(str_sortm):
        lst_sortm_in = str_sortm.split()
# The string is splitted by spaces into strings list.

        lst_sortm_out = []
        for i in lst_sortm_in:
            if u"-" in i:
# A substring with a dash should be transformed.

                n = i.split(u"-")
                n0 = int(n[0])
                n1 = int(n[1])
                k = range(n0, n1, (int(copysign(1, (n1 - n0))))) + [n1]
# Also we should add right interval limit to the range.

                lst_sortm_out += k
            else:
                lst_sortm_out.append(int(i))
        return(lst_sortm_out)
# Here it is a function to parse input string with setted sorting mode.

    def do_sortm(lst_numbz_in, str_sortm):
        lst_sortm = parse_sortm(str_sortm)
        lst_numbz_out = []
        lst_numbz_in.sort()
        for i in lst_sortm:
            lst_numbz_out.append(lst_numbz_in[i - 1])
        return(lst_numbz_out)
# Here it is a function to apply setted sorting mode.

    matrix = []
    errorz = []
    dict_txt  = {
    "str_numbz": u"",
    "str_infoz": u""}
    mini = set_float_data(dict_val["str_minim"])
    maxi = set_float_data(dict_val["str_maxim"])
    if (dict_val["str_avera"] != ""):
        mean = punctu(dict_val["str_avera"])
    n = set_int_data(dict_val["str_quant"], 1)
    rounding = set_int_data(dict_val["str_round"], -1)

    limits_add = []
    if dict_val["log_min_v"]:
        limits_add.append(mini)
    if dict_val["log_max_v"]:
        limits_add.append(maxi)
# Here it is a list with interval limit(s) marked to be added.

    if mini > maxi:
        maxi, mini = mini, maxi
        errorz.append(u"Минимальное значение больше максимального!")
#Если при вводе были перепутаны границы, то они меняются местами.
#Запись соответствующего сообщения об ошибке.

    if dict_val["str_avera"] != "":

        if dict_val["str_minim"] == "":
            if mean > 0:
                mini = 0
            else:
                mini = 10 * mean
            if (mean == 0) and (dict_val["str_maxim"] != ""):
                mini = -1 * maxi
        if dict_val["str_maxim"] == "":
            if mean > 0:
                maxi = 10 * mean
            else:
                maxi = 0
            if (mean == 0) and (dict_val["str_minim"] != ""):
                maxi = -1 * mini
# If a limit value isn't set but an average value is set
# the limit will be calculated according to the average.

        if (maxi > mean > mini):
            average_used = True
        else:
            errorz.append(u"Среднее значение вне заданного диапазона!")
            average_used = False
            print(u"Average value was selected but couldn't be randorated.")
    else:
        average_used = False
        print(u"Average value wasn't selected.")
# The existence and the possibility of use of average value is checked.
#Запись соответствующего сообщения об ошибке.

    if limits_add != []:
        if average_used:
            dict_check = check_limits(limits_add, dict_val["str_avera"], n, mini, maxi, mean)
            average_used = dict_check["log_avera"]
            if average_used:
                mean = dict_check["num_avera"]
            if dict_check["str_error"] != u"":
                errorz.append(dict_check["str_error"])
        else:
            dict_check = check_limits(limits_add, "", n, mini, maxi, None)
        n = dict_check["num_quant"]

    m = n - 1
    fromzeroton = xrange(n)
    fromzerotom = xrange(m)
#Создаются пустые списки и текст. Обрабатываются числовые параметры.
#Вычисляется удобное число m. Создаются удобные списки.

    rsd_used = False
    rsd_used2 = False
    if dict_val["str_rsd_p"] != "":
        if (not dict_val["log_max_v"]) and (not dict_val["log_min_v"]):
# RSD adjustment with maximum or minimum included to the output isn't implemented.

            if n > 1:
                if (mini * maxi >= 0):
                    rsd = punctu(dict_val["str_rsd_p"])
                    if not average_used:
                        mean = (mini + maxi) / 2
                    if mean != 0:
                        if rsd > 0:
                            rsd_used = True
                            if dict_val["log_rsd_w"]:
                                matrix = randorateGauss(fromzeroton, mean, (mean * rsd / 100))
                                print(u"RSD value was selected and randorated.")
                                rsd_used2 = True
                                if dict_val["log_algor"]:
                                    errorz.append(u"No true random if precise RSD value!")
# rsd_used2 indicates if matrix has been already randorated.
# rsd_used indicates if rsd algorithms will be used at all.
                        else:
                            errorz.append(u"RSD должно быть больше 0!")
                            print(u"RSD value was selected but couldn't be randorated.")
                else:
                    errorz.append(u"RSD не может быть рассчитано для интервала, включающего 0!")
                    print(u"RSD value was selected but couldn't be randorated.")
            else:
                errorz.append(u"RSD не может быть рассчитано менее чем для двух чисел!")
                print(u"RSD value was selected but couldn't be randorated.")

        else:
            errorz.append(u"Оптимизация по RSD отключена при добавлении границы интервала!")
            print(u"RSD value was selected but couldn't be randorated.")
# If fixed RSD value is set and can be used Gauß distribution will be randorated.

    if (not rsd_used2):
        if average_used:
            matrix = average(mini, maxi, n, mean, m, fromzerotom, dict_val["log_algor"])
            print(u"Average value was selected and randorated.")
        else:
            matrix = rando(mini, maxi, fromzeroton, dict_val["log_algor"])

    if rsd_used:
        if not average_used:
            mean = sum(matrix) / n
        dict_torsd = {
            "lst_numbz": matrix,
            "str_quant": n,
            "str_avera": mean,
            "str_rsd_p": rsd,
            "lst_index": fromzeroton,
            "log_rsd_w": dict_val["log_rsd_w"]}
        dict_rsd = relstdev(dict_torsd)
        rsd_used = True
# RSD value is adjusted.

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

    if dict_val["log_rsd_a"]:
        rsd_out = [False, None]

        if rsd_used:
            rsd_out = [True, dict_rsd["num_rsd_q"]]
# Use calculated RSD value when it exists.

        else:
            if (n > 1) and (mini * maxi >= 0):
                if not average_used:
                    mean = sum(matrix) / n
                if mean != 0:
                    rsd_out = [True, rsd_calc(fromzeroton, matrix, mean, n, True)]
# Or calculate it if it is possible.

            else:
                errorz.append(u"Невозможно рассчитать RSD!")
                print(u"RSD couldn't be calculated.")

        if rsd_out[0]:
            dict_txt["str_infoz"] += u"RSD, % = " + str(rsd_out[1])
# If RSD is requested to show and could be get it will be outputed.
# NOTE I don't really understand why this code is required but it is:
            if ((errorz != []) and (dict_val["log_verbo"])):
                dict_txt["str_infoz"] = "\n" + dict_txt["str_infoz"]
            else:
                dict_txt["str_infoz"] = dict_txt["str_infoz"] + "\n"
# End of NOTE

    if dict_val["log_verbo"] and (errorz != []):
        TempList = []
        for i in xrange(len(errorz)):
            TempList.append(errorz[i])
            TempList.append("\n")
        dict_txt["str_infoz"] = dict_txt["str_infoz"].join(TempList)
#Если задано, и ошибки есть, они переносятся в текст.

    if matrix != []:
        n = len(matrix)
        m = n - 1
        fromzerotom = xrange(m)
# Proper values are restored.

        if dict_val["str_sortm"] != u"":
            if dict_val["str_sortm"] == u"1-":
                matrix.sort()
            elif dict_val["str_sortm"] == u"-1":
                matrix.sort()
                matrix.reverse()
            else:
                try:
                    matrix = do_sortm(matrix, dict_val["str_sortm"])
                except (IndexError, ValueError, UnicodeEncodeError):
                    dict_txt["str_infoz"] += u"Некорректный режим сортировки!" + "\n"
        else:
            if n > 2:
                shuffle(matrix)
        TempList = []
        for i in fromzerotom:
            TempList.append(to_text(matrix[i], rounding))
            TempList.append("\n")
        if m >= 0:
            TempList.append(to_text(matrix[m], rounding))
        dict_txt["str_numbz"] = dict_txt["str_numbz"].join(TempList)
#Cписок c количеством элементов больше 3 перемешивается и преобразуется в текст.
#Каждое число с красной строки. Округление при необходимости.
    
    if not dict_val["log_punct"]:
        dict_txt["str_numbz"] = dict_txt["str_numbz"].replace(".", ",")
#Если требуется, то точки заменяются запятыми.

    return(dict_txt)
#Возврат текста.

#================================|Direct_Run|===============================#

if __name__ == '__main__':
# Проверка, запускается ли файл как самостоятельное приложение.

    from i18n.locator import locale
    from randorator import Settingz

    def my_input(LocaleID, DefaultValue):
        if DefaultValue ==  u"":
            print(locale(LocaleID, Settingz["str_langu"]))
            OutputValue = raw_input()
        else:
            OutputValue = DefaultValue
        return(OutputValue)

    dict_val = {
    "str_minim": "",
    "str_maxim": "",
    "str_quant": "",
    "str_avera": "",
    "str_rsd_p": "",
    "str_round": "",
    "log_punct": False,
    "log_verbo": False,
    "log_algor": False,
    "log_min_v": False,
    "log_max_v": False,
    "log_rsd_a": True,
    "log_rsd_w": False,
    "str_sortm": ""}
# Here it is a blank dictionary with almost all output values.
        
    print(locale(u"ui_about", Settingz["str_langu"]) + u"\n")
    print u"Please press Enter after option typed, blank values are allowed.\n"

    dict_val["str_minim"] = my_input(u"ui_minim", Settingz["str_minim"])
    dict_val["str_maxim"] = my_input(u"ui_maxim", Settingz["str_maxim"])
    dict_val["str_quant"] = my_input(u"ui_quant", Settingz["str_quant"])
    dict_val["str_avera"] = my_input(u"ui_avera", Settingz["str_avera"])
    dict_val["str_rsd_p"] = my_input(u"ui_rsd_p", Settingz["str_rsd_p"])
    dict_val["str_round"] = my_input(u"ui_round", Settingz["str_round"])
    dict_val["str_sortm"] = my_input(u"ui_sortm", Settingz["str_round"])
# Импорт параметров.

    dict_val["log_punct"] = Settingz["log_punct"]
    dict_val["log_algor"] = Settingz["log_algor"]
    dict_val["log_min_v"] = Settingz["log_min_v"]
    dict_val["log_max_v"] = Settingz["log_max_v"]
    dict_val["log_rsd_a"] = Settingz["log_rsd_a"]
    dict_val["log_rsd_w"] = Settingz["log_rsd_w"]
# Logical data are refined.

    while True:
        dict_out = randorator(dict_val)
        print(u"\nСгенерировано:\n" + dict_out["str_infoz"] + dict_out["str_numbz"])
# Вход в бесконечный цикл, получение снегерированных данных.

        try:
            print(u"\nEnter to regenerate. Ctrl+C to exit.")
            raw_input()
# При любом вводе цикл возвращается в начало.

        except KeyboardInterrupt:
            print "\n\n\tBye!\n"
            quit()
# В случае клавиатурного прерывания программа завершается.
