from .status import Status
from .status_enum import StatusE
from utils.log import log

class Burn(Status):
    def __init__(self, waifu):
        super().__init__(StatusE.BURN, waifu)

    def apply_status(self):
        """
        Burn status effect.
        every turn, the waifu lose 1/8 of its max hp.
        """
        self.waifu.hp -= (self.waifu.hp_max * 1/8)
        log("Burn", f"{self.waifu.name} is hurt by burn! Lost {self.waifu.hp_max * 1/8} HP.")
        