from colorama import Fore, Style
from random import choice

def log(*args):
    """
    Affiche un message dans la console
    """
    print(random_color(), end="")
    print(f"[{args[0]}]", end=" ")
    print(Fore.WHITE, end="")
    print(*args[1:])
    print(Style.RESET_ALL, end="")


def random_color():
    """
    Renvoie une couleur aléatoire != de la couleur blanche
    """
    color = choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
    return color