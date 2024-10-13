# Détection de signatures
from scapy.all import *

def detecter_scan_syn(packet):
    """Détecte un scan SYN en vérifiant si le paquet TCP a le drapeau SYN activé."""
    if TCP in packet and packet[TCP].flags == 'S':  # Drapeau SYN
        src_ip = packet[IP].src
        print(f"Scan SYN détecté de {src_ip}")

def detecter_scan_fin(packet):
    """Détecte un scan FIN en vérifiant si le paquet TCP a le drapeau FIN activé."""
    if TCP in packet and packet[TCP].flags == 'F':  # Drapeau FIN
        src_ip = packet[IP].src
        print(f"Scan FIN détecté de {src_ip}")

def detecter_scan_xmas(packet):
    """Détecte un scan XMAS en vérifiant si le paquet TCP a les drapeaux FIN, URG, et PSH activés."""
    if TCP in packet and packet[TCP].flags == 'FPU':  # Drapeaux FIN, PSH, URG
        src_ip = packet[IP].src
        print(f"Scan XMAS détecté de {src_ip}")

def detecter_scan_icmp(packet):
    """Détecte un scan ICMP en vérifiant si le paquet ICMP est reçu."""
    if ICMP in packet:
        src_ip = packet[IP].src
        print(f"Scan ICMP détecté de {src_ip}")

# Ajout d'autres fonctions de détection

#sniff(filter="tcp", prn=detecter_scan_syn)
