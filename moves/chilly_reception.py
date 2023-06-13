from .move import Move
from waifu_types.type import Type

class ChillyReception(Move):
    def __init__(self):
        super().__init__("Chilly Reception", type=Type.ICE, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Switches out and summons a snowstorm lasting 5 turns.
        """
        pass
