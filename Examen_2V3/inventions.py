#auteur: William Levasseur Lafrenière 
#date: 2026-11-19
#description: Examen 2 partie 1

"""Examen 2 - Programme 1 - Quiz : les grandes inventions (420-116-RI, A2026).

Le joueur doit deviner l'année de grandes inventions et découvertes, tirées
au hasard. Une réponse exacte vaut 3 points et une réponse à 5 ans près
vaut 1 point. Les inventions et leurs années sont dans donnees_examen_2.py.
Après chaque partie, on affiche le pointage et les inventions à réviser.
À la fin, on affiche le nombre de parties et le meilleur résultat.

Auteur : __________
Date   : __________
"""

# TODO 1 : importer le module random, les fonctions lire_entier() et
#          lire_oui_non() de utilitaires.py, puis les listes INVENTIONS
#          et ANNEES de donnees_examen_2.py
# ---------------------------------------------------------------------------
# Import
# ---------------------------------------------------------------------------
import random
from utilitaires import lire_entier, lire_oui_non
from donnees_examen_2 import INVENTIONS, ANNEES
# ---------------------------------------------------------------------------
# liste
# ---------------------------------------------------------------------------
inventions_ratees = []
annees_ratees = []


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR = 60
ANNEE_MIN = 1700
ANNEE_MAX = 2026
NB_QUESTIONS_MIN = 3
POINTS_EXACT = 3
POINTS_PROCHE = 1
ECART_TOLERE = 5      # en années
SEMENCE = 66          # pour avoir les mêmes questions que l'exemple de l'énoncé
nb_question = 0

# ---------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------
def afficher_bienvenue():
    """Affiche la bannière et les règles du jeu."""
    print("=" * LARGEUR)
    print(f"{'QUIZ — LES GRANDES INVENTIONS':^{LARGEUR}}")
    print("=" * LARGEUR)
    print(f"Réponse exacte : {POINTS_EXACT} points. "
          f"À {ECART_TOLERE} ans près : {POINTS_PROCHE} point.")


def calculer_pourcentage(points, points_max):
    """Calcule un pourcentage de réussite, arrondi à l'entier.

    Args:
        points (int): Les points obtenus.
        points_max (int): Le nombre maximal de points.

    Returns:
        int: Le pourcentage de réussite.
    """
    return round(points / points_max * 100)


def afficher_revision(inventions_ratees, annees_ratees):
    """Affiche la liste des inventions à réviser.

    Args:
        inventions_ratees (list): Les inventions pour lesquels le joueur
            n'a obtenu aucun point.
        annees_ratees (list): Les années de ces inventions, associées par
            l'index à inventions_ratees.
    """
    print()
    print("À RÉVISER")
    print("-" * LARGEUR)
    if len(inventions_ratees) == 0:
        print("Rien à réviser, bravo!")
    else:
        for i in range(len(inventions_ratees)):
            print(f"{annees_ratees[i]}  {inventions_ratees[i]}")
    print("-" * LARGEUR)


def calculer_points(reponse, annee):
    """Calcule les points obtenus pour une réponse.

    Args:
        reponse (int): L'année donnée par le joueur.
        annee (int): L'année exacte de l'invention.

    Returns:
        int: POINTS_EXACT si la réponse est exacte, POINTS_PROCHE si elle
            est à ECART_TOLERE ans près ou moins, 0 sinon.
    """
    # TODO 2 : indice : abs(x) renvoie la valeur absolue de x
    valeur_aleatoire = random.randrange(0,len(INVENTIONS))
    liste_valeur_aleatoire = random.sample(range(0, len(INVENTIONS)), nb_question)
    if reponse == ANNEES[valeur_aleatoire]:
        print(f"Exact! +{POINTS_EXACT}")
    # elif reponse < {ANNEES[valeur_aleatoire] + ECART_TOLERE} and reponse > {ANNEES[valeur_aleatoire - ECART_TOLERE]}:
    #     print(f"Preque! C'était en {ANNEES[valeur_aleatoire]}. +{POINTS_PROCHE}")
    else:
        print(f"Non, c'étais en {ANNEES[valeur_aleatoire]}.")
        inventions_ratees.append(reponse)
        annees_ratees.append(ANNEES[valeur_aleatoire])
    pass

def jouer_partie(nb_questions):
    """Joue une partie, puis affiche le pointage et la révision.

    Les inventions sont tirées au hasard, sans répétition.

    Args:
        nb_questions (int): Le nombre de questions de la partie.

    Returns:
        int: Le pourcentage de réussite de la partie.
    """
    # TODO 3 : voir l'énoncé (tirage avec random.sample(), questions
    #          numérotées, rétroaction, listes des inventions ratées, bilan)
    for i in range(lire_entier(message="Nombre de questions (3 à 25): ",maximum=25, minimum=NB_QUESTIONS_MIN)):
            valeur_aleatoire = random.randrange(0,len(INVENTIONS))
            liste_valeur_aleatoire = random.sample(range(0, len(INVENTIONS)), nb_question)
            print(f"Question {i+1} de {3} - {INVENTIONS[valeur_aleatoire]}")
            reponse=int(input("Année : "))
            calculer_points(reponse,ANNEES)
            print("")

    pass

# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Fait jouer des parties tant que le joueur veut rejouer."""
    afficher_bienvenue()
    random.seed(SEMENCE) # À commenter pour avoir des questions aléatoires

    # TODO 4 : voir l'énoncé (nombre de questions, rejouer, résultats)
rejouer = 0
if __name__ == "__main__":
    main()
print("")
while rejouer == 0:
    jouer_partie(nb_question)
    afficher_revision(inventions_ratees,annees_ratees)
    choix_valides = ("o", "n")

    valide = False
    while not valide:
        try:
            choix = str(input("Voulez-vous rejouer? (o/n) : "))
            if choix in choix_valides:
                valide = True
            else:
                print(f"Erreur : répondez par o ou n.")
        except ValueError:
            print(f"Ce n'est pas un nombre entier.")
        if choix == "n":
            rejouer +=1















