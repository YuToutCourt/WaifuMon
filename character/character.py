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
        self.position = (coordinates.x, coordinates.y) # Position du personnage
        self.image = pygame.image.load(image_path) # Image du personnage
        self.image = self.get_image(0, 0) # Image du personnage
        self.image.set_colorkey((255, 0, 220)) # Couleur de transparence
        self.rect = self.image.get_rect() # Rectangle de collision
        self.team: List[Waifu] = [] # Liste des waifus du personnage (6 max) TODO: créer une box pour stocker les waifus
        self.__create_random_team() # Création d'une équipe aléatoire, POUR TEST

    def get_image(self, x: int, y: int): 
        image = pygame.Surface([38, 46])
        image.blit(self.image, (0, 0), (x, y, 38, 46))
        return image

    def update(self):
        """
        Mise à jour de la position du rectangle de collision
        """
        self.rect.topleft = self.position 

    def print_team(self):
        """
        Affiche les waifus de l'équipe
        """
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
        """
        Retourne les waifus qui sont en vie
        """
        return [waifu for waifu in self.team if not waifu.KO]

    def __create_random_team(self):
        """
        POUR TEST
        Création d'une équipe aléatoire
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
