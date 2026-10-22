
# ligne1 = [1,2,3,4]
# ligne2 = [5,6,7,8]
# ligne3 = [9,10,11,12]

# liste_valeurs = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# print(liste_valeurs[2])
# print(liste_valeurs[2][2])



# liste_avions = ["A", "B", "C", "D"]
# liste_marques_avions = ["Boing", "Airbus", "Airbus", "Bombardier"]
# index_de_mon_avion = liste_avions.index("C")

# print(liste_avions.index("C"))
# print(f"marque est : {liste_marques_avions[index_de_mon_avion]}")




# for i in range(len(liste_valeurs)):
#     for j in range(len(liste_valeurs[i])):
#         print(liste_valeurs[i][j])



# # for ligne in liste_valeurs:
#     for colonne in ligne:
#         print(colonne)



# for i in range(len(liste_valeurs)):
#     print(liste_valeurs[2][2])               #[i] [j]







# liste_chats = ["Minou", "Grisou", "Poupou", "Garfield"]
# liste_chatons = [["bebe1", "bebe2", "bebe3"], ["bebe4", "bebe5", "ronron"], ["Ponpon"], []]

# for i in range(len(liste_chats)):
#     chat_actuel = liste_chats[i]
#     print(f"Chat: {chat_actuel}")
#     for j in range(len(liste_chatons[i])):
#         chaton_actuel = liste_chatons[i][j]
#         print(f" Chaton: {chat_actuel}")



notes = [
    [78, 85, 92],    # ligne 0 : notes de l'étudiant 0
    [65, 70, 58],    # ligne 1 : notes de l'étudiant 1
    [90, 88, 95],    # ligne 2 : notes de l'étudiant 2
    [72, 60, 81],    # ligne 3 : notes de l'étudiant 3
]



for i in range(len(notes)):    
    print(f"Étudiant #{i+1}")
    somme_par_etudiant = 0
    for j in range(len(notes[i])):
         somme_par_etudiant = somme_par_etudiant + notes[i][j]


    moyenne_notes = somme_par_etudiant / len(notes[i])
    print(f"la somme des notes est: {somme_par_etudiant}")
    print(f"la moyenne des notes est: {moyenne_notes}")








#python tutor-


