#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   crack_handshake.py - Resolve PSK from handshake capture file.
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
import base64
#Import our custom modules
from modules import *
from .manage_wordlists import *
#Create our 'cap' class
class capObj(object):
    def __init__(self, colors, capFile=None, wordList=None):
        self.colors = colors
        self.aircrackPath = "~/.airscriptNG/air/*/src/aircrack-ng"
        self.hashcatFolder = "~/.airscriptNG/gpu/"
        self.hashcatUtilsFolder = self.hashcatFolder + "hashcat-utils/"
        self.capFile = capFile
        self.wordList = wordList
    def showLogo(self):
        #This wasn't done by hand.
        #Some quick base64 + list comprehension + some print statements!
        crackCapLogo = ("CiDilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgIOKWiOK"
        "WiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWXICDilo"
        "jilojilZcgICAgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojil"
        "ojilZcg4paI4paI4paI4paI4paI4paI4pWXIArilojilojilZTilZDilZDilZDilZDi"
        "lZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZf"
        "ilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZEg4paI4paI4pWU4pWdICAgIC"
        "AgIOKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl"
        "+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlwrilojilojilZEgICAgIOKWiOKWiOKWiOKW"
        "iOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkSAgICA"
        "g4paI4paI4paI4paI4paI4pWU4pWdICAgICAgICDilojilojilZEgICAgIOKWiOKWiO"
        "KWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnQrilojilojil"
        "ZEgICAgIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKW"
        "iOKVkeKWiOKWiOKVkSAgICAg4paI4paI4pWU4pWQ4paI4paI4pWXICAgICAgICDiloj"
        "ilojilZEgICAgIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkO"
        "KVkOKVnSAK4pWa4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWRICDilojilojil"
        "ZHilojilojilZEgIOKWiOKWiOKVkeKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKW"
        "iOKVkSAg4paI4paI4pWXICAgIOKWiOKWiOKVl+KVmuKWiOKWiOKWiOKWiOKWiOKWiOK"
        "Vl+KWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICAgICAKIOKVmuKVkOKVkOKVkO"
        "KVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0g4"
        "pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0gICAg4pWa4pWQ"
        "4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pW"
        "Q4pWdICAgICAK")
        crackCapLogo = b64D(crackCapLogo)
        print(crackCapLogo)
        startupInfo = returnGreenDeep(self.colors,"Developed by Sh3llCod3, Using Hashcat and Aircrack-ng. 2017-2018.")
        printInfo(self.colors,startupInfo)
    def selectCapFile(self):
        COLOR = self.colors
        createNewLine()
        printDeepBlue(COLOR, returnGreenDeep(COLOR, "Let's pick a Handshake Capture file."))
        printDeepBlue(COLOR, returnGreenDeep(COLOR, "Please ensure this file has not been cleaned with wpaclean."))
        printDeepBlue(COLOR, returnGreenDeep(COLOR, "Normally, handshake files are found in the HANDSHAKES folder."))
        createNewLine()
        input(returnBlueDeep(COLOR, "Ready? press {}enter{} to choose. >> ".format(COLOR.endl_deep,COLOR.blue_deep)))
        self.capFile = pickFile()
        createNewLine()
    #Select user-chosen wordlist file
    def chooseCustomWordlist(self):
        COLOR = self.colors
        createNewLine()
        input(returnBlueDeep(COLOR, "Please locate a wordlist and press {}enter{} to choose. >> ".format(COLOR.endl_deep,COLOR.blue_deep)))
        self.wordList = pickFile()
    #Select between all online wordlists
    def getWordlists(self):
        totalLists = wordlistObj(self.colors)
        baseDir = totalLists.globalDirPath
        #Add rockyou
        totalLists.addName("Skull-Security/Rockyou.txt ~15 Million lines.")
        totalLists.addPath("rockyou.txt")
        totalLists.addMethod("cd {} && wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2"
                             " && bzip2 -d rockyou.txt.bz2".format(baseDir))
        #Add phpbb
        totalLists.addName("Skull-Security/Phpbb.txt.")
        totalLists.addPath("phpbb.txt")
        totalLists.addMethod("cd {} && wget http://downloads.skullsecurity.org/passwords/phpbb.txt.bz2 "
                             " && bzip2 -d phpbb.txt.bz2".format(baseDir))
        #Add a tiny one, that's on my other repository
        totalLists.addName("Github/Top 1350~ WPA/WPA2 list.")
        totalLists.addPath("Small-wpa-list")
        totalLists.addMethod("cd {} && wget https://raw.githubusercontent.com/Sh3llcod3/"
                             "Dependencies-for-Airscript-ng/master/Small-wpa-list".format(baseDir))
        #Add the cain-and-abel list
        totalLists.addName("Skull-Security/Cain-and-Abel.txt")
        totalLists.addPath("cain.txt")
        totalLists.addMethod("cd {} && wget http://downloads.skullsecurity.org/passwords/cain.txt.bz2 "
                             " && bzip2 -d cain.txt.bz2".format(baseDir))
        #Add Berzerk0's Probable-wordlists. Full credits to https://github.com/berzerk0
        totalLists.addName("Berzerk0/Probable-Wordlists ~200K lines.")
        totalLists.addPath("Top204Thousand-WPA-probable-v2.txt")
        totalLists.addMethod("cd {} && wget https://github.com/berzerk0/Probable-Wordlists/raw/master/"
                             "Real-Passwords/WPA-Length/Top204Thousand-WPA-probable-v2.txt".format(baseDir))
        #Add Daniel Miessler's seclists. Again Full credit to: https://github.com/danielmiessler
        totalLists.addName("Seclists/Darkc0de.txt")
        totalLists.addPath("darkc0de.txt")
        totalLists.addMethod("cd {} && wget https://github.com/danielmiessler/SecLists/raw/master/"
                             "Passwords/darkc0de.txt".format(baseDir))
        #Add the lists, and ask user to choose one.
        totalLists.commitList()
        self.wordList = totalLists.chooseList()
    #Download hashcat and hashcat-utils, compile it, ready for WPA/WPA2 cracking.
    def downloadHashcat(self):
        COLOR = self.colors
        clearTerm()
        hashcatDict = {}
        cuteCat = ("ICAgICAgICAgICAgICAgICAgYSAgICAgICAgICBhCiAgICAgICAgICAgICAgICAgYWFhICAg"
        "ICAgICBhYWEKICAgICAgICAgICAgICAgIGFhYWFhYWFhYWFhYWFhYWEKICAgICAgICAgICAg"
        "ICAgYWFhYWFhYWFhYWFhYWFhYWFhCiAgICAgICAgICAgICAgYWFhYWFmYWFhYWFhYWZhYWFh"
        "YWEKICAgICAgICAgICAgICBhYWFhYWFhYWFhYWFhYWFhYWFhYQogICAgICAgICAgICAgICBh"
        "YWFhYWFhYWFhYWFhYWFhYWEKICAgICAgICAgICAgICAgIGFhYWFhYWEgIGFhYWFhYWEKICAg"
        "ICAgICAgICAgICAgICBhYWFhYWFhYWFhYWFhYQogICAgICBhICAgICAgICAgYWFhYWFhYWFh"
        "YWFhYWFhYQogICAgIGFhYSAgICAgICBhYWFhYWFhYWFhYWFhYWFhYWEKICAgICBhYWEgICAg"
        "ICBhYWFhYWFhYWFhYWFhYWFhYWFhYQogICAgIGFhYSAgICAgYWFhYWFhYWFhYWFhYWFhYWFh"
        "YWFhYQogICAgIGFhYSAgICBhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWEKICAgICAgYWFhICAg"
        "YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhCiAgICAgIGFhYSAgIGFhYWFhYWFhYWFhYWFhYWFh"
        "YWFhYWFhYQogICAgICBhYWEgICAgYWFhYWFhYWFhYWFhYWFhYWFhYWFhYQogICAgICAgYWFh"
        "ICAgIGFhYWFhYWFhYWFhYWFhYWFhYWFhCiAgICAgICAgYWFhYWFhYWFhYWFhYWFhYWFhYWFh"
        "YWFhYWEKICAgICAgICAgYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYQoKICAgIOKWiOKWiOKV"
        "lyAg4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojiloji"
        "lZfilojilojilZcgIOKWiOKWiOKVlyDilojilojilojilojilojilojilZcg4paI4paI4paI"
        "4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICAKICAgIOKWiOKWiOKV"
        "kSAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWQ"
        "4pWQ4pWd4paI4paI4pWRICDilojilojilZHilojilojilZTilZDilZDilZDilZDilZ3iloji"
        "lojilZTilZDilZDilojilojilZfilZrilZDilZDilojilojilZTilZDilZDilZ0gICAgICAg"
        "CiAgICDilojilojilojilojilojilojilojilZHilojilojilojilojilojilojilojilZHi"
        "lojilojilojilojilojilojilojilZfilojilojilojilojilojilojilojilZHilojiloji"
        "lZEgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkSAgIOKWiOKWiOKVkSAgICAgICAKICAg"
        "IOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKVmuKV"
        "kOKVkOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVkSAg"
        "ICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWRICAg4paI4paI4pWRICAgICAgIAogICAg4paI"
        "4paI4pWRICDilojilojilZHilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKW"
        "iOKWiOKVkeKWiOKWiOKVkSAg4paI4paI4pWR4pWa4paI4paI4paI4paI4paI4paI4pWX4paI"
        "4paI4pWRICDilojilojilZEgICDilojilojilZEgICAgICAgCiAgICDilZrilZDilZ0gIOKV"
        "muKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa"
        "4pWQ4pWdICDilZrilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZri"
        "lZDilZ0gICDilZrilZDilZ0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg"
        "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCg==")
        cuteCat = b64D(cuteCat)
        print(cuteCat)
        if yesNo("Download and setup hashcat for GPU-based cracking?", COLOR):
            clearTerm()
            hashcatFilterPath = ("https://hashcat.net/hashcat/"
                                 " 2>/dev/null | grep -i 'a href='"
                                 " | grep -iv '.asc' | awk -F '\"' {'print $2'}"
                                 " | grep -iv '.tar.gz' | grep -i '.7z'")
            hashcatDownloadWebPath = ioStream("wget -O- {0} || curl {0}".format(hashcatFilterPath)).split()
            for i in enumerate(hashcatDownloadWebPath):
                hashcatDict[i[0]] = i[1]
            hashcatLatestVersion = hashcatDict[0][15:-3]
            while True:
                clearTerm()
                try:
                    createNewLine()
                    print(returnRed(COLOR, "Latest Version"), "to be downloaded:", returnBlue(COLOR, hashcatLatestVersion))
                    createNewLine()
                    for i in sorted(hashcatDict.items()):
                        if i[0] > 0:
                            versionString = lambda strLen: i[1][14:-3] + " " * (strLen - len(i[1][14:-3]))
                            print("Alternatively, to choose", returnGreen(COLOR, versionString(13)), "version type", returnRed(COLOR, i[0]))
                    createNewLine()
                    prependHashcatUrl = "https://hashcat.net"
                    askHashcatVersion = ("Type {0}a number{1} to download that version,"
                                         " or type [{0}l{1}] to get latest >> ".format(
                                         COLOR.blue,
                                         COLOR.endl))
                    confirmVersionChoice = input(askHashcatVersion).lower()
                    if confirmVersionChoice.startswith("l"):
                        self.hashcatVersionStr = hashcatDict[0][15:-3]
                        self.hashcatVersionChosen = prependHashcatUrl + hashcatDict[0]
                    elif int(confirmVersionChoice) in hashcatDict.keys() and int(confirmVersionChoice) > 0:
                        self.hashcatVersionStr = hashcatDict[int(confirmVersionChoice)][14:-3]
                        self.hashcatVersionChosen = prependHashcatUrl + hashcatDict[int(confirmVersionChoice)]
                    else:
                        raise ValueError
                    if hasattr(self, "hashcatVersionChosen"):
                        if yesNo("Confirm download of Hashcat Version: {}?".format(self.hashcatVersionStr), COLOR):
                            if connActive():
                                printInfo(COLOR, "Removing any pre-existing versions.")
                                bashRun("rm -r {} 2>/dev/null".format(self.hashcatFolder))
                                passTime(0.25)
                                printInfo(COLOR, "Creating directories.")
                                bashRun("mkdir -p {}".format(self.hashcatFolder))
                                passTime(0.25)
                                printInfo(COLOR, "Downloading version: {}.".format(self.hashcatVersionStr))
                                passTime(0.25)
                                bashRun("cd {} && wget {} && 7z x hashcat-*"
                                        " && git clone https://github.com/hashcat/hashcat-utils.git"
                                        " && cd hashcat-utils/src/ && make".format(
                                        self.hashcatFolder,
                                        self.hashcatVersionChosen))
                                createNewLine()
                                printSuccess(COLOR, "Hashcat is ready to use.")
                                self.hashcatInstalled = True
                                break
                            else:
                                printRed(COLOR, "Failed to aquire internet connection. Please try again.")
                                normalQuit(1)
                except(ValueError, TypeError, NameError):
                    continue
    def cpuCrack(self):
        COLOR = self.colors
        try:
            createNewLine()
            if yesNo("Ready? Start cracking using CPU?", COLOR):
                bashRun("{} {} -w {}".format(self.aircrackPath, self.capFile, self.wordList))
        except(KeyboardInterrupt, EOFError):
            bashRun("killall aircrack-ng")
            printDeepBlue(COLOR, "Recieved interrupt signal, quitting...")
    def gpuCrack(self):
        COLOR = self.colors
        while True:
            if self.checkHashcatPresence():
                break
            else:
                createNewLine()
                input(returnBlueDeep(COLOR, "Hashcat is not installed, let's fix that. Press enter >> "))
                self.downloadHashcat()
                continue
        if ioStream("getconf LONG_BIT") == "64":
            self.hashcatDetectedPath += "/hashcat64.bin "
        else:
            self.hashcatDetectedPath += "/hashcat32.bin "
        clearTerm()
        '''
        #-----------------------------------------------------------------------------------
        #Removed as newer versions of hashcat don't support the --gpu-temp-retain flag
        #Further, only setting --gpu-temp-abort will set both retain and max to the same
        #This means your GPU's fan won't spin until it reaches --gpu-temp-abort
        #By that time it will abort the session.
        #This may be re-enabled later in the future if Hashcat decides to add the flag back
        #-----------------------------------------------------------------------------------
        createNewLine()
        infoTextOne = ("The {}retain temperature{}"
                       " is the temperature it will try to hold.".format(
                        COLOR.yellow_deep, 
                        COLOR.endl_deep))
        infoTextTwo = ("The {}max temperature{}"
                       " is where Hashcat will abort the cracking session.".format(
                        COLOR.yellow_deep, 
                        COLOR.endl_deep))
        infoTextThree = ("When using Hashcat,"
                         " we can {}specify a max temperature value{}.".format(
                         COLOR.yellow_deep,
                         COLOR.endl_deep))
        firstGpuQuestion = ("What temperature do you want to"
                            " {0}retain{1}? (Degress Celsius) >> ".format(
                            COLOR.red_deep,
                            COLOR.endl_deep))
        secondGpuQuestion = ("What should be the"
                             " {0}maximum{1} value? >> ".format(
                            COLOR.red_deep,
                            COLOR.endl_deep))
        printDeepBlue(COLOR, infoTextThree)
        printDeepBlue(COLOR, infoTextOne)
        printDeepBlue(COLOR, infoTextTwo)
        createNewLine()
        while True:
            try:
                
                #gpuTempHold = input(firstGpuQuestion)
                gpuTempMax = input(secondGpuQuestion)
                if int(gpuTempMax) <= 85:
                    break
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Invalid temperature values entered, please enter valid integers.")
                printDeepBlue(COLOR, "Please ensure they are within 85C for max temperature.")
                printDeepBlue(COLOR, "This is to make sure your GPU doesn't over-heat under prolonged loads.")
                createNewLine()
                continue
        '''
        clearTerm()
        print("\n[" + returnGreenDeep(COLOR, "CAP FILE") + "]: {}".format(returnBold(COLOR, self.capFile)))
        print("[" + returnGreenDeep(COLOR, "HASHCAT PATH") + "]: {}".format(returnBold(COLOR, self.hashcatDetectedPath)))
        print("[" + returnGreenDeep(COLOR, "HASHCAT-UTILS PATH") + "]: {}".format(returnBold(COLOR, self.hashcatFolder + "hashcat-utils")))
        print("[" + returnGreenDeep(COLOR, "WORDLIST") + "]: {}".format(returnBold(COLOR, self.wordList)))
        print("[" + returnGreenDeep(COLOR, "ATTACK MODE") + "]: {}".format(returnBold(COLOR, "Straight/Dictionary")))
        #print("[" + returnGreenDeep(COLOR, "TEMPERATURE RETAIN") + "]: {}°C".format(returnBold(COLOR, gpuTempHold)))
        #print("[" + returnGreenDeep(COLOR, "TEMPERATURE ABORT") + "]: {}°C".format(returnBold(COLOR, gpuTempMax)))
        print("[" + returnGreenDeep(COLOR, "HASHCAT VERSION") + "]: {}".format(returnBold(COLOR, self.detectedVersion)))
        rootHashcatPath = self.hashcatFolder + self.detectedVersion + "/"
        currentWorkingDir = ioStream("pwd")
        createNewLine()
        try:
            if yesNo("Everything set correctly? Start cracking using GPU?", COLOR):
                finalHashcatCommand = ("cd {0}/src/ && ./cap2hccapx.bin {1} ~/.airscriptNG/HANDSHAKEFILE"
                                       " && cd {5} && {2} -a 0 -m 2500 ~/.airscriptNG/HANDSHAKEFILE"
                                       " {3} -D 2 &&"
                                       " echo '\n\nHere is any cracked hashes:'"
                                       " && cat {4}/hashcat.potfile".format(
                                       self.hashcatUtilsFolder,
                                       self.capFile,
                                       self.hashcatDetectedPath,
                                       self.wordList,
                                       rootHashcatPath,
                                       currentWorkingDir))
                bashRun("touch ~/.airscriptNG/HANDSHAKEFILE")
                bashRun(finalHashcatCommand)
        finally:
            bashRun("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
            bashRun("rm {0}/hashcat.potfile {0}/hashcat.log 2>/dev/null".format(rootHashcatPath))
        createNewLine()
        printSuccess(COLOR, "Finished session, quitting.")
        normalQuit(0)
    def selectWordlistMethod(self):
        COLOR = self.colors
        wordlistMethodsList = \
        [
            ["Choose your own list from disk.", self.chooseCustomWordlist],
            ["Use a built-in wordlist.", self.getWordlists]
        ]
        wordlistMethodsDict = {}
        for i in enumerate(wordlistMethodsList, start=1):
            wordlistMethodsDict[i[0]] = i[1]
        printDeepBlue(COLOR, returnBold(COLOR, "Now let's pick a wordlist. Where do you want to get it from?:\n"))
        for i in wordlistMethodsDict.items():
            print(returnRed(COLOR, i[0]) + ") " + returnGreenDeep(COLOR, i[1][0]))
        createNewLine()
        while True:
            try:
                askWordlistMethod = int(input(returnBlueDeep(COLOR, "Which method would you like? >> ")))
                if askWordlistMethod in wordlistMethodsDict.keys():
                    createNewLine()
                    if yesNo("Get wordlist with this method?", COLOR):
                        self.invokeWordlistMethod = wordlistMethodsDict[askWordlistMethod][1]
                        break
                    else:
                        createNewLine()
                        continue
                else:
                    raise ValueError
            except(ValueError, TypeError):
                printYellow(COLOR, "Please enter a valid integer.\n")
                continue
        self.invokeWordlistMethod()
    def enumerateMissingOptions(self):
        if self.capFile is None:
            self.selectCapFile()
        if self.wordList is None:
            self.selectWordlistMethod()
    def checkHashcatPresence(self):
        if bashReturnValue("ls {}/hashcat-*".format(self.hashcatFolder)) == "0":
            self.detectedVersion = ioStream("ls {} | grep -ivE"
            " 'hashcat-utils|*.7z'".format(
            self.hashcatFolder)).split()[0]
            self.hashcatDetectedPath = self.hashcatFolder + self.detectedVersion
            return True
        else:
            return False