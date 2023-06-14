from ..move import Move
from waifu_types.type import Type

class MagicRoom(Move):
    def __init__(self):
        super().__init__("Magic Room", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Suppresses the effects of held items for five turns.
        """
        pass
