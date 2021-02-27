import pygame
import LoadFile
from settings import *
from entity import *


class Player(entity):
    Player = LoadFile.spritesheet
    sprite = pygame.Rect(168, 0, SPRITESIZE, SPRITESIZE)
    width = SPRITESIZE
    height = SPRITESIZE
    posx = 0
    posy = 0
    speed = 2
    turnLeft = False
    turnRight = False
    turnUp = False
    turnDown = False
    # allTurns = (turnUp,turnDown,turnLeft,turnRight)
    condition = "none"
    rect = pygame.Rect(posx, posy, width, height)

    def changeDirection(self, currentDirection):
        if currentDirection == "Left":
            self.sprite = pygame.Rect(0, 0, SPRITESIZE, SPRITESIZE)
            return self.sprite
        elif currentDirection == "Right":
            self.sprite = pygame.Rect(168, 0, SPRITESIZE, SPRITESIZE)
            return self.sprite
        elif currentDirection == "Up":
            self.sprite = pygame.Rect(336, 0, SPRITESIZE, SPRITESIZE)
            return self.sprite
        elif currentDirection == "Down":
            self.sprite = pygame.Rect(504, 0, SPRITESIZE, SPRITESIZE)
            return self.sprite

    def updatePosition(self):
        self.rect.x = self.posx
        self.rect.y = self.posy
