#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

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

#=================================|Import|==================================#

# Here it is a simple wrapper to use some random functions transparently.

from urllib2 import urlopen, URLError
from thirdparty.randomdotorg import RandomDotOrg
import random
# A site opening function and true and pseudorandom random generation modules are imported.

#=============================|Module_Wrapper|==============================#

def checkthemall():
    try:
        if (urlopen("http://www.random.org/", timeout = 0.02).getcode() < 400) and (RandomDotOrg().get_quota() > 15):
            wrapper = RandomDotOrg()
# If response of random.org is OK and if the site quota allows using it
# the wrapper will became a synonym of the true random generation module.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/

        else:
            wrapper = random
    except URLError:
        wrapper = random
    return(wrapper)
# Else the wrapper will became synonym of pseudorandom random generation module.

#===========================|Functions_Wrappers|============================#

def random():
    return(checkthemall().random())

def shuffle(matrix):
    return(checkthemall().shuffle(matrix))

def triangular(mini, maxi, mean):
    return(checkthemall().triangular(mini, maxi, mean))

def uniform(mini, maxi):
    return(checkthemall().uniform(mini, maxi))
# Some functions are wrapped.
