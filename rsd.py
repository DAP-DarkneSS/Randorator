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

#=================================|Import|==================================#

# Square root and sign copy functions are imported.

from math import copysign, sqrt

#=============================|RSD_calculation|=============================#

# Here it is a function to calculate RSD value.

def rsd_calc(fromzeroton, matrix, mean, n, real):

    if real:
        summ = 0
        for i in fromzeroton:
            summ += ((matrix[i] - mean) ** 2)
# The summ to get true RSD value is calculated.

    else:
        deviat_cra = min((max(matrix) - mean), (min(matrix) - mean))
        summ = n * (deviat_cra ** 2)
# The summ to get maximum RSD value is calculated.

    rsd = 100 * (sqrt(summ / (n - 1))) / abs(mean)

    return(rsd)

#==============================|RSD_decreasing|=============================#

# Here it is a function to decreased matrix RSD value
# via decreasing numbers with maximum deviations by increment.

def rsd_decr(matrix, increment):

    matrix[matrix.index(max(matrix))] -= increment
    matrix[matrix.index(min(matrix))] += increment

    return(matrix)

#==============================|RSD_increasing|=============================#

# Here it is a function to increased matrix RSD value.

def rsd_incr(matrix, increment, mean, index):

    if matrix.count(mean) > 1:
        closest_min = matrix.index(mean)
        closest_mp1 = closest_min + 1
        closest_max = matrix[closest_mp1:].index(mean) + closest_mp1
# The easiest way is to decrease two numbers that are equal to mean value.

    else:
        deviat_val = []
        deviat_sig = []
        for i in index:
            if matrix[i] != mean:
                delta = matrix[i] - mean
                deviat_val.append(abs(delta))
                deviat_sig.append(copysign(1, delta))
# Values and signs of deviations are calculated and stored
# for numbers that are not equal to mean value.

            else:
                deviat_val.append(float("inf"))
                deviat_sig.append(0)
# Infinity (+∞) and zero are stored instead of
# value (zero) and sign (ill-defined) of mean value deviation.

        if matrix.count(mean) == 1:
            closest_min = matrix.index(mean)
            closest_max = deviat_val.index(min(deviat_val))
# Another easy way is to decrease a number that is equal to mean value
# and a number with minimum deviation.

        else:
            closest_min = deviat_val.index(min(deviat_val))
            closest_max = deviat_sig.index(-1 * deviat_sig[closest_min])
# The truest way is to decrease a number with absolute minimum deviation…

            for i in range((closest_max + 1), len(matrix)):
                if (deviat_sig[i] == deviat_sig[closest_max]) and (deviat_val[i] < deviat_val[closest_max]):
                    closest_max = i
# … and a number with minimum deviation and sign that differs to previous one.

    if matrix[closest_min] > matrix[closest_max]:
        closest_min, closest_max = closest_max, closest_min
# Values are swapped if needed.

    matrix[closest_min] -= increment
    matrix[closest_max] += increment
# Numbers with minimum deviations are decreased by increment.

    return(matrix)

#===============================|Coefficient|===============================#

# Here it is a function to increased the coefficient
# when decreasing is replaced by increasing or vice versa.
# This will entail the increment decreasing.

def check_k(k, ref):
    if (k[1] != 0) and (k[1] != ref):
        k[0] += 1
    k[1] = ref
    return(k)

#===================================|Gauß|===================================#

def randorateGauss(IndexList, Mean, StandardDeviation):
    from random import gauss
    OutputMatrix = []
    for i in IndexList:
        OutputMatrix.append(gauss(Mean, StandardDeviation))
    return(OutputMatrix)

#=================================|Kernel|==================================#

# Here it is a function to adjust RSD value in compliance with the criteria specified.

def relstdev(dict_val):
# Input dictionary description:
# lst_numbz — list of values,
# str_quant — quantity of values,
# str_avera — average value of numbers list,
# str_rsd_p — relative standart deviation value,
# lst_index — list of indexes of numbers list,
# log_rsd_w — is RSD value exact or limit.

    matrix = dict_val["lst_numbz"]
    op_margin = 0.1
# There is a precison of "exact" RSD value.

    if dict_val["log_rsd_w"]:
        rsd_cra = rsd_calc(None, matrix, dict_val["str_avera"], dict_val["str_quant"], False)
        rsd_max = dict_val["str_rsd_p"] * (1 + op_margin)
        rsd_min = min(dict_val["str_rsd_p"], rsd_cra) * (1 - op_margin)
# There are limits of "exact" RSD value.
# The minimum limit must be less then theoretically possible maximum RSD value.
    else:
        rsd_max = dict_val["str_rsd_p"]
        rsd_min = 0
# There are limits of "limit" RSD value.

    k = [3, 0]
    rsd = -1
# There are initial RSD and coefficient values.

    while (rsd > rsd_max) or (rsd < rsd_min):
        rsd = rsd_calc(dict_val["lst_index"], matrix, dict_val["str_avera"], dict_val["str_quant"], True)
        increment = (max(matrix) - min(matrix)) / k[0]
# RSD and increment values are calcaluted.

        if rsd > rsd_max:
            matrix = rsd_decr(matrix, increment)
            k = check_k(k, -1)

        elif rsd < rsd_min:
            matrix = rsd_incr(matrix, increment, dict_val["str_avera"], dict_val["lst_index"])
            k = check_k(k, 1)
# RSD value is adjusted if needed. Coefficient value is increased if needed.

    dict_out = {
    "lst_matrix": matrix,
    "num_rsd_q": rsd}

    return(dict_out)
# Dictionary with numbers list and rsd value is created and returned.
