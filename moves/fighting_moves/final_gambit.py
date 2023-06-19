from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class FinalGambit(Move):
    def __init__(self):
        super().__init__(
            "Final Gambit",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Inflicts damage equal to the user's remaining HP. User faints.
        """
        waifu_receiver.current_health -= waifu_user.current_health
        waifu_user.current_health = 0
        log(
            "Final Gambit",
            f"{waifu_user.name} inflicted {waifu_user.current_health} damage to {waifu_receiver.name}",
        )
