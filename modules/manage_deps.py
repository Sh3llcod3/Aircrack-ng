#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   manage_deps.py - Keep script up to date and handle dependencies.
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
#Import the needed modules
from .run_command import *
from .term_colors import col, printRed, printDeepBlue
from .gui_elements import pickYesOrNo
#List all the apt packages we need.
aptDepsList = \
    ["xterm",
    "gawk",
    "reaver",
    "aircrack-ng",
    "wireless-tools",
    "ethtool",
    "apt-transport-https",
    "iproute2",
    "git",
    "wget",
    "curl",
    "p7zip",
    "p7zip-full",
    "libnl-3-dev",
    "autoconf",
    "automake",
    "libtool",
    "pkg-config",
    "libsqlite3-dev",
    "libpcre3-dev",
    "shtool",
    "rfkill",
    "libc-bin",
    "openssl",
    "libgcrypt20-dev",
    "build-essential",
    "libssl-dev",
    "libpcap-dev",
    "isc-dhcp-server",
    "python3-tk",
    "python3-requests",
    "dsniff",
    "driftnet",
    "bzip2",
    "gnome-terminal",
    "hostapd",
    "psmisc",
    "coreutils"]
#Join together the list
fullList = ' '.join(i for i in aptDepsList)
allowUnauth = "--allow-unauthenticated"
additionalPackages = " libnl*-gen*"
#Check and install packages if not present
def installDependencies():
    if connActive():
        #global fullList
        installList = fullList
        installList += additionalPackages
        if bashReturnValue("hash apt") == '0':
            bashRun("apt update {0} && apt install -y {1} {0}".format(allowUnauth,installList))
        elif bashReturnValue("hash apt-get") == '0':
            bashRun("apt-get update {0} && apt-get install -y {1} {0}".format(allowUnauth,installList))
        else:
            printRed(col,"Package manager not found. Are you using Ubuntu, Debian or Kali?")
            normalQuit(1)
    else:
        printRed(col,"Unable to connect, please check internet connection.")
        normalQuit(1)
def checkDependencies():
    if bashReturnValue("hash dpkg") == "0":
        if bashReturnValue("dpkg -s {} ".format(fullList)) != '0':
            installDependencies()
    else:
        printRed(col,"Dependency verification failed. Please install dpkg.")
        normalQuit(1)
def quickCheckDepsInstalled():
    gitBinaryPaths = " ~/.airscriptNG/air/*/src/aircrack-ng"
    gitBinaryPaths += " ~/.airscriptNG/wps/*/src/reaver"
    gitBinaryPaths += " ~/.airscriptNG/magic/*/pixiewps"
    gitBinaryPaths += " ~/.airscriptNG/mdk/*/src/mdk4"
    itemSearchList = ["hash dpkg","dpkg -s {}".format(fullList),"ls {}".format(gitBinaryPaths)]
    for i in itemSearchList:
        if bashReturnValue(i) != "0":
            return False
    return True
#Pull the latest version of this script from GitHub
def stashAndPullUpdate(COLORS):
    userConfirmationQuestion = "Pull the latest version from GitHub?"
    if yesNo(userConfirmationQuestion, COLORS):
        if bashReturnValue("git stash && git stash clear && git pull && chmod +x ./setup.sh && ./setup.sh") == "0":
            return True
        else:
            userHostId = ioStream("id -u -n")
            userName = ioStream("uname -n")
            bashRun("git config user.email '{0}@{1}.com' ".format(userHostId,userName))
            bashRun("git config user.name '{0}' ".format(userHostId))
            if bashReturnValue("git stash && git stash clear && git pull && chmod +x ./setup.sh && ./setup.sh") == "0":
                return True
            else:
                printRed(col,"Couldn't pull update, try 'git stash && git pull'. ")
                normalQuit(1)
    else:
        return False
#Git clone and make some packages from source
def cloneAircrackDeps():
    bashRun("rm ~/.airscriptNG/air/ -r 2>/dev/null")
    aircrackCloneAndBuild = "mkdir -p ~/.airscriptNG/air && cd ~/.airscriptNG/air && "
    aircrackCloneAndBuild += "git clone git://git.kali.org/packages/aircrack-ng.git -b upstream "
    aircrackCloneAndBuild += "&& cd * && make gcrypt=true"
    bashRun(aircrackCloneAndBuild)
    bashRun("chmod +x ~/.airscriptNG/air/*/scripts/airmon-ng")
def cloneReaverDeps():
    bashRun("rm ~/.airscriptNG/wps/ -r 2>/dev/null")
    reaverCloneAndBuild = "mkdir -p ~/.airscriptNG/wps && cd ~/.airscriptNG/wps && "
    reaverCloneAndBuild += "git clone git://git.kali.org/packages/reaver.git -b upstream && "
    reaverCloneAndBuild += "cd */src && ./configure && make"
    bashRun(reaverCloneAndBuild)
def clonePixiewpsDeps():
    bashRun("rm ~/.airscriptNG/magic/ -r 2>/dev/null")
    pixiewpsCloneAndBuild = "mkdir -p ~/.airscriptNG/magic && cd ~/.airscriptNG/magic && "
    pixiewpsCloneAndBuild += "git clone git://git.kali.org/packages/pixiewps.git -b upstream && "
    pixiewpsCloneAndBuild += "cd * && make && make install"
    bashRun(pixiewpsCloneAndBuild)
