#!/usr/bin/python3

from scapy.all import *
from scapy.sendrecv import sendp, sniff
import sys

source_interface = ''
normal_destination = ''
icmp_destination = ''
filter_function = None


def send_packets(packet):
    if ICMP in packet:
        sendpfast(x=packet, iface=icmp_destination)
    else:
        sendpfast(x=packet, iface=normal_destination)


def start():
    sniff(iface=source_interface, prn=send_packets)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python3 firewall.py <source_interface> <normal_destination> <icmp_destination>")
    else:
        source_interface = sys.argv[1]
        normal_destination = sys.argv[2]
        icmp_destination = sys.argv[3]
        start()
