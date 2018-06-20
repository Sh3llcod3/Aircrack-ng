#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   manage_wordlists.py - Download, store, create and delete wordlists.
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
#Import our custom module
from modules import *
#Create our 'wordlist' class
class wordlistObj(object):
    globalWordlistMap = {}
    #Add init method and set attributes.
    def __init__(self, colorsClass):
        self.colorsClass = colorsClass
        self.globalDirPath = "~/.airscriptNG/wordlists/"
        self.listName = []
        self.listPath = []
        self.fetchListMethod = []
        self.chosenList = None
        self.downloadProceedure = None
        self.listIsInstalled = None
        self.localDiskPath = None
    #Add the names to the name list
    def addName(self, wordlistName):
        self.listName.append(wordlistName)
    #Add the wordlist local-disk paths
    def addPath(self, localPath):
        self.listPath.append(self.globalDirPath + localPath)
    #Add the instructions to download it online.
    def addMethod(self, downloadInstructions):
        self.fetchListMethod.append(downloadInstructions)
    #Check if list is present.
    def verifyPresence(self, locationToCheck):
        if bashReturnValue("ls {}".format(locationToCheck)) == "0":
            return True
        else:
            return False
    #Add the values to the global class dictionary
    def commitList(self):
        for i in enumerate(zip(self.listName, self.listPath, self.fetchListMethod), start=1):
            tempValList = list(i[1])
            tempValList.append(self.verifyPresence(tempValList[1]))
            wordlistObj.globalWordlistMap[i[0]] = tempValList
    #Fetch the list, by simply running the download instructions
    def downloadList(self):
        if connActive():
            bashRun(self.downloadProceedure)
        elif not hasattr(self, "TriedWaiting"):
            sysWrite("\n")
            printYellow(self.colorsClass, "Internet connection not found...\n")
            for i in range(10,0,-1):
                sysWrite("Sleeping for {} seconds before retrying \r".format(i))
                passTime(1)
            self.TriedWaiting = True
            clearTerm()
            self.downloadList()
        else:
            sysWrite("\n")
            printRed(self.colorsClass, "Waited, but no connection was found. Quitting...")
            normalQuit(1)
    #Delete the wordlists folder
    def deleteFolder(self):
        bashRun("rm -rf {} 2>/dev/null".format(self.globalDirPath))
    #Create the wordlists folder
    def createFolder(self):
        bashRun("mkdir -p {}".format(self.globalDirPath))
    #Give user option to choose wordlist of their preference
    def chooseList(self):
        COLOR = self.colorsClass
        clearTerm()
        printInfo(COLOR, "Viewing all available wordlists: \n")
        defineColor = lambda x: returnGreenDeep(COLOR, "Yes") if x else returnRedDeep(COLOR, "No")
        for i in wordlistObj.globalWordlistMap.items():
            installState = returnYellowDeep(COLOR, " Cached: ") + "{}".format(defineColor(i[1][-1]))
            print(returnRed(COLOR, i[0]) + ") " + returnBlueDeep(COLOR, i[1][0]) + installState)
        while True:
            try:
                askUserWordlist = int(input(returnGreenDeep(COLOR, "\nWhich wordlist would you like to use? $ ")))
                if askUserWordlist in wordlistObj.globalWordlistMap.keys():
                    self.chosenList = wordlistObj.globalWordlistMap[askUserWordlist][0]
                    self.downloadProceedure = wordlistObj.globalWordlistMap[askUserWordlist][2]
                    self.listIsInstalled = wordlistObj.globalWordlistMap[askUserWordlist][-1]
                    self.localDiskPath = wordlistObj.globalWordlistMap[askUserWordlist][1]
                    if yesNo("Confirm use: {}?".format(self.chosenList[:-1]), COLOR):
                        break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid wordlist selected, please try again.")
                continue
        if not self.listIsInstalled:
            self.createFolder()
            self.downloadList()
        return self.localDiskPath