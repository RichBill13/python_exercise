# Ce script permet de générer un dictionnaire à partir de trois paires clé/valeur saisies par l'utilisateur.
# Ensuite, il tente de "craquer" un mot de passe en testant si l'une des valeurs du dictionnaire correspond au mot de passe saisi.
# Auteur : [kamdem keumogne rich bill]
# Date : 2025-05-31

# Demande à l'utilisateur de saisir trois paires clé/valeur
donnee1 = input("entrez la premiere donnee: ")
valeur1 = input("entrez la premiere valeur: ")

donnee2 = input("entrez la seconde donnee: ")
valeur2 = input("entrez la seconde valeur: ")

donnee3 = input("entrez la troisieme donnee: ")
valeur3 = input("entrez la troisieme valeur: ")

# Crée un dictionnaire avec les données saisies
dictionnaire = {
    donnee1: valeur1,
    donnee2: valeur2,
    donnee3: valeur3
}

print("Dictionnaire genere: \n")
print(dictionnaire)

# Demande à l'utilisateur de saisir le mot de passe à deviner
print("Saisie du mot de passe à craquer \n")
mot_de_passe_secret = input("Entrez le mot de passe à deviner : ")

# Récupère les valeurs du dictionnaire sous forme de liste
valeurs_a_tester = list(dictionnaire.values())

print("Tentative de cracking...\n")

trouve = False

# Boucle sur chaque valeur pour tenter de trouver le mot de passe
for essai in valeurs_a_tester:
    print(f"Essai avec : {essai}")
    if essai == mot_de_passe_secret:
        print(f"Mot de passe trouvé : {essai}\n")
        trouve = True
        break

# Si aucune valeur ne correspond, affiche un message d'échec
if not trouve:
    print("\nMot de passe introuvable dans les valeurs du dictionnaire.")