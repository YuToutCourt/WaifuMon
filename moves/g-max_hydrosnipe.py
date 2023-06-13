from .move import Move
from waifu_types.type import Type

class G-MaxHydrosnipe(Move):
    def __init__(self):
        super().__init__("G-Max Hydrosnipe", type=Type.WATER, power=160, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Inteleon-exclusive G-Max Move. Ignores target's ability.
        """
        pass
