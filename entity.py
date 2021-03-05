import pygame
from settings import *

class Entity:

    def Move(obj, direction):
        if direction == "Left":
           obj.posx -= obj.speed

        if direction == "Right":
            obj.posx += obj.speed

        if direction == "Up":
            obj.posy -= obj.speed

        if direction == "Down":
            obj.posy += obj.speed

'''
    def moveLeft(self, obj):
        obj.changeDirection(obj, "Left")
        obj.posx -= obj.speed
        obj.location_rect.x = obj.posx

    def moveRight(self, obj):
        obj.changeDirection(obj, "Right")
        obj.posx += obj.speed
        obj.location_rect.x = obj.posx

    def moveUp(self, obj):
        obj.changeDirection(obj, "Up")
        obj.posy -= obj.speed
        obj.location_rect.y = obj.posy

    def moveDown(self, obj):
        obj.changeDirection(obj, "Down")
        obj.posy += obj.speed
        obj.location_rect.y = obj.posy
'''