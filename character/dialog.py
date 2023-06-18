import pygame
import time
from character.npc import NPC

class Dialog:

    X_POSITION = 370
    Y_POSITION = 700

    def __init__(self):
        self.box = pygame.image.load("asset/Dialog/dialog_box.png")
        self.box = pygame.transform.scale(self.box, (800, 100))
        self.font = pygame.font.Font("asset/Dialog/dialog_font.ttf", 20)
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.reading = False

    def display(self, screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
                
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 50, self.Y_POSITION + 20))
        
    def set_text(self, texts):
        self.texts = []
        self.texts.append(texts)
        self.text_index = 0
        self.letter_index = 0

    def next_text(self,npc, screen, player):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            time.sleep(1)
            self.reading = False
            NPC.handle_interaction(npc,screen, player)
    
    def end_dialog(self):
        self.reading = False
        
    def start_dialog(self, npc, screen, player):
        if self.reading:
            self.next_text(npc,screen, player)
        else:
            self.reading = True
            self.text_index = 0