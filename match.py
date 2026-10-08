
jour = int(input("entrez un numéro de jour (1-7) : "))

match jour:
    case 1:
        print("lundi")
    case 2:
        print("mardi")
    case 3:
        print("mercredi")
    case 4:
        print("jeudi")
    case 5:
        print("vendredi")
    case 6:
        print("samedi")
    case 7:
        print("dimanche")
    case _:
        print("numéro invalide")


