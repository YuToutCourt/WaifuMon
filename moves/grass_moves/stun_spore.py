from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis


class StunSpore(Move):
    def __init__(self):
        super().__init__(
            "Stun Spore",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=75,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Paralyzes opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log("StunSpore", f"{waifu_reciver.name} is now paralyzed !")
