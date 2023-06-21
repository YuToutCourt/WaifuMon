from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_heal

class HealPulse(Move):
    def __init__(self):
        super().__init__(
            "Heal Pulse",
            type=TypeFactory.create_type(Types.PSYCHIC),
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
        animation_heal(waifu_user, healing)
