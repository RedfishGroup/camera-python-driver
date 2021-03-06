#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of pydc1394.
# 
# pydc1394 is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# pydc1394 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with pydc1394.  If not, see
# <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2009, 2010 by Holger Rapp <HolgerRapp@gmx.net>
# and the pydc1394 contributors (see README File)


from distutils.core import setup

setup(
    name="pydc1394",
    version="1.0b",
    description="A Pythonic Wrapper around libdc1394 V2",
    author = "Holger Rapp",
    author_email = "sirver@users.sf.net",
    url="https://launchpad.net/pydc1394",

    packages = [ "pydc1394", "pydc1394.ui", "pydc1394.ui.qt", "pydc1394.ui.wx" ],
)

