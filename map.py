import pygame
import LoadFile
import csv
import os
from settings import *


class mainMap(pygame.sprite.Sprite):
    def __init__(self, mapSize):
        super().__init__()
        self.mapSurface = pygame.Surface(mapSize)
        self.mapSurface.set_colorkey((0, 0, 0))
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

    def getSurface(self):
        return self.mapSurface

    def drawObject(self, image, position, sprite_rect, location_rect):
        self.mapSurface.fill((0, 0, 0), location_rect)
        self.mapSurface.blit(image, position, sprite_rect)


class Tile:

    def __init__(self, key, posx, posy, rectx, recty):
        self.key = key
        self.rectx = rectx
        self.recty = recty
        self.posx = posx
        self.posy = posy
        self.initrect()

    def initrect(self):
        self.rect = pygame.Rect(self.rectx, self.recty, CUBESIZE, CUBESIZE)


    def getRect(self):
        return self.rect