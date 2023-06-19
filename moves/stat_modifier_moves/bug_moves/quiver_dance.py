from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class QuiverDance(Move):
    def __init__(self):
        super().__init__(
            "Quiver Dance",
            type=TypeFactory.create_type(Types.BUG),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises user's Attack, Defense and Speed.
        """

        if waifu_user.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_reciver.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been raised !")

        if waifu_user.stat_stage_def >= 6:
            log("TOO HIGH", f"{waifu_reciver.name} Defense can't be raised anymore !")

        else:
            waifu_user.stat_stage_def += 1
            multiplier = (abs(waifu_user.stat_stage_def) + 2) / 2
            waifu_user.defense = waifu_user.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been raised !")

        if waifu_user.stat_stage_spd >= 6:
            log("TOO HIGH", f"{waifu_reciver.name} Speed can't be raised anymore !")

        else:
            waifu_user.stat_stage_spd += 1
            multiplier = (abs(waifu_user.stat_stage_spd) + 2) / 2
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been raised !")
