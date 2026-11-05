

# for i in range(1, 21):
#     print(i, "", end="")
# print("")
# for j in range(1, 20, 2):
#     print(j, "", end="")

import random
# for a in range(10, 20, -1):
#     print(a)
NB_QUESTIONS = 9
MONDE = 1

noms = ["Brouillette", "Adam", "Lanouette", "Bissonette"]
prenoms = ["Davis", "Benoit", "Nicole", "Gérard"]

random.seed(1000)
valeur_aléatoire = random.randrange(0,len(noms))
liste_valeur_aloeatoire = random.sample(range(0, len(liste_questions), NB_QUESTIONS))

print(valeur_aléatoire)
print(f"Noms: {noms[valeur_aléatoire]} Prénom: {prenoms[valeur_aléatoire]}")

question = prenoms[valeur_aléatoire]
reponse = noms[valeur_aléatoire]

reponse_utilisateur = input(f"yo nom? {prenoms[valeur_aléatoire]}")

if (reponse_utilisateur == reponse):
    print(f"WOW ses {noms[valeur_aléatoire] , prenoms[valeur_aléatoire]}")
else:
    print("erreur")






