#!/usr/bin/python3

from scapy.all import *
from scapy.sendrecv import sendp, sniff
import sys

source_interface = ''
destination_interface = ''
filter_function = None

def send_packets(packet):
    sendp(packet, destination_interface)


def start():
    sniff(iface=source_interface, prn=send_packets)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: python3 route.py <source_interface> <destination_interface>")
    else:
        source_interface = sys.argv[1]
        destination_interface = sys.argv[2]
        start()
