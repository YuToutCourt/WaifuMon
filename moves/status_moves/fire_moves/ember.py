from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn


class Ember(Move):
    def __init__(self):
        super().__init__(
            "Ember",
            type=TypeFactory.create_type(Types.FIRE),
            power=40,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Ember", f"{waifu_receiver.name} is burned!")
