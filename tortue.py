#auteur: William Levasseur Lafrenière 
#date: 2026-10-29
#description: quiz 3


liste_tortues = []



# Recette — Valider un intervalle numérique
valide = False
while not valide:
    try:
        Nombre_de_tortue =int(input("Nombre de tortue (5 à 10) : ")) # ou conversion avec float()
        if 5 <= Nombre_de_tortue <= 10:
            valide = True
        else:
            print("Le nombres de tortues doit être entre 5 et 10.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

# Nombre_de_tortue =int(input("Nombre de tortue (5 à 10) : "))


i = 1


for i in range(Nombre_de_tortue):
    i = i + 1
    longueur =float(input(f"Carapace de la tortue {i} (cm): "))
    liste_tortues.append(longueur)
print("")
print("")
print("Résultat de l'inventaire")
print(f"Carapace saisie : {liste_tortues}")
liste_tortues.insert(1, 12.3)
print(f"Tortue oubliée ajouté en position 2 : {liste_tortues}")
print(f"Nombre se tortues mesuré : {(len(liste_tortues))}")
print(f"PLus petite carapace : {(min(liste_tortues))}")
print(f"Plus grande carapace : {(max(liste_tortues))}")
liste_tortues.sort(reverse=True)
print(f"De la plus grande à la plus petite : {liste_tortues}")



