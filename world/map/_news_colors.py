#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##    _colors.py - colors that can be used in news
##
##    Copyright © 2012 Ben Longbons <b.r.longbons@gmail.com>
##
##    This file is part of The Mana World (Athena server)
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Color(object):
    __slots__ = ('txt', 'rgb')
    def __init__(self, txt, rgb):
        self.txt = txt
        self.rgb = rgb

BLACK  = Color(txt='##0', rgb=0x000000)
RED    = Color(txt='##1', rgb=0xff0000)
GREEN  = Color(txt='##2', rgb=0x009000)
BLUE   = Color(txt='##3', rgb=0x0000ff)
ORANGE = Color(txt='##4', rgb=0xe0980e)
YELLOW = Color(txt='##5', rgb=0xf1dc27)
PINK   = Color(txt='##6', rgb=0xff00d8)
PURPLE = Color(txt='##7', rgb=0x8415e2)
GRAY   = Color(txt='##8', rgb=0x919191)
BROWN  = Color(txt='##9', rgb=0x8e4c17)
