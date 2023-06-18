from wtypes.type import Type
from wtypes.enum_types import Types


class TypeFactory:
    @staticmethod
    def create_type(type_name: Types) -> Type:
        if isinstance(type_name, str):
            type_name = Types[type_name.upper()]

        if type_name == Types.BUG:
            return Type(
                Types.BUG,
                [Types.FIRE, Types.FLYING, Types.ROCK],
                [Types.FIGHTING, Types.GRASS, Types.GROUND],
                [],
            )
        elif type_name == Types.DARK:
            return Type(
                Types.DARK,
                [Types.BUG, Types.FAIRY, Types.FIGHTING],
                [Types.DARK, Types.GHOST],
                [Types.PSYCHIC],
            )
        elif type_name == Types.DRAGON:
            return Type(
                Types.DRAGON, [Types.ICE, Types.DRAGON, Types.FAIRY], [Types.FIRE, Types.WATER, Types.ELECTRIC, Types.GRASS], []
            )
        elif type_name == Types.ELECTRIC:
            return Type(
                Types.ELECTRIC,
                [Types.GROUND],
                [Types.ELECTRIC, Types.FLYING, Types.STEEL],
                [],
            )
        elif type_name == Types.FAIRY:
            return Type(
                Types.FAIRY,
                [Types.POISON, Types.STEEL],
                [Types.FIGHTING, Types.BUG, Types.DARK],
                [Types.DRAGON],
            )
        elif type_name == Types.FIGHTING:
            return Type(
                Types.FIGHTING,
                [Types.FLYING, Types.PSYCHIC, Types.FAIRY],
                [Types.BUG, Types.DARK, Types.ROCK],
                [],
            )
        elif type_name == Types.FIRE:
            return Type(
                Types.FIRE,
                [Types.WATER, Types.GROUND, Types.ROCK],
                [Types.FIRE, Types.GRASS, Types.ICE, Types.BUG, Types.STEEL],
                [],
            )
        elif type_name == Types.FLYING:
            return Type(
                Types.FLYING,
                [Types.ELECTRIC, Types.ICE, Types.ROCK],
                [Types.GRASS, Types.FIGHTING, Types.BUG],
                [Types.GROUND],
            )
        elif type_name == Types.GHOST:
            return Type(
                Types.GHOST,
                [Types.DARK, Types.GHOST],
                [Types.POISON, Types.BUG],
                [Types.NORMAL, Types.FIGHTING],
            )
        elif type_name == Types.GRASS:
            return Type(
                Types.GRASS,
                [Types.FIRE, Types.ICE, Types.POISON, Types.FLYING, Types.BUG],
                [Types.WATER, Types.ELECTRIC, Types.GRASS, Types.GROUND],
                [],
            )

        elif type_name == Types.GROUND:
            return Type(
                Types.GROUND,
                [Types.WATER, Types.GRASS, Types.ICE],
                [Types.POISON, Types.ROCK],
                [Types.ELECTRIC],
            )
        elif type_name == Types.ICE:
            return Type(
                Types.ICE,
                [Types.FIRE, Types.FIGHTING, Types.ROCK, Types.STEEL],
                [Types.ICE],
                [],
            )
        elif type_name == Types.NORMAL:
            return Type(Types.NORMAL, [Types.FIGHTING], [], [Types.GHOST])

        elif type_name == Types.POISON:
            return Type(
                Types.POISON,
                [Types.GROUND, Types.PSYCHIC],
                [Types.GRASS, Types.FIGHTING, Types.POISON, Types.BUG, Types.FAIRY],
                [],
            )
        elif type_name == Types.PSYCHIC:
            return Type(
                Types.PSYCHIC,
                [Types.BUG, Types.DARK, Types.GHOST],
                [Types.FIGHTING, Types.PSYCHIC],
                [],
            )
        elif type_name == Types.ROCK:
            return Type(
                Types.ROCK,
                [Types.WATER, Types.GRASS, Types.FIGHTING, Types.GROUND, Types.STEEL],
                [Types.NORMAL, Types.FIRE, Types.POISON, Types.FLYING],
                [],
            )
        elif type_name == Types.STEEL:
            return Type(
                Types.STEEL,
                [Types.FIRE, Types.FIGHTING, Types.GROUND],
                [
                    Types.NORMAL,
                    Types.GRASS,
                    Types.ICE,
                    Types.FLYING,
                    Types.PSYCHIC,
                    Types.BUG,
                    Types.ROCK,
                    Types.DRAGON,
                    Types.FAIRY,
                    Types.STEEL,
                ],
                [Types.POISON],
            )

        elif type_name == Types.WATER:
            return Type(
                Types.WATER,
                [Types.ELECTRIC, Types.GRASS],
                [Types.FIRE, Types.WATER, Types.ICE, Types.STEEL],
                [],
            )
