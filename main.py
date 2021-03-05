import pygame
import pacman
import enemy
from map import mainMap
from settings import *
from entity import Entity



pygame.init()  # to init pygame
clock = pygame.time.Clock()

# to create screen
screen = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption("Pacman")
icon = pygame.image.load("sea.png")
pygame.display.set_icon(icon)
fullMap = mainMap(RESOLUTION)
player = pacman.Player()

def drawObjects():
    fullMap.setObject_toDraw(player.playerImage, player.getPosition(), player.getRect())
    screen.blit(fullMap.drawMap(), (0, TOPSECTION))


def resizeSurface(Surface):
    Surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)



collision = False
running = True
direction = 0
animationCounter = 0
while running:
    screen.fill((0, 0, 0))
    drawObjects()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            resizeSurface(fullMap.drawMap())
            resizeSurface(screen)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                direction = "Left"
            if event.key == pygame.K_d:
                direction = "Right"
            if event.key == pygame.K_w:
                direction = "Up"
            if event.key == pygame.K_s:
                direction = "Down"
            if event.key == pygame.K_SPACE:
                direction = "Hell"
    if keys[pygame.K_ESCAPE]:
        running = False

    animationCounter += clock.get_time()
    if animationCounter > 100:
        player.animate(direction)
        animationCounter = 0

    player.Move(direction)

    pygame.display.update()

    clock.tick(40)



"""
##FOR FUTURE REFERENCE
  if event.type == pygame.KEYDOWN: --- for single key press
  if event.type == pygame.KEYUP: -- for single key press then release
    if event.key == pygame.K_a or event.key == pygame.K_d:
       print("key released")
"""