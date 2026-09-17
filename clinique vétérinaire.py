# auteur: William Levasseur LAfrenière 
#date: 2026-09-17
#description: TP Clinique vétérinaire

REQUIN_TEMP_MIN = 22
REQUIN_TEMP_MAX = 26
REQUIN_MASSE_MIN = 60
REQUIN_MASSE_MAX = 150
REQUIN_ADULTE = 60
REQUIN_SENIOR = 240
TIGRE_TEMP_MIN = 37,5
TIGRE_TEMP_MAX = 39
TIGRE_MASSE_MIN = 100
TIGRE_MASSE_MAX = 260
TIGRE_ADULTE = 36
TIGRE_SENIOR = 144
GNOU_TEMP_MIN = 37,5
GNOU_TEMP_MAX = 39
GNOU_MASSE_MIN = 120
GNOU_MASSE_MAX = 270
GNOU_ADULTE = 36
GNOU_SENIOR = 180

import math

Requin = 1
Tigre = 2
Gnou = 3


print("----------------INFORMATION SUR LE SPÉCIMEN----------------")

Nom =str(input("Nom de l'animal : "))
Espece =int(input("Espèce de l'animal : "))
Âge_total_en_mois =int(input("Âge de l'animal (en mois) : "))
Masse_en_livres =float(input("Masse de l'animal (en livres) : "))
masse_en_kg=  0.45359237


Température_corporelle_en_Fahrenheit =float(input("Température corporelle de l'animal (en °F) : "))


print(Nom)
if (Espece == Requin):
    print("Requin")

if (Espece == Tigre):
    print("Tigre")

if (Espece == Gnou):
    print("Gnou")


print(f"{Âge_total_en_mois // 12} ans   {Âge_total_en_mois % 12} mois")

print(f"{Masse_en_livres} lbs =  {Masse_en_livres / 0.45359237}")





