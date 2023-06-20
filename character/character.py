import pygame
from utils.coordinates import Coordinates
from waifu.waifu import Waifu
from typing import List
from wtypes.type_factory import TypeFactory
from abc import ABC

import json
from random import shuffle, randint


class Character(pygame.sprite.Sprite, ABC):
    def __init__(self, coordinates: Coordinates, image_path: str):
        super().__init__()
        self.position = (coordinates.x, coordinates.y)
        self.image = pygame.image.load(image_path)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey((255, 0, 220))
        self.rect = self.image.get_rect()
        self.team: List[Waifu] = []
        self.__create_random_team()

    def get_image(self, x: int, y: int):
        image = pygame.Surface([38, 46])
        image.blit(self.image, (0, 0), (x, y, 38, 46))
        return image

    def update(self):
        self.rect.topleft = self.position

    def print_team(self):
        for waifu in self.team:
            print(waifu.name)

    def get_waifu_in_fight(self):
        """
        Retourne le waifu qui est en combat
        """
        for waifu in self.team:
            if waifu.in_fight:
                return waifu
        return None

    def get_alive_waifu(self):
        return [waifu for waifu in self.team if not waifu.KO]

    def __create_random_team(self):
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
                waifu = Waifu(
                    id,
                    name,
                    randint(50, 200),
                    randint(50, 200),
                    randint(50, 200),
                    randint(50, 100),
                    types_,
                    randint(1, 100),
                )
                self.team.append(waifu)
