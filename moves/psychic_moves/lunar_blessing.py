from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class LunarBlessing(Move):
    def __init__(self):
        super().__init__(
            "Lunar Blessing",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Heals user's status conditions and recovers HP.
        """
        waifu_user.status = None

        # 25% of max HP
        heal = waifu_user.hp_max * 0.25

        if waifu_user.hp + heal > waifu_user.hp_max:
            heal = waifu_user.hp_max - waifu_user.hp
        waifu_user.hp += heal
        log(self.name, waifu_user.name, f"recovered {heal} HP, and cleared status conditions")
