from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Infestation(Move):
    def __init__(self):
        super().__init__(
            "Infestation",
            type=TypeFactory.create_type(Types.BUG),
            power=20,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )
        self.effect_turns = 0

    def effect(self, waifu_user, waifu_receiver):
        """
        Traps opponent, damaging them for 4 turns.
        """
        if self.effect_turns < 4:
            self.effect_turns += 1
            waifu_receiver.hp -= waifu_receiver.hp_max * (1 / 8)
            log(
                self.name,
                waifu_receiver.name,
                f"lost {waifu_receiver.hp_max * (1/8)} HP",
            )
