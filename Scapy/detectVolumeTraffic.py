'''
from scapy.all import *
from collections import Counter
import time

# Compteur pour suivre le nombre de paquets par IP source
volume_trafic = Counter()

def compter_paquets(packet):
    if IP in packet:
        src_ip = packet[IP].src
        volume_trafic[src_ip] += 1

def afficher_volume():
    # Afficher les IP qui ont envoyé plus de 100 paquets (seuil arbitraire)
    for src_ip, count in volume_trafic.items():
        if count > 100:
            print(f"Activité anormale détectée : {src_ip} a envoyé {count} paquets.")

# Capture pendant 10 secondes
sniff(prn=compter_paquets, timeout=10)
afficher_volume()
'''

from scapy.all import *
import time

# Dictionnaire pour suivre les informations par IP source
volume_trafic = {}

def compter_paquets(packet):
    if IP in packet:
        src_ip = packet[IP].src

        # Si l'IP n'est pas dans le dictionnaire, on l'ajoute
        if src_ip not in volume_trafic:
            volume_trafic[src_ip] = {
                "count": 0,           # Nombre de paquets envoyés
                "first_seen": time.time(),  # Temps du premier paquet
                "last_seen": time.time()    # Temps du dernier paquet
            }

        # Mise à jour des informations pour l'IP
        volume_trafic[src_ip]["count"] += 1
        volume_trafic[src_ip]["last_seen"] = time.time()

        print ("LAAAAAAA : ",volume_trafic,"\n")

def afficher_volume():
    # Afficher les IP qui ont envoyé plus de 100 paquets (seuil arbitraire)
    for src_ip, info in volume_trafic.items():
        if info["count"] > 100:
            print(f"Activité anormale détectée : {src_ip} a envoyé {info['count']} paquets.")
            print(f"Premier paquet vu à : {time.ctime(info['first_seen'])}")
            print(f"Dernier paquet vu à : {time.ctime(info['last_seen'])}")

# Capture pendant 10 secondes
sniff(prn=compter_paquets, timeout=10)
afficher_volume()
