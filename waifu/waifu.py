import pygame
from wtypes.type import Type
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
        self.front_image = pygame.image.load(f"asset/waifu_sprite/{self.id}/redimensionnees/{self.id}_front.png")
        self.back_image = pygame.image.load(f"asset/waifu_sprite/{self.id}/redimensionnees/{self.id}_back.png")
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
    
    def choice_move(self):
        """
        Display the moves of the waifu and let the player choose one
        return the move chosen
        """
        # Code à faire
        for move in self.list_of_moves:
            print(move.name)
        self.move_to_use = self.list_of_moves[0]

        return self.move_to_use

