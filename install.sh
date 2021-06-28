if [[ $EUID -ne 0 ]]; then
   echo "Error, please run this script as root user!"
   exit 1
fi
RED='\033[0;31m'
NC='\033[0m'
GREEN="\e[32m"
apt install figlet -y
clear
figlet "StrongDDos"
echo "\n"
echo "${RED}[*] Started installing StrongDDos script!"
echo "${NC}\n"
apt install python2 python3
clear
figlet "All Packages Successfully installed"
echo "${GREEN}[*] Now you can run script with command 'python3 script.py'"
