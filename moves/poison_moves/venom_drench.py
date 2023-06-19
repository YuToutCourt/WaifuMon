from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class VenomDrench(Move):
    def __init__(self):
        super().__init__(
            "Venom Drench",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Lowers poisoned opponent's Attack and Speed.
        """
        if waifu_receiver.stat_stage_atk <= -6:
            log(self.name, waifu_receiver.name, "cannot go lower")
            return
        waifu_receiver.stat_stage_atk -= 1
        multiplier = 2 / 2 + abs(waifu_receiver.stat_stage_atk)
        waifu_receiver.attack = waifu_receiver.base_attack * multiplier
        log(self.name, waifu_receiver.name, "Attack fell")

        if waifu_receiver.stat_stage_spd <= -6:
            log(self.name, waifu_receiver.name, "cannot go lower")
            return
        waifu_receiver.stat_stage_spd -= 1
        multiplier = 2 / 2 + abs(waifu_receiver.stat_stage_spd)
        waifu_receiver.speed = waifu_receiver.base_speed * multiplier
        log(self.name, waifu_receiver.name, "Speed fell")