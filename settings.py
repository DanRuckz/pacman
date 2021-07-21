from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    HELL = 0


WIDTH = 750
HEIGHT = 991
RESOLUTION = [WIDTH, HEIGHT]
CUBESIZE = 30
SPRITESIZE = CUBESIZE - 2
TOPSECTION = 0
BLACKCUBE = 11
