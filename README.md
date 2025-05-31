# Documentation du projet Python

Ce projet regroupe plusieurs scripts illustrant la manipulation de dictionnaires, la communication réseau et la simulation d'attaques/réponses entre un client et un serveur.

---

## Fichiers principaux

### genere_dictionnaire.py
Ce script permet à l'utilisateur de générer un dictionnaire à partir de trois paires clé/valeur saisies au clavier, puis affiche le dictionnaire généré.

- Saisie de trois clés et valeurs par l'utilisateur
- Création d'un dictionnaire Python
- Affichage du dictionnaire

**Utilisation :**
Lancer le script et suivre les instructions à l'écran.

---

### password_crak.py
Ce script génère un dictionnaire à partir de trois paires clé/valeur saisies par l'utilisateur, puis tente de deviner un mot de passe en testant si l'une des valeurs du dictionnaire correspond au mot de passe à trouver.

- Saisie de trois clés et valeurs
- Création d'un dictionnaire
- Saisie d'un mot de passe à deviner
- Test de chaque valeur du dictionnaire contre le mot de passe
- Affichage du résultat (trouvé ou non)

**Utilisation :**
Lancer le script, saisir les données et le mot de passe à deviner.

---

## scripts/attaquant.py
Script serveur qui attend une connexion entrante sur le port 4444. Une fois connecté, il permet d'envoyer des commandes à un client distant et d'afficher les réponses reçues.

- Ouvre un socket serveur sur le port 4444
- Attend une connexion d'un client
- Permet de saisir des commandes à envoyer au client
- Affiche la réponse du client pour chaque commande
- Tapez `exit` pour fermer la connexion

**Utilisation :**
Lancer le script, attendre la connexion d'un client, puis saisir les commandes à exécuter à distance.

---

## scripts/cible.py
Script client qui se connecte à un serveur distant (IP et port configurables), reçoit des commandes, les exécute localement et renvoie le résultat au serveur.

- Se connecte à l'adresse IP et au port du serveur (attaquant)
- Attend de recevoir des commandes
- Exécute chaque commande reçue et renvoie le résultat
- Se termine si la commande reçue est `exit`

**Utilisation :**
Lancer le script sur la machine cible, il attendra les commandes du serveur.

---

## screens/
Ce dossier contient des captures d'écran (capture1.png, capture2.png, capture3.png, capture4.png) illustrant l'exécution des scripts ou les résultats obtenus.

---

**Auteur :** kamdem keumogne rich bill  
**Date :** 31/05/2025
