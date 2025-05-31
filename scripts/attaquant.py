import socket

# On ouvre un socket pour le serveur
# On écoute les connexions entrantes sur le port 4444
serveur = socket.socket()
serveur.bind(("0.0.0.0", 4444))
serveur.listen(1)


# On attend une connexion entrante
print("Attente de connexion entrante ....")
client, addr = serveur.accept()
print(f"Connecte a {addr}")

# Pour chaque commande saisie par l'utilisateur, on l'envoie au client
# et on affiche la réponse reçue
while True:
	commande = input (">>> ")


	if commande.lower() == "exit":
		client.send(b"exit")
		break
	client.send(commande.encode())
	reponse = client.recv(4096).decode()
	print(reponse)
client.close()







