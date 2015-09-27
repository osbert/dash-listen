# sudo apt-get install python-scapy tcpdump tcpreplay wireshark

# Note that wireshark prompts during installation if non-root users
# should be allowed to perform packed capture.

from scapy.all import *
import os
import requests

DASH_MAC_ADDRESS=os.environ.get('DASH_MAC_ADDRESS')
URL_CALLBACK=os.environ.get('URL_CALLBACK')

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == DASH_MAC_ADDRESS:
        requests.get(URL_CALLBACK)
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc


while True:
    try:
        print sniff(prn=arp_display, filter="arp", store=0, count=10)
    except:
        pass
