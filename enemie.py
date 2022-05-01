import math
import pygame

class Enemie:
    def __init__ (self, ecran,x,y, direction):
        self.width = 50
        self.height = 50
        self.x = 10
        self.y = 400
        self.vit = 100
        self.dir = direction
        self.ecran = ecran

    def Draw(self):
        red = pygame.image.load("red.png")
        self.ecran.blit(red, (self.x,self.y))

    def Update(self, deltatime) :
        if self.dir == "right":
            self.x += deltatime* self.vit
        elif self.dir == "left":
            self.x -= deltatime* self.vit
        self.y += deltatime* 200

    def Collision(self,player) :
        if math.sqrt((player.x-self.x)**2+(player.y - self.y)**2) <= 40:
            pygame.quit()