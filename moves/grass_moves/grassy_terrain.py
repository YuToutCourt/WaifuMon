from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class GrassyTerrain(Move):
    def __init__(self):
        super().__init__(
            "Grassy Terrain",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Restores a little HP
        """
        from random import randint

        restore = randint(1, 5) * waifu_user.level
        if waifu_user.hp + restore > waifu_user.hp_max:
            waifu_user.hp = waifu_user.hp_max
        waifu_user.hp += restore
        log(self.name, waifu_user.name, "restores", restore, "HP")
