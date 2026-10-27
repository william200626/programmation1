# eleves = [
#     [60,60,60],
#     [100,97,95],
#     [55,65,95],
#     [83,75,90]
# ]


nom_eleves = ["gabriel", "steve", "antoine", "mathew"]
nom_examen = ["quiz #1", "quiz #2", "examen intra"]

## for eleve in eleves:
##     #pour tous les eleves
##     print ("--------")
##     for note in eleve:
##         print(note)
##         print("--------")

# for i in range(len(eleves)):
#     print(f"Liste des  notes de {nom_eleves[i]}")
#     for j in range(len(eleves[i])):
#         print(f"Note pour  {nom_examen[j]}: {eleves[i][j]}")
#         # print(eleves[i][j])
#     print("--------")


eleves = [
    [[1,2],[3,4],[5,6,100]],
    [[7,8],[9,10],[11,12,100]],
    [[1,1],[1,1],[1,1,100]],
    [[0,0],[0,0],[0,0,100]]
]

for i in range(len(eleves)):
    print(f"Liste des  notes de {nom_eleves[i]}")
    for j in range(len(eleves[i])):
        print(f"Note pour  {nom_examen[j]}: {eleves[i][j]}")
        # print(eleves[i][j])
        for k in range(len(eleves[i][j])):
            print(f"Note : {eleves[i][j][k]}")
    print("--------")







