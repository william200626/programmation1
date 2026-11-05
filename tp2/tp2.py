# auteur: William Levasseur Lafrenière 
#date: 2026-22-17
#description: tp2

#-----------------------------------------
# import
import random
import colorama

from donnees_tp2 import CAPITALES_ETATS, CAPITALES_PAYS, CAPITALES_PROVINCES, PAYS,PROVINCES, ETATS

random.seed(1000)
#-----------------------------------------
# constantes

LIGNE = ""




#-----------------------------------------
#def

# Recette — Valider une chaîne non vide
def lire_texte(Nom):
    Nom =str(input("Votre nom : ")).strip()
    while Nom == "":
        print("Le nom ne peut pas être vide.")
        Nom = input("Votre nom : ").strip()

def construire_liste(option_mode):
    if(option_mode == 1):
        liste_lieu = PAYS
        liste_reponce = CAPITALES_PAYS
    else:
        liste_lieu = PAYS + ETATS + PROVINCES
        liste_reponce = CAPITALES_PAYS + CAPITALES_ETATS + CAPITALES_PROVINCES

    return liste_lieu, liste_reponce        

# example = construire_liste(1)

#-----------------------------------------
# programme principal
#Tableau
print(f"/{LIGNE:-<76}\\")
print(f"|{"Jeu questionnaire - Les capitales":^76}|")
print(f"|{"réalisé par William Levasseur Lafrenière":^76}|")
print(f"\\{LIGNE:-<76}/")
print("")
lire_texte(Nom="")
print("")

#Choisir mode
print("MONDE DE JEU")
print("  1 - Srandart (196 pays du monde)\n  2 - Aventure (259 lieux : pays + provinces et territoires du Canada + États américans)")
valide = False
while not valide:
    try:
        Choix_mode =int(input("Votre choix : "))
        if 1 <= Choix_mode <= 2:
            valide = True
        else:
            print("Erreur : entrez un nombre entre 1 et 2.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

#Choisir difficulté
print("NIVEAU DE DIFFICULTÉ")
print("  1 - Facile (5 questions)\n  2 - Normal (10 questions)\n  3 - Avancé (15 questions)")
valide = False
while not valide:
    try:
        Choix_difficulte =int(input("Votre choix : ")) # ou conversion avec float()
        if 1 <= Choix_difficulte <= 3:
            valide = True
        else:
            print("Erreur : entrez un nombre entre 1, 2 et 3.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

if Choix_difficulte == 1:
    Nb_question = 5
elif Choix_difficulte == 2:
    Nb_question = 10
else:
    Nb_question = 15



j = 0
if Choix_mode == 1:
    for i in range(Nb_question):
        valeur_aleatoire = random.randrange(0,len(PAYS))
        liste_valeur_aleatoire = random.sample(range(0, len(PAYS)), Nb_question)
        print(f"Question {i+1} de {Nb_question} - {PAYS[valeur_aleatoire]}")
        reponce=str(input("Capitale : "))
        if reponce == CAPITALES_PAYS[valeur_aleatoire]:
            j += 1
        if reponce == CAPITALES_PAYS[valeur_aleatoire]:
            print(f"Bonne réponce! Pointage : {j}/{i+1}")
        else:
            print(f"Mauvaise réponce. On cherchait : {CAPITALES_PAYS[valeur_aleatoire]}. Pointage : {j}/{i+1}")
else:        
    for i in range(Nb_question):
        valeur_aleatoire = random.randrange(0,len(PAYS + ETATS + PROVINCES))
        liste_valeur_aleatoire = random.sample(range(0, len(PAYS + ETATS + PROVINCES)), Nb_question)
        print(f"Question {i+1} de {Nb_question} - {(PAYS + ETATS + PROVINCES)[valeur_aleatoire]}")
        reponce=str(input("Capitale : "))
        if reponce == (CAPITALES_PAYS + CAPITALES_ETATS + CAPITALES_PROVINCES)[valeur_aleatoire]:
            j += 1
        if reponce == (CAPITALES_PAYS + CAPITALES_ETATS + CAPITALES_PROVINCES)[valeur_aleatoire]:
            print(f"Bonne réponce! Pointage : {j+1}/{i+1}")
        else:
            print(f"Mauvaise réponce. On cherchait : {(CAPITALES_PAYS + CAPITALES_ETATS + CAPITALES_PROVINCES)[valeur_aleatoire]}. Pointage : {j}/{i+1}")









# if (Choix_difficulte == 1):





#-----------------------------------------










