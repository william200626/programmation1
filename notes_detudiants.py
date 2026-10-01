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
calcul = 0
j = 0
i = 0
note_min = 0
NOTE_MAX = 100

while i < NOTE_A_DONNER:
    
    note = int(input("Donne une note : "))
    i = i + 1

    while note_min < note:
        note_min = note
         

    
    j = 0  #calcul de la moyenne
    while j < NOTE_POUR_J:
        j = j + 1
        
        calcul = calcul + note
  

#moyenne
print(calcul // 2)

    






