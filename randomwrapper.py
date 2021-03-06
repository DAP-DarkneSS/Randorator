#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

#=================================|Copying|=================================#

# Randorator is an advanced graphical generator of random numbers.
# Copyright (C) 2011-2018 Dmitriy A. Perlow <dap.darkness@gmail.com>

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

from sys import version
# To support Python 2 & 3.
if version < '3':
    from urllib2 import urlopen, URLError, HTTPError
else:
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError
from socket import error
# A site opening function and exceptions are imported.

def truerando():
    from thirdparty.randomdotorg import RandomDotOrg
    return(RandomDotOrg())
def pseudorando():
    import random
    return(random)
# There are functions to import true and pseudorandom generation modules.

#=============================|Module_Wrapper|==============================#

def checkthemall():
    try:
        if urlopen("http://www.random.org/", timeout = 0.3).getcode() < 400:
            wrapper = truerando()
# If response of random.org is OK
# the wrapper will became a synonym of the true random generation module.
# randomdotorg is licenced under GPLv3 and/or any later. The creator is
# Clovis Fabricio. See more at http://code.google.com/p/randomdotorg/

            rorg_quota = wrapper.get_quota()
            print(str(rorg_quota) + u" of random.org quota left over.")
# Here it is an announcement of the random.org quota left over.

            if rorg_quota < 90:
                wrapper = pseudorando()
# If the site quota disallows using it the wrapper will
# became a synonym of pseudorandom random generation module.

        else:
            wrapper = pseudorando()
    except (URLError, HTTPError, ValueError, error):
# URLError and HTTPError are Internet connection errors.
# ValueError is generated when random.org is substituted by another site.
# Socket error seems to be a pyinstaller or/and wine issue.
        wrapper = pseudorando()
    print(str(wrapper) + u" was used.")
    return(wrapper)
# Else the wrapper will became synonym of pseudorandom random generation module.
# There is an announcement of the module was used.

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
