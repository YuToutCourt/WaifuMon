from .status import Status
from .status_enum import StatusE
from utils.log import log
from random import randint

class Paralysis(Status):
    def __init__(self, waifu, afer_attack:bool):
        super().__init__(StatusE.PARALYSIS, waifu, afer_attack)

    def apply_status(self):
        """
        Paralysis status effect.
        The paralysis condition (PAR) reduces the Pokémon's Speed stat
        and causes it to have a 25% chance of being unable to use a move
        :return: True if the pokemon is able to attack else False
        """
        if randint(0, 100) <= 25 :
            log("Paralyse", f"{self.waifu.name} is paralysis! Can't attack")
            return False
        else :
            return True