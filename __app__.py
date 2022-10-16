import pygame
import random


pygame.init()


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Dino Game")


dino = pygame.image.load('d.png')
Px = 50
Py = 300
def dinos(x,y):
    screen.blit(dino,(x,y))
PyC = 0
run = True
zıp = True

cX = 600
cY = 310

cac = pygame.image.load('engel2.png')
def cactus(x,y):
    screen.blit(cac,(x,y))

fontZ = pygame.font.Font('freesansbold.ttf',32)
def score(x):
    text = fontZ.render('Score:'+str(int(skor)),True,(50,50,50))
    screen.blit(text,(20,20))

font = pygame.font.Font('freesansbold.ttf',50)
def Game():
    text = font.render('GAME OVER',True,(50,50,50))
    screen.blit(text,(250,200))

a = True
skor = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if a == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if zıp == True:
                    PyC = 0.7
                    print("ok")
        
        
        screen.fill((255,255,255))
        dinos(Px,Py)
        Py = Py - PyC 

        cactus(cX,cY)
        if 200 >= Py:
            zıp =False
            PyC = -0.5
        if Py >= 300:
            PyC = 0
            Py = 300
        if Py == 300:
            zıp = True

        cX = cX - 0.5

        if cX < 0:
            cX = 800

        if cX+20>=Px>=cX and cY>=Py>=cY-20:
            a = False

        skor += 0.01
        score(skor)
    else:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                a = True

         skor = 0
         Game()
    pygame.display.update()