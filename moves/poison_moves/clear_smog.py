from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class ClearSmog(Move):
    def __init__(self):
        super().__init__(
            "Clear Smog",
            type=TypeFactory.create_type(Types.POISON),
            power=50,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Removes all of the target's stat changes.
        """
        waifu_receiver.stat_stage_atk = 0
        waifu_receiver.stat_stage_def = 0
        waifu_receiver.stat_stage_spd = 0

        waifu_receiver.attack = waifu_receiver.base_attack
        waifu_receiver.defense = waifu_receiver.base_defense
        waifu_receiver.speed = waifu_receiver.base_speed

        log(self.name, waifu_receiver.name, "stat changes were removed")
