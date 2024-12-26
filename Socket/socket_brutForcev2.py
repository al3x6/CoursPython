import string
import socket
import time

def generate_words():
    """
    Génère tous les mots de passe possibles en utilisant des lettres minuscules et majuscules, des chiffres et des symboles.
    """
    # Crée un alphabet contenant minuscules, majuscules, chiffres et symboles
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + ".,:;!?()")
    
    words = []
    
    # Génération de mots de passe allant de 1 à 4 caractères
    for word_length in range(1, 13):
        for letter1 in alphabet:
            words.append(letter1)
            if word_length > 1:
                for letter2 in alphabet:
                    words.append(letter1 + letter2)
                    if word_length > 2:
                        for letter3 in alphabet:
                            words.append(letter1 + letter2 + letter3)
                            if word_length > 3:
                                for letter4 in alphabet:
                                    words.append(letter1 + letter2 + letter3 + letter4)

    return words

def client_program():
    host = socket.gethostname()
    port = 3837

    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    message = client_socket.recv(1024).decode()
    print(f"Serveur : {message}")
    
    client_socket.send("admin".encode())
    message = client_socket.recv(1024).decode()
    print(f"Serveur : {message}")
    
    start_time = time.time()
    
    #liste=[]
    liste=generate_words()
    print(liste)
    
    input()
    
    for password in liste:
        print("password :",password)
        
        client_socket.send(password.encode())
        message = client_socket.recv(1024).decode()
        print(f"Serveur : {message}")
        
        if message == "Connexion réussie !":
            end_time = time.time()
            print(f"Mot de passe trouvé : {password}")
            print(f"Temps écoulé : {end_time - start_time} secondes")
            return
    
    client_socket.close()

if __name__ == "__main__":
    client_program()