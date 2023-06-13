from .move import Move
from waifu_types.type import Type

class BodyPress(Move):
    def __init__(self):
        super().__init__("Body Press", type=Type.FIGHTING, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The higher the user's Defense, the stronger the attack.
        """
        pass
