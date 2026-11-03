# auteur: William Levasseur Lafrenière 
#date: 2026-22-17
#description: tp2

#-----------------------------------------
# import
import random
import colorama

from donnees_tp2 import CAPITALES_ETATS, CAPITALES_PAYS, CAPITALES_PROVINCES


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



#-----------------------------------------
# programme principal


print(f"/{LIGNE:-<76}\\")
print(f"|{"Jeu questionnaire - Les capitales":^76}|")
print(f"|{"réalisé par William Levasseur Lafrenière":^76}|")
print(f"\\{LIGNE:-<76}/")
print("")
lire_texte(Nom="")
print("")
print("MONDE DE JEU")
#-----------------------------------------










