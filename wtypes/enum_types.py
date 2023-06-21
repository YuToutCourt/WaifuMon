from enum import Enum
from colorama import Fore, init

init()

class Types(Enum):
    WATER = Fore.BLUE + "WATER"
    FIRE = Fore.RED + "FIRE"
    GRASS = Fore.GREEN + "GRASS"
    ELECTRIC = Fore.YELLOW + "ELECTRIC"
    NORMAL = Fore.LIGHTWHITE_EX + "NORMAL"
    FIGHTING = Fore.RED + "FIGHTING"
    FLYING = Fore.CYAN + "FLYING" 
    POISON = Fore.MAGENTA + "POISON"
    GROUND = Fore.YELLOW + "GROUND" 
    ROCK = Fore.LIGHTBLACK_EX + "ROCK" 
    BUG = Fore.GREEN + "BUG" 
    GHOST = Fore.MAGENTA + "GHOST" 
    STEEL = Fore.LIGHTCYAN_EX + "STEEL" 
    PSYCHIC = Fore.MAGENTA + "PSYCHIC" 
    ICE = Fore.CYAN + "ICE" 
    DRAGON = Fore.LIGHTMAGENTA_EX + "DRAGON"
    DARK = Fore.BLACK + "DARK" 
    FAIRY = Fore.LIGHTMAGENTA_EX + "FAIRY"
