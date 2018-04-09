# What is this?
This is a script written in Python3 to automate the process of performing basic pen-testing on a WPA/WPA2/WPS network. The goal here is not to compete with existing tools or scripts, but to provide as much functionality and simplicity to the end user as possible, so that someone with no previous experience can use a WiFi-cracking tool such as aircrack-ng or reaver. As long as you know some of the general theory behind cracking WPA2 or WPS, you will be able to use this script with ease.

In addition to allowing a user to capture a handshake, this script can host a basic Evil-Twin wireless AP and crack a WPA2 handshake using your GPU with Hashcat. see https://hashcat.net/hashcat/.

![GitHub forks](https://img.shields.io/github/forks/Sh3llcod3/Airscript-ng.svg?style=for-the-badge&label=Fork)
![GitHub stars](https://img.shields.io/github/stars/Sh3llcod3/Airscript-ng.svg?style=for-the-badge&label=Stars)
![GitHub watchers](https://img.shields.io/github/watchers/Sh3llcod3/Airscript-ng.svg?style=for-the-badge&label=Watch)

# Prerequisites 
- Some familiarity with the Linux command line (e.g. Basic usage, running python scripts, filesystem navigation)
- [Some basic knowledge of how WiFi hacking works.](https://null-byte.wonderhowto.com/how-to/wi-fi-hacking/)
- The APT package manager (Must be able to install packages and have appropriate repository lists)
- The bash/dash shell (Any shell that works with the Python3 subprocess module)
- A stable internet connection (To fetch dependencies and updates)
- A Debian based distro. (e.g. Kali Linux/Debian/Ubuntu and must follow their file structure)
- Access to the root/superuser account (The user's home directory must be the same as the superuser's)
- The ~/ path must be the same as /root/ (Just become the root/super user. That's it!)
- A WiFi-card/chipset that is capable of supporting monitor mode. (see: https://www.aircrack-ng.org/doku.php?id=compatible_cards)
- Wireless interface names must start with "wl". E.g. "wlan1" or "wlxxxx" (Custom interface names are not supported) 
- Drivers capable of running in promiscuous monitor mode/packet injection mode.
- A x86_64 or AMD64 (64 bit) processor. (32bit will work to an extent)
- 300-500MiB free space (For caching and storing wordlists)
- (Optional) A hashcat supported GPU, with appropriate drivers installed.
- (Optional) A second WiFi card, needed to create a Evil-Twin/Fake-AP. This doesn't need monitor mode or packet injection.


# Usage?
```shell
$ sudo su
$ python3 airscript-ng.py
```
Alternatively: 
```shell
$ sudo su
$ chmod +x airscript-ng.py no-color-airscript-ng.py airscript-old-stable.py
$ ./airscript-ng.py
```
or, if you want it without colours:
```shell
$ sudo su
$ ./no-color-airscript-ng.py
```
The rest is self explainatory once run, choose your attack option from the menu and you are good to go! Anyone can use this script to pentest a wireless network, it really is that simple to use.

Additonal note: If you're going to fork this project, please ensure to keep checking back, as your fork may be outdated. Any contributions are absolutely welcome, please create a pull request.

How do you update this script? just run it and type `5` in the menu. Want to update manually? Simply `git stash` the changes and `git pull` the new additions.

## Upcoming
- [x] Make a basic python script
- [x] Make and integrate similar script for reaver/other-tools [Reaver/Pixie Dust added 11/06/17]
- [x] Add option to resolve dependencies [Added 17/06/17]
- [x] Add option to create captive portal/Evil-twin AP [Added 24/08/2017]
- [x] Add option to crack existing *.cap* files using hashcat/GPU/CPU/Aircrack [Added 24/08/2017]
- [x] Improve menu layout [Improved 30/9/2017]
- [x] Add options to install opencl-runtime for hashcat [Added 30/9/2017]
- [x] Add support for Hostapd [Added 27/10/2017]
- [x] Add Airodump-ng CSV files support [Added 16/11/2017]
- [ ] Add support for GENPMK/CoWPAtty [Coming soon]
- [ ] Make code more efficient 
- [ ] Add FHS support/compliancy
- [ ] Add support for MDK3
- [ ] Design and build a Gtk/Qt or any type of GUI [Help needed, due to limited knowledge of GUIs]

## Screenshots
[Title Menu](https://goo.gl/h16ecK)
[Aircrack-ng](https://goo.gl/FBd2r3)
[Reaver](https://goo.gl/G4PsNm)
[Fake AP](https://goo.gl/8KsYEf)
[MITM](https://goo.gl/e2YsZa)
[Crack Handshake](https://goo.gl/HnBUpE)

## Credits and inspirations.
> **Thanks to Joshua D. for extensively testing it on his machine!**
> **Thanks to [TomHulmeUK](https://github.com/TomHulmeUK) for helping with testing!**
> **Project inspired by [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) and [Fluxion](https://github.com/FluxionNetwork/fluxion)**

> [*__WPA3 ANNOUNCED!__*](https://www.theverge.com/2018/1/9/16867940/wi-fi-alliance-new-wpa3-security-protections-wpa2-announced)

![Cool logo](https://goo.gl/wNmRxs)
