from .status import Status
from .status_enum import StatusE
from utils.log import log
from random import randint

class Freeze(Status):
    def __init__(self, waifu):
        super().__init__(StatusE.FREEZE, waifu)

    def apply_status(self):
        """
        Freeze status effect.
        The freeze condition (FRZ) causes a Pokémon to be unable to use moves
        The frozen Pokémon has a chance to be thawed each turn 20%, possibly even thawing right after being frozen
        Max turn frozen == 4
        :return: True if the pokemon has been thawed else False
        """
        if randint(0, 100) <= 20 or self.turns == 4 :
            self.waifu.status = None
            self.turns = 0
            return True
        else :
            log("Freeze", f"{self.waifu.name} is frozen ! Can't attack.")
            self.turns += 1
            return False