
#ouverture fichier en txt

liste_noms = []
with open("menu.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip())
        liste_noms.append(ligne.strip())

print(liste_noms)

with open("resultat.txt","w",encoding="utf-8") as fichier_resultat:
    for nom in liste_noms:
        fichier_resultat.write(f"{nom} \n")
    # fichier_resultat.writelines(liste_noms)

#avec nombre
with open("nombre.txt","r",encoding="utf-8") as fichier_nombre:
    for nombre in fichier_nombre:
        valeur_depart = float(nombre.strip())
        valeur_fin = valeur_depart + 10
        print(f"valeur départ {valeur_depart} valeur fin {valeur_fin}")

