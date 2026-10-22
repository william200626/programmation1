

# poules = ["pauline", "poulette", "pierrette", "yvette"]
# poules.append("marrie-poule")   #fin
# poules.insert(0,"jean-poule")   #nomporte où

# print(poules)
# nom_poule = poules.pop(0)
# print(nom_poule)





# for poule in poules:
#     print(poule)
# print(poules[3])
# --------------------------------------------------------
# poules = "pouline,poulette,jean,sam".split(",")

# # --------------------------------------------------------
# for i in range(len(poules)):
#     print(poules[i])

# # --------------------------------------------------------
# avions = [40,30,20,50,10]
# for avion in avions:
#     print(f"Avion #: {avion}")

# print("décollage en cours...")
# liste_decollage = avions.copy
# for avion in avions:
#     numéro_avion = liste_decollage.pop(0)
#     print(f"décollage de l'avion {numéro_avion}")


# print("décolage en cours")
# while(len(avions) > 0):
#     numéro_avion = avions.pop(0)
#     print(f"décollage de l'avion : {numéro_avion}")




# valeurs = ["a", "b", "b", "f", "c", "b", ]
# valeur_a_supprimer = "b"
# while valeur_a_supprimer in valeurs:
#     valeurs.remove(valeur_a_supprimer)
#     print(valeurs)

#-----------------------------------------------

# valeurs = [10,20,44,22,11,35]
# # valeurs.sort()
# valeurs_trier = sorted(valeurs)
# print(valeurs)
# print(valeurs_trier)

# valeurs_trier.sort(reverse=True)



# --------------------------------------------------------

# poules = [10,20,30,50,10] 
# print(max(poules))                #SA C VRAIMENT COOL!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(min(poules))
# print(len(poules))
# print(poules.count(10))



#=================================================
#on reparle des listes


# avions.append("d")
# avions.insert(0,"a")

# print(avions[0])
# print(avions[1])
# print(avions[1:3])
# print(avions[-1])



# avion = avions.pop(0)

# for avion in avions:
#     print (avion)

# for i in range(len(avions)):
#     print(avions[i])

# if "e" in avions:
#     print("youhou")
# else:
#     print("bouh")


# while "e"not in avions:
#     ...

# ************************************************
avions = ["a", "b", "c", "d"]


valide = False
while valide == False:
    valeur_avion = input("bojour c quoi ton avion")
    if valeur_avion in avions:
        avions.remove(valeur_avion)
    valide == True
    
else:
    print("existe pas")


    
print(avions)








