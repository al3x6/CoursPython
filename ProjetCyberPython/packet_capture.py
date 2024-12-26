# Capture des paquets
from scapy.all import *

def start_packet_capture(detecter_scan_syn, compter_paquets, duree, ip):
    def packet_callback(packet):
        detecter_scan_syn(packet)
        compter_paquets(packet)

    # Si aucune adresse IP n'est spécifiée, capturer tous les paquets
    if ip:
        filtre = f"tcp and host {ip}"
    else:
        filtre = "tcp"  # Capturer tous les paquets TCP

    sniff(filter=filtre, prn=packet_callback, store=0, timeout= duree )
