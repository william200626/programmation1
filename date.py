import datetime


# date_du_jour = datetime.date.today()     #pas besoin de faire selui la l'autre marche pour tout
# print(date_du_jour)
# print(date_du_jour.year)
# print(date_du_jour.month)
# print(date_du_jour.day)

maintenant = datetime.datetime.now()
print(maintenant)
print(maintenant.year)
print(maintenant.month)
print(maintenant.day)
print(maintenant.hour)
print(maintenant.minute)
print(maintenant.second)
print(maintenant.microsecond)

print (maintenant.strftime("%Y %m %d"))
print (maintenant.strftime("Bilan executer le: %d-%B-%Y"))