#These functions below will clone the packages mentioned above from GitHub
#This is there as a backup as git.kali.org could experience outages
#MDK4 is only on GitHub (as of now), so it can only be cloned from GitHub
def cloneMDK4Deps():
    #https://github.com/aircrack-ng/mdk4.git
    bashRun("rm ~/.airscriptNG/mdk/ -r 2>/dev/null")
    mdkCloneAndBuild = "mkdir -p ~/.airscriptNG/mdk && cd ~/.airscriptNG/mdk && "
    mdkCloneAndBuild += "git clone https://github.com/aircrack-ng/mdk4.git "
    mdkCloneAndBuild += "&& cd */src/ && make "
    bashRun(mdkCloneAndBuild)
def cloneAircrackGitHub():
    bashRun("rm ~/.airscriptNG/air/ -r 2>/dev/null")
    aircrackCloneAndBuild = "mkdir -p ~/.airscriptNG/air && cd ~/.airscriptNG/air && "
    aircrackCloneAndBuild += "git clone https://github.com/aircrack-ng/aircrack-ng.git "
    aircrackCloneAndBuild += "&& cd * && autoreconf -i && ./configure --with-gcrypt "
    aircrackCloneAndBuild += "&& make"
    bashRun(aircrackCloneAndBuild)
    bashRun("chmod +x ~/.airscriptNG/air/*/scripts/airmon-ng")
def cloneReaverGitHub():
    bashRun("rm ~/.airscriptNG/wps/ -r 2>/dev/null")
    reaverCloneAndBuild = "mkdir -p ~/.airscriptNG/wps && cd ~/.airscriptNG/wps && "
    reaverCloneAndBuild += "git clone https://github.com/t6x/reaver-wps-fork-t6x.git && "
    reaverCloneAndBuild += "mv * reaver && "
    reaverCloneAndBuild += "cd */src && ./configure && make "
    bashRun(reaverCloneAndBuild)
def clonePixiewpsGitHub():
    bashRun("rm ~/.airscriptNG/magic/ -r 2>/dev/null")
    pixiewpsCloneAndBuild = "mkdir -p ~/.airscriptNG/magic && cd ~/.airscriptNG/magic && "
    pixiewpsCloneAndBuild += "git clone https://github.com/wiire-a/pixiewps.git && "
    pixiewpsCloneAndBuild += "cd * && make && make install"
    bashRun(pixiewpsCloneAndBuild)
#FINISH THIS
def gitDeps():
    directoryMap = \
    {"aircrackDir" : "~/.airscriptNG/air/*/src/aircrack-ng",
    "reaverDir" : "~/.airscriptNG/wps/*/src/reaver",
    "pixiewpsDir" : "~/.airscriptNG/magic/*/pixiewps",
    "mdk4Dir" : "~/.airscriptNG/mdk/*/src/mdk4"}
    cloneFunctionMap = \
    {"aircrackDir" : cloneAircrackDeps,
     "reaverDir" : cloneReaverDeps,
     "pixiewpsDir" : clonePixiewpsDeps,
     "mdk4Dir" : cloneMDK4Deps}
    initialSearchPath = ' '.join([directoryMap[i] for i in directoryMap])
    if bashReturnValue("ls {}".format(initialSearchPath)) != "0":
        if connActive():
            while True:
                try:
                    clearTerm()
                    printDeepBlue(col,"The following packages may need compilation: aircrack-ng, reaver, pixiewps and MDK4.")
                    printDeepBlue(col,"This may take up to 5 mins on older systems. This will only happen once (on first run).")
                    getGitCloneConfirmation = input("{}[i]{} Proceed and install? y/n >> ".format(col.blue_deep,col.endl))
                    if getGitCloneConfirmation.lower().startswith("y"):
                        break
                    elif getGitCloneConfirmation.lower().startswith("n"):
                        normalQuit(0)
                    else:
                        continue
                except(KeyboardInterrupt,EOFError):
                    continue
            #Git clone and make the programs
            try:
                for i in directoryMap.keys():
                    if bashReturnValue("ls {}".format(directoryMap[i])) != "0":
                        if connActive():
                            cloneFunctionMap[i]()
                        else:
                            raise ConnectionError
                if bashReturnValue("~/.airscriptNG/air/*/scripts/airmon-ng") != '0':
                    bashRun('chmod +x ~/.airscriptNG/air/*/scripts/airmon-ng &>/dev/null')
            except(ConnectionError):
                printRed(col,"Failed to get an internet connection, please try again\n")
                normalQuit(1)
        else:
            printRed(col,"Failed to get a connection to the internet.\n")
            if startNetworkManager():
                printDeepBlue(col,"Network Manager was inactive, its been restarted.")
                for i in range(20,0,-1):
                    sysWrite("[{}i{}] Waiting {} seconds before retrying. \r".format(col.blue,col.endl,i))
                    passTime(1)
                gitDeps()
            else:
                printRed(col,"Please check connection and try again.")
                normalQuit(1)
    if bashReturnValue("~/.airscriptNG/air/*/scripts/airmon-ng") != '0':
        bashRun('chmod +x ~/.airscriptNG/air/*/scripts/airmon-ng &>/dev/null')
#TODO: Add arch linux support. Somehow, magically.
#Although I have no idea as I've never touched arch before.
#Any help would be greatly appreciated.
