![Cool logo](https://goo.gl/wNmRxs)
# What is this?
This is a python script to automate the process of performing basic pen-testing on a WPA/WPA2/WPS network. The goal here is not to compete with existing tools or scripts, but to leverage them to provide as much functionality and simplicity to the end user as possible, so that someone with no previous knowledge or experience can use tools like aircrack-ng or reaver with ease. As long as you can type single digit numbers and letters, you can use this script.

This script not only aids an user in gaining a handshake but it supports them through the process of cracking the handshake using tools like hashcat. see https://hashcat.net/hashcat/

# Prerequisites 
- Some familiarity with the Linux command line (e.g. Basic usage, running python scripts, filesystem navigation)
- [Some basic knowledge of how WiFi hacking works.](https://null-byte.wonderhowto.com/how-to/wi-fi-hacking/)
- The APT package manager (Must be functional and not broken, have proper sources and needed packages)
- The bash/dash shell (Usually located at /bin/bash and /bin/sh respectively)
- A stable internet connection (To fetch dependencies and updates)
- A Debian based distro. (e.g. Kali Linux/Debian/Ubuntu and must follow their file structure)
- Access to the root/superuser account
- A WiFi-card/chipset that is capable of supporting monitor mode. (see: https://www.aircrack-ng.org/doku.php?id=compatible_cards)
- Drivers capable of running in promiscuous monitor mode/packet injection mode.
- A x86_64 or AMD64 (64 bit) processor. (32bit will work to an extent)
- 300-500MiB free space (For caching and storing wordlists)
- (Optional) A hashcat supported GPU, with appropriate drivers installed.
- (Optional) A second WiFi card, needed to create a Evil-Twin/Fake-AP. This doesn't need monitor mode or packet injection.


# Usage?
```
sudo su
python3 airscript-ng.py
```
Alternatively: 
```
sudo su
chmod +x airscript-ng.py no-color-airscript-ng.py airscript-old-stable.py
./airscript-ng.py
```
or, if you want it without colours:
```
sudo su
./no-color-airscript-ng.py
```
The rest is self explainatory once run. Anyone can use this script to pentest a wireless network, it really is that simple.

Please note, the code is neither efficient or very advanced. This likely won't affect usage and while efficiency is very important, functionality is a must. As long as it runs with as little bugs as possible, I am satisfied for the time being. 

Additonal note: Since I am actively developing this, lots of new elements have been introduced since then. Therefore, I have decided to keep the airscript-old-stable.py version and airscript-ng.py separate. This allows me to experiment with new features and release them without causing problems with existing versions. I'll keep updating the old stable version, but often it will feature an older build that is known to run stable. If you want the latest and greatest, you have to run airscript-ng.py. If you're going to fork this project, please ensure to keep checking back, as your fork may be outdated.

How do you update this script? just run it and type `5` in the menu.

## Upcoming
- [x] Make a basic python script
- [x] Make and integrate similar script for reaver/other-tools [Reaver/Pixie Dust added 11/06/17]
- [x] Add option to resolve dependencies [Added 17/06/17]
- [x] Add option to create captive portal/Evil-twin AP [Added 24/08/2017]
- [x] Add option to crack existing *.cap* files using hashcat/GPU/CPU/Aircrack [Added 24/08/2017]
- [x] Improve menu layout [Added 30/9/2017 In beta]
- [x] Add options to install opencl-runtime for hashcat [Added 30/9/2017 In beta]
- [x] Add support for Hostapd [Added 27/10/2017]
- [x] Add Airodump-ng CSV files support [Added 16/11/2017]
- [ ] Add support for GENPMK/CoWPAtty [COMING SOON]
- [ ] Make my own tools [Unlikely]
- [ ] (Ultimate Goal) Design and build a Gtk/Qt or any type of GUI [Help needed, due to limited knowledge of GUIs]

## Screenshots
[Title Menu](https://goo.gl/bGp5gk)
[Aircrack-ng](https://goo.gl/UwPb6c)
[Fake AP](https://goo.gl/fDxzdZ)
[Crack Existing](https://goo.gl/y5f2zS)

## Credits
> **Thanks to Joshua D. for extensively testing it on his machine!**
> **Thanks to [TomHulmeUK](https://github.com/TomHulmeUK) for helping with testing!**
> **Project inspired by [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) and [Fluxion](https://github.com/FluxionNetwork/fluxion)**
