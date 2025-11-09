import os
os.system("WIFI.py")
apt update && apt upgrade -y
pkg install git
pkg install python
pip install requests
rm -rf WIFI-HACKING
git clone --depth=1 https://github.com/U7P4L-IN/WIFI-HACKING.git
cd WIFI-HACKING
python WIFI.py 
