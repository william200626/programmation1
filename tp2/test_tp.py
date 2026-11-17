# auteur: William Levasseur Lafrenière 
#date: 2026-22-17
#description: tp2

#-----------------------------------------
# import
import random
import colorama
from colorama import Fore, Back, Style, init 

from donnees_tp2 import CAPITALES_ETATS, CAPITALES_PAYS, CAPITALES_PROVINCES, PAYS,PROVINCES, ETATS

random.seed(1000)
#-----------------------------------------
# constantes

LIGNE = ""




#-----------------------------------------
#fonction



# Recette — Valider une chaîne non vide
def lire_texte(message):
    valeur =str(input(message)).strip()
    while valeur == "":
        print(f"{Fore.RED}La valeur ne peut pas être vide.{Style.RESET_ALL}")
        valeur = input(message).strip()
    return valeur

def construire_liste(option_mode):
    if(option_mode == 1):
        liste_lieu = PAYS
        liste_reponce = CAPITALES_PAYS
    else:
        liste_lieu = PAYS + ETATS + PROVINCES
        liste_reponce = CAPITALES_PAYS + CAPITALES_ETATS + CAPITALES_PROVINCES

    return liste_lieu, liste_reponce        

def menu_fonction(LIGNE):
    print(f"/{LIGNE:-<76}\\")
    print(f"|{"Jeu questionnaire - Les capitales":^76}|")
    print(f"|{"réalisé par William Levasseur Lafrenière":^76}|")
    print(f"\\{LIGNE:-<76}/")
    print("")


# example = construire_liste(1)

#-----------------------------------------
# programme principal
#Tableau
menu = menu_fonction(LIGNE="")

nom = lire_texte("Votre nom:")
print("")

k = 0
while k == 0:
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
                print(f"{Fore.RED}Erreur : entrez un nombre entre 1 et 2.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Ce n'est pas un nombre entier.{Style.RESET_ALL}")

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
                print(f"{Fore.RED}Erreur : entrez un nombre entre 1, 2 et 3.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Ce n'est pas un nombre entier.{Style.RESET_ALL}")

    if Choix_difficulte == 1:
        Nb_question = 5
    elif Choix_difficulte == 2:
        Nb_question = 10
    else:
        Nb_question = 15


    #questionaire
    liste_bonne_reponse = []
    liste_mauvaise_reponse = []
    liste_lieu = []


    liste_lieux, liste_capitales = construire_liste(Choix_mode)


    j = 0
    erreur = 0
    for i in range(Nb_question):
        valeur_aleatoire = random.randrange(0,len(liste_lieux))
        liste_valeur_aleatoire = random.sample(range(0, len(liste_lieux)), Nb_question)
        print(f"Question {i+1} de {Nb_question} - {liste_lieux[valeur_aleatoire]}")
        reponce=str(input("Capitale : "))
        if reponce == liste_capitales[valeur_aleatoire]:
            j += 1
        if reponce == liste_capitales[valeur_aleatoire]:
            print(f"{Fore.GREEN}Bonne réponce! Pointage : {j}/{i+1}{Style.RESET_ALL}")
        else:
            erreur += 1
            print(f"{Fore.RED}Mauvaise réponce. On cherchait : {liste_capitales[valeur_aleatoire]}. Pointage : {j}/{i+1}{Style.RESET_ALL}")
            liste_mauvaise_reponse.append(reponce)
            liste_bonne_reponse.append(liste_capitales[valeur_aleatoire])
            liste_lieu.append(liste_lieux[valeur_aleatoire])


    #pointage
    print(f"{LIGNE:*<78}")
    print(F"{nom}, votre pointage est de {j} sur {i+1} ({j * 100 // i} %).")

    #calcul pourcentage
    if j * 100 / i > 99:
        print("Parfait! Un vrai globe-trotter!")
    elif j * 100 / i <= 99 and j * 100 / i >=80:
        print("Excellent!")
    elif j * 100 / i <= 79 and j * 100 / i >=60:
        print("Bon travail!")
    elif j * 100 / i <= 59 and j * 100 / i >=40:
        print("Pas mal, mais l'atlas pourrait vous aider.")
    else:
        print("Il est temps de sortir l'atlas!")
    print(LIGNE)

    print(f"{LIGNE:*<78}")
    #réviser
    print(f"{"À RÉVISER":^78}")
    print(f"{LIGNE:-<78}")
    print(f"Lieu {"| Votre réponce   |":>46}")
    print(f"{LIGNE:-<78}")
    for i in range(erreur):
        print(f"{liste_lieu[0]:<31} | {liste_mauvaise_reponse[0]:<15} | {liste_bonne_reponse[0]}")
        liste_mauvaise_reponse.pop(0)
        liste_bonne_reponse.pop(0)
        liste_lieu.pop(0)


    # Recette — Valider l'appartenance à un ensemble de valeurs
    choix_valides = ("o", "n")

    valide = False
    while not valide:
        try:
            choix = str(input("Voulez-vous rejouer? (o/n) : "))
            if choix in choix_valides:
                valide = True
            else:
                print(f"{Fore.RED}Erreur : répondez par o ou n.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Ce n'est pas un nombre entier.{Style.RESET_ALL}")
        if choix == "n":
            k +=1




#-----------------------------------------










