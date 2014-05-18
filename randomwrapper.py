#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programming language and character encoding setting.

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

#=============================|Module_Wrapper|==============================#

def checkThemAll():

    try:
        if urlopen("http://www.random.org/", timeout = 0.3).getcode() < 400:
            from thirdparty.randomapi import RandomJSONRPC
            from base64 import b64decode
            TrueServer = RandomJSONRPC(b64decode("NTdiYTBlOGEtOWI3OC00OTc1LWEwNjktMTM5NjFiZDgwY2I0"))
# If response of random.org is OK, RandomJSONRPC will be imported
# RandomJSONRPC is licenced under MIT license. The creator is
# Mitchell Cohen. See more at http://github.com/mitchchn/randomapi

            TrueInfo = TrueServer.get_usage()
            print(str(TrueInfo["bitsLeft"]) + " bits and " + str(TrueInfo["requestsLeft"]) + " requests of random.org left over.")
# Here it is an announcement of the random.org quota left over.

            if (TrueInfo["bitsLeft"] * TrueInfo["requestsLeft"]) < 9:
                TrueServer = False
# If the site quota disallows using it, RandomJSONRPC will not be returned.

        else:
            TrueServer = False
    except (URLError, HTTPError, ValueError, error):
# URLError and HTTPError are Internet connection errors.
# ValueError is generated when random.org is substituted by another site.
# Socket error seems to be a pyinstaller or/and wine issue.
        TrueServer = False
    print("True Randoration is " + str(TrueServer) + ".")
    return(TrueServer)
# Else RandomJSONRPC will not be returned.
# There is an announcement of the module was used.

#===========================|Functions_Wrappers|============================#

def gaussWrapped(Mean, StandardDeviation, Quantity = 1, TrueRandoration = False, Index = [0]):
# Gaußian (normal) distribution.
    OutPut = []
    if TrueRandoration:
        TrueServer = checkThemAll()
        if TrueServer:
            OutPut = TrueServer.generate_gaussians(Quantity, Mean, StandardDeviation, 17)
# Python supports not more than 16 digits after the decimal mark.
    if OutPut == []:
        from random import gauss
        for i in Index:
            OutPut.append(gauss(Mean, StandardDeviation))
    return(OutPut)

def uniformWrapped(Minimum = 0, Maximum = 1, Quantity = 1, TrueRandoration = False, Index = [0]):
# Continuous uniform distribution.
    OutPut = []
    if TrueRandoration:
        TrueServer = checkThemAll()
        if TrueServer:
            OutPut = TrueServer.generate_decimal_fractions(Quantity, 17)
# Python supports not more than 16 digits after the decimal mark.
            Delta = Maximum - Minimum
            for i in Index:
                OutPut[i] = (OutPut[i] * Delta) + Minimum
    if OutPut == []:
        from random import uniform
        for i in Index:
            OutPut.append(uniform(Minimum, Maximum))
    return(OutPut)
