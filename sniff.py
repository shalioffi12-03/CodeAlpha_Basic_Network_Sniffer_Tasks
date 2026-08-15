from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        print("----------------------------")
        print("Source IP :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol :", packet[IP].proto)

sniff(prn=packet_callback, count=10)
