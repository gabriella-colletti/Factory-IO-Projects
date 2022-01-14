# Gabriella Colletti
# Cyber-physical systems
# Project 0
# Task 1

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

# Sniff all the packets from a pcap file and filter for ip addresses
packets = sniff(offline = 'sample.pcap', timeout=120, filter="ip", prn = find_src_dest)

# All the packet's summary information
packets.nsummary()

# Write unique source ip address to file called source.txt
with open('source.txt', 'w') as file:
	file.write('\n'.join(np.unique(source_ip)))

# Write unique destination ip addresses to file called dest.txt
with open('dest.txt','w') as file:
	file.write('\n'.join(np.unique(dest_ip)))

# Print Number of Src and Dest IP Addresses found
print('Number of Unique Source IP Addresses:      ', len(np.unique(source_ip)))
print('Number of Unique Destination IP  Addresses: ', len(np.unique(dest_ip)))

	
