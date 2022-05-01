import pygame

from enemie import Enemie
class Sol:
    def __init__(self,ecran,x,y,width,height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ecran = ecran
        self.image = image
    
    def Draw(self):
        imageshaped = pygame.transform.scale(self.image, (self.width, self.height))
        self.ecran.blit(imageshaped, (self.x,self.y))
        #pygame.draw.rect(self.ecran, (0, 155, 0), pygame.Rect(self.x, self.y, self.width, self.height))

    def Collision(self, player):
        if self.y <= player.y +50 and player.x +50 >= self.x:
            if player.x -50 <= self.x + self.width and player.y-50<=self.y+self.height:
                x = self.x + self.width/2
                y = self.y + self.height/2
                if player.y > self.y and player.y < self.y + self.height:
                    if player.x < x:
                        player.x = self.x-50
                        if type(player) == Enemie:
                            player.dir = 'left'
                    if player.x > x:
                        player.x = self.x + self.width+50
                        if type(player) == Enemie:
                            player.dir = 'right'
                if player.x > self.x and player.x < self.x + self.width:
                    if player.y < y:
                        player.y = self.y -50
                        player.canjump = True  
                    if player.y > y:
                        player.y = self.y +50