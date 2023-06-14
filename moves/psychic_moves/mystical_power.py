from ..move import Move
from waifu_types.type import Type

class MysticalPower(Move):
    def __init__(self):
        super().__init__("Mystical Power", type=Type.PSYCHIC, power=70, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack or Defense.
        """
        pass
