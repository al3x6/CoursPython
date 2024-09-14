import socket

# Client qui se connecte au serveur
host = 'localhost'  # Adresse IP du serveur
port = 1234

def justeprix_client():
    # Connexion au serveur
    s = socket.socket()
    s.connect((host, port))
    
    # Envoie du nombre max au serveur
    nbrmax = int(input("Entrez le nombre maximum : "))
    s.send(str(nbrmax).encode())
    
    while True:
        # Propose un nombre au serveur
        nombreDevine = int(input("Devinez le nombre : "))
        s.send(str(nombreDevine).encode())
        
        # Reçoit la réponse du serveur
        data = s.recv(1024).decode()
        if data == "moins":
            print("C'est moins !")
        elif data == "plus":
            print("C'est plus !")
        elif data == "gagne":
            print("Bravo, vous avez trouvé le bon nombre !")
            break
    
    # Reçoit le nombre de coups et affiche la fin du jeu
    phrase = s.recv(1024).decode()
    print(phrase)
    
    # Fermeture de la connexion
    s.close()

# Exécution du client
justeprix_client()
