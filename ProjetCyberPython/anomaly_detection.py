from scapy.all import *
from collections import Counter
import time

# Dictionnaire pour stocker le volume de trafic par adresse IP
volume_trafic = Counter()
seuil_volume = 3  # Seuil pour déterminer une activité anormale

def compter_paquets(packet):
    """Compter le nombre de paquets envoyés par chaque adresse IP source."""
    if IP in packet:
        src_ip = packet[IP].src
        volume_trafic[src_ip] += 1
        print(packet[IP].src)

def afficher_volume():
    """Afficher les résultats du volume de trafic."""
    for src_ip, count in volume_trafic.items():
        if count > seuil_volume:  # Vérifier si le volume dépasse le seuil
            print(f"Activité anormale détectée : {src_ip} a envoyé {count} paquets.")



#### TEST
#def surveiller_traffic(duree):
#    """Surveiller le trafic pendant une durée donnée."""
#    print(f"Surveillance du trafic pendant {duree} secondes...")
#    time.sleep(duree)  # Simuler une surveillance active
#    afficher_volume()  # Afficher le volume après la période de surveillance
