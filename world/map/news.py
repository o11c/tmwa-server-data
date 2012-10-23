#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##    news.py - User-edited news script
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
#from datetime import datetime

from _news import TxtSink
from _news_colors import *

for n in (TxtSink(open('news.txt', 'w')),):
    with n.entry(title='New News',
                date='October 2012',
                author='o11c'):
        with n.p():
            n.l("If you're reading this, the news is now synchronized.")
            with n.color(RED):
                n.c('This is ')
                with n.color(GREEN):
                    n.c('a test ')
                    with n.color(BLUE):
                        n.c('of nested')
                    n.c(' colors that')
                n.c(' remember the')
            n.l(' outer color.')

    with n.entry(title='Converted News',
                date='September 2012',
                author='The News Converter'):
        with n.p():
            n.l(''' Agostine is well known for his magnificent winter clothes,
                    but he always dreamed of creating something truly exquisite,
                    something noble...''')
        with n.p():
            n.l(''' An old veteran has set up camp in the caves below Hurnscald
                    after a life full of hardship and battle.''')
            n.l(''' He may be old now, but he surely didn't lose his interest
                    in the art of combat!''')

    with n.entry(title='Converted News',
                date='April/May 2012',
                author='The News Converter'):
        with n.p():
            n.l('''Strange and ominous things are going on in Kaizei.''')
            n.l(''' Many people around Nivalis have noticed White and Blue Slimes
                    around the area, which they have never seen before.''')
            n.l(''' Where do those come from? Are they dangerous?''')
            n.l(''' And why did they show up now?''')
            n.l(''' Rumors say that they originate from the snowy mountains
                    north-west of Nivalis, where the famous Sage Nikolai
                    has his residence.''')
        with n.p():
            n.l(''' Summer is coming near and it might be a good time
                    to visit the beach with your Towel and relax a while.''')
            n.l(''' Oh, you don't have a Towel?''')
            n.l(''' Well, in that case you might find someone on the beach
                    who can give you one!''')

    with n.entry(title='Two announcements to make:',
                date='March 2012',
                author='The News Converter'):
        with n.p():
            n.l(''' It seems Tulimshar is finally recovering from the impacts
                    of the great earthquake.''')
            n.l(''' Although the eastern half of the city is still closed,
                    it has become much more lively, with children playing between the houses,
                    farmers going back to their fields, reports of increased trade activity.''')
        with n.p():
            n.l(''' Surely there are lots of tasks for a young adventurer!''')
        with n.p():
            n.l(''' Near Hurnscald a bunny showed up that looks like an older version
                    of our well-known Easter Bunny.''')
            n.l(''' But what is he doing there? And where is Easter Bunny?''')

    with n.entry(title='Three pieces of news today.',
                date='2012-02-12 (ooh, what a nice date)',
                author='o11c'):
        with n.p():
            n.c('First, Mana 0.6.0 got released today. You can find it at ')
            n.link('http://manasource.org')
            n.l(', or wait for your distribution.')
        with n.p():
            n.l(''' Second, we will be completely dropping support for the old
                    TMW 0.0.29.1 client soon - unless there is further reason
                    for delay, in April 2012.''')
        with n.p():
            n.l(''' Finally, there will be a purge of accounts that have not been
                    used for over a year. This should help responsiveness
                    when logging in and choosing a character.''')

    with n.entry(title='Converted News',
                date='February 2012',
                author='The News Converter'):
        with n.p():
            n.l(''' After all the activity in Nivalis due to the Christmas time,
                    the townsfolk would like things to be quiet again.''')
            n.l(''' Unfortunately, some strange people have set up their camp
                    near the woods west of town.''')
            n.l(''' They came from their village high up in the northern snow mountains.''')
            n.l(''' What might have caused them to leave their hunting grounds
                    and come down to Nivalis?''')

    with n.entry(title='Converted News',
                date='Christmas 2011',
                author='The News Converter'):
        with n.p():
            n.l(''' Christmas is coming near and Santa and his helpers are busy
                    preparing everything for the celebration in Santa's house near Nivalis.''')
            n.l(''' But somehow... everything seems to go wrong.''')
            n.l(''' Bad luck? Or rather - malicious interference?''')
            n.l(''' It looks like someone could use your help.''')

    with n.color(BLUE):
        with n.entry(title='A Rule Correction on "No Botting"',
                    date='November 2011',
                    author='The News Converter'):
            with n.p():
                n.l(''' Previously, only activity while the user was
                        away from the keyboard was a bannable offense.''')
                n.l('''Now, any sort of automated following
                        (especially, but not only, attack-following)
                        is also covered.''')
            with n.p():
                n.l(''' If you know any of the people who left this game
                        due to the prevalence of bots that were previously
                        tolerated, please tell them it's time to return.''')
