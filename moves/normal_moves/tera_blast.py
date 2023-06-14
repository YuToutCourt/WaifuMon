from ..move import Move
from waifu_types.type import Type

class TeraBlast(Move):
    def __init__(self):
        super().__init__("Tera Blast", type=Type.NORMAL, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes type when the user has Terastallized.
        """
        pass
