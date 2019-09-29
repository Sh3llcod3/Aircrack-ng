#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   manage_interfaces.py - Take full manual control of the systems wireless interfaces.
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
#Create our 'interface' class
class interfaceObj(object):
    def __init__(self,colors):
        self.colors = colors
        self.currentCard = None
    #Display the logo
    def showLogo(self):
        #This wasn't done by hand.
        #Some quick base64 + list comprehension + some print statements!
        interfacesLogo = ("CuKWiOKWiOKVl+KWiOKWiOKWiOKVlyAgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWi"
        "OKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiO"
        "KWiOKWiOKVlyDilojilojilojilojilojilojilojilZcg4paI4paI4paI4paI4pa"
        "I4pWXICDilojilojilojilojilojilojilZfilojilojilojilojilojilojiloji"
        "lZfilojilojilojilojilojilojilojilZcK4paI4paI4pWR4paI4paI4paI4paI4"
        "pWXICDilojilojilZHilZrilZDilZDilojilojilZTilZDilZDilZ3ilojilojilZ"
        "TilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZT"
        "ilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZTi"
        "lZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTil"
        "ZDilZDilZDilZDilZ0K4paI4paI4pWR4paI4paI4pWU4paI4paI4pWXIOKWiOKWiO"
        "KVkSAgIOKWiOKWiOKVkSAgIOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4pa"
        "I4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4pWXICDilojilojilojilojiloji"
        "lojilojilZHilojilojilZEgICAgIOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4"
        "paI4paI4paI4paI4paI4pWXCuKWiOKWiOKVkeKWiOKWiOKVkeKVmuKWiOKWiOKVl+"
        "KWiOKWiOKVkSAgIOKWiOKWiOKVkSAgIOKWiOKWiOKVlOKVkOKVkOKVnSAg4paI4pa"
        "I4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWdICDilojilojilZTi"
        "lZDilZDilojilojilZHilojilojilZEgICAgIOKWiOKWiOKVlOKVkOKVkOKVnSAg4"
        "pWa4pWQ4pWQ4pWQ4pWQ4paI4paI4pWRCuKWiOKWiOKVkeKWiOKWiOKVkSDilZrilo"
        "jilojilojilojilZEgICDilojilojilZEgICDilojilojilojilojilojilojiloj"
        "ilZfilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVkSAgICAg4paI4paI4pWRICDi"
        "lojilojilZHilZrilojilojilojilojilojilojilZfilojilojilojilojilojil"
        "ojilojilZfilojilojilojilojilojilojilojilZEK4pWa4pWQ4pWd4pWa4pWQ4p"
        "WdICDilZrilZDilZDilZDilZ0gICDilZrilZDilZ0gICDilZrilZDilZDilZDilZD"
        "ilZDilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVnSAgICAg4pWa4pWQ"
        "4pWdICDilZrilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWQ4"
        "pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdCg==")
        interfacesLogo = b64D(interfacesLogo)
        print(interfacesLogo)
        startupInfo = returnGreenDeep(self.colors,"Developed by Sh3llCod3, Using airmon-ng, iproute2 and net-tools. 2017-2018.")
        printInfo(self.colors,startupInfo)
    #Display the menu
    def displayMenu(self):
        COLORS = self.colors
        clearTerm()
        self.showLogo()
        if self.currentCard is not None:
            self.updateState()
            createNewLine()
            print(returnBlueDeep(COLORS, "-"*25 + "CARD STATS" + "-"*25))
            createNewLine()
            print(returnRedDeep(COLORS, " CARD NAME    : {}".format(
                COLORS.green + self.currentCard
            )))
            print(returnRedDeep(COLORS, " CARD CHIPSET : {}".format(
                COLORS.green + self.currentChipset
            )))
            print(returnRedDeep(COLORS, " CARD STATUS  : {}".format(
                COLORS.green + self.currentState
            )))
            print(returnRedDeep(COLORS, " CARD STATE   : {}".format(
                COLORS.green + getInterfaceState(self.currentCard)
            )))
        createNewLine()
        print(returnYellowDeep(COLORS, "-"*24 + "MENU OPTIONS" + "-"*24))
        menuOptionsList = \
        [
            ["Select a card", self.selectCurrentCard],
            ["Clear the selected card", self.clearSelectedCard],
            ["Refresh this screen", self.refreshMenu],
            ["Set card in monitor mode", self.setCardMonitor],
            ["Set card in managed more", self.setCardManaged],
            ["Set interface down", self.setCardStateDown],
            ["Set interface up", self.setCardStateUp],
            ["Set monitor mode with alternate method", self.setAlternateMonitor],
            ["Set managed more with alternate method", self.setAlternateManaged],
            ["Set interface to unmanaged", self.setCardUnmanaged],
            ["Set interface to managed", self.setManagedState],
            ["Turn off network-manager service", stopNetworkManager],
            ["Turn on network-manger service", startNetworkManager],
            ["Kill any interfering processes", self.stopInterferingProcesses],
            ["Restart the interfering processes", self.restartInterferingProcesses],
            ["Execute a bash shell", self.execBashShell],
            ["Launch an airodump-ng session", self.launchAirodumpSession],
            ["Launch a wash session", self.launchWashSession],
            ["Run a packet injection test", self.launchPacketTest],
            ["Return back to menu", self.returnToMenu]
        ]
        menuOptionsDict, menuMapDict = createDictMap(menuOptionsList)
        showDictList(menuOptionsDict, COLORS)
        lowestVal, GreatestVal = getDictRange(menuMapDict)
        menuMapDict[
            takeNumericInput(
                "{}@{}".format(getUserName(), getNodeName()),
                lowestVal,
                GreatestVal,
                COLORS)]()
    #Execute a bash shell and run commands manually
    def execBashShell(self):
        try:
            clearTerm()
            createNewLine()
            if getUid() == "0":
                printYellow(self.colors, "Warning: Bash is running as root. Be careful!")
            printYellow(self.colors, "Type 'exit' or Ctrl-D to exit.")
            createNewLine()
            bashRun("/usr/bin/env bash")
        except(KeyboardInterrupt, EOFError, Exception):
            createNewLine()
        finally:
            self.displayMenu()
    #Return to menu
    def returnToMenu(self):
        raise Exception
    #Clear the currently selected card selection.
    def clearSelectedCard(self):
        self.currentCard = None
        if self.cardSelected():
            self.cardSelection.resetCards()
            delattr(self, 'cardSelection')
    #Select a card to work with
    def selectCurrentCard(self):
        COLORS = self.colors
        clearTerm()
        self.clearSelectedCard()
        self.cardSelection = wirelessCard()
        self.cardSelection.enumerateCards()
        createNewLine()
        printBlue(COLORS, "Here are your cards:")
        createNewLine()
        self.cardSelection.listCards(COLORS)
        createNewLine()
        chosenCardNumber = takeNumericInput(
            "Select a card",
            1,
            self.cardSelection.totalCardCount,
            COLORS
        )
        self.cardSelection.chooseCard(chosenCardNumber)
        self.currentCard = self.cardSelection.cardName
        self.currentChipset = self.cardSelection.cardChipset
    #Check if card has been selected
    def cardSelected(self):
        if hasattr(self, 'cardSelection'):
            return True
        else:
            return False
    #Update the cards state
    def updateState(self):
        if self.cardSelected():
            self.currentState = getInterfaceStatus(self.currentCard)
    #Get the interfering processes
    def checkProcessConflicts(self):
        conflictingProcesses = ioStream(
            "~/.airscriptNG/air/*/scripts/airmon-ng"
            " check | awk -F ' ' {'print $1'} |"
            " grep -Eiv \"Found|If|a|PID|Process\" ").lstrip().split("\n")
        return conflictingProcesses
    #Kill any interfering processes
    def stopInterferingProcesses(self):
        interferingProcessList = []
        interferingProcessList = self.checkProcessConflicts()
        createNewLine()
        if interferingProcessList == ['']:
            printYellow(self.colors, "Error: Processes have already been stopped.")
        elif bool(interferingProcessList):
            self.processNameList = []
            for pid in interferingProcessList:
                self.processNameList.append(getProcessName(pid))
            for i in zip(interferingProcessList, self.processNameList):
                currentProcessName = i[1]
                printYellow(self.colors, "Killing Process: {} ({})".format(
                    i[0],
                    self.colors.green + currentProcessName + self.colors.endl
                ))
                bashRun("kill {} 2>/dev/null".format(i[0]))
                passTime(0.1)
        else:
            printYellow(self.colors, "Error: No conflicting processes found.")
            del interferingProcessList
            if hasattr(self, "processNameList"):
                delattr(self, "processNameList")
        createNewLine()
        input(
            returnBlue(self.colors, "[i]") + \
            " Done. Press Enter " + \
            returnRed(self.colors, ">")
        )
    #If interfering processes were stopped, restart them
    def restartInterferingProcesses(self):
        createNewLine()
        if hasattr(self, "processNameList"):
            for i in self.processNameList:
                printYellow(self.colors, "Starting Process: {}".format(i))
                bashRun("service {} start 2>/dev/null".format(i))
                passTime(0.1)
            delattr(self, "processNameList")
        else:
            printYellow(self.colors, "Error: No processes to restart.")
        createNewLine()
        input(
            returnBlue(self.colors, "[i]") + \
            " Done. Press Enter " + \
            returnRed(self.colors, ">")
        )
    #Base method for displaying errors.
    def showError(self):
        createNewLine()
        printYellow(self.colors, "Error: No cards have been selected.")
        createNewLine()
        input(
            returnBlue(self.colors, "[i]") + \
            " Press Enter to return" + \
            returnRed(self.colors, ">")
        )
    #Put card into monitor mode
    def setCardMonitor(self):
        if self.cardSelected():
            self.cardSelection.setMonitorMode()
        else:
            self.showError()
    #Put card into managed more
    def setCardManaged(self):
        if self.cardSelected():
            self.cardSelection.setManagedMode()
        else:
            self.showError()
    #Use the alternate method of putting card in monitor mode
    def setAlternateMonitor(self):
        if self.cardSelected():
            self.cardSelection.setAlternativeMonitorMode()
        else:
            self.showError()
    #Use the alternate method for putting in managed mode
    def setAlternateManaged(self):
        if self.cardSelected():
            self.cardSelection.setAlternativeManagedMode()
        else:
            self.showError()
    #Set the card interface to down
    def setCardStateDown(self):
        if self.cardSelected():
            self.cardSelection.setCardDown()
        else:
            self.showError()
    #Bring up the card interface
    def setCardStateUp(self):
        if self.cardSelected():
            self.cardSelection.setCardUp()
        else:
            self.showError()
    #Set card as unmanaged. Useful for master mode.
    def setCardUnmanaged(self):
        if self.cardSelected():
            self.cardSelection.setStateUnmanaged()
        else:
            self.showError()
    #Set card back to managed state
    def setManagedState(self):
        if self.cardSelected():
            self.cardSelection.setStateManaged()
        else:
            self.showError()
    #Re-draw the menu
    def refreshMenu(self):
        clearTerm()
    #Launch a basic airodump session
    def launchAirodumpSession(self):
        if self.cardSelected():
            try:
                bashRun("~/.airscriptNG/air/*/src/airodump-ng {}".format(
                    self.currentCard
                ))
            except(KeyboardInterrupt, EOFError):
                pass
        else:
            self.showError()
    #Launch a wash session for wps
    def launchWashSession(self):
        if self.cardSelected():
            try:
                createNewLine()
                bashRun("~/.airscriptNG/wps/*/src/wash -i {} -F".format(
                    self.currentCard
                ))
            except(KeyboardInterrupt, EOFError):
                pass
        else:
            self.showError()
    #Run the aireplay-ng packet injection test
    def launchPacketTest(self):
        if self.cardSelected():
            try:
                bashRun("~/.airscriptNG/air/*/src/aireplay-ng -9 {}".format(
                    self.currentCard
                ))
            except(KeyboardInterrupt, EOFError):
                pass
        else:
            self.showError()
