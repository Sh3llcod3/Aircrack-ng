![alt text](https://goo.gl/wNmRxs)
# What is this?
A python script to automate the process of pentesting a WPA/WPA2/WPS network. Very quickly made. The focus is not to beat or re-write existing tools or scripts, but to leverage them to provide functionality and simplicity to the end user while performing existing attacks using widely recognised tools like aircrack-ng or reaver.

It not only aids an user in gaining a handshake but it supports them through the process of cracking the handshake using tools like hashcat. see https://hashcat.net/hashcat/

# Requirements?
A chipset/wifi-card that supports monitor-mode/packet-injection and some distro of linux that uses the apt package manager (kali/ubuntu/debian). Dependancies will resolve automatically, and there is an option if additional repositories are needed.

# Usage?
```
sudo python3 airscript-ng.py
```
Alternatively: 
```
sudo chmod +x airscript-old-stable.py no-color-airscript-ng.py airscript-ng.py
sudo su
./airscript-ng.py
```
or, if you want it without colours:
```
sudo su
./no-color-airscript-ng.py
```
The rest is self explainatory once run. Anyone can use this script to pentest a wireless network, it really is that simple.

Please note, the code is neither efficient or very advanced. This likely won't affect usage and while efficiency is very important, functionality is a must. As long as it runs with as little bugs as possible, I am satisfied for the time being. 

Additonal note: Since I am actively developing this, lots of new elements have been introduced since then. Therefore, I have decided to keep the airscript-old-stable.py version and airscript-ng.py separate. This allows me to experiment with new features and release them without causing problems with existing versions. I'll keep updating the old stable version, but often it will feature an older build that is known to run stable. If you want the latest and greatest, you have to run airscript-ng.py

## Upcoming
- [x] Make a basic python script
- [x] Make and integrate similar script for reaver/other-tools [Reaver/Pixie Dust added 11/06/17]
- [x] Add option to resolve dependencies [Added 17/06/17]
- [x] Add option to create captive portal/Evil-twin AP [Added 24/08/2017]
- [x] Add option to crack existing *.cap* files using hashcat/GPU/CPU/Aircrack [Added 24/08/2017]
- [x] Improve menu layout [Added 30/9/2017 In beta]
- [x] Add options to install opencl-runtime for hashcat [Added 30/9/2017 In beta]
- [ ] Add support for GENPMK/CoWPAtty [COMING SOON]
- [ ] Make and integrate my own tools [VERY UNLIKELY]
- [ ] (Ultimate Goal) Design and build a Gtk/Qt or any type of GUI [HELP REQUIRED, AS LIMITED KNOWLEDGE]

## Screenshots
[Title Menu](https://goo.gl/bGp5gk)
[Aircrack-ng](https://goo.gl/UwPb6c)
[Fake AP](https://goo.gl/fDxzdZ)
[Crack Existing](https://goo.gl/y5f2zS)
