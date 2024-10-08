from scapy.all import *

def detecter_scan_syn(packet):
    # Vérifier si le paquet est un paquet TCP avec un flag SYN
    if TCP in packet and packet[TCP].flags == 'S':  # Flag SYN
        src_ip = packet[IP].src
        print(f"Scan SYN détecté de {src_ip}")

# Capture du trafic réseau et application de la détection
sniff(filter="tcp", prn=detecter_scan_syn)