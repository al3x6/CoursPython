import socket
import random

def server_program_Jeu():
    host = socket.gethostname()
    port = 1234

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen()
    print("Serveur prêt à recevoir des connexions...")

    client_socket, address = server_socket.accept()
    print(f"Connexion de {address}")

    client_socket.send("Bienvenue, nous allons jouer au pierre feuille ciseau.\n Nous allons choisir pour vous...".encode())

    liste_choix = ["pierre","feuille","ciseaux"]
    compteur = 1

    point_client = 0
    point_serveur = 0
    while compteur<6:
        client_socket.send((str(compteur) + "er/ième tour(s)").encode())
        
        compteur +=1
        choix_serveur = random.choice(liste_choix)
        print(f"On a choisi {choix_serveur} pour toi serveur")

        choix_client = client_socket.recv(1024).decode()
        print(f"Le client a choisi {choix_client}")

        client_socket.send((choix_serveur).encode())

        if ((choix_client == "ciseaux" and choix_serveur == "feuille") or (choix_client == "pierre" and choix_serveur == "ciseaux") or (choix_client == "feuille" and choix_serveur == "pierre")):
            point_client +=1

        # si pierre == pierre ..., on rejoue
        elif (choix_client == choix_serveur):
            compteur -=1 
        else :
            point_serveur +=1

    if point_client > point_serveur:
        client_socket.send(("Tu as gagné avec " +str(point_client) + " points et le serveur " + (str(point_serveur))).encode())
    else : 
        client_socket.send(("Tu as perdu avec " +str(point_client) + " point(s) et le serveur " + (str(point_serveur))).encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server_program_Jeu()