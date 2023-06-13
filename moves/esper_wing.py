from .move import Move
from waifu_types.type import Type

class EsperWing(Move):
    def __init__(self):
        super().__init__("Esper Wing", type=Type.PSYCHIC, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio. Raises user's Speed.
        """
        pass
