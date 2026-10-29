TAUX_TPS = 0.075


#fonction


def obtenir_nombre(nombre_minimal, nombre_maximal,type_nombre="nombre"):
    valide = False
    while not valide:
        try:
            nombre = int(input(f"entré un {type_nombre} ({nombre_minimal} à {nombre_maximal})")) 
            if nombre_minimal <= nombre <= nombre_maximal:
                valide = True
                return nombre
            else:
                print(f"La note doit être entre {nombre_minimal} et {nombre_maximal} ")
        except ValueError:
            print("Ce n'est pas un nombre entier.")



def afficher_menu(nom, options):
    print(f"Bonjour {nom}, bienvenue dans mon programme")
    print("-------------------------")
    # for option in liste_option:
    #     print(option)

    for i in range(len(options)):
        print(f"{i+1} - {options[i]}")
    print("-------------------------")
    valeur_menu = obtenir_nombre(1, len(options), "votre choix")
    return(valeur_menu)




def afficher_rectangle(hauteur, largeur, motif="* "):
    valeur_forme = calculer_forme(hauteur, largeur)
    for i in range(hauteur):
        for i in range(largeur):
            print(f"{motif}", end="")
        print("")
    print(f"fin de mon {valeur_forme}")

def afficher_carre(hauteur, motif="*"):
    largeur = hauteur
    afficher_rectangle(hauteur, largeur, motif)



#prog principal

liste_option = []
liste_option.append("Afficher un rectengle")
liste_option.append("Afficher un carré")
liste_option.append("Afficher un triangle")

print(obtenir_nombre)




# liste_option.append("biddon")
# liste_option.remove("biddon")

# liste_option.append("biddon2")
# liste_option.pop()

liste_option.sort(reverse=True)
print(liste_option)






valeur_du_menu = afficher_menu("Benoit", liste_option)

match(valeur_du_menu):
    case 1:
            print("...")
    case 2:
            print("ou ...")
    case 3:
            print("ou encore ...")
# afficher_menu("Pierre", ["A ...", "B ...", "c ...", "D ...", "E ..."])
# afficher_menu("Nicolle")










