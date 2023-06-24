import pygame
import time
from utils.logger import log
class Dialog:

    X_POSITION = 370
    Y_POSITION = 700
    # X_POSITION_FIGHT = 600
    # Y_POSITION_FIGHT = 700

    def __init__(self, text):
        box = pygame.image.load("asset/Dialog/dialog_box.png")
        self.box = pygame.transform.scale(box, (800, 100))
        self.font = pygame.font.Font("asset/Dialog/dialog_font.ttf", 20)
        self.texts = text.split("\n")
        self.text_index = 0
        self.letter_index = 0
        self.reading = True
        # self.data_fight = "CECI EST UN TEST"
        # self.fight = False
        # self.box_fight = pygame.transform.scale(box, (500, 150))


    def end_dialog(self):
        self.reading = False
        self.text_index = 0


    def display(self, screen):
        
        self.letter_index += 1

        if self.letter_index >= len(self.texts[self.text_index]):
            self.letter_index = self.letter_index
        screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
        text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
        screen.blit(text, (self.X_POSITION + 70, self.Y_POSITION + 20))


    def next_text(self):
        self.letter_index += 1
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            time.sleep(1)
            self.end_dialog()
                # self.fight = True
    

    # def display_fight(self, screen):        
    #     screen.blit(self.box_fight, (self.X_POSITION_FIGHT, self.Y_POSITION_FIGHT))
    #     text = self.font.render(self.data_fight, False, (0, 0, 0))
    #     screen.blit(text, (self.X_POSITION_FIGHT + 100, self.Y_POSITION_FIGHT + 30))


    # def add_data_fight(self, datas):
    #     self.data_fight = datas


        
