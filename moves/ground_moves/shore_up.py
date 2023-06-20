from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


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
        The user regains up to half of its max HP.
        """
        heal = waifu_user.hp_max // 2
        if waifu_user.hp + heal >= waifu_user.hp_max:
            heal = waifu_user.hp_max - waifu_user.hp
        waifu_user.hp += heal 
        log("HEAL", f"{waifu_user.name} a récupéré la moitié de ses PV !")
