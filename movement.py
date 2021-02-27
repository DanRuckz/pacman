import pygame
import pacman
import auxiliary
import enemy
from entity import entity

borders = [1260, 1000]
direction = "None"

class Move:
    @staticmethod
    def movement(obj, direction):
        if direction == "Left":
            obj.moveLeft(entity, obj)
        if direction == "Right":
            obj.moveRight(entity, obj)
        if direction == "Up":
            obj.moveUp(entity, obj)
        if direction == "Down":
            obj.moveDown(entity, obj)
        if direction == "None":
            rect = 0





"""     if keys[pygame.K_a] and pacman.Player.posx >0 and not collision:
            self.moveLeft(self,pacman.Player)
        elif keys[pygame.K_d] and pacman.Player.posx < borders[0] - pacman.Player.width and not collision:
            self.moveRight(self,pacman.Player)
        elif keys[pygame.K_w] and pacman.Player.posy > 0 and not collision:
            self.moveUp(self,pacman.Player)
        elif keys[pygame.K_s] and pacman.Player.posy < borders[1] - pacman.Player.height and not collision:
            self.moveDown(self,pacman.Player)
        if collision:
            auxiliary.colisionHandler(pacman.Player,collision)
"""
