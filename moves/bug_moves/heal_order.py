from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.animation import animation_heal
from utils.logger import log

class HealOrder(Move):
    def __init__(self):
        super().__init__(
            "Heal Order",
            type=TypeFactory.create_type(Types.BUG),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        User recovers half its max HP.
        """
        healing = waifu_user.hp_max / 2
        if healing + waifu_user.hp >= waifu_user.hp_max:
            healing = waifu_user.hp_max - waifu_user.hp
        animation_heal(waifu_user, healing)
        log(f"{waifu_user.name} recovered {healing} HP")
