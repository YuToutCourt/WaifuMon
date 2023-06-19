from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Geomancy(Move):
    def __init__(self):
        super().__init__(
            "Geomancy",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Charges on first turn, sharply raises user's Attack, Defense and Speed on the second.
        """

        if waifu_reciver.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_reciver.name} Attack can't be raised anymore !")
        else:
            waifu_reciver.stat_stage_atk += 2
            multiplier = (2 + abs(waifu_reciver.stat_stage_atk)) / 2
            waifu_reciver.attack = waifu_reciver.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been raised !")

        if waifu_reciver.stat_stage_def >= 6:
            log("TOO HIGH", f"{waifu_reciver.name} Defense can't be raised anymore !")
        else:
            waifu_reciver.stat_stage_def += 2
            multiplier = (2 + abs(waifu_reciver.stat_stage_def)) / 2
            waifu_reciver.defense = waifu_reciver.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been raised !")

        if waifu_reciver.stat_stage_spd >= 6:
            log("TOO HIGH", f"{waifu_reciver.name} Speed can't be raised anymore !")
        else:
            waifu_reciver.stat_stage_spd += 2
            multiplier = (2 + abs(waifu_reciver.stat_stage_spd)) / 2
            waifu_reciver.speed = waifu_reciver.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been raised !")
