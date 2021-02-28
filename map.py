import pygame
import LoadFile
import csv
import os
from settings import *



class Tiles(pygame.sprite.Sprite):
    def __init__(self, mapSize):
        super().__init__()
        self.bigSurface = pygame.Surface(mapSize)
        self.bigSurface.set_colorkey((0, 0, 0))
        self.tiles = []
        self.parseData()
        self.fillMap()

    def parseData(self):
        key = "none"
        csvmap = self.readcsv("spritesheet/big_map.csv")
        x = y = 0
        for row in csvmap:
            x = 0
            for tile in row:
                key = int(tile)
                key = int(tile)
                self.tiles.append(Tile(key, x * CUBESIZE, y * CUBESIZE, key * CUBESIZE, 0))
                x += 1
            y += 1

    def readcsv(self, filename):
        csvmap = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                csvmap.append(list(row))
            return csvmap

    def fillMap(self):
        for tile in self.tiles:
            self.bigSurface.blit(LoadFile.map, (tile.posx, tile.posy), tile.getRect())

    def drawMap(self):
        return self.bigSurface

    def drawObject(self, image, position, rect):
        self.bigSurface.blit(image, position, rect)

class Tile:

    def initrect(self):
        self.rect = pygame.Rect(self.rectx, self.recty, CUBESIZE, CUBESIZE)

    def getRect(self):
        return self.rect

    def __init__(self, key, posx, posy, rectx, recty):
        self.key = key
        self.rectx = rectx
        self.recty = recty
        self.posx = posx
        self.posy = posy
        self.initrect()








    # POS = (50,50)
    # sprites.append(pygame.Rect(0,0,SPRITESIZE,SPRITESIZE))
    # sprites.append(pygame.Rect(25,0,SPRITESIZE,SPRITESIZE))


"""
#def fillArray():
    #mapArray = []
    #file = open("MapBoxes.txt", "r")
    #content = file.read()
    #file.close()
    #for i in range(0, len(content)):
    #    mapArray.append(content[i])
    #return mapArray


class Hitbox:

    #array = fillArray()

    def insertPlayer(self):
        i = 0
        j = 0
        for box in range(0, len(self.array)):
            if self.array[box] == "\n":
                j += 1
                i = 0
            if self.array[box] == "P":
                Player.posx += i * CUBESIZE + 3
                Player.posy += j * CUBESIZE + 3
                Player.updatePosition(Player)
            if self.array[box] != "\n":
                i += 1

    rect = []

    def drawMapHitboxes(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), Player.rect, 1)
        i = 0
        j = 0

        for box in range(0, len(self.array)):
            if self.array[box] == "\n":
                j += 1
                i = 0
            if self.array[box] == "#":
                #pygame.draw.rect(screen, (255, 255, 255), (i * CUBESIZE, j * CUBESIZE, CUBESIZE, CUBESIZE), 1)
                temp = (i * CUBESIZE, j * CUBESIZE, CUBESIZE, CUBESIZE)
                self.rect.append(temp)
            if self.array[box] != "\n":
                i += 1
        return self.rect
"""

"""
bgrects = (pygame.Rect(0, 0, 1260, 18), pygame.Rect(0, 0, 25, 425), pygame.Rect(0, 494, 25, 509),pygame.Rect(borders[0] - 25, 0, 25, 425), pygame.Rect(borders[0] - 25, 494, 25, 509))

fullMap = (pygame.Rect(0, 0, 1260, 18), pygame.Rect(0, 0, 25, 425), pygame.Rect(0, 494, 25, 509),pygame.Rect(borders[0] - 25, 0, 25, 425), pygame.Rect(borders[0] - 25, 494, 25, 509),
           pygame.Rect(0,982,1260,17),pygame.Rect(335,244,medium_vertical_line[0],medium_vertical_line[1]),pygame.Rect(224,326,small_vertical_line[0],small_vertical_line[1]),
           pygame.Rect(110,80,small_vertical_line[0],small_vertical_line[1]),pygame.Rect(225,80,small_vertical_line[0],small_vertical_line[1]),
           pygame.Rect(336,80,medium_horizontal_line[0],medium_horizontal_line[1]),pygame.Rect(448,408,large_horizontal_line[0],large_horizontal_line[1]),
           pygame.Rect(675,80,medium_horizontal_line[0],medium_horizontal_line[1]),pygame.Rect(335,163,huge_horizontal_line[0],huge_horizontal_line[1]),
           pygame.Rect(1010,80,small_vertical_line[0],small_vertical_line[1]),pygame.Rect(1123,80,small_vertical_line[0],small_vertical_line[1]),
           pygame.Rect(111,244,small_vertical_line[0],small_vertical_line[1]),pygame.Rect(225,244,small_horizontal_line[0],small_horizontal_line[1]),
           pygame.Rect(448,243,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(448,243,medium_vertical_line[0],medium_vertical_line[1]),
           pygame.Rect(675,244,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(786,244,medium_vertical_line[0],medium_vertical_line[1]),
           pygame.Rect(898,244,medium_vertical_line[0],medium_vertical_line[1]),pygame.Rect(898,244,small_horizontal_line[0],small_horizontal_line[1]),
           pygame.Rect(1124,245,small_vertical_line[0],small_vertical_line[1]),pygame.Rect(1010,326,small_vertical_line[0],small_vertical_line[1]),
           pygame.Rect(225,490,small_horizontal_line[0],medium_horizontal_line[1]),pygame.Rect(899,490,small_horizontal_line[0],small_horizontal_line[1]),
           pygame.Rect(0,408,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(0,490,small_horizontal_line[0],small_horizontal_line[1]),
           pygame.Rect(1127,408,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(1127,490,small_horizontal_line[0],small_horizontal_line[1]),
           pygame.Rect(452,489,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(452,489,small_vertical_line[0],small_vertical_line[1]),
           pygame.Rect(560,490,small_vertical_line[0],small_vertical_line[1]),pygame.Rect(449,572,small_horizontal_line[0],small_horizontal_line[1]),
           pygame.Rect(673,490,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(673,490,small_vertical_line[0],small_vertical_line[1]),
           pygame.Rect(673,573,small_horizontal_line[0],small_horizontal_line[1]),pygame.Rect(784,490,small_vertical_line[0],small_vertical_line[1]))
           """
