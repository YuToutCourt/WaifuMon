from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_heal

class SoftBoiled(Move):
    def __init__(self):
        super().__init__(
            "Soft-Boiled",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User recovers half its max HP.
        """
        heal = waifu_user.hp_max / 2
        animation_heal(waifu_user, heal)
        log(self.name, waifu_user.name, f"recovered {heal} HP")
