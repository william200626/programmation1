import csv
import json

INDEX_COLONE_NOM = 0
INDEX_COLONE_NBVIE = 1


# liste_produits = []
# with open("menu.csv", "r", encoding="utf-8") as fichier:
#     lecteur = csv.reader(fichier,delimiter=",")
#     for champs in lecteur:
#         print(champs)




def sauvegarder_liste_csv(liste_valeurs, liste_valeurs_entete,nom_de_fichier):#sauvgarde d'une liste format csv
    with open(nom_de_fichier, "w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(liste_valeurs_entete)
        ecrivain.writerows(liste_valeurs)


def charger_liste_csv(nom_de_fichier):
    with open(nom_de_fichier, "r", encoding="utf-8", newline="") as fichier:
        liste_valeur = []
        lecteur = csv.reader(fichier)
        next(lecteur)

        # pour toute les ligne
        for ligne in lecteur:
            #ajoute a la liste
            liste_valeur.append(ligne)

        return liste_valeur

def retirer_vie_csv(liste_personnages):
    for personnage in liste_personnages:
        nb_vie = int(personnage[INDEX_COLONE_NBVIE])
        if(nb_vie > 0):
            personnage[INDEX_COLONE_NBVIE] = nb_vie - 1
        else:
            liste_personnages.remove(personnage)
        
    return liste_personnages

def afficher_personnages_csv(liste_personnages):
    for personnage in liste_personnages:
        print(f"Nom: {personnage[INDEX_COLONE_NOM]} Vie(s): {personnage[INDEX_COLONE_NBVIE]}")

def main():
    liste_personnages = []

    with open("scores.json", "r", encoding="utf-8") as fichier:
        liste_personnages = json.load(fichier)

    liste_personnages.append(["CoinCoin", 100])

    with open("scores.json", "w", encoding="utf-8") as fichier:
        json.dump(liste_personnages, fichier, indent=4, ensure_ascii=False)



    # liste_personnages = charger_liste("personnages.csv")

    # afficher_personnages(liste_personnages)
    # liste_personnages = retirer_vie(liste_personnages)
    # retirer_vie(liste_personnages)

    # sauvegarder_liste(liste_personnages, ["Nom", "Nombre de vie"], "personnages,csv")


main()


