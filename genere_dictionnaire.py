# Ce script demande à l'utilisateur de saisir trois paires clé/valeur, puis génère un dictionnaire avec ces données.
# Enfin, il affiche le dictionnaire généré.
# Auteur : [kamdem keumogne rich bill]
# Date : 2025-05-31

donnee1 = input("entrez la premiere donnee: ")
valeur1 = input("entrez la premiere valeur: ")

donnee2 = input("entrez la seconde donnee: ")
valeur2 = input("entrez la seconde valeur: ")

donnee3 = input("entrez la troisieme donnee: ")
valeur3 = input("entrez la troisieme valeur: ")

dictionnaire = {
    donnee1: valeur1,
    donnee2: valeur2,
    donnee3: valeur3
}

print("Dictionnaire genere: \n")
print(dictionnaire)