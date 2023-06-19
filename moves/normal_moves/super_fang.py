from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class SuperFang(Move):
    def __init__(self):
        super().__init__(
            "Super Fang",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Always takes off half of the opponent's HP.
        """
        waifu_receiver.hp = waifu_receiver.hp // 2
        log(self.name, waifu_receiver.name, f"lost half of its HP")
