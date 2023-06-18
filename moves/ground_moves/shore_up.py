from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class ShoreUp(Move):
    def __init__(self):
        super().__init__(
            "Shore Up",
            type=TypeFactory.create_type(Types.GROUND),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The user regains up to half of its max HP. It restores more HP in a sandstorm.
        """
        waifu_user.hp = waifu_user.hp_max//2
        log("HEAL", f"{waifu_user.name} a récupéré la moitié de ses PV !")
