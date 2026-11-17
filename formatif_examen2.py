
def affivher_mote_eleves(liste_notes):
    for i in range(len(liste_notes)):
        print(f"élève : {i+1}")
        for j in range(len(liste_notes[i])):
            print(f"Examen : {j+1}: {liste_notes[i][j]}")

def calculer_nb_eleves(liste_notes):
    return len(liste_notes)

def calculer_nb_examens(liste_notes):
    if(len(liste_notes) > 0):
        return len(liste_notes[0])
    else:
        return 0


def afficher_note_examens(liste_notes):
    for i in range(len(liste_notes)):
        print(f"Examen {i+1}")
        nb_eleves = calculer_nb_eleves(liste_notes)
        for j in range(len(nb_eleves)):
            if(liste_notes[j][i] < 60):
                print(f"Étudiant {j+1}: {liste_notes[j][i]} (échec)")
            else:
                print(f"Étudiant {j+1}: {liste_notes[j][i]}")

def calculer_moyenne__pour_un_examen(liste_notes, index_examen):
    nb_eleves = calculer_nb_eleves(liste_notes)
    somme_examen = 0
    for j in range(nb_eleves):
        somme_examen += liste_notes[j][index_examen]

    moyenne = somme_examen / nb_eleves
    return moyenne

def calculer_moyenne_examens(liste_notes):
    for i in range(len(liste_notes)):
        nb_eleves = calculer_nb_eleves(liste_notes)
        somme_examen = 0
        for j in range(nb_eleves):
            somme_examen += liste_notes[j][i]

        moyenne = somme_examen / nb_eleves
        print(f"examen {i + 1}: moyenne {moyenne}")





notes = [
    [50, 90, 75],
    [70, 45, 80],
    [90, 80, 35],
]

# affivher_mote_eleves(notes)
# afficher_note_examens(notes)

# nb_examen = calculer_nb_examens(notes)
# print(nb_examen)
# calculer_moyenne_examens(notes)
nb_examen = calculer_nb_examens(notes)
for i in range(nb_examen):
    moyenne_examen = calculer_moyenne__pour_un_examen(notes, i)
    print(f"moyenne exam {i+1}: {moyenne_examen}")










