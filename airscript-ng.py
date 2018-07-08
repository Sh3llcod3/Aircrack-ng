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
#Import standard modules
import os
import subprocess
import time
import sys
import traceback
import csv
import sys
import atexit
#Import custom modules
import modules
import attacks
#Add some aliases for commonly used functions
ioStream = modules.ioStream
bashRun = modules.bashRun
bashReturnValue = modules.bashReturnValue
clearTerm = modules.clearTerm
col = modules.col
#Script Version number
scriptVersion = "1.9_build_date_07/07/2018"
#Some variables which will find out some basic system info
cpuModel = ioStream("cat /proc/cpuinfo | grep -i \"Model name\" | sort | uniq | awk -F ' ' {'print $4,$5,$6,$7,$8,$9,$10'}")
userName = ioStream("uname -n")
userDistro = ioStream("lsb_release -d | awk -F ':' {'print $2'} | tr -d \"\t\" ")
userKernel = ioStream("uname -r")
userArch = ioStream("uname -m")
userArchDpkg = ioStream("dpkg --print-architecture 2>/dev/null").upper()
invocationType = sys.argv[0]
#Determines a few values, useful when the -v argument is used
if invocationType.lower().startswith('./'):
    scriptInvocation = ('%s' %(sys.argv[0]))
else:
    scriptInvocation = ('python3 %s' %(sys.argv[0]))
#A quick check to determine if dependencies are installed
def dependenciesInstalled():
    if modules.quickCheckDepsInstalled():
        return '{}Installed{}'.format(col.green,col.endl)
    else:
        return '{}Not installed{}'.format(col.red,col.endl)
#The GPLv3+ exclusion of warranty. Just in case.
def displayWarranty():
    print("    %sAirscript-ng Copyright (C) 2017-2018 Sh3llcod3%s" %(col.red,col.endl))
    print("    %sThis program comes with ABSOLUTELY NO WARRANTY; for details visit: https://goo.gl/W1jcr5.%s" %(col.red,col.endl))
    print("    %sThis is free software, and you are welcome to redistribute it%s" %(col.red,col.endl))
    print("    %sunder certain conditions; visit: https://goo.gl/FSy6nc for details.%s" %(col.red,col.endl))
    print("    %sPlease follow all instructions that appear. Thanks for using this program.%s\n" %(col.red,col.endl))
