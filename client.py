#!/usr/bin/python3

from scapy.all import *
from scapy.sendrecv import sendp, sniff
import sys

source_interface = ''
destination_interface = ''
filter_function = None


def send_packets(packets):
    sendp(packets, destination_interface, inter=1./20)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python3 client.py <pcap_file> <destination_interface>")
    else:
        destination_interface = sys.argv[2]
        reader = PcapReader(sys.argv[1])
        send_packets(reader.read_all())
