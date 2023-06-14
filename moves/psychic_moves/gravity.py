from ..move import Move
from waifu_types.type import Type

class Gravity(Move):
    def __init__(self):
        super().__init__("Gravity", type=Type.PSYCHIC, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents moves like Fly and Bounce and the Ability Levitate for 5 turns.
        """
        pass
