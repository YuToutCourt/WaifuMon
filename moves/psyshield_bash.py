from .move import Move
from waifu_types.type import Type

class PsyshieldBash(Move):
    def __init__(self):
        super().__init__("Psyshield Bash", type=Type.PSYCHIC, power=70, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises user's Defense and Special Defense.
        """
        pass
