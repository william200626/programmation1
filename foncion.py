
# fonction afficher carré
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

def calculer_aire_carre(hauteur):
    return calculer_aire_rectangle(hauteur,hauteur)

def calculer_aire_rectangle(hauteur, largeur):
    aire_rectangle = hauteur * largeur
    return aire_rectangle

def calculer_forme(hauteur, largeur):
        if(hauteur == largeur):
            forme = "carré"
        else:
            forme = "rectangle"
        return forme


def obtenir_nombre_de_carre(nombre_minimal, nombre_maximal,type_nombre="nombre"):
    valide = False
    while not valide:
        try:
            nombre = int(input(f"entré un {type_nombre} ({nombre_minimal} à {nombre_maximal})")) 
            if nombre_minimal <= nombre <= nombre_maximal:
                valide = True
                return nombre
            else:
                print("La note doit être entre 0 et 100.")
        except ValueError:
            print("Ce n'est pas un nombre entier.")


############################ prog principal ##############################

nombre_carre = obtenir_nombre_de_carre(1,10, "un nombre")
for i in range(1,nombre_carre+1):
    afficher_carre(i)


# for i in range(1,5):
#     afficher_carre(i,"#")
#     afficher_rectangle(i,i*2)
# for i in range(1,5):
#     valeur_aire = calculer_aire_carre(i)
#     print(f"la valeur de l'aire pour une hauteur de {i} est : {valeur_aire}")

# calculer_aire_rectangle(largeur=10,hauteur=10)
# print(calculer_aire_carre(10))












