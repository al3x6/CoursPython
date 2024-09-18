from scapy.all import *

def maFonction(trame):
    print(trame)

sniff(iface="en0", prn=maFonction)
