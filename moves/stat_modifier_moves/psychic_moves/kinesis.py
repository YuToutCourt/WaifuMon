from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_heal

class Kinesis(Move):
    def __init__(self):
        super().__init__(
            "Kinesis",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=80,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Recover 1/4 of the hp_max.
        """
        heal = 1 / 4 * waifu_user.hp_max
        animation_heal(waifu_user, heal)
        log(waifu_user.name, "Recover", heal, "hp")
