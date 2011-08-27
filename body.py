#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform

def randorator(t_mini, t_maxi, t_n, t_mean, t_rsd, punctuation):
    text = ""
    mini = float(t_mini.replace(",", "."))
    maxi = float(t_maxi.replace(",", "."))
    n = int(t_n)
    mean = float(t_mean.replace(",", "."))
    rsd = float(t_rsd.replace(",", "."))

#        mini = float((entry_mini.get()).replace(",", "."))
#    maxi = float((entry_maxi.get()).replace(",", "."))
#Очистка текстового поля. Импорт минимума и максимума,
#замена запятых на точки, если необходимо.
#
#    if vcheck_punctuation.get():
#        for i in xrange((int(entry_n.get()) - 1)):
#            text_out.insert(END, str(uniform(mini, maxi))+"\n")
#        text_out.insert(END, str(uniform(mini, maxi)))
#Если не требуется вывод чисел с запятыми,
#текстовое поле заполняется случайными числами,
#каждое с новой строки. Последнее значение вставляется без перевода строки.
#
#    else:
#        for i in xrange((int(entry_n.get()) - 1)):
#            text_out.insert(END, str(uniform(mini, maxi)).replace(".", ",")+"\n")
#        text_out.insert(END, str(uniform(mini, maxi)).replace(".", ","))
#Иначе в аналогичных операциях точки заменяются на запятые.

    for i in xrange(n - 1):
        text += (str(uniform(mini, maxi)) + "\n")
    text += str(uniform(mini, maxi))
    if not punctuation:
        text = text.replace(".", ",")
    return(text)
