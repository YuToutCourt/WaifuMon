from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class ForestCurse(Move):
    def __init__(self):
        super().__init__(
            "Forest's Curse",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Adds Grass type to opponent.
        """
        for type_ in waifu_receiver.type:
            if type_.type_name == Types.GRASS:
                return

        waifu_receiver.type.append(TypeFactory.create_type(Types.GRASS))
        log(waifu_receiver.name, "is cursed by the forest")
