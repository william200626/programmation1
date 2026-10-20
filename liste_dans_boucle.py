# #Nombre d'éléments connu → for

# NB_NOTES = 4
# notes = []
# for i in range(1, NB_NOTES + 1):
#     note = float(input(f"Note {i} : "))
#     notes.append(note)

# print("Notes :", notes)
# print(f"Moyenne : {sum(notes) / len(notes):.2f}")

# #-----------------------------------------------------
# #Nombre d'éléments inconnu → while avec sentinelle

# prenoms = []
# prenom = input("Prénom (Entrée pour terminer) : ").strip()
# while prenom != "":
#     prenoms.append(prenom)
#     prenom = input("Prénom (Entrée pour terminer) : ").strip()

# print(f"{len(prenoms)} prénom(s) saisi(s) :", ", ".join(prenoms))

# #-----------------------------------------------------
# #À partir d'une autre liste

# temperatures_c = [-5, 0, 12, 23]
# temperatures_f = []
# for t in temperatures_c:
#     temperatures_f.append(t * 9 / 5 + 32)
# print(temperatures_f)    # [23.0, 32.0, 53.6, 73.4]
# #-----------------------------------------------------

