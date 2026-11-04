


nombre = int(input("donne un nombre : "))


liste = []

while nombre > 0:
    modulo = nombre % 2
    nombre = nombre // 2
    
    liste.append(modulo)


liste.reverse()
print(liste)

