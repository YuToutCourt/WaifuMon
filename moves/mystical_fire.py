from .move import Move
from waifu_types.type import Type

class MysticalFire(Move):
    def __init__(self):
        super().__init__("Mystical Fire", type=Type.FIRE, power=75, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
