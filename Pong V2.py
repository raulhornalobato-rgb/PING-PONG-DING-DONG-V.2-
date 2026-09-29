import pygame
import random as rd
import time

GoUp = False
GoDown = False

ForwardBackward = True
UpDown = False

PaddleX = 20
PaddleY = 200

BallX = rd.randint(50,450)
BallY = rd.randint(150,300)

pygame.init()

Screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")

def BallMove():
    global BallX
    global BallY

    global ForwardBackward
    global UpDown

    if ForwardBackward == True:
        BallX += 1
    elif ForwardBackward == False:
        BallX -= 1

    if UpDown == True:
        BallY -= 1
    elif UpDown == False:
        BallY += 1
def BallPhysics():
    global BallX
    global BallY

    global ForwardBackward
    global UpDown

    if BallY == 0:
        UpDown = False
    elif BallY == 600:
        UpDown = True

    if BallX == 600:
        ForwardBackward = False
    elif BallX == 0:
        ForwardBackward = True

def PaddleCollisions():
    global BallX
    global BallY

    global ForwardBackward
    global UpDown

    global PaddleX
    global PaddleY

    global Choice

    if PaddleX == BallX:
        Choice = rd.randint(0,1)
        if Choice == 0:
            UpDown = True
        else:
            UpDown = False
while True:
    BallMove()
    BallPhysics()
    PaddleCollisions()

    time.sleep(0.01)
    Screen.fill((0,0,0))
    Rectangle = pygame.draw.rect(Screen, (255,255,255),(PaddleX,PaddleY,10,150), width = 2)
    Rectangle = pygame.draw.circle(Screen, (255,255,255),(BallX,BallY), 10, width = 2)
    # the width part can make the squares fill empty, yes this is possible using pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Screen.fill((0,0,0))
                PaddleY -= 15
            elif event.key == pygame.K_s:
                Screen.fill((0,0,0))
                PaddleY += 15
            # Screen.fill is to delete past paddles.
    pygame.display.update()