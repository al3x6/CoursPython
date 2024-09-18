import socket
import random

def client_program_Jeu():
    host = socket.gethostname()
    port = 1234

    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    message = client_socket.recv(1024).decode()
    print(f"{message}")

    liste_choix = ["pierre","feuille","ciseaux"]
    compteur = 1
    while compteur < 6 :
        tour = client_socket.recv(1024).decode()
        print(tour)

        compteur +=1
        choix_client = random.choice(liste_choix)
        print(f"On a choisi {choix_client} pour toi")
        client_socket.send(choix_client.encode())

        choix_serveur = client_socket.recv(1024).decode()
        print(f"Le choix du serveur {choix_serveur}")

        # si pierre == pierre ..., on rejoue
        if (choix_client == choix_serveur):
            compteur -=1 

    Resultat = client_socket.recv(1024).decode()
    print(f"Résultat : {Resultat}")
    
    client_socket.close()

if __name__ == "__main__":
    client_program_Jeu()