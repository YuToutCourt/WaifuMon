from .status import Status
from .status_enum import StatusE
from utils.logger import log
from random import randint

class Confusion(Status):
    def __init__(self, waifu, afer_attack:bool):
        super().__init__(StatusE.CONFUSE, waifu, afer_attack)

    def apply_status(self):
        """
        Confuse status effect.
        Pokémon confuse have 33% to sometimes attack itself
        instead of executing the selected move for a random 1-4 turns
        :return: True if the pokemon has been thawed else False
        """
        if randint(0, 100) >= 33 or self.turns == 4 :
            self.waifu.status = None
            self.turns = 0
            log("Confuse", f"{self.waifu.name} is not confuse anymore.")
            return True
        else :
            log("Confuse", f"{self.waifu.name} hurt him self.")
            dmg = self.__calculate_damage(self.waifu, self.waifu)
            self.waifu.hp -= dmg

            self.turns += 1
            return False


    def __calculate_damage(self, attacker, opponent):
        damage = (
            ((2 * attacker.level + 10) / 250)
            * (attacker.attack / opponent.defense)
            * 40
            + 2
        ) * 1

        return damage