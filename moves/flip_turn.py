from .move import Move
from waifu_types.type import Type

class FlipTurn(Move):
    def __init__(self):
        super().__init__("Flip Turn", type=Type.WATER, power=60, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        After making its attack, the user rushes back to switch places with a party Pokémon in waiting.
        """
        pass
