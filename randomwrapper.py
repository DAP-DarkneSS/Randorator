#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Указывается язык и кодировка.

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

# Вызывается модуль истинно случаных чисел, если http://www.random.org/
# доступен, и квота не исчерпана. Иначе вызывается модуль псевдослучайных чисел.

from urllib2 import urlopen
from thirdparty.randomdotorg import RandomDotOrg

if (urlopen("http://www.random.org/").getcode() < 400) and (RandomDotOrg().get_quota() > 0):
    wrapper = RandomDotOrg()
else:
    import random
    wrapper = random
    
def random():
    return(wrapper.random())

def shuffle(matrix):
    return(wrapper.shuffle(matrix))
    
def triangular(mini, maxi, mean):
    return(triangular(mini, maxi, mean))
    
def uniform(mini, maxi):
    return(wrapper.uniform(mini, maxi))