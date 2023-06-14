from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BoneClub(Move):
    def __init__(self):
        super().__init__("Bone Club", type=TypeFactory.create_type(Types.GROUND), power=65, accuracy=85, pp=20, priority=0, proba_effect=10)

    def effect(self):
        """
        May cause flinching.
        """
        pass
