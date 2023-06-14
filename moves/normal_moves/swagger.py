from ..move import Move
from waifu_types.type import Type

class Swagger(Move):
    def __init__(self):
        super().__init__("Swagger", type=Type.NORMAL, power=0, accuracy=85, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent, but sharply raises its Attack.
        """
        pass
