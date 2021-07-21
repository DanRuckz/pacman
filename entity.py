import pygame
from settings import *


class Entity:

    def Move(obj, direction, colliding):

        if direction == Direction.LEFT and not Direction.LEFT in colliding:
            obj.posx -= obj.speed

        if direction == Direction.RIGHT and not Direction.RIGHT in colliding:
            obj.posx += obj.speed

        if direction == Direction.UP and not Direction.UP in colliding:
            obj.posy -= obj.speed

        if direction == Direction.DOWN and not Direction.DOWN in colliding:
            obj.posy += obj.speed

        obj.setMovingDirection(direction)

    def checkPosition_forMovement(obj):
        if (obj.posx - 1) % CUBESIZE == 0 and (obj.posy - 1) % CUBESIZE == 0:
            return True
