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

        obj.setMovingDirection(direction)

    def checkPosition_forMovement(obj):
        if (obj.posx - 1) % CUBESIZE == 0 and (obj.posy - 1) % CUBESIZE == 0:
            return True
