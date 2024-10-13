import argparse
import sys
import time
from packet_capture import start_packet_capture
from signature_detection import detecter_scan_syn, detecter_scan_fin, detecter_scan_xmas
from anomaly_detection import compter_paquets, afficher_volume

def main(duree, ip):
    print("Démarrage du système de détection d'intrusion réseau (NIDS)...")
    print(f"Capture des paquets en cours pendant {duree} secondes...")

    try:
        # Démarrer la capture des paquets
        start_packet_capture(detecter_scan_syn, compter_paquets, duree, ip)

        # Attendre la fin de la capture
        time.sleep(3)

        # Afficher les résultats d'analyse
        afficher_volume()

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NIDS - Système de Détection d'Intrusions Réseau")
    parser.add_argument("--duree", type=int, default=10, help="Durée de capture en secondes")
    parser.add_argument("--ip", type=str, default=None, help="Adresse IP à surveiller")
    args = parser.parse_args()

    main(args.duree, args.ip)
