from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_heal

class JungleHealing(Move):
    def __init__(self):
        super().__init__(
            "Jungle Healing",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Restores HP and cures status conditions.
        """
        animation_heal(waifu_user, waifu_user.hp_max * 0.8)
        waifu_user.status = None
        log(
            "HEAL",
            f"{waifu_user.name} a récupéré 80% de ses PV !, et n'a plus de status !",
        )
