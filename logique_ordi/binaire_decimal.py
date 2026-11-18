


nombre = int(input("donne un nombre : "))


liste_nombre = []

while nombre > 0:
    dernier_chiffre = nombre % 10
    liste_nombre.append(dernier_chiffre)
    nombre = nombre // 10
# liste_nombre.reverse()

    

resultat = 0
for i in (liste_nombre):
    resultat = resultat + liste_nombre[-1] * 2 ** i+1

print(resultat)




