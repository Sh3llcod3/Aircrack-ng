#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   gui_elements.py - Basic GUI elements for airscript-ng.
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
#Import gui modules
from tkinter import filedialog
from tkinter import Tk
from tkinter import messagebox
Tk().withdraw() #Don't show the root window
#Define function to pick directory
def pickDirectory():
    while True:
        dirPath = filedialog.askdirectory()
        if dirPath is None:
            continue
        elif str(dirPath) in ["()",""]:
            continue
        else:
            return str(dirPath)
#Define function to choose file
def pickFile():
    while True:
        filePath = filedialog.askopenfilename()
        if filePath is None:
            continue
        elif str(filePath) in ["()",""]:
            continue
        else:
            return str(filePath)
#Define function to ask yes/no question
def pickYesOrNo(windowTitle,windowText):
    return messagebox.askyesno(windowTitle,windowText)
#Define function to ask retry/cancel question
def pickRetryOrCancel(windowTitle,windowText):
    return messagebox.askretrycancel(windowTitle,windowText)
#Define function to ask ok/cancel question
def pickOkOrCancel(windowTitle,windowText):
    return messagebox.askokcancel(windowTitle,windowText)