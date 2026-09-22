# auteur: William Levasseur LAfrenière 
#date: 2026-09-17
#description: TP Clinique vétérinaire

REQUIN_TEMP_MIN = 22.0
REQUIN_TEMP_MAX = 26.0
REQUIN_MASSE_MIN = 60.0
REQUIN_MASSE_MAX = 150.0
REQUIN_ADULTE = 60
REQUIN_SENIOR = 240
TIGRE_TEMP_MIN = 37.5
TIGRE_TEMP_MAX = 39.0
TIGRE_MASSE_MIN = 100.0
TIGRE_MASSE_MAX = 260.0
TIGRE_ADULTE = 36
TIGRE_SENIOR = 144
GNOU_TEMP_MIN = 37.5
GNOU_TEMP_MAX = 39.0
GNOU_MASSE_MIN = 120.0
GNOU_MASSE_MAX = 270.0
GNOU_ADULTE = 36
GNOU_SENIOR = 180




import math

Requin = 1
Tigre = 2
Gnou = 3


print("----------------INFORMATION SUR LE SPÉCIMEN----------------")

Nom =str(input("Nom de l'animal : "))
Espece =int(input("Espèce de l'animal (1 = requin, 2 = tigre, 3 = gnou): "))
Âge_total_en_mois =int(input("Âge de l'animal (en mois) : "))
Masse_en_livres =float(input("Masse de l'animal (en livres) : "))
Température_corporelle_en_Fahrenheit =float(input("Température corporelle de l'animal (en °F) : "))

masse_en_kg =  Masse_en_livres * 0.45359237
nombre_année = Âge_total_en_mois // 12
restant_mois = Âge_total_en_mois % 12
Température_corporelle_en_celcius = (Température_corporelle_en_Fahrenheit - 32) *(5/9)


print("======================================================================")
print(f"                    CLINIQUE VÉTÉRINAIRE EXOTIQUE")
print(f"                         DES ÎLES ST-MAURICE")
print("======================================================================")
if (Espece == Requin):
    print(f"Patient                   : {Nom} (requin)")
    if (Âge_total_en_mois < REQUIN_SENIOR):
        print(f"Âge                       : {nombre_année} ans et {restant_mois} mois (adulte)")
    else:
        print(f"Âge                       : {nombre_année} ans et {restant_mois} mois (sénior)")

print("Saisie                    : masse en lbs, température en °F")
print("----------------------------------------------------------------------")
print("mesure                                  valeur    Norme")
print(f"Température (°C)                         {Température_corporelle_en_celcius:.2f}    {REQUIN_TEMP_MIN}-{REQUIN_TEMP_MAX}")
print(f"Masse (kg)                              {masse_en_kg:.2f}    {REQUIN_MASSE_MIN}-{REQUIN_MASSE_MAX}")
print("----------------------------------------------------------------------")
print("conversions")
print(f"Masse          :         {Masse_en_livres:.2f} lbs =    {masse_en_kg:.2f} kg")
print(f"Température    :         {Température_corporelle_en_Fahrenheit:.2f} °F   =    {Température_corporelle_en_celcius:.2f} °C")



if (Espece == Tigre):
    print("Tigre")

if (Espece == Gnou):
    print("Gnou")




print(f"{Masse_en_livres} lbs =  {masse_en_kg} kg")

print(f"{Température_corporelle_en_Fahrenheit} °F =   {Température_corporelle_en_celcius}°C")



