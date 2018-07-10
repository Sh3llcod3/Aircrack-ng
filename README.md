# Airscript-ng ![Build](https://img.shields.io/badge/build-passing-green.svg?longCache=true&style=flat-square&colorA=273133) ![Version](https://img.shields.io/badge/version-1.9-blue.svg?longCache=true&style=flat-square&colorA=273133&colorB=2962FF) ![Bash_Version](https://img.shields.io/badge/bash-4.2+-blue.svg?longCache=true&style=flat-square&colorA=273133&colorB=FFD600) ![Python_Version](https://img.shields.io/badge/python-3.4+-blue.svg?longCache=true&style=flat-square&colorA=273133&colorB=E65100) ![Dependencies](https://img.shields.io/badge/dependencies-up--to--date-blue.svg?longCache=true&style=flat-square&colorA=273133&colorB=004D40)
Airscript-ng is a modular, object-oriented program written in python3 to automate the process of performing basic manipulation on a wireless network. The goal here is not to compete with existing tools or scripts, but to provide as much functionality and simplicity to the end user as possible, so that someone with no previous experience can use a WiFi-cracking tool such as aircrack-ng or reaver. As long as you know some of the general theory behind cracking WPA2 or WPS, you will be able to use this script with ease.

In addition to allowing a user to capture a handshake, this script can host a basic Evil-Twin wireless AP and crack a WPA2 handshake using your GPU with Hashcat. see https://hashcat.net/hashcat/.

![GitHub forks](https://img.shields.io/github/forks/Sh3llcod3/Airscript-ng.svg?style=for-the-badge&label=Fork&colorA=273133)
![GitHub stars](https://img.shields.io/github/stars/Sh3llcod3/Airscript-ng.svg?style=for-the-badge&label=Stars&colorA=273133)
![GitHub watchers](https://img.shields.io/github/watchers/Sh3llcod3/Airscript-ng.svg?style=for-the-badge&label=Watch&colorA=273133)

# Prerequisites 
- Some familiarity with the Linux command line (e.g. filesystem navigation)
- [General overview of how WiFi hacking works.](https://null-byte.wonderhowto.com/how-to/wi-fi-hacking/)
- The APT package manager (Must be able to install packages and have appropriate repository lists)
- The bash shell (version 4.2+ is preferred)
- A stable internet connection (To fetch dependencies and updates)
- A Debian based distro. (Tested on: Kali Linux 2018.2/Ubuntu 16.04.04 LTS)
- Root access. Otherwise the program will not work.
- A WiFi-card/chipset that is capable of supporting monitor mode. (see: https://www.aircrack-ng.org/doku.php?id=compatible_cards)
- Wireless interface names must start with "wl". E.g. "wlan1" or "wlxxxx" (Custom interface names are not supported) 
- Drivers capable of running in promiscuous monitor mode/packet injection mode.
- A x86_64 or AMD64 (64 bit) processor. (32bit will work to an extent)
- 300-500MiB free space (For caching and storing wordlists)
- (Optional) A hashcat supported GPU, with appropriate drivers installed.
- (Optional) A second WiFi card, needed to create a Evil-Twin/Fake-AP. This doesn't need monitor mode or packet injection.


# Usage
```shell
$ sudo chmod +x ./setup.sh
$ sudo ./setup.sh
$ sudo ./airscript-ng.py
```
The rest is self explainatory once run, choose your attack option from the menu and you are good to go! Anyone can use this script to pentest a wireless network, it really is that simple to use. Try it out!

Additonal note: Airscript-ng is in active development. If you're going to fork this project, please ensure to keep checking back, as your fork may be outdated. Any contributions are absolutely welcome, please create a pull request.

How do you update this script? just run it and type `5` in the menu. Want to update manually? Simply `git stash` the changes and `git pull` the new additions.

## Upcoming
- [x] Make a basic python script
- [x] Add support for reaver/pixiedust [Added 11/06/17]
- [x] Add function to automatically download dependencies [Added 17/06/17]
- [x] Add support for captive portal/Evil-twin AP [Added 24/08/2017]
- [x] Add function to crack *.cap* files using GPU/CPU [Added 24/08/2017]
- [x] Improve menu layout [Improved 30/9/2017]
- [x] Add function to install Hashcat/Hashcat-utils [Added 30/9/2017]
- [x] Add Hostapd as AP hosting method [Added 27/10/2017]
- [x] Improve network selection process [Added 16/11/2017]
- [x] Make code object oriented [Rewritten 20/06/2018] 
- [x] Add support for MDK4 (Beacon-Flood and Deauth-DOS) [Added 07/07/2018]
- [ ] Add support for Cowpatty/Genpmk [Coming soon]
- [ ] Add FHS compliancy and lint code to conform with PEP8
- [ ] Improve startup times, performance and code efficiency

## Screenshots
[Title Menu](https://goo.gl/b94o9v)
[Aircrack-ng](https://goo.gl/xEaXi1)
[Reaver](https://goo.gl/aH4WGy)
[Fake AP](https://goo.gl/mXuBwR)
[MITM](https://goo.gl/EmWBiH)
[Crack Handshake](https://goo.gl/nSL1Bd)

## Credits and inspirations
> **Thanks to Joshua. for extensively testing it on his machine!**
> **Thanks to [TomHulmeUK](https://github.com/TomHulmeUK) for helping with testing!**
> **Project inspired by [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) and [Fluxion](https://github.com/FluxionNetwork/fluxion)**

> [*__WPA3 ANNOUNCED!__*](https://www.theverge.com/2018/1/9/16867940/wi-fi-alliance-new-wpa3-security-protections-wpa2-announced)

<img src="https://goo.gl/wNmRxs" width="870px" height="auto">
