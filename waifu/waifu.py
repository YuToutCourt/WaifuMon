import pygame
import random
from wtypes.type import Type
from typing import List
from moves.move_factory import MoveFactory
from moves.enum_moves import Moves
from utils.logger import log
from utils.handle_input import input_int


class Waifu(pygame.sprite.Sprite):
    def __init__(
        self,
        id: int,
        name: str,
        hp: int,
        attack: int,
        defense: int,
        speed: int,
        types: List[Type],
        level: int = 1,
    ):
        super().__init__()
        self.id = id
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.attack = attack
        self.base_attack = attack
        self.defense = defense
        self.base_defense = defense
        self.speed = speed
        self.base_speed = speed
        self.types = types
        self.level = level
        self.list_of_moves = [MoveFactory.create_move(random.choice(list(Moves))) for _ in range(4)]
        self.front_image = pygame.image.load(
            f"asset/waifu_sprite/{self.id}/{self.id}_front.png"
        )
        self.back_image = pygame.image.load(
            f"asset/waifu_sprite/{self.id}/{self.id}_back.png"
        )
        # self.inventory_image = pygame.image.load(f"asset/waifu_sprite/{self.id}/{self.id}_inventory.png")
        self.in_fight = False
        self.KO = False
        self.move_to_use = None
        self.stat_stage_def = 0
        self.stat_stage_atk = 0
        self.stat_stage_spd = 0
        self.status = None

    def __eq__(self, other):
            if isinstance(other, self.__class__):
                return (
                    self.id == other.id
                    and self.name == other.name
                    and self.hp == other.hp
                    and self.attack == other.attack
                    and self.defense == other.defense
                    and self.speed == other.speed
                    and self.types == other.types
                    and self.level == other.level
                    and self.list_of_moves == other.list_of_moves
                    and self.front_image == other.front_image
                    and self.back_image == other.back_image
                    and self.in_fight == other.in_fight
                    and self.KO == other.KO
                    and self.move_to_use == other.move_to_use
                    and self.stat_stage_atk == other.stat_stage_atk
                    and self.stat_stage_def == other.stat_stage_def
                    and self.stat_stage_spd == other.stat_stage_spd
                )
            return False

    def __hash__(self):
        return hash(
            (
                self.id,
                self.name,
                self.hp,
                self.attack,
                self.defense,
                self.speed,
                tuple(self.types),
                self.level,
                tuple(self.list_of_moves),
                self.front_image,
                self.back_image,
                self.in_fight,
                self.KO,
                self.move_to_use,
                self.stat_stage_atk,
                self.stat_stage_def,
                self.stat_stage_spd,
            )
        )

    def get_name(self):
        return self.nom

    def get_front_image(self):
        return self.front_image

    def get_back_image(self):
        return self.back_image

    def get_inventory_image(self):
        return self.inventory_image

    def display_stats(self):
        from tabulate import tabulate

        table = [["Name", "HP", "Attack", "Defense", "Speed", "Types", "Level"]]
        table.append(
            [
                self.name,
                self.hp,
                self.attack,
                self.defense,
                self.speed,
                [type.type_name.name for type in self.types],
                self.level,
            ]
        )
        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


    def display_hp(self):
        """
        Display the pv of the waifu in the console
        Fill the bar gradually with blocks
        Example: ■■■■■■□□□ as a percentage
        """
        if self.hp <= 0:
            self.hp = 0
        filled_bar = "■" * 10  # Represent a full health bar

        # Calculate the percentage of the bar based on the hp and hp_max
        value = self.hp * 100 / self.hp_max

        num_filled_blocks = int(value / 10)

        # Calculate the number of empty blocks based on the remaining percentage
        num_empty_blocks = 10 - num_filled_blocks

        # Construct the bar with filled and empty blocks
        bar = filled_bar[:num_filled_blocks] + "□" * num_empty_blocks

        print(f"{self.name} Lv.{self.level}")
        print(f"{bar} {round(self.hp, 2)} / {round(self.hp_max, 2)} ❤")

    def __display_moves(self):
        from colorama import Fore
        log("Choice a move")
        for i, move in enumerate(self.list_of_moves):
            print(f"{i} - {move.type.type_name.value} {move.name} {Fore.RESET} ({move.pp} PP)")

    def choice_move(self):
        """
        Display the moves of the waifu and let the player choose one
        return the move chosen
        """

        if all(move.pp <= 0 for move in self.list_of_moves):
            log("PP", "Not enough PP, your waifu use struggle")
            self.move_to_use = MoveFactory.create_move(Moves.STRUGGLE)
            return self.move_to_use    

        self.__display_moves()
        choice = input_int("Choice a move: ", 0, len(self.list_of_moves) - 1)
        while self.list_of_moves[choice].pp <= 0:
            log("PP", "Not enough PP, choose another move")
            self.__display_moves()
            choice = input_int("Choice a move: ", 0, len(self.list_of_moves) - 1)

        self.move_to_use = self.list_of_moves[choice]
        self.move_to_use.pp -= 1
        return self.move_to_use
