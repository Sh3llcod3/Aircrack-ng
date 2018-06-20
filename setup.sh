#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root."
   echo "Try doing sudo chmod +x setup.sh"
   echo "Then sudo ./setup.sh"
   exit 1
fi
set -x
cd attacks/
chmod +x *
cd ../modules/
chmod +x *
cd ..
chmod +x airscript-ng.py
/usr/bin/env python3 -c "import attacks, modules"
set +x
echo -e "\nSetup completed successfully!"
echo "To run, just do: sudo ./airscript-ng.py"
echo "Any problems, create an issue on GitHub"
echo "Best of luck, on your WiFi-cracking journey!"
exit 0
