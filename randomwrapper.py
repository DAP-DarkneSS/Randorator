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

from urllib2 import urlopen
from thirdparty.randomdotorg import RandomDotOrg
# A site opening function and a true random generation module are imported.

#=============================|Module_Wrapper|==============================#

if (urlopen("http://www.random.org/").getcode() < 400) and (RandomDotOrg().get_quota() > 15):
    wrapper = RandomDotOrg()
# If response of random.org is OK and if the site quota allows using it
# the wrapper will became a synonym of the true random generation module.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/

else:
    import random
    wrapper = random
# Else a pseudorandom generation module will be imported
# and the wrapper will became it's synonym.

#===========================|Functions_Wrappers|============================#

def random():
    return(wrapper.random())

def shuffle(matrix):
    return(wrapper.shuffle(matrix))
    
def triangular(mini, maxi, mean):
    return(wrapper.triangular(mini, maxi, mean))
    
def uniform(mini, maxi):
    return(wrapper.uniform(mini, maxi))
# Some functions are wrapped.
