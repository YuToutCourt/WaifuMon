from ..move import Move
from waifu_types.type import Type

class GearUp(Move):
    def __init__(self):
        super().__init__("Gear Up", type=Type.STEEL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        The user engages its gears to raise the Attack and Sp. Atk stats of ally Pokémon with the Plus or Minus Ability.
        """
        pass
