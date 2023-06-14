from ..move import Move
from waifu_types.type import Type

class G-MaxFireball(Move):
    def __init__(self):
        super().__init__("G-Max Fireball", type=Type.FIRE, power=160, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Cinderace-exclusive G-Max Move. Ignores target's ability.
        """
        pass
