import pygame
import random

class Perso:
    def __init__(self,ecran):
        self.width = 50
        self.height = 50
        self.x = 500
        self.y = -2000
        self.vit = 500
        self.ecran = ecran
        self.canjump = True
        self.sautForce = 0
        self.maxSautForce = 1500
    
    def Draw(self):
        image = pygame.image.load("amogus.png")
        imageshaped = pygame.transform.scale(image, (self.width, self.height))
        self.ecran.blit(imageshaped, (self.x,self.y))
        #pygame.draw.image(self,ecran, ())
        #pygame.draw.circle(self.ecran, (0,0,255), (self.x,self.y), 20)
    def Update(self,deltatime):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += deltatime * self.vit
        if pygame.key.get_pressed()[pygame.K_q]:
            self.x += -deltatime * self.vit
        self.y += deltatime* 1000
        self.jump(deltatime)

    def jump(self,deltatime):
        self.y -= deltatime* self.sautForce
        self.sautForce -= deltatime* 1500
        if self.sautForce < 0 : self.sautForce = 0