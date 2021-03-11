import pygame
import LoadFile
from settings import *
from entity import Entity


class Player(Entity):

    def __init__(self):
        self.playerImage = LoadFile.spritesheet
        self.width = SPRITESIZE
        self.height = SPRITESIZE
        self.spriteinRect_posx = 0
        self.spriteinRect_posy = 0
        self.posx = CUBESIZE + 1
        self.posy = CUBESIZE + 1
        self.speed = 2
        self.sprite_rect = pygame.Rect(self.spriteinRect_posx, self.spriteinRect_posy, self.width, self.height)
        self.rect = 0
        self.animationDirection = 0
        self.animationIndex = 0
        self.scrollDirection = 0
        self.movingDirection = 0
        self.pendingMovingDirection = 0
        self.updateRect()

    def Move(self, direction):
        self.pendingMovingDirection = direction
        if self.movingDirection == "Left" or self.movingDirection == "Right":
            horizontal = True
        else:
            horizontal = False

        if horizontal and (direction == "Left" or direction == "Right"):
            super().Move(direction)

        elif not horizontal and (direction == "Up" or direction == "Down"):
            super().Move(direction)

        elif horizontal and (direction == "Up" or direction == "Down"):
            if super().checkPosition_forMovement() is True:
                super().Move(direction)
            else:
                super().Move(self.movingDirection)

        elif not horizontal and (direction == "Left" or direction == "Right"):
            if super().checkPosition_forMovement() is True:
                super().Move(direction)
            else:
                super().Move(self.movingDirection)

        elif self.movingDirection == 0:
            super().Move(direction)

        self.updateRect()

    def getImage(self):
        return self.playerImage

    def getPosition(self):
        return self.posx, self.posy

    def getRect(self):
        return self.rect

    def getspriteRect(self):
        return self.sprite_rect

    def animate(self, direction):

        if direction == "Hell":
            return

        if self.animationIndex == 0:
            self.scrollDirection = "Incrementing"

        if self.animationIndex == 2:
            self.scrollDirection = "Decrementing"

        if self.scrollDirection == "Incrementing":
            self.animationIndex += 1

        if self.scrollDirection == "Decrementing":
            self.animationIndex -= 1

        if self.movingDirection == "Left":
            self.animationDirection = 0 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

        elif self.movingDirection == "Right":
            self.animationDirection = 3 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

        elif self.movingDirection == "Up":
            self.animationDirection = 6 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

        elif self.movingDirection == "Down":
            self.animationDirection = 9 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

    def setMovingDirection(self, direction):
        self.movingDirection = direction

    def updateRect(self):
        self.rect = pygame.Rect(self.posx, self.posy, SPRITESIZE, SPRITESIZE)

    def collision(self, other):
        for element in other:
            if element.rect.collidepoint(self.rect.midleft):
                print("midleft collision")
            if element.rect.collidepoint(self.rect.midtop):
                print("midtop collision")
            if element.rect.collidepoint(self.rect.midright):
                print("midright collision")
            if element.rect.collidepoint(self.rect.midbottom):
                print("midbottom collision")
