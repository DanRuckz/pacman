import pygame
from settings import *
from abc import ABC, abstractmethod

class Entity:

    @abstractmethod
    def Move(self, direction):
       pass


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