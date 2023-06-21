from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.animation import animation_damage

class NatureMadness(Move):
    def __init__(self):
        super().__init__(
            "Nature's Madness",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Halves the foe's HP. Deals dmg equal to 50% of the target's current HP.
        """
        animation_damage(waifu_receiver, waifu_receiver.hp / 2)
