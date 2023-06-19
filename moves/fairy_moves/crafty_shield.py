from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class CraftyShield(Move):
    def __init__(self):
        super().__init__(
            "Crafty Shield",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Protects the Pokemon from status moves.
        """
        waifu_user.status = None
        log(waifu_user.name, "remove every status")
