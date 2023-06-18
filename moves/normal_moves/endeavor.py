from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Endeavor(Move):
    def __init__(self):
        super().__init__(
            "Endeavor",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Reduces opponent's HP to same as user's.
        """
        waifu_receiver.hp = waifu_user.hp
        log(self.name, "reduces", waifu_receiver.name, "HP to", waifu_user.hp)
