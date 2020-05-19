import pygame
import random 

class Enemy:

    def __init__(self,Window, Width = None, Height = None):
        self.bg = Window
        self.Width = Width if Width else 100
        self.Height = Height if Height else 100
        self.enmy = pygame.transform.scale(pygame.image.load('IMGS//enmy.png',),(self.Width,self.Height))
        self.x_position = self.bg.Width
        self.bx = self.x_position + self.Width//2 
        self.y_position = random.randint(0, self.bg.Height-self.Height)
        self.bulletImg = pygame.transform.scale(pygame.image.load('IMGS//bullet.png'),(30,15))
        self.bulletImg = pygame.transform.flip(self.bulletImg,True,False)
        self.playSound('Sounds\enemy.mp3')
    
    def playSound(self,Sound):
        pygame.mixer.init()
        pygame.mixer.music.load(Sound)
        pygame.mixer.music.play()
    
    def draw(self, Speed = None):
        self.Velocity = 12 if Speed == None else Speed
        self.x_position -= self.Velocity
        if (self.bx - 2*self.Velocity) > 0 - 40:
            self.bx = (self.bx - 2*self.Velocity)
        else:
            self.bx = self.x_position
        self.bg.Window.blit(self.enmy,(self.x_position,self.y_position))
        if self.x_position > 300:
            self.bg.Window.blit(self.bulletImg, (self.bx,self.y_position + self.Height//2))
        if self.bx == self.x_position and self.bx > 300:
            self.playSound('Sounds\enemy.mp3')
    
    def collide(self,object):
        omask = object.get_mask()
        emask = pygame.mask.from_surface(self.enmy)
        enemy_offset = (self.x_position - object.x_position, self.y_position - round(object.y_position))
        enemyPoint = omask.overlap(emask,enemy_offset)
        if object.name == "Jet":
            bmask = pygame.mask.from_surface(self.bulletImg)
            bullet_offset = (self.bx - object.x_position, (self.y_position+self.Height//2) - round(object.y_position))
            bulletPoint = omask.overlap(bmask,bullet_offset)
            if bulletPoint:
                return True
        return True if enemyPoint else False
            