# auteur: William Levasseur Lafrenière 
#date: 2026-11-03
#description: outils


def afficher_message(message):
    print(f"Message: {message}")



def main():
    afficher_message("Bonjour!")

try:
    main()
except:
    print("une erreur est survenu")