# auteur: William Levasseur Lafrenière 
#date: 2026-10-06
#description: Examen1



#constante
PETIT = 1 
MOYEN = 2
LARGE = 3
X_LARGE = 4

OBJECTIF_PETIT = 5.0
OBJECTIF_MOYEN = 7.0
OBJECTIF_LARGE = 8.0
OBJECTIF_X_LARGE =10.0

RCETTES_MAX = 0
RECETTES_MIN = 40


#format de pizza
commande = int(input(" quel est votre commande (1 à 4): "))
match commande:
    case 1:
        print("petit")
    case 2:
        print("moyen")
    case 3:
        print("large")
    case 4:
        print("x-large")
    case _:
         print("Ce format n'est pas offert. Recommencer, SVP")




# combien de jour
jour = int(input("La machine à été en marche pendant combien de jour cette semaine (1-7) : "))

print(jour)



nb_jour = 0
prix_min = 40
total = 0
j = 0
moyenne = 0
#commande
while nb_jour < jour:
    recettes = float(input("Quelle recette on été prise : "))

    #calcul min
    while recettes < prix_min :
        prix_min = recettes

    #calcul total
    total = total + recettes

    #moyenne
    j = j + 1        
    moyenne = moyenne + recettes


    nb_jour = nb_jour + 1

moyenne = moyenne / nb_jour


#bilan
ligne = ""
print(f"{ligne:~<50}")
if commande == 1:
    print(f"| Format de pizza       : {"":>17}petit |")
elif commande == 2:
    print(f"| Format de pizza       : {"":>17}Moyen |")
elif commande == 3:
    print(f"| Format de pizza       : {"":>17}Large |")
elif commande == 4:
    print(f"| Format de pizza       : {"":>15}X-large |")
print(f"| Nombre de jours       : {nb_jour:>22} |")
print(f"| Recette total         : {total:>20.2f} $ |")
print(f"| Plus faible jour      : {prix_min:>20.2f} $ |")
if commande == 1:
    print(f"| Objectif par jour     : {OBJECTIF_PETIT:>20.2f} $ |")
elif commande == 2:
    print(f"| Objectif par jour     : {OBJECTIF_MOYEN:>20.2f} $ |")
elif commande == 3:
    print(f"| Objectif par jour     : {OBJECTIF_LARGE:>20.2f} $ |")
elif commande == 4:
    print(f"| Objectif par jour     : {OBJECTIF_X_LARGE:>20.2f} $ |")
print(f"| Moyenne par jour      : {moyenne:>20.2f} $ |")
print(f"| Objectif manqué       : {1:>16} sur {3} |")
print(f"| Niveau                : {1:>22} |")
print(f"{ligne:~<50}")






















