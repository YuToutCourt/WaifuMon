from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Explosion(Move):
    def __init__(self):
        super().__init__(
            "Explosion",
            type=TypeFactory.create_type(Types.NORMAL),
            power=250,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User faints.
        """
        waifu_user.hp = 0
        log(self.name, "makes", waifu_user.name, "faint")
