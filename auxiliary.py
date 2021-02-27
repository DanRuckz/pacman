import pygame
from settings import *

white = (255, 255, 255)



def divideMap(screen):
    for x in range(0, WIDTH, CUBESIZE):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, CUBESIZE):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (WIDTH, y))


def hitboxCollision(firstRect, secondRect):
    if (firstRect.x + firstRect.width > secondRect.x and firstRect.x < secondRect.x + secondRect.width) and (
            firstRect.y + firstRect.height > secondRect.y and firstRect.y < secondRect.y + secondRect.height):
        print(True)
        return True
    else:
        print(False)
        return False


def drawHitbox(screen, object):
    pygame.draw.rect(screen, white, (object.posx, object.posy, object.width, object.height), 2)


def rotateImage(image, degree):
    image = pygame.transform.rotate(image, degree)
    return image


def colisionHandler(object, collision):
    offset = 1
    # print(collision,pacman.Player.allTurns)
    if collision and object.turnLeft:
        object.posx += offset
    elif collision and object.turnRight:
        object.posx -= offset

    elif collision and object.turnUp:
        object.posy += offset

    elif collision and object.turnDown:
        object.posy -= offset
    object.updatePosition(object)
#  print(pacman.Player.rect)
