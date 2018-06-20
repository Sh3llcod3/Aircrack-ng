#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   term_colors.py - Enable colorised output for airscript-ng.
#    Copyright (C) 2018 Yudhajit N. (Sh3llcod3)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>
#   Contact: Please create a issue on my GitHub <https://github.com/Sh3llcod3>
#
#Define all our colors here.
class col:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endl = '\033[0m'
    bold = '\033[1m'
    uline = '\033[4m'
    blue_deep = '\033[1;34;48m'
    yellow_deep = '\033[1;33;48m'
    red_deep = '\033[1;31;48m'
    green_deep = '\033[1;32;48m'
    endl_deep = '\033[1;39;48m'
    black = '\033[0;30;48m'
    marine_blue = '\033[0;36;48m'
    yellow_dark = '\033[0;33;48m'
    black_deep = '\033[1;30;48m'
    pink_deep = '\033[1;35;48m'
    light_blue = '\033[1;36;48m'
    highlight = '\033[1;37;40m'
#If no colors are chosen, this class is used
class blank_col:
    pink = str()
    blue = str()
    green = str()
    yellow = str()
    red = str()
    endl = str()
    bold = str()
    uline = str()
    blue_deep = str()
    yellow_deep = str()
    red_deep = str()
    green_deep = str()
    endl_deep = str()
    black = str()
    marine_blue = str()
    yellow_dark = str()
    black_deep = str()
    pink_deep = str()
    light_blue = str()
    highlight = str()
#Define a few colored method presets for easy use
def printRed(classFrom,strToPrint):
    print("{}[-]{} {}".format(classFrom.red,classFrom.endl,strToPrint))
def printGreen(classFrom,strToPrint):
    print("{}[+]{} {}".format(classFrom.green_deep,classFrom.endl,strToPrint))
def printYellow(classFrom,strToPrint):
    print("{}[!]{} {}".format(classFrom.yellow,classFrom.endl,strToPrint))
def printBlue(classFrom,strToPrint):
    print("{}[i]{} {}".format(classFrom.blue,classFrom.endl,strToPrint))
def printDeepBlue(classFrom,strToPrint):
    print("{}[i]{} {}".format(classFrom.blue_deep,classFrom.endl,strToPrint))
def printInfo(classFrom,strToPrint):
    print("{}[info]{} {}".format(classFrom.yellow_deep,classFrom.endl,strToPrint))
def printSuccess(classFrom,strToPrint):
    print("{}[ok]{} {}".format(classFrom.green_deep,classFrom.endl,strToPrint))
#Define a few more presets
def returnRed(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.red,strToReturn,classFrom.endl)
def returnRedDeep(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.red_deep,strToReturn,classFrom.endl)
def returnGreen(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.green,strToReturn,classFrom.endl)
def returnGreenDeep(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.green_deep,strToReturn,classFrom.endl)
def returnBlue(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.blue,strToReturn,classFrom.endl)
def returnBlueDeep(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.blue_deep,strToReturn,classFrom.endl)
def returnYellow(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.yellow,strToReturn,classFrom.endl)
def returnYellowDeep(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.yellow_deep,strToReturn,classFrom.endl)
def returnYellowDark(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.yellow_dark,strToReturn,classFrom.endl)
def returnPink(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.pink,strToReturn,classFrom.endl)
def returnPinkDeep(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.pink_deep,strToReturn,classFrom.endl)
def returnBold(classFrom,strToReturn):
    return "{}{}{}".format(classFrom.endl_deep,strToReturn,classFrom.endl)