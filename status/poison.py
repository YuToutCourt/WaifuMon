from .status import Status
from .status_enum import StatusE
from utils.log import log

class Poison(Status):
    def __init__(self, waifu):
        super().__init__(StatusE.POISON, waifu)

    def apply_status(self):
        """
        Poison status effect.
        every turn, the waifu lose turns/16 of its max hp.
        """
        self.waifu.hp -= (self.waifu.hp_max * self.turns/16)
        log("Poison", f"{self.waifu.name} is hurt by poison! Lost {self.waifu.hp_max * self.turns/16} HP.")
        self.turns += 1