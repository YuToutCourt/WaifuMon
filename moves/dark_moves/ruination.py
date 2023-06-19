from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Ruination(Move):
    def __init__(self):
        super().__init__(
            "Ruination",
            type=TypeFactory.create_type(Types.DARK),
            power=1,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Halves the opponent's HP.
        """
        waifu_receiver.hp //= 2
        log(self.name, waifu_receiver.name, "lost half of their HP")
