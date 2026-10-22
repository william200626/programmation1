#3

# liste_articles = []
# for i in range(4):
#     article = input("entrez un article: ").strip()
#     while article == "":
#         print("")
#         article = input("l'article ne peurta pas être vide").strip()
#         article = input("entrez un article: ")

#     liste_articles.append(article)

# for i in range(len(liste_articles)):
#     print(f"{i+1}. {liste_articles[i]}")

# nb_articles_total = len(liste_articles)
# print(f"{nb_articles_total} articles")

# ---------------------------------------------------------
#4

nombres = []
for i in range(5):
    valide = False
    while not valide:
        try:
            nombre = int(input("Entrez un nombre : "))
            valide = True
        except ValueError:
            print("Ce n'est pas un nombre entier.")

    nombres.append(nombre)



print(f"Liste : {nombres}")
print("Somme :", sum(nombres))

    















