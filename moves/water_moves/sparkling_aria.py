from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SparklingAria(Move):
    def __init__(self):
        super().__init__(
            "Sparkling Aria",
            type=TypeFactory.create_type(Types.WATER),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Heals the burns of its target.
        """
        if waifu_receiver.status.status.name == "BURN":
            waifu_receiver.status = None
            print(f"{waifu_receiver.name} is no longer burned")
        else:
            print(f"{waifu_receiver.name} is not burned")
