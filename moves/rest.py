from .move import Move
from waifu_types.type import Type

class Rest(Move):
    def __init__(self):
        super().__init__("Rest", type=Type.PSYCHIC, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User sleeps for 2 turns, but user is fully healed.
        """
        pass
