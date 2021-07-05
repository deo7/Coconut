#     _____               ____          _____             
#    |  __ \             |  _ \        |  __ \            
#    | |  | | _____   __ | |_) |_   _  | |  | | ___  ___  
#    | |  | |/ _ \ \ / / |  _ <| | | | | |  | |/ _ \/ _ \ 
#    | |__| |  __/\ V /  | |_) | |_| | | |__| |  __/ (_) |
#    |_____/ \___| \_/   |____/ \__, | |_____/ \___|\___/ 
#                                __/ |                    
#                               |___/                     


# Salut c'est Ninho, si tu veux écouter ma dernière mixtape sur Apple Music, swipe up. On est ensemble.

import sys
import os
import colorama
import pyfiglet
import time
import string
import argparse
import getpass
import random
from colorama import Fore, Style
from colorama.initialise import reset_all
from passpwnedcheck.pass_checker import PassChecker

os.system("cls")
colorama.init()
pass_checker = PassChecker()


def banner():
    print(pyfiglet.figlet_format("Coconut"))
    print("Made with", Fore.RED, chr(9829), Style.RESET_ALL, "by Déodorant")


def menu():
    print("Menu:")
    print("[1]  Générateur de mot de passe")
    print("[2]  Checker de sécurité de mot de passe")
    print("[3]  Checker de leak de mot de passe")
    print("[4]  Documentation sur les mots de passe")


def genpass():
    print("Générateur de mot de passe - Coconut")

    separator(2)

    length = int(input("Combien de caractères voulez vous dans le mot de passe ? "))
    
    def getpswd(length):
        str = string.ascii_letters + string.digits
        return "".join([random.choice(str) for i in range(length)])

    symbols = ["&+", "=!", "[)", "'#", ":/", ";}", "*_", "-$", ".<"]
    password = getpswd(length).__add__(random.choice(symbols))

    separator(2)

    print("Voici le mot de passe:", password)


def secucheck():
    print("Checker de sécurité de mot de passe - Coconut")

    separator(2)

    password = getpass.getpass("Quel mot de passe voulez vous tester? (invisible dans le terminal) ")
    advicelist = []

    upper = True if any(map(str.isupper, password)) else False

    lower = True if any(map(str.islower, password)) else False

    digits = True if any(map(str.isdigit, password)) else False

    if upper == False:
        advicelist.append("Rajouter une/des majuscules")

    if lower == False:
        advicelist.append("Rajouter une/des minuscules")

    if digits == False:
        advicelist.append("Rajouter un/des chiffres")

    if len(password) <= 5:
        advicelist.append("Longueur insuffisante")

    if len(advicelist) == 0:
        advicelist.append("Aucun conseil, parfait!")

    else:
        pass

    advices = ", ".join(advicelist)

    separator(2)

    print("Mot de passe testé   :   ", password)
    print("Longueur             :   ", len(password))
    print("Conseils (beta)      :   ", advices)


def leakcheck():
    print("Checker de leak de mot de passe - Coconut")

    separator(2)

    password = getpass.getpass("Quel mot de passe voulez vous tester? (invisible dans le terminal) ")

    is_leaked, count = pass_checker.is_password_compromised(password)

    if is_leaked:
        leak = "Oui"
        countleak = count
    
    else:
        leak = "Non"
        countleak = 0

    symbollist = ["!", "|", "&", "-", "+", "/", "?"]
    
    idea = password.replace("i", "!").replace("e", "3").replace("a", "@").replace("o", "0").replace("9", "6").title().__add__(random.choice(symbollist))

    separator(2)

    print("Mot de passe testé   :   ", password)
    print("Leak                 :   ", leak)
    print("Nombre de leak       :   ", countleak)
    print("Idée de mdp (beta)   :   ", idea)

def documentation():
    print("Documentation sur les mots de passe - Coconut")

    separator(2)

    print("Voici quelques docs intéressantes sur les mots de passe - Mises à jour régulières")

    separator(2)

    print("https://howsecureismypassword.net/")
    print("https://haveibeenpwned.com/Passwords")
    print("https://www.youtube.com/watch?v=YI-6nZFxwNg")
    print("https://lurcat-villejuif.ac-creteil.fr/wordpress/wp-content/uploads/2020/12/Mot-de-passe-1024x936.jpg")

def separator(type):
    if type == 1:
        print("----------------------------------------")
    
    elif type == 2:
        print("--------------------")

parser = argparse.ArgumentParser()
parser.add_argument('-g', help="Générateur de mot de passe", action="store_true")
parser.add_argument('-s', help="Checker de sécurité de mot de passe", action="store_true")
parser.add_argument('-l', help="Checker de leak de mot de passe", action="store_true")
parser.add_argument("-d", help="Documentation sur les mots de passe", action="store_true")
args = parser.parse_args()

if args.g:
    banner()

    time.sleep(1)

    separator(1)

    genpass()

    separator(1)

elif args.s:
    banner()

    time.sleep(1)

    separator(1)

    secucheck()

elif args.l:
    banner()

    time.sleep(1)

    separator(1)

    leakcheck()

elif args.d:
    banner()

    time.sleep(1)
    
    separator(1)

    documentation()
    
else:
    banner()

    time.sleep(1)

    separator(1)

    menu()

    choice = int(input("Choix: "))

    if choice == 1:
        separator(2)

        genpass()

    elif choice == 2:
        separator(2)

        secucheck()

    elif choice == 3:
        separator(2)

        leakcheck()

    elif choice == 4:
        separator(2)

        documentation()

    else:
        separator(2)

        sys.exit("Erreur") 



#         _                _                                   _                              _ _                      
#        | |              | |            ____                 | |                            (_) |                     
#      __| | ___  ___   __| | _____   __/ __ \ _ __  _ __ ___ | |_ ___  _ __  _ __ ___   __ _ _| |  ___ ___  _ __ ___  
#     / _` |/ _ \/ _ \ / _` |/ _ \ \ / / / _` | '_ \| '__/ _ \| __/ _ \| '_ \| '_ ` _ \ / _` | | | / __/ _ \| '_ ` _ \ 
#    | (_| |  __/ (_) | (_| |  __/\ V / | (_| | |_) | | | (_) | |_ (_) | | | | | | | | | (_| | | |_ (__ (_) | | | | | |
#     \__,_|\___|\___/ \__,_|\___| \_/ \ \__,_| .__/|_|  \___/ \__\___/|_| |_|_| |_| |_|\__,_|_|_(_)___\___/|_| |_| |_|
#                                       \____/| |                                                                      
#                                             |_|                                                                      