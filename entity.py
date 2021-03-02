import pygame
from settings import *


class Entity:
    # @staticmethod

    def setMove(self, obj, direction):
        if direction == "Left":
            self.moveLeft(self, obj)
        if direction == "Right":
            self.moveRight(self, obj)
        if direction == "Up":
            self.moveUp(self, obj)
        if direction == "Down":
            self.moveDown(self, obj)

    def moveLeft(self, obj):
        obj.changeDirection(obj, "Left")
        obj.posx -= obj.speed
        obj.rect.x = obj.posx
        obj.turnLeft = True

    def moveRight(self, obj):
        obj.changeDirection(obj, "Right")
        obj.posx += obj.speed
        obj.rect.x = obj.posx
        obj.turnRight = True

    def moveUp(self, obj):
        obj.changeDirection(obj, "Up")
        obj.posy -= obj.speed
        obj.rect.y = obj.posy
        obj.turnUp = True

    def moveDown(self, obj):
        obj.changeDirection(obj, "Down")
        obj.posy += obj.speed
        obj.rect.y = obj.posy
        obj.turnDown = True
