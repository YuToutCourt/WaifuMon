import pygame
from waifu_types.type import Type
from typing import List

class Waifu(pygame.sprite.Sprite):
    def __init__(self, id:int, nom:str, pv:int, attaque:int, defense:int, vitesse:int, types:List[Type], niveau:int=1):
        super().__init__()
        self.id = id
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.types = types
        self.niveau = niveau
        self.list_of_moves = []
        self.front_image = pygame.image.load(f"asset/waifu_sprite/{self.id}/{self.id}_front.png")
        self.back_image = pygame.image.load(f"asset/waifu_sprite/{self.id}/{self.id}_back.png")
        self.inventory_image = pygame.image.load(f"asset/waifu_sprite/{self.id}/{self.id}_inventory.png")


    def get_front_image(self):
        return self.front_image

    def get_back_image(self):
        return self.back_image

    def get_inventory_image(self):
        return self.inventory_image
    

