# Gabriella Colletti
# Cyber-physical System
# Project 0 
# Task 2

# Import Libraries
from scapy.all import sniff
import numpy as np


source_ip = []         # Contains all Source IP Addresses
dest_ip = []           # Contains all Destination IP Addresses


def find_src_dest(packet):
	'''Arguments: packet := packet representing network traffic
	Adds the packet's source ip address to global source ip address list
	Adds the packet's destination address ip to the global destination
        ip address list'''
	source_ip.append(packet[0][1].src)
	dest_ip.append(packet[0][1].dst)

# Sniffs first 10 packets from a enp0s3 interface and filter for ip addresses
packets = sniff( iface='enp0s3', filter="ip",count = 6, prn = find_src_dest)

# Write unique source ip address to file called source.txt
with open('source.txt', 'w') as file:
        file.write('\n'.join(np.unique(source_ip)))

# Write unique destination ip addresses to file called dest.txt
with open('dest.txt','w') as file:
        file.write('\n'.join(np.unique(dest_ip)))

