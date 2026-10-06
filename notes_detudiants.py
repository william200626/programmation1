# auteur: William Levasseur LAfrenière 
#date: 2026-09-17
#description: notes détudiants




nom = input("Quelle est le nom complet de l'étudiant : ").strip()
while nom == "":
    print("Le nom ne peut pas être vide.")
    nom = input("Entrez votre nom : ").strip()
print(nom)

NOTE_POUR_J = 1
NOTE_A_DONNER = 5
moyenne = 0
j = 0
i = 0
nombre_déchec = 0
note_min = 100
note_max = 0
NOTE_MAX = 100
écart = note_max - note_min


while i < NOTE_A_DONNER:
    
    note = int(input("Donne une note : "))
    i = i + 1

    while note_min > note:
        note_min = note

    while note_max < note:
        note_max = note

    if note < 60:
        nombre_déchec = nombre_déchec + 1

    
    j = 0  #calcul de la moyenne
    while j < NOTE_POUR_J:
        j = j + 1
        
        moyenne = moyenne + note
  
écart = note_max - note_min
moyenne = moyenne / 5
#moyenne
print(f"{moyenne:>12}")
print(note_min)
print(note_max)
print(écart)
print(nombre_déchec)

if moyenne >= 90:
    print("Excellent")
elif moyenne < 90 and moyenne >= 75:
    print("Très bien")
elif moyenne < 75 and moyenne >=60:
    print("Réussite")
else:
    print("Échec")





