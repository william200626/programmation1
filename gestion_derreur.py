# aureur: William Lvasseur LAfrenière
# date: 29 septembre 2026
#description: gestion derreur


# print("debut")

# try:
#     age = int(input("quel est ton age "))
#     valeur_de_divison = int(input("on divise par quoi "))
#     try:
#         age = age / valeur_de_divison
#     except:
#         print("erreur")




#     print(age)
# except NameError:
#     print("erreur de variable")
# except ZeroDivisionError:
#     print("pas div par 0")
# except ValueError:
#     print("inscrire un chiffre")
# except:
#     print("une erreur")

# print("fin")

# # ============================================


# valide = False
# while valide == False:

#     try:
#         age = int(input("quel est ton age:"))
#         age = age + 1

#         valide = True
#     except:
#         print("erreur")


# print ("fin")


# #=======================================
# # Recette — Valider un entier
# valide = False
# while not valide:
#     try:
#         age = int(input("Entrez votre âge : "))
#         valide = True
#     except ValueError:
#         print("Ce n'est pas un nombre entier.")

# #=========================================
# # Recette — Valider un nombre réel

# valide = False
# while not valide:
#     try:
#         prix = float(input("Entrez un prix : "))
#         valide = True
#     except ValueError:
#         print("Ce n'est pas un nombre valide.")

#=========================================
# # Recette — Valider une chaîne non vide
# nom = input("Entrez votre nom : ").strip()
# while nom == "":
#     print("Le nom ne peut pas être vide.")
#     nom = input("Entrez votre nom : ").strip()

#============================================
# # Recette — Valider un intervalle numérique
# valide = False
# while not valide:
#     try:
#         note = int(input("Entrez une note (0 à 100) : ")) # ou conversion avec float()
#         if 0 <= note <= 100:
#             valide = True
#         else:
#             print("La note doit être entre 0 et 100.")
#     except ValueError:
#         print("Ce n'est pas un nombre entier.")

#=========================================
# # Recette — Valider l'appartenance à un ensemble de valeurs
# choix_valides = (1, 2, 3, 4)

# valide = False
# while not valide:
#     try:
#         choix = int(input("Votre choix (1 à 4) : "))
#         if choix in choix_valides:
#             valide = True
#         else:
#             print("Choix invalide.")
#     except ValueError:
#         print("Ce n'est pas un nombre entier.")

# #=============================================
# # Exemple avec des chaînes de caractères
# reponses_valides = ("o", "n")

# reponse = input("Continuer ? (o/n) : ").strip().lower()
# while reponse not in reponses_valides:
#     print("Réponse invalide.")
#     reponse = input("Continuer ? (o/n) : ").strip().lower()


