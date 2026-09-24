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

Requin = 1
Tigre = 2
Gnou = 3
Indice_De_Vitalité = 100

import math

print("----------------INFORMATION SUR LE SPÉCIMEN----------------")
Nom =str(input("Nom de l'animal : "))
Espece =int(input("Espèce de l'animal (1 = requin, 2 = tigre, 3 = gnou): "))
Âge_total_en_mois =int(input("Âge de l'animal (en mois) : "))
Masse_en_livres =float(input("Masse de l'animal (en livres) : "))
Température_corporelle_en_Fahrenheit =float(input("Température corporelle de l'animal (en °F) : "))

masse_en_kg =  Masse_en_livres * 0.45359237
nombre_année = (Âge_total_en_mois // 12)
restant_mois = (Âge_total_en_mois % 12)
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
    print(f"Masse (kg)                               {masse_en_kg:.2f}   {REQUIN_MASSE_MIN}-{REQUIN_MASSE_MAX}")
    print("----------------------------------------------------------------------")
    print("conversions")
    print(f"Masse          :         {Masse_en_livres:.2f} lbs  =    {masse_en_kg:.2f} kg")
    print(f"Température    :         {Température_corporelle_en_Fahrenheit:.2f} °F   =    {Température_corporelle_en_celcius:.2f} °C")
    print("----------------------------------------------------------------------")
    if (f"{Température_corporelle_en_celcius:.2f} = {REQUIN_TEMP_MAX:.2f} and {Âge_total_en_mois:.2f} = {REQUIN_ADULTE:.2f}"):
        print("Mesure à la limite                : oui")
    else:
        print("Mesure à la limite                : non")
    print("----------------------------------------------------------------------")
    if(Température_corporelle_en_celcius > REQUIN_TEMP_MAX or Température_corporelle_en_celcius < REQUIN_TEMP_MIN):
        Indice_De_Vitalité = Indice_De_Vitalité -30
    if(masse_en_kg > REQUIN_MASSE_MAX or masse_en_kg < REQUIN_MASSE_MIN):
        Indice_De_Vitalité = Indice_De_Vitalité -20
    print(f"Indice de vitalité : {Indice_De_Vitalité} / 100")
    if( Indice_De_Vitalité < 100 and Indice_De_Vitalité > 50):
        print("VERDICT : SURVEILLANCE")
    elif( Indice_De_Vitalité == 50):
        print("VERDICT : URGENCE")
    else:
        print("VERDICT : NORMAL")
    print("======================================================================")


if (Espece == Tigre):
    print(f"Patient                   : {Nom} (tigre)")
    if (Âge_total_en_mois < TIGRE_SENIOR):
        print(f"Âge                       : {nombre_année} ans et {restant_mois} mois (adulte)")
    else:
        print(f"Âge                       : {nombre_année} ans et {restant_mois} mois (sénior)")        

    print("Saisie                    : masse en lbs, température en °F")
    print("----------------------------------------------------------------------")
    print("mesure                                  valeur    Norme")
    print(f"Température (°C)                         {Température_corporelle_en_celcius:.2f}    {TIGRE_TEMP_MIN}-{TIGRE_TEMP_MAX}")
    print(f"Masse (kg)                               {masse_en_kg:.2f}   {TIGRE_MASSE_MIN}-{TIGRE_MASSE_MAX}")
    print("----------------------------------------------------------------------")
    print("conversions")
    print(f"Masse          :         {Masse_en_livres:.2f} lbs  =    {masse_en_kg:.2f} kg")
    print(f"Température    :         {Température_corporelle_en_Fahrenheit:.2f} °F   =    {Température_corporelle_en_celcius:.2f} °C")
    print("----------------------------------------------------------------------")
    if (f"{Température_corporelle_en_celcius:.2f} = {TIGRE_TEMP_MAX:.2f} and {Âge_total_en_mois:.2f} = {TIGRE_ADULTE:.2f}"):
        print("Mesure à la limite                : oui")
    else:
        print("Mesure à la limite                : non")
    print("----------------------------------------------------------------------")
    if(Température_corporelle_en_celcius > TIGRE_TEMP_MAX or Température_corporelle_en_celcius < TIGRE_TEMP_MIN):
        Indice_De_Vitalité = Indice_De_Vitalité -30
    if(masse_en_kg > TIGRE_MASSE_MAX or masse_en_kg < TIGRE_MASSE_MIN):
        Indice_De_Vitalité = Indice_De_Vitalité -20
    print(f"Indice de vitalité : {Indice_De_Vitalité} / 100")
    if( Indice_De_Vitalité < 100 and Indice_De_Vitalité > 50):
        print("VERDICT : SURVEILLANCE")
    elif( Indice_De_Vitalité == 50):
        print("VERDICT : URGENCE")
    else:
        print("VERDICT : NORMAL")
    print("======================================================================")
    




if (Espece == Gnou):
    print(f"Patient                   : {Nom} (gnou)")
    if (Âge_total_en_mois < GNOU_SENIOR):
        print(f"Âge                       : {nombre_année} ans et {restant_mois} mois (adulte)")
    else:
        print(f"Âge                       : {nombre_année} ans et {restant_mois} mois (sénior)")

    print("Saisie                    : masse en lbs, température en °F")
    print("----------------------------------------------------------------------")
    print("mesure                                  valeur    Norme")
    print(f"Température (°C)                         {Température_corporelle_en_celcius:.2f}    {GNOU_TEMP_MIN}-{GNOU_TEMP_MAX}")
    print(f"Masse (kg)                               {masse_en_kg:.2f}   {GNOU_MASSE_MIN}-{GNOU_MASSE_MAX}")
    print("----------------------------------------------------------------------")
    print("conversions")
    print(f"Masse          :         {Masse_en_livres:.2f} lbs  =    {masse_en_kg:.2f} kg")
    print(f"Température    :         {Température_corporelle_en_Fahrenheit:.2f} °F   =    {Température_corporelle_en_celcius:.2f} °C")
    print("----------------------------------------------------------------------")
    if (f"{Température_corporelle_en_celcius:.2f} = {GNOU_TEMP_MAX:.2f} and {Âge_total_en_mois:.2f} = {GNOU_ADULTE:.2f}"):
        print("Mesure à la limite                : oui")
    else:
        print("Mesure à la limite                : non")
    print("----------------------------------------------------------------------")
    if(Température_corporelle_en_celcius > GNOU_TEMP_MAX or Température_corporelle_en_celcius < GNOU_TEMP_MIN):
        Indice_De_Vitalité = Indice_De_Vitalité -30
    if(masse_en_kg > GNOU_MASSE_MAX or masse_en_kg < GNOU_MASSE_MIN):
        Indice_De_Vitalité = Indice_De_Vitalité -20
    print(f"Indice de vitalité : {Indice_De_Vitalité} / 100")
    if( Indice_De_Vitalité < 100 and Indice_De_Vitalité > 50):
        print("VERDICT : SURVEILLANCE")
    elif( Indice_De_Vitalité == 50):
        print("VERDICT : URGENCE")
    else:
        print("VERDICT : NORMAL")
    print("======================================================================")



if (Espece > 3):
    print("ERREUR : code d'espece inconnu")
    print("Espèces acceptées : 1 = requin, 2 = tigre, 3 = gnou.")
    print("Bilan interrompu.")
    print("======================================================================")





