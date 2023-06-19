from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Synthesis(Move):
    def __init__(self):
        super().__init__(
            "Synthesis",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User recovers HP.
        """
        recover = waifu_user.max_hp * 0.4
        if waifu_user.hp + recover > waifu_user.hp_max:
            recover = waifu_user.hp_max - waifu_user.hp

        waifu_user.hp += recover
        log(self.name, waifu_user.name, "recovers", recover, "HP")
