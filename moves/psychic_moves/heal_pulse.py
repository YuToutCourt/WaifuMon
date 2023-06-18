from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


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
        if healing + waifu_user.hp >= waifu_user.hp_max:
            waifu_user.hp = waifu_user.hp_max
        else:
            waifu_user.hp += healing
