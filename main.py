import pygame
import pacman
import enemy
from map import *
import movement
import auxiliary
from settings import *
from movement import Move
from movement import direction
from pacman import *
from enemy import *
import collision_objects

pygame.init()  # to init pygame
clock = pygame.time.Clock()
borders = [750, 991]
origin = OFFSET

# to create screen
screen = pygame.display.set_mode(borders, pygame.RESIZABLE)
pygame.display.set_caption("Pacman")
icon = pygame.image.load("sea.png")
pygame.display.set_icon(icon)
fullMap = Tiles(borders)


#map.Hitbox.insertPlayer(map.Hitbox)
#rect = map.Hitbox.drawMapHitboxes(map.Hitbox, screen)

#def mapColision(rect):
    #for element in rect:
       # temp = pygame.Rect(element)
        #auxiliary.hitboxCollision(Player.rect, temp)

def drawObjects():
    screen.blit(fullMap.getSurface(), (0, TOPSECTION))
    fullMap.drawObject(Player.Player, (Player.posx, Player.posy), Player.sprite)
    #screen.blit(Player.Player, (Player.posx, Player.posy), Player.sprite)


def resizeSurface(Surface):
    Surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


    #screen.blit(Tile.Map, Tile.POS, Tile.sprites[1])
#def enemyMove():
    #screen.blit(Enemy.Enemy, (Enemy.posx, Enemy.posy))
    #auxiliary.drawHitbox(screen, enemy.Enemy)

collision = False
running = True
while running:
    screen.fill((0, 0, 0))
    #fullMap.getSurface().fill((0, 0, 0))
    drawObjects()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            resizeSurface(fullMap.getSurface())
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
    Move.movement(pacman.Player, direction)
    #auxiliary.divideMap(screen)
    #mapColision(rect)
    #print(Player.rect)
    pygame.display.update()
    clock.tick(60)
# if event.type == pygame.KEYDOWN: --- for single key press
# if event.type == pygame.KEYUP: -- for single key press then release
#   if event.key == pygame.K_a or event.key == pygame.K_d:
#      print("key released")
