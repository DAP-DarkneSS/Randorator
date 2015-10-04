#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2015 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

# The are some tests to prevent some known bugs.

from body import randorator
# A program kernel function is imported.

#=================================|Global|==================================#

dict_def = {
"str_langu": "en",
"str_minim": "0",
"str_maxim": "9",
"str_quant": "5",
"str_avera": "",
"str_rsd_p": "",
"str_round": "",
"log_punct": True,
"log_verbo": True,
"log_algor": False,
"log_min_v": False,
"log_max_v": False,
"log_rsd_a": True,
"log_rsd_w": False,
"log_horiz": False,
"str_sortm": ""}
# Default values are set.

def test_rando(dict_in):
    dict_out = randorator(dict_in)
    print(dict_out["str_infoz"] + dict_out["str_numbz"])
# A function to transform input values into printed ootput.

tests = []
# A blank tests list is created.

#=================================|Test_1|==================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/1

def test_1():
    print u"Test #1: not (min < mean < max)."
    
    dict_1 = dict(dict_def)
# The dictionary is truly copied.
    dict_1["str_minim"] = "0"
    dict_1["str_maxim"] = "1"
    dict_1["str_avera"] = "2"

    test_rando(dict_1)

tests.append(test_1)

#=================================|Test_4|==================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/4

def test_4():
    print u"Test #4: (mean = 0) and (rsd != Nill)."
    
    dict_4 = dict(dict_def)
    dict_4["str_minim"] = "-1"
    dict_4["str_maxim"] = "1"
    dict_4["str_avera"] = "0"
    dict_4["str_rsd_p"] = "1"

    test_rando(dict_4)

tests.append(test_4)

#=================================|Test_12|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/12

def test_12():
    print u"Test #12 (at least one number should be generated): n = Nill."
    
    dict_12 = dict(dict_def)
    dict_12["str_quant"] = ""

    test_rando(dict_12)

tests.append(test_12)

#=================================|Test_24|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/24

def test_24():
    print u"Test #24 (zero rounding must work): rounding = 0."
    
    dict_24 = dict(dict_def)
    dict_24["str_round"] = "0"

    test_rando(dict_24)

tests.append(test_24)

#=================================|Test_25|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/25

def test_25():
    print u"Test #25 (rounding should be limited): rounding = 20."
    
    dict_25 = dict(dict_def)
    dict_25["str_minim"] = "0"
    dict_25["str_maxim"] = "1"
    dict_25["str_round"] = "20"

    test_rando(dict_25)

tests.append(test_25)

#=================================|Test_29|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/29

def test_29():
    print u"Test #29 (no rounding by default): rounding = Nill."
    
    dict_29 = dict(dict_def)
    dict_29["str_round"] = ""

    test_rando(dict_29)

tests.append(test_29)

#=================================|Test_30|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/30

def test_30():
    print u"Test #30: (not min < mean < max) and (n > 1) and (rsd != Nill)."
    
    dict_30 = dict(dict_def)
    dict_30["str_minim"] = "0"
    dict_30["str_maxim"] = "1"
    dict_30["str_avera"] = "1"
    dict_30["str_rsd_p"] = "1"

    test_rando(dict_30)

tests.append(test_30)

#=================================|Test_40|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/40

def test_40():
    print u"Test #40: (min and max are added) and (n = Nill) and (mean != Nill)."
    
    dict_40 = dict(dict_def)
    dict_40["str_minim"] = "0"
    dict_40["str_maxim"] = "2"
    dict_40["str_quant"] = ""
    dict_40["str_avera"] = "1"
    dict_40["log_min_v"] = True
    dict_40["log_max_v"] = True

    test_rando(dict_40)

tests.append(test_40)

#=================================|Test_48|=================================#

# https://github.com/DAP-DarkneSS/Randorator/issues/48

def test_48():
    print u"Test #48: (rsd ~ 1) and (n = 2)."

    dict_48 = dict(dict_def)
    dict_48["str_minim"] = ""
    dict_48["str_maxim"] = ""
    dict_48["str_quant"] = "2"
    dict_48["str_avera"] = "11"
    dict_48["str_rsd_p"] = "1"
    dict_48["log_rsd_w"] = True

    test_rando(dict_48)

tests.append(test_48)


#================================|Direct_Run|===============================#

if __name__ == '__main__':
    print u"Testing...\n-------\n"
    for test in tests:
        test()
        print u"-------\n"
# All tests will be run if this file is directly executed.
