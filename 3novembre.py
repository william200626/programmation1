#autodocstring

import outils


def afficher_message(message):
    print(f"Message: {message}")



def main():
   outils.afficher_message("Bonjour!")
   outils.afficher_message("comment sa va" \
   "")

try:
    main()
except:
    print("une erreur est survenu")