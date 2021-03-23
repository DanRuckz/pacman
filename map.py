import csv
import os
import pygame
import LoadFile
from settings import *


class mainMap(pygame.sprite.Sprite):

    def __init__(self, mapSize):
        super().__init__()
        self.mapSurface = pygame.Surface(mapSize)
        self.mapSurface.set_colorkey((0, 0, 0))
        self.tiles = []
        self.nonblack = []
        self.parseData()
        self.fillMap()
        self.nonBlackRects()


    def parseData(self):
        key = "none"
        csvmap = self.readcsv("spritesheet/big_map.csv")
        x = y = 0
        for row in csvmap:
            x = 0
            for tile in row:
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
            self.mapSurface.blit(LoadFile.map, (tile.posx, tile.posy), tile.getRect())

    def drawMap(self):
        for black in self.tiles:
            if black.key is BLACKCUBE:
                self.mapSurface.blit(LoadFile.map, (black.posx, black.posy), black.getRect())
        self.mapSurface.blit(self.objectImage, self.objectPos, self.objspriteRect)
        # pygame.draw.rect(self.mapSurface, (255, 255, 255), self.objectRect, 3)
        return self.mapSurface

    def setObject_toDraw(self, image, pos, rect, sprite_rect):
        self.objectImage = image
        self.objectPos = pos
        self.objectRect = rect
        self.objspriteRect = sprite_rect

    def getTiles(self):
        return self.tiles

    def nonBlackRects(self):
        for nonblack in self.tiles:
            if nonblack.key is not BLACKCUBE:
                self.nonblack.append(nonblack)
                #pygame.draw.rect(self.mapSurface, (255, 255, 255), (nonblack.posx, nonblack.posy, CUBESIZE, CUBESIZE), 3)

    def getNonBlack(self):
        return self.nonblack


class Tile:

    def __init__(self, key, posx, posy, rectx, recty):
        self.key = key
        self.rectx = rectx
        self.recty = recty
        self.posx = posx
        self.posy = posy
        self.initspriterect()
        self.initrect()

    def initspriterect(self):
        self.spriterect = pygame.Rect(self.rectx, self.recty, CUBESIZE, CUBESIZE)

    def initrect(self):
        self.rect = pygame.Rect(self.posx, self.posy, CUBESIZE, CUBESIZE)

    def getRect(self):
        return self.spriterect
