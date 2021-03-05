import pygame
import LoadFile
from settings import *
from entity import Entity


class Player(Entity):

    Player = LoadFile.spritesheet
    width = SPRITESIZE
    height = SPRITESIZE
    posx = 1
    posy = 1
    speed = 2
    sprite_rect = pygame.Rect(posx, posy, width, height)

    def Move(self, direction):

        if direction == "Left":
            self.sprite_rect.x = SPRITESIZE*0

        elif direction == "Right":
            self.sprite_rect.x = SPRITESIZE*3

        elif direction == "Up":
            self.sprite_rect.x = SPRITESIZE*6

        elif direction == "Down":
            self.sprite_rect.x = SPRITESIZE*9

        super().Move(direction)

    def getPosision(self):
        POS = [self.posx, self.posy]
        return POS