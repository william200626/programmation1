
# for i in range(1,10,):
#     print(f"je tourne... tour #{i}")
#     print("...")

# print("fin")

#--------------------------------------

# nom = "david"
# for c in nom:
#     print(c)

# liste_personnage = ("mario", "luigi", "peach")
# for personnage in liste_personnage:
#     print(f"mon personnage se nomee {personnage}")

#----------------------------------------------------


# for i in range(10,0,-1):
#     print(f"{i} seconde...")

# print("décolage")

#----------------------------------------------

valide = False
while not valide:
    try:
        nb_ligne = int(input("Entrez un nombre de ligne(1 à 5) : ")) # ou conversion avec float()
        if 0 <= nb_ligne <= 5:
            valide = True
        else:
            print("Le nombre de lignes doit être entre 1 et 5.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")


nb_colone = nb_ligne
for i in range(nb_ligne):
    for j in range(nb_colone):
            print("*", end="")
    print("")
    nb_colone = nb_colone -1








#---------------------------------------------------------