#Create the functions class, where all the re-usable code for the main functions will reside
class functions:
    #Exit the program after a functions has finshed running.
    def silentExit():
        clearTerm()
        if modules.startNetworkManager():
            bashRun("rm ./HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
            print("\n[{}+{}] Detected network-manager as inactive,"
                  " restarted it.".format(
                col.green,
                col.endl))
            print("[{}+{}] Internet connection may take up"
                  " to 10 seconds to come back.\n".format(
                col.green,
                col.endl))
        modules.normalQuit(0)
    #Give the user the option to quit or head to menu.
    def menuOrExit():
        while True:
            modules.createNewLine()
            getUserChoice = input("[{0}+{2}] Head to [{1}m{2}]enu"
            " or [{1}q{2}]uit? m/q >> ".format(
                col.green,
                col.red,
                col.endl)).lower()
            if getUserChoice.startswith('m'):
                mainMenu()
            elif getUserChoice.startswith('q'):
                functions.silentExit()
    #Check for missing dependencies and if there are any, fetch them.
    def getDependencies():
        print("{}[-] {}Checking for dependancies".format(
            col.yellow_deep,
            col.endl))
        modules.checkDependencies()
        modules.gitDeps()
        print("{}[-] {}All dependancies are met."
              " Make sure you have correct drivers! {}".format(
            col.yellow_deep,
            col.pink,
            col.endl))
        clearTerm()
    #Downloads and builds hashcat and hashcat-utils, which are needed for GPU based cracking.
    #Note: this doesn't install the Opencl-drivers, which still needs to be installed by hand.
    def hashcatDownloadFunction():
        try:
            if not modules.connActive():
                raise ConnectionError
            hashcatDownloader = attacks.capObj(col)
            hashcatDownloader.downloadHashcat()
        except(ConnectionError):
            clearTerm()
            modules.createNewLine()
            modules.printRed(col, "Internet connection not found!")
        finally:
            functions.menuOrExit()
    #This function used to add the Kali-Rolling repository to the apt lists, however it was too dangerous, so its has been deprecated and removed.
    #Why was it dangerous? Because it replaces Ubuntu's Coreutils with Kali's Coreutils,Display manager, and breaks GPU (OpenCL) drivers. 
    #Your system will refuse to boot properly if kali tools aren't installed correctly. Use Katoolin if your're on Ubuntu >> https://goo.gl/rykBwg
    #This function switches the colors on/off in realtime, without changing programs or restarting.
    def switchColors():
        clearTerm()
        global col
        if col == modules.col:
            col = modules.blank_col
        else:
            col = modules.col
    #This function simply performs a full-upgrade of all system packages from apt, a nice to have add-on.
    #It also pulls the latest version from GitHub as an added bonus.
    def updateAptPackagesFull():
        functions.getDependencies()
        modules.createNewLine()
        if modules.yesNo("Run apt update and full-upgrade?", col):
            bashRun("apt update && apt full-upgrade -y"
                    " && apt autoremove -y && apt autoclean")
        modules.createNewLine()
        modules.stashAndPullUpdate(col)
    #This will restore the /etc/apt/source.list file. It won't be needed as the option to append the kali sources has been removed.
    #This mainly concerns users who used a very early build of this program. This is here for compatibility reasons.
    def revertKaliSources():
        clearTerm()
        if bashReturnValue("ls backup-repos") == '0':
            if not modules.pickYesOrNo("Restore sources.list",
            "Restore repository sources list?"):
                return None
            bashRun("cp backup-repos/sources.list /etc/apt/sources.list")
            modules.printSuccess(col,"Successfully reverted sources file back!")
            bashRun("apt update")
            printInfo(col,"If you don't see errors above then sources.list file is OK.")
            functions.menuOrExit()
        else:
            modules.printRed(col, "Backup file not found!")
            functions.menuOrExit()
    #This will help in displaying input prompts.
    def displayCurrentPlace(prompt,*args):
        currentPlace = col.endl + "|" + \
        modules.returnRed(col,"MENU")
        BASH_PROMPT = modules.returnRed(col, " ~# ")
        for i in args:
            currentPlace += col.endl + "|" +\
            modules.returnRed(col, i)
        currentPlace += col.endl + "|(" +\
        modules.returnGreen(col, prompt) +\
        ")" + BASH_PROMPT
        return currentPlace
    #A basic check to see if airscript-ng already exists in /usr/local/bin
    def checkExistingSymlink():
        if bashReturnValue("ls /usr/local/bin/airscript-ng") == "0":
            return True
        else:
            return False
    #Install all dependencies from GitHub instead of git.kali.org
    #If dependencies are already built, remove and replace them.
    def fetchGitHubDeps():
        clearTerm()
        try:
            modules.createNewLine()
            modules.printBlue(col, "This will clone aircrack-ng, reaver, pixiewps and mdk4 from GitHub.")
            modules.printBlue(col, "This is not normally required, as the script will automatically get")
            modules.printBlue(col, "any missing dependencies from git.kali.org. However, you can get them")
            modules.printBlue(col, "from GitHub instead of git.kali.org, if you want.")
            modules.createNewLine()
            modules.printYellow(col, "Warning: This may result in compatibility or instability issues!")
            modules.printYellow(col, "Warning: Compilation may take longer due to different procedures.")
            modules.createNewLine()
            if modules.yesNo("Confirm download from GitHub?", col):
                modules.cloneAircrackGitHub()
                modules.cloneReaverGitHub()
                modules.clonePixiewpsGitHub()
                modules.cloneMDK4Deps()
                modules.createNewLine()
                modules.printSuccess(col, "Successfully built all dependencies.")
        except(KeyboardInterrupt, EOFError, Exception):
            modules.createNewLine()
        finally:
            functions.menuOrExit()
    #Delete the dependencies folder, if the user wants.
    def removeResidualFiles():
        clearTerm()
        modules.createNewLine()
        if modules.yesNo("Confirm delete all residual files?", col):
            bashRun("rm ~/.airscriptNG/ -rf 2>/dev/null")
            modules.printSuccess(col, "Successfully removed the files.")
        functions.menuOrExit()
    #Allow the use full manual control over their wireless cards.
    def manualCardControl():
        functions.getDependencies()
        try:
            interfaceMethod = attacks.interfaceObj(col)
            while True:
                interfaceMethod.displayMenu()
        except(KeyboardInterrupt, EOFError, Exception):
            modules.createNewLine()
        finally:
            functions.menuOrExit()
    #Finish this function!
#Create the main class, which will store all the main functions of the program
class main:
    #This function is responsible for hosting the evil-twin/fake AP
    def EvilTwinFakeAP():
        functions.getDependencies()
        try:
            apMethod = attacks.apObj(col)
            apMethod.setInitialFiles()
            apMethod.showLogo()
            apMethod.selectOptions()
            apMethod.setupConfigFiles()
            apMethod.hostFakeAp()
            apMethod.cleanupFakeAp()
        except(KeyboardInterrupt, EOFError, Exception):
            try:
                apMethod.cleanupFakeAp()
            except(KeyboardInterrupt, EOFError, Exception):
                modules.createNewLine()
        finally:
            functions.menuOrExit()
    #This is here to remind me of how XTERM handles its geometry. Interesting.
    #xterm -geometry 125x35+4320 -bg '#FFFFFF' -fg '#000000' THIS MAKES IT APPEAR TOP RIGHT
    #xterm -geometry 125x35+4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM RIGHT
    #xterm -geometry 125x35-4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM LEFT
    #xterm -geometry 125x35-7640 -bg '#FFFFFF' -fg '#000000' TOP LEFT
    #This function will allow a user to crack a WPA/WPA2 handshake file (.cap file)
    def crackCaptureFile():
        functions.getDependencies()
        try:
            capMethod = attacks.capObj(col)
            capMethod.showLogo()
            modules.createNewLine()
            print("{}Type [1] - Crack the WPA-HANDSHAKE with CPU".format(
                col.blue_deep))
            print("{}Type [2] - Crack the WPA-HANDSHAKE with GPU (Much faster)".format(
                col.green_deep))
            print("\n{}Type [99] - Return to menu {}".format(
                col.highlight,
                col.endl))
            while True:
                modules.createNewLine()
                getOption = input(functions.displayCurrentPlace(
                    "ENTER CHOICE",
                    "PRE-EXISTING_HANDSHAKE"))
                if getOption.isdigit() and int(getOption) in [1,2,99]:
                    break
            if int(getOption) == 1:
                capMethod.enumerateMissingOptions()
                capMethod.cpuCrack()
            elif int(getOption) == 2:
                capMethod.enumerateMissingOptions()
                capMethod.gpuCrack()
            #FINISH THIS
        except(KeyboardInterrupt, EOFError, Exception) as e:
            bashRun("killall aircrack-ng 2>/dev/null")
            bashRun("kill $(ps aux | grep -i hashcat |"
                " awk -F ' ' {'print $2'}) 2>/dev/null")
        finally:
            functions.menuOrExit()
    #This function used to revert a backup of the .bashrc file to its original location.
    #However this was deprecated in favor of symbolic links.
    #This is cleaner and easier to maintain as well as being a more efficient method.
    #Now, this function removes any created symlinks from the function below.
    def removeSymlink():
        clearTerm()
        modules.createNewLine()
        modules.printBlue(col,"This option will remove the symlink created in option [7].")
        modules.printBlue(col,"If you haven't used option [7], then this isn't necessary.")
        modules.printBlue(col,"However, this should be safe to run.")
        modules.printBlue(col,"Unless you already have another airscript-ng in /usr/local/bin.")
        modules.createNewLine()
        try:
            if modules.yesNo("Remove the symbolic link?",col):
                if functions.checkExistingSymlink():
                    modules.createNewLine()
                    modules.printSuccess(col, "Found airscript-ng in /usr/local/bin.")
                    if bashReturnValue("rm -f /usr/local/bin/airscript-ng") == "0":
                        modules.printSuccess(col, "Successfully deleted the symlink.")
                        modules.printGreen(col, "Typing 'airscript-ng' will no longer invoke it.")
                    else:
                        raise ValueError
                else:
                    raise FileNotFoundError
        except(FileNotFoundError):
            modules.createNewLine()
            modules.printYellow(col, "Symlink not found. No need to remove anything.")
        except(ValueError):
            modules.createNewLine()
            modules.printYellow(col, "An error occured while removing the symlink.")
            modules.printYellow(col, "Try running this manually: unlink /usr/local/bin/airscript-ng")
        finally:
            functions.menuOrExit()
    #This function creates a symlink, which allows you to invoke this program like any other binary.
    #Using lots of nested-ifs is far from ideal, however it's all I can think of at present.
    def createSymlink():
        clearTerm()
        modules.createNewLine()
        modules.printBlue(col,"Creating a symbolic link allows you to run airscript-ng from anywhere.")
        modules.printBlue(col,"Essentially, this adds an entry in /usr/local/bin.")
        modules.printBlue(col,"Next time you want to run airscript-ng, just type 'airscript-ng'.")
        modules.printBlue(col,"You can run this from anywhere, any folder you want.")
        modules.printBlue(col,"If you change your mind, you can always delete this using option [8].")
        modules.createNewLine()
        try:
            if sys.argv[0].lower().startswith("./"):
                FILE_NAME = sys.argv[0][2:]
            elif sys.argv[0].lower().startswith("/usr/local/bin/"):
                raise TypeError
            else:
                FILE_NAME = sys.argv[0]
            if modules.yesNo("Create the symbolic link?",col):
                if not functions.checkExistingSymlink():
                    modules.createNewLine()
                    modules.printSuccess(col, "Adding Symbolic link -> /usr/local/bin/airscript-ng")
                    if bashReturnValue("ls /usr/local/bin") == "0":
                        if bashReturnValue("echo $PATH | grep \"/usr/local/bin\"") == "0":
                            if bashReturnValue("ln -sf $(find $(pwd) -name {}) /usr/local/bin/airscript-ng".format(FILE_NAME)) == "0":
                                modules.printSuccess(col, "Successfully created the symlink.")
                                modules.printGreen(col, "Now you can type 'airscript-ng' from anywhere.")
                                modules.printGreen(col, "Go ahead, quit and try typing: airscript-ng")
                            else:
                                raise ValueError
                        else:
                            raise FileNotFoundError
                    else:
                        raise NotADirectoryError
                else:
                    raise FileExistsError
        except(FileExistsError):
            modules.createNewLine()
            modules.printYellow(col, "Symbolic link already exists. Will not overwrite.")
            modules.printYellow(col, "Is this an error? You can delete the link manually.")
            modules.printYellow(col, "Try running this: unlink /usr/local/bin/airscript-ng")
        except(ValueError):
            modules.createNewLine()
            modules.printYellow(col, "An error occured while creating the symlink.")
            modules.printYellow(col, "Run this manually:")
            modules.printYellow(col, "ln -sf $(find $(pwd) -name {}) /usr/local/bin/airscript-ng".format(
                FILE_NAME))
        except(FileNotFoundError):
            modules.createNewLine()
            modules.printYellow(col, "Unable to find /usr/local/bin in the $PATH env variable.")
            modules.printYellow(col, "If $PATH doesn't exist, then how are you running this?")
            modules.printYellow(col, "Otherwise, you can add to your $PATH variable by following this guide.")
            modules.printYellow(col, "Visit: https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix")
        except(NotADirectoryError):
            modules.createNewLine()
            modules.printYellow(col, "Unable to find the /usr/local/bin directory.")
            modules.printYellow(col, "Please choose a linux distro that utilises this directory.")
            modules.printYellow(col, "Otherwise, I can't add the Symlink.")
        except(TypeError):
            modules.createNewLine()
            modules.printYellow(col, "Wrong method of invocation.")
            modules.printYellow(col, "You're probably running this using 'airscript-ng'.")
            modules.printYellow(col, "That won't work. You'll have to run it manually for this occasion.")
            modules.printYellow(col, "Please head to where Airscript-ng is stored.")
            modules.printYellow(col, "Then run it manually with: ./airscript-ng")
            modules.printYellow(col, "If you're confused, please consult the README.md file.")
        finally:
            functions.menuOrExit()
    #This function is to use the reaver tool, to crack wps.
    def reaver():
        functions.getDependencies()
        try:
            reaverMethod = attacks.wpsObj(col)
            reaverMethod.showLogo()
            reaverMethod.getWpsTargets()
            reaverMethod.parseWpsCsv()
            reaverMethod.pixieDust()
            reaverMethod.cleanupWpsFiles()
        except(KeyboardInterrupt, EOFError, Exception) as e:
            try:
                reaverMethod.cleanupWpsFiles()
            except(KeyboardInterrupt, EOFError, Exception):
                modules.createNewLine()
        finally:
            functions.menuOrExit()
    #This will handle Aircrack-ng, for most users this will be the go-to choice.
    #Again, this isn't the most efficient way, and I will re-write this at some point.
    def aircrackng():
        functions.getDependencies()
        try:
            aircrackMethod = attacks.aircrackObj(col)
            aircrackMethod.showLogo()
            aircrackMethod.createTempFiles()
            aircrackMethod.selectInitialCard()
            aircrackMethod.gatherInitialData()
            aircrackMethod.parseCsvData()
            aircrackMethod.selectTargetNetwork()
            aircrackMethod.callCompleteCleanup()
            clearTerm()
            modules.printDeepBlue(col, "{1}Did you see WPA Handshake: {0} at the top right?".format(
                aircrackMethod.selectedNetworkTarget[1],
                col.green_deep))
            modules.printDeepBlue(col, modules.returnBold(col, "If you didn't see that,"
                    "then {}cleanup with CTRL+C{} and try again.".format(
                    col.red_deep, col.endl_deep)))
            decryptHandshake = attacks.capObj(col, aircrackMethod.captureFilePath)
            decryptHandshake.enumerateMissingOptions()
            clearTerm()
            modules.printDeepBlue(col, "Which method do you want to crack the Handshake with:\n")
            while True:
                choice_of_cpu_gpu = input("{0}Crack using{1}: CPU-->[c] (all CPUs)|"
                                          " GPU-->[g] (GTX 9xx,10xx+/AMD ROCM GPU) {2}${1} ".format(
                                            col.blue_deep,
                                            col.endl,
                                            col.green)).lower()
                if choice_of_cpu_gpu.startswith(("c","g")):
                    break
            if choice_of_cpu_gpu.startswith("c"):
                decryptHandshake.cpuCrack()
            elif choice_of_cpu_gpu.startswith("g"):
                decryptHandshake.gpuCrack()
        except(KeyboardInterrupt, EOFError, Exception) as e:
            try:
                aircrackMethod.callCompleteCleanup()
            except(KeyboardInterrupt, EOFError, Exception):
                modules.createNewLine()
        finally:
            functions.menuOrExit()
    #This will handle mdk4. A very useful tool with quite a few interesting options.
    def mdk4():
        functions.getDependencies()
        try:
            mdkMethod = attacks.mdkObj(col)
            mdkMethod.showLogo()
            mdkMethod.selectAttackMode()
        except(KeyboardInterrupt, EOFError, Exception) as e:
            try:
                mdkMethod.cleanupCard()
            except(KeyboardInterrupt, EOFError, Exception):
                modules.createNewLine()
        finally:
            functions.menuOrExit()
#Define the main menu, where user will be presented with options and function of script.
def mainMenu():
    try:
        clearTerm()
        #Check if user has root permissions.
        if os.getuid() != 0:
            print("{}[?]{} Please make sure you have followed the steps:\n".format(
                col.yellow_deep,
                col.endl))
            print("\t{0}->{1} [{0}i{1}] Made script executable with '{2}sudo chmod +x {3}{1}' ".format(
                col.blue,
                col.endl,
                col.red,
                sys.argv[0]))
            print("\t{0}->{1} [{0}i{1}] Ran it with '{2}sudo {3}{1}' \n".format(
                col.blue,
                col.endl,
                col.red,
                scriptInvocation))
            print(modules.returnYellow(col, "\tAlternatively,"))
            print("\t{0}->{1} [{0}i{1}] If you have symlinked the program, just do '{2}sudo airscript-ng{1}' \n".format(
                col.blue,
                col.endl,
                col.red))
            modules.normalQuit(1)
        print("Hello {}{}{}!\n".format(col.yellow,userName,col.endl))
        displayWarranty() #Display the warranty information, as recommened by the GPLv3 license.
        print("{0}Your CPU{1}: {2}{3}{1}".format(col.red,col.endl,col.green,cpuModel))
        print("{0}Your OS{1}: {2}{3}{1}".format(col.red,col.endl,col.green,userDistro))
        print("{0}Your Kernel{1}: {2}{3}{1}".format(col.red,col.endl,col.green,userKernel))
        print("{0}Your Architecture{1}: {2}{3}\\{4}{1}".format(col.red,col.endl,col.green,userArch,userArchDpkg))
        print("{0}Dependencies{1}: {2}{3}{1}".format(col.red,col.endl,col.green,dependenciesInstalled()))
        print("{0}Script version{1}: {2}{3}{1}".format(col.red,col.endl,col.green,scriptVersion))
        #A 2d list spanning across multiple lines that stores all the info for the menu.
        #Probably not the most efficient solution here, but its simple to maintain.
        menuTextItemArray = \
    [[col.pink_deep,'Aircrack-ng to crack WPA/WPA2','1','main.aircrackng'],
    [col.blue_deep,'Reaver with pixie dust to crack WPS','2','main.reaver'],
    [col.endl_deep,'Host a Evil-Twin/MITM AP to phish credentials, sniff traffic and more.','3','main.EvilTwinFakeAP'],
    [col.red_deep,'Crack an existing WPA/WPA2 handshake using CPU/GPU.','4','main.crackCaptureFile'],
    [col.green_deep,'Use mdk4 to create a beacon flood, denial-of-service and more.','5','main.mdk4'],
    [col.yellow_deep,'Manipulate the system\'s WiFi-cards with manual control.','6','functions.manualCardControl'],
    [col.blue_deep,'Download and build the dependencies from GitHub.','7','functions.fetchGitHubDeps'],
    [col.yellow_deep,'Update/upgrade all system packages and this script','8','functions.updateAptPackagesFull'],
    [col.green_deep,'Setup Hashcat and Hashcat-utils to use GPU for cracking','9','functions.hashcatDownloadFunction'],
    [col.light_blue,'Add a symlink to invoke from anywhere','10','main.createSymlink'],
    [col.pink_deep,'Delete the symlink from option [10]','11','main.removeSymlink'],
    [col.black_deep,'Turn the colors on/off','12','functions.switchColors'],
    [col.endl_deep,'If apt is broken, use this to fix it','13','functions.revertKaliSources'],
    [col.red_deep,'Delete the folder containing dependencies.','14','functions.removeResidualFiles'],
    [col.highlight+'\n','Exit \033[0m'+col.endl,'99','functions.silentExit']]
        #The menu, in short.
        print("\n%s[?] %sWhat tool would you like to use? Please run as root." %(col.yellow_deep,col.endl))
        print("\n{}-----------------------------------------ATTACKS-----------------------------------------{}\n".format(
            col.yellow_deep,
            col.endl))
        for i in range(1,int(menuTextItemArray[-2][2])+2):
            print("%sType [%s] - %s" %(menuTextItemArray[i-1][0],menuTextItemArray[i-1][2],menuTextItemArray[i-1][1]))
            if i == 6:
                print("\n{}----------------------------------------DOWNLOADS----------------------------------------{}\n".format(
                    col.green_deep,
                    col.endl))
            if i == 9:
                print("\n{}--------------------------------------INSTALLATIONS--------------------------------------{}\n".format(
                    col.blue_deep,
                    col.endl))
        while True:
            mainMenuChoice = input('\n|%sMENU%s|(Choose an option) >>' %(col.red,col.endl))
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
