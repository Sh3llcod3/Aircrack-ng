#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   manage_inputs.py - Manage different types of inputs for Airscript-ng.
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
#Import any needed modules.
from .run_command import *
from .term_colors import printYellow, returnRed
# Create a function to handle numerical input ranges.
def takeNumericInput(inputQuestion, minimumValue, maximumValue, colorClass):
    COL = colorClass
    INPUTPROMPT = COL.green + "[+] " + COL.endl
    PS1 = COL.blue + " ~" + COL.red + "$ " + COL.endl
    while True:
        try:
            inputValue = int(input(INPUTPROMPT + inputQuestion + PS1))
            if minimumValue <= inputValue <= maximumValue:
                break
            else:
                raise ValueError
        except(ValueError):
            createNewLine()
            printYellow(COL, "Error: Please enter an integer between {} and {}.".format(
                minimumValue,
                maximumValue))
            createNewLine()
            continue
    return inputValue
#Create a function to get the numeric dictionary values
def getDictRange(inputDict):
    minVal = list(inputDict.items())[0][0]
    maxVal = list(inputDict.items())[-1][0]
    return (minVal, maxVal)
#Create function to list items from dictionary.
def showDictList(inputDict, colorClass):
    createNewLine()
    for i in inputDict.items():
        print(" (" + returnRed(colorClass, i[0]) + ") " + i[1])
    createNewLine()
#From a 2D list, return two dictionaries
def createDictMap(inputList):
    menuDict = {}
    mappingDict = {}
    for i in enumerate(inputList, start=1):
        menuDict[i[0]] = i[1][0]
        mappingDict[i[0]] = i[1][1]
    return (menuDict, mappingDict)
