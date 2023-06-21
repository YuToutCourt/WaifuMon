from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.animation import animation_heal

class Moonlight(Move):
    def __init__(self):
        super().__init__(
            "Moonlight",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User recovers half HP.
        """
        heal = waifu_user.max_health / 2
        animation_heal(waifu_user, heal)
        print(f"{waifu_user.name} recovered half HP")
