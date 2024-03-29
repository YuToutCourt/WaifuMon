import pygame
from utils.coordinates import Coordinates
from waifu.waifu import Waifu
from typing import List
from wtypes.type_factory import TypeFactory
from abc import ABC, abstractmethod

import json
from random import shuffle, randint


class Character(pygame.sprite.Sprite, ABC):
    def __init__(self, coordinates: Coordinates, image_path: str):
        super().__init__()
        self.position = (coordinates.x, coordinates.y)
        self.image = pygame.image.load(image_path)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey((255, 0, 220)) # Color key for transparency
        self.rect = self.image.get_rect() # Rectangle for collision
        self.team: List[Waifu] = [] # TODO: Create a box to store the waifus
        self.__create_random_team()

    def get_image(self, x: int, y: int): 
        image = pygame.Surface([38, 46])
        image.blit(self.image, (0, 0), (x, y, 38, 46))
        return image

    def update(self):
        """
        Update the position of the character
        """
        self.rect.topleft = self.position 

    def print_team(self):
        """
        Display the team of the character in the console
        """
        for waifu in self.team:
            print(waifu.name)

    def get_waifu_in_fight(self):
        """
        Return the waifu in fight
        """
        for waifu in self.team:
            if waifu.in_fight:
                return waifu
        return None

    def get_alive_waifu(self):
        """
        Return all the waifu alive
        """
        return [waifu for waifu in self.team if not waifu.KO]


    def __create_random_team(self):
        """
        /!\ POUR TEST /!\
        In the main game you will start with 0 waifu
        """
        with open(
            "asset/waifu_sprite/all_waifu_name.json", "r", encoding="utf-8"
        ) as file:
            data = json.load(file)["characters"]
            shuffle(data)
            for w in data[:6]:
                name = w["nom"]
                types = w["types"]
                id = w["id"]
                types_ = [TypeFactory.create_type(type) for type in types]
                owner = "player"

                while True:
                    hp = randint(50, 255)
                    attack = randint(40, 190)
                    defense = randint(40, 230)
                    speed = randint(35, 180)
                    somme = hp + attack + defense + speed
                    if 330 <= somme <= 550:
                        break

                waifu = Waifu(
                    id,
                    name,
                    randint(50, 255),
                    randint(40, 190),
                    randint(40, 230),
                    randint(35, 180),
                    types_,
                    randint(45, 60),
                )
                self.team.append(waifu)

    @abstractmethod
    def move_back(self, movement):
        pass