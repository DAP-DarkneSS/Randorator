#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform

def rando(mini, maxi, n):
    matrix = []
    for i in xrange(n):
        matrix.append(uniform(mini, maxi))
    return(matrix)
#Создаётся пустой список, заполняется определённым количеством
#случайных значений из выбранного интервала и возвращается.