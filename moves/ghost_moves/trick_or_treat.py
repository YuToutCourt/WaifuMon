from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class TrickorTreat(Move):
    def __init__(self):
        super().__init__(
            "Trick-or-Treat",
            type=TypeFactory.create_type(Types.GHOST),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Adds Ghost type to opponent.
        """
        for type_ in waifu_receiver.type:
            if type_.type_name == Types.GHOST:
                return

        waifu_receiver.type.append(TypeFactory.create_type(Types.GHOST))            

