import pygame
from settings import *

class entity:
    @staticmethod
    def moveLeft(self, obj):
        obj.changeDirection(obj, "Left")
        obj.posx -= obj.speed
        obj.rect.x = obj.posx
        obj.turnLeft = True
        self.turnOffSwitch(obj, "moveLeft")

    def moveRight(self, obj):
        obj.changeDirection(obj, "Right")
        obj.posx += obj.speed
        obj.rect.x = obj.posx
        obj.turnRight = True
        self.turnOffSwitch(obj, "moveRight")

    def moveUp(self, obj):
        obj.changeDirection(obj, "Up")
        obj.posy -= obj.speed
        obj.rect.y = obj.posy
        obj.turnUp = True
        self.turnOffSwitch(obj, "moveUp")

    def moveDown(self, obj):
        obj.changeDirection(obj, "Down")
        obj.posy += obj.speed
        obj.rect.y = obj.posy
        obj.turnDown = True
        self.turnOffSwitch(obj, "moveDown")

    def turnOffSwitch(obj, condition):

        if condition == "moveLeft":
            obj.turnRight = False
            obj.turnUp = False
            obj.turnDown = False

        if condition == "moveRight":
            obj.turnLeft = False
            obj.turnUp = False
            obj.turnDown = False

        if condition == "moveUp":
            obj.turnLeft = False
            obj.turnRight = False
            obj.turnDown = False

        if condition == "moveDown":
            obj.turnLeft = False
            obj.turnRight = False
            obj.turnUp = False
