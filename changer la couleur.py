from colorama import Fore, Back, Style, init       #sa c importanttttt!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# init(autoreset=True)                               #pip install colorama (si sa marche pas)


nom = input(f"votre nom : {Fore.GREEN}")
print(end=Style.RESET_ALL)
print(f"Bienvenu, {Fore.GREEN}{nom}")
print(f"Style.RESET_ALL")

print(f"Le verdict est: {Fore.RED}URGENT {Style.RESET_ALL}")
print(f"Le verdict est: {Fore.GREEN}Normal {Style.RESET_ALL}")
print(f"Le verdict est: {Fore.YELLOW}À surveiller {Style.RESET_ALL}")
print(f"Le verdict est: {Back.RED}URGENT {Style.RESET_ALL}")

