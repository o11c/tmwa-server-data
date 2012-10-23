#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##    _news.py - news backend
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

from __future__ import print_function, division

import sys
import os

from abc import ABCMeta, abstractmethod

from _news_colors import *

class Entry(object):
    __slots__ = ('sink', 'title', 'date', 'author')
    def __init__(self, sink, title, date, author):
        self.sink = sink
        self.title = title
        self.date = date
        self.author = author

    def __enter__(self):
        self.sink.begin_entry(title=self.title, date=self.date, author=self.author)
        return self

    def __exit__(self, type, value, trace):
        self.sink.end_entry(title=self.title, date=self.date, author=self.author)

class Paragraph(object):
    __slots__ = ('sink',)
    def __init__(self, sink):
        self.sink = sink

    def __enter__(self):
        self.sink.begin_paragraph()

    def __exit__(self, type, value, trace):
        self.sink.end_paragraph()

class StackedColor(object):
    __slots__ = ('sink', 'color')
    def __init__(self, sink, color):
        self.sink = sink
        self.color = color

    def __enter__(self):
        self.sink.begin_color(color=self.color)

    def __exit__(self, type, value, trace):
        self.sink.end_color(color=self.color)

class BaseSink(object):
    __slots__ = ('out')
    __metaclass__ = ABCMeta
    def __init__(self, stream):
        self.out = stream

    def entry(self, **kwargs):
        return Entry(self, **kwargs)

    @abstractmethod
    def begin_entry(self, title, date, author):
        pass

    @abstractmethod
    def end_entry(self, title, date, author):
        pass

    def p(self):
        return Paragraph(self)

    @abstractmethod
    def begin_paragraph(self):
        pass

    @abstractmethod
    def end_paragraph(self):
        pass

    def color(self, color):
        return StackedColor(self, color=color)

    @abstractmethod
    def begin_color(self, color):
        pass

    @abstractmethod
    def end_color(self, color):
        pass

    @abstractmethod
    def link(self, url, text):
        pass

class TxtSink(BaseSink):
    __slots__ = ('colors', 'column', 'next')
    def __init__(self, *args, **kwargs):
        BaseSink.__init__(self, *args, **kwargs)
        self.colors = [BLACK.txt]
        self.column = 0
        self.next = ''

    def _w(self, chars):
        if self.next != '':
            self.out.write(self.next)
            self.next = ''
        self.out.write(chars)

    def _p(self, chars):
        self.column += len(chars)
        self._w(chars)

    def _n(self):
        self.out.write('\n')
        self.next = self.colors[-1]
        self.column = 0

    def begin_entry(self, title, date, author):
        with self.color(BLUE):
            self.l(date)
        self.l(title)
        self.l('')

    def begin_paragraph(self):
        pass

    def c(self, chars, WRAP=60):
        """ This method assumes that all words are shorter than WRAP
        """
        if not self.column:
            # pad from the initial color change
            # also the reason for [i:] instead of [i+1:] below
            chars = ' ' + chars
        avail = WRAP - self.column
        if len(chars) <= avail:
            self._p(chars)
            return

        i = chars[:avail].rfind(' ')
        if i != -1:
            self._w(chars[:i])
            chars = chars[i:]
        else:
            chars = ' ' + chars
        self._n()

        while len(chars) > WRAP:
            i = chars[:WRAP].rindex(' ')
            self._w(chars[:i])
            self._n()
            chars = chars[i:]
        self._p(chars)

    def l(self, chars):
        self.c(' '.join(l.strip() for l in chars.split('\n')))
        self._n()

    def end_paragraph(self):
        self.l('')

    def end_entry(self, title, date, author):
        # avoid counting columns, since we're doing our own newline
        self._w(' - %s' % author)
        # not self._w - skip the color prefix
        self.out.write('\n \n')

    def begin_color(self, color):
        self.colors.append(color.txt)
        self.next = self.colors[-1]

    def end_color(self, color):
        self.colors.pop()
        self.next = self.colors[-1]

    def link(self, url, text=None):
        with self.color(BLUE):
            if (not text) or text == url:
                self.c(url)
            else:
                self.c('%s (%s)' % (text, url))
