"""Examen 2 - Programme 2 - Kiosque de la fête de quartier (420-116-RI, A2026).

Affiche les ventes du kiosque (une ligne par article, une colonne par heure)
avec la meilleure heure de chaque article, puis le total de chaque heure, la
meilleure vente de la journée et le nombre d'heures payantes.

Auteur : __________
Date   : __________
"""
# ---------------------------------------------------------------------------
# Import
# ---------------------------------------------------------------------------
# from utilitaires import 
# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR = 54
ARTICLES = ("Limonade", "Maïs soufflé", "Barbe à papa", "Hot-dog", "Popsicle")
# VENTES[l][c] : nombre d'unités de ARTICLES[l] vendues pendant l'heure c + 1
VENTES = [
    [14, 22, 31, 18],
    [9, 17, 12, 21],
    [6, 11, 25, 16],
    [19, 34, 27, 13],
    [11, 15, 29, 24],
]
SEUIL_PAYANT = 20


# ---------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation.

    Args:
        caractere (str): Le caractère répété LARGEUR fois.
    """
    print(caractere * LARGEUR)


def calculer_maximum(ligne):
    """Trouve la plus grande valeur d'une liste.

    Args:
        ligne (list): Les valeurs d'une ligne.

    Returns:
        int: La plus grande valeur.
    """
    maximum = ligne[0]
    for valeur in ligne:
        if valeur > maximum:
            maximum = valeur
    return maximum


def afficher_tableau(articles, ventes, seuil):
    """Affiche le tableau des ventes de la journée.

    Chaque ligne contient le nom de l'article, ses ventes de chaque heure (suivies d'une marque « $ »
    si elles atteignent le seuil) et ses meilleures ventes en une heure.

    Args:
        articles (tuple): Le nom des articles.
        ventes (list): La liste 2D des ventes (une ligne par article).
        seuil (int): Les ventes minimales d'une heure payante.
    """
    # Ligne des titres : une colonne par heure
    print(f"{'Article':<14}", end="")
    for no_col in range(len(ventes[0])):
        print(f"{'H' + str(no_col + 1):>8}", end="")
    print(f"{'Max':>8}")
    afficher_separateur("-")
    # for i in range(len(articles)):
    #     print(f"{articles[i]:>8}", end="")
    #     for j in range(len(ventes)):
    #         print(f"{ventes[i]:>8}")


def affivher_mote_eleves(liste_notes):
    for i in range(len(liste_notes)):
        print(f"élève : {i+1}")
        for j in range(len(liste_notes[i])):
            print(f"Examen : {j+1}: {liste_notes[i][j]}")
            
    print("")


    # TODO 1 : afficher une ligne par article : son nom,
    #          ses ventes de chaque heure (chacune suivie
    #          de « $ » si elle atteint le seuil, d'une espace sinon),
    #          puis ses meilleures ventes, obtenues avec calculer_maximum().
    pass


def calculer_total_heure(ventes, no_col):
    """Calcule le total des ventes d'une heure (une colonne).

    Args:
        ventes (list): La liste 2D des ventes.
        no_col (int): L'index de la colonne (0 pour la première).

    Returns:
        int: Le total des ventes de cette heure.
    """
    # TODO 2
    pass


def trouver_meilleure_vente(ventes):
    """Trouve la meilleure vente de la journée et sa position.

    En cas d'égalité, on garde la première rencontrée.

    Args:
        ventes (list): La liste 2D des ventes.

    Returns:
        tuple: L'index de l'article, l'index de l'heure et les ventes.
    """
    # TODO 3 : parcours par index, sans max()
    pass


def compter_heures_payantes(ventes, seuil):
    """Compte les heures payantes (ventes qui atteignent le seuil).

    Args:
        ventes (list): La liste 2D des ventes.
        seuil (int): Les ventes minimales d'une heure payante.

    Returns:
        int: Le nombre de valeurs supérieures ou égales au seuil.
    """
    # TODO 4
    pass


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Affiche les ventes de la journée."""
    afficher_separateur("=")
    print(f"{'KIOSQUE DE LA FÊTE DE QUARTIER':^{LARGEUR}}")
    afficher_separateur("=")
    afficher_tableau(ARTICLES, VENTES, SEUIL_PAYANT)
    afficher_separateur("-")
    

    # TODO 5 : afficher la ligne « Total » (un total par heure),
    #          une ligne de « = », la meilleure vente de la journée
    #          et le nombre d'heures payantes.


# if __name__ == "__main__":
#     main()
afficher_separateur("=")
print(f"{'KIOSQUE DE LA FÊTE DE QUARTIER':^{LARGEUR}}")
afficher_separateur("=")
afficher_tableau(ARTICLES, VENTES, SEUIL_PAYANT)
afficher_separateur("-")