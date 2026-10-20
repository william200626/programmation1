#3

liste_articles = []
for i in range(4):
    article = input("Entrez votre nom : ").strip()
while article == "":
    print("entrez un article.")
    article = input("Entrez votre nom : ").strip()
    article = input("quel est l'article:")
    liste_articles.append(article)

for i in range(len(liste_articles)):
    print(f"{i+1}. {liste_articles[i]}")

nb_articles_total = len(liste_articles)
print(f"{}")