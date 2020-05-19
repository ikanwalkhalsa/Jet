import pygame


class Bullet:

    def __init__(self,Window,Jet):
        self.name = 'Bullet'
        self.bg = Window
        J = Jet
        self.bulletImg = pygame.transform.scale(pygame.image.load('IMGS//bullet.png'),(60,20))
        self.x_position , self.y_position = J.x_position + J.Width//2, J.y_position + J.Height //2
        self.Velocity = 50
        self.bulletCount = 1
    
    def draw(self):
        self.bg.Window.blit(self.bulletImg,(self.x_position,self.y_position))
        self.x_position += self.Velocity     

    def get_mask(self):
        return pygame.mask.from_surface(self.bulletImg)   