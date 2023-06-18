from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


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
        waifu_user.current_health += waifu_user.max_health / 2
        if waifu_user.current_health > waifu_user.max_health:
            waifu_user.current_health = waifu_user.max_health
        print(f"{waifu_user.name} recovered half HP")
