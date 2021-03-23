import pygame
from settings import *


class Entity:

    def Move(obj, direction, colliding):

        if direction == "Left" and not "Left" in colliding:
            obj.posx -= obj.speed

        if direction == "Right" and not "Right" in colliding:
            obj.posx += obj.speed

        if direction == "Up" and not "Up" in colliding:
            obj.posy -= obj.speed

        if direction == "Down" and not "Down" in colliding:
            obj.posy += obj.speed

        obj.setMovingDirection(direction)

    def checkPosition_forMovement(obj):
        if (obj.posx - 1) % CUBESIZE == 0 and (obj.posy - 1) % CUBESIZE == 0:
            return True
