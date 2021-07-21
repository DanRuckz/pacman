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
        self.colliding = []
        self.updateRect()

    def Move(self, direction):
        self.pendingMovingDirection = direction
        if self.movingDirection == Direction.LEFT or self.movingDirection == Direction.RIGHT:
            horizontal = True
        else:
            horizontal = False

        if horizontal and (direction == Direction.LEFT or direction == Direction.RIGHT):
            super().Move(direction, self.colliding)

        elif not horizontal and (direction == Direction.UP or direction == Direction.DOWN):
            super().Move(direction, self.colliding)

        elif horizontal and (direction == Direction.UP or direction == Direction.DOWN):
            if super().checkPosition_forMovement() is True:
                super().Move(direction, self.colliding)
            else:
                super().Move(self.movingDirection, self.colliding)

        elif not horizontal and (direction == Direction.LEFT or direction == Direction.RIGHT):
            if super().checkPosition_forMovement() is True:
                super().Move(direction, self.colliding)
            else:
                super().Move(self.movingDirection, self.colliding)

        elif self.movingDirection == 0:
            super().Move(direction, self.colliding)

        print(self.movingDirection)
        self.updateRect()
        self.colliding.clear()

    def getImage(self):
        return self.playerImage

    def getPosition(self):
        return self.posx, self.posy

    def getRect(self):
        return self.rect

    def getspriteRect(self):
        return self.sprite_rect

    def animate(self, direction):

        if direction == Direction.HELL:
            return

        if self.animationIndex == 0:
            self.scrollDirection = "Incrementing"

        if self.animationIndex == 2:
            self.scrollDirection = "Decrementing"

        if self.scrollDirection == "Incrementing":
            self.animationIndex += 1

        if self.scrollDirection == "Decrementing":
            self.animationIndex -= 1

        if self.movingDirection == Direction.LEFT:
            self.animationDirection = 0 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

        elif self.movingDirection == Direction.RIGHT:
            self.animationDirection = 3 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

        elif self.movingDirection == Direction.UP:
            self.animationDirection = 6 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

        elif self.movingDirection == Direction.DOWN:
            self.animationDirection = 9 + self.animationIndex
            self.sprite_rect.x = SPRITESIZE * self.animationDirection

    def setMovingDirection(self, direction):
        self.movingDirection = direction

    def updateRect(self):
        self.rect = pygame.Rect(self.posx, self.posy, SPRITESIZE, SPRITESIZE)

    def collision(self, other):
        for element in other:

            if element.rect.collidepoint(self.rect.left - 2, self.rect.centery):
                colliding_left = Direction.LEFT
                self.colliding.append(colliding_left)

            elif element.rect.collidepoint(self.rect.centerx, self.rect.top - 2):
                colliding_up = Direction.UP
                self.colliding.append(colliding_up)

            elif element.rect.collidepoint(self.rect.right + 2, self.rect.centery):
                colliding_right = Direction.RIGHT
                self.colliding.append(colliding_right)


            elif element.rect.collidepoint(self.rect.centerx, self.rect.bottom + 2):
                colliding_down = Direction.DOWN
                self.colliding.append(colliding_down)
