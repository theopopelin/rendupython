import pygame
import random
from player import Perso
from sol import Sol
from enemie import Enemie

pygame.init()

ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Le titre !")
p = Perso(ecran)
solList=[]
enemies=[]
barrel = pygame.image.load("keg.png")
ground = pygame.image.load("dirt.jpg")
obstaclelist=[pygame.image.load("mcgrass.png"),pygame.image.load("dirt.jpg")]
for x in range(0, 10):
    picture = random.choice(obstaclelist)
    solList.append(Sol(ecran, random.randint(0,1000), random.randint(200,500), random.randint(50,100), random.randint(50,100), picture))
solList.append(Sol(ecran, 0, 800, 1000, 50, ground))
solList.append(Sol(ecran, 980, 700, 50, 100, ground))
solList.append(Sol(ecran, 20, 700, 50,  100, ground))
enemies.append(Enemie(ecran, 50, 50, 'right'))
loop = True
getTicksLastFrame = 0
while loop:
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    p.Update(deltaTime)

    for sol in solList:
        sol.Collision(p)
        for en in enemies:
            sol.Collision(en)
    for en in enemies:
        en.Collision(p)
        en.Update(deltaTime)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if p.canjump:
                    p.canjump = False
                    p.sautForce = p.maxSautForce
        if event.type == pygame.QUIT:
            loop = False
    bgraw = pygame.image.load("paysage.jpg")
    bg = pygame.transform.scale(bgraw, (1000, 1000))
    ecran.blit(bg,(0, 0))

    for sol in solList:
        sol.Draw()
    p.Draw()
    for en in enemies:
        en.Draw()
    pygame.display.flip()

pygame.quit()