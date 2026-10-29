
def valider_entier():
    # Recette — Valider un entier
    valide = False
    while not valide:
        try:
            age = int(input("Entrez votre âge : "))
            valide = True
        except ValueError:
            print("Ce n'est pas un nombre entier.")



def nombre_reel():
    # Recette — Valider un nombre réel
    valide = False
    while not valide:
        try:
            prix = float(input("Entrez un prix : "))
            valide = True
        except ValueError:
            print("Ce n'est pas un nombre valide.")


def chaine_non_vide():
    # Recette — Valider une chaîne non vide
    nom = input("Entrez votre nom : ").strip()
    while nom == "":
        print("Le nom ne peut pas être vide.")
        nom = input("Entrez votre nom : ").strip()


def interval():
    # Recette — Valider un intervalle numérique
    valide = False
    while not valide:
        try:
            note = int(input("Entrez une note (0 à 100) : ")) # ou conversion avec float()
            if 0 <= note <= 100:
                valide = True
            else:
                print("La note doit être entre 0 et 100.")
        except ValueError:
            print("Ce n'est pas un nombre entier.")







