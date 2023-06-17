import pygame
from wtypes.type import Type
from typing import List
from moves.move_factory import MoveFactory
from moves.enum_moves import Moves

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
        self.defense = defense
        self.speed = speed
        self.types = types
        self.level = level
        self.list_of_moves = [MoveFactory.create_move(Moves.ATTACK_ORDER)]
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

    def get_name(self):
        return self.nom

    def get_front_image(self):
        return self.front_image

    def get_back_image(self):
        return self.back_image

    def get_inventory_image(self):
        return self.inventory_image

    def display_pv(self):
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

    def choice_move(self):
        """
        Display the moves of the waifu and let the player choose one
        return the move chosen
        """
        # Code à faire
        _ = input("tape to continu: ")
        self.move_to_use = self.list_of_moves[0]

        return self.move_to_use
