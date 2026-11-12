# auteur: William Levasseur LAfrenière 
#date: 15 septembre 2026
#description: exemple cours IF


age = int(input("quel est ton age:"))
avoir_faim = input("as-tu faim? Oui ou Non")
print(age)
if (age >= 18):
    if (avoir_faim == "Oui"):
        print("bienvenu")
        print("quel est votre commande")
    else:
        ("pk tu est la")

    print("merci de votre visite")
else:
    print("Trop jeune")

print("fin")




# age = int (input("quel est ton age?:"))
# avoir_faim = bool(input("as tu faim? True ou False:"))
# print(age)

# if (age >= 18 and avoir_faim == True):
#     print("merci de votre visite")
# else:
#     print("trop jeune ou pas faim")




# age = int(input("quel est tona age"))

# if(age >= 90):
#     print("tres vieux")
# elif age >= 80:
#     print("vieux")
# elif age >= 30:
#     print ("adulte")
# elif age >= 18:
#     print ("jeune_adulte")
# else:
#     print("enfant")



# if (a < 1 or a > 16):
#     print("no go")
# else:
#     print("GO!")