from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class EerieSpell(Move):
    def __init__(self):
        super().__init__(
            "Eerie Spell",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=80,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Deals damage and reduces opponent's PP.
        """
        waifu_receiver.move_to_use.pp -= 4
        log(self.name, waifu_receiver.name,waifu_receiver.move_to_use.name, "lost 4 PP")
