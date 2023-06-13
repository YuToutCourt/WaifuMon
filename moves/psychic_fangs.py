from .move import Move
from waifu_types.type import Type

class PsychicFangs(Move):
    def __init__(self):
        super().__init__("Psychic Fangs", type=Type.PSYCHIC, power=85, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user bites the target with its psychic capabilities. This can also destroy Light Screen and Reflect.
        """
        pass
