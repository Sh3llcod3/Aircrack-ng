#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   run_command.py - Execute shell commands and manage output for airscript-ng.
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
#Import needed modules
import os
import subprocess
import sys
import time
import base64
import requests
#Define the commonly used functions
def ioStream(value):
    #I am using shell=True here as no user input will ever reach any of this.
    return subprocess.check_output('%s' %(value),shell=True).decode("utf-8").rstrip()
def bashRun(value):
    subprocess.call('%s' %(value),shell=True)
def bashReturnValue(value):
    try:
        returnBashValue = str(subprocess.check_call('%s 2>/dev/null >/dev/null' %(value),shell=True))
    except(subprocess.CalledProcessError):
        returnBashValue = '1'
    return returnBashValue
def clearTerm():
    bashRun('clear || tput clear')
def quickQuit(number=1):
    os._exit(number)
def normalQuit(exitCode=0):
    sys.exit(exitCode)
def sysWrite(strToWrite):
    sys.stdout.write(strToWrite)
    sys.stdout.flush()
def networkManagerActive():
    nmState = "systemctl is-active network-manager.service"
    nmState += " | tr -d [:space:]"
    if ioStream(nmState).lower().startswith("active"):
        return True
    else:
        return False
def startNetworkManager():
    if not networkManagerActive():
        bashRun("sudo systemctl restart NetworkManager.service")
        bashRun("sudo systemctl restart wpa_supplicant.service")
        return True
    else:
        return False
def stopNetworkManager():
    if networkManagerActive():
        bashRun("sudo systemctl stop NetworkManager.service")
        bashRun("sudo systemctl stop wpa_supplicant.service")
        return True
    else:
        return False
def passTime(timeQuantity):
    time.sleep(timeQuantity)
def connActive():
    try:
        _checkRequestsCode = requests.get("http://www.google.com").status_code
        return True
    except(requests.exceptions.ConnectionError, Exception):
        return False
    #connActiveResult = bashReturnValue("/usr/bin/env ping -c1 8.8.8.8")
    #return True if connActiveResult == "0" else False
def yesNo(questionAsked,cL):
    try:
        while True:
            inputQuestion = "{}[i]{}".format(cL.yellow_deep,cL.blue_deep)
            inputQuestion += " {}".format(questionAsked)
            inputQuestion += " {1}y{0}".format(cL.endl,cL.green_deep)
            inputQuestion += "{2}/{0}{1}n{0} {2}>>{0} ".format(cL.endl,cL.red_deep,cL.marine_blue)
            userAnswer = input(inputQuestion).lower()
            if userAnswer.startswith("y"):
                return True
            elif userAnswer.startswith("n"):
                return False
    except(KeyboardInterrupt,EOFError):
        return False
def b64D(encodedStr):
    return base64.b64decode(encodedStr.encode('utf-8')).decode('utf-8')
def createNewLine():
    sysWrite("\n")