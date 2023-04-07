import pygame

class Waifu(pygame.sprite.Sprite):
    super().__init__()
    def __init__(self, id:int, nom:str, pv:int, attaque:int, defense:int, vitesse:int, niveau:int=1):
        self.id = id
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.niveau = niveau
        self.list_attaque = []
        self.front_image = pygame.image.load(f"asset/Tileset/waifu_sprite/{self.id}/{self.id}_front.png")
        self.back_image = pygame.image.load(f"asset/Tileset/waifu_sprite/{self.id}/{self.id}_back.png")
        self.inventory_image = pygame.image.load(f"asset/Tileset/waifu_sprite/{self.id}/{self.id}_inventory.png")


    def get_front_image(self):
        return self.front_image

    def get_back_image(self):
        return self.back_image

    def get_inventory_image(self):
        return self.inventory_image