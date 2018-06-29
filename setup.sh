#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root."
   echo "Try doing sudo chmod +x setup.sh"
   echo "Then sudo ./setup.sh"
   exit 1
fi
set -x
chmod +x attacks/*
chmod +x modules/*
chmod +x scripts/* 2>/dev/null
chmod +x airscript-old-stable.py 2>/dev/null
chmod +x airscript-ng.py
checkForDpkg=$(hash dpkg 2>/dev/null;printf $?)
checkForApt=$(hash apt 2>/dev/null;printf $?)
# Check if system has both apt and dpkg.
# Otherwise, check presence of certain modules
if [ $checkForDpkg -ne 0 ] || [ $checkForApt -ne 0 ];
then
	printf "You don't seem to have apt/dpkg package installed.\n"
	printf "Please install apt and dpkg.\n"
	printf "If your distro doesn't have apt or dpkg,"
	printf "then airscript-ng will not work."
	exit 1
else
	checkForTk=$(dpkg -s python3-tk >/dev/null 2>/dev/null;printf $?)
	if [ $checkForTk -ne 0 ];
	then
		sudo apt update
		sudo apt install python3-tk python3-requests -y
	fi
fi
/usr/bin/env python3 -c "import attacks, modules"
set +x
echo -e "\nSetup completed successfully!"
echo "To run, just do: sudo ./airscript-ng.py"
echo "Any problems, create an issue on GitHub"
echo "Best of luck, on your WiFi-cracking journey!"
exit 0
