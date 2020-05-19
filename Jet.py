import pygame

class Jet:

    def __init__(self, Window, Height = None, Width = None, x_position = None, y_position = None, Velocity = None):
        self.name = 'Jet'
        self.bg = Window
        self.Height = 160 if not Height else Height
        self.Width = 200 if not Width else Width
        self.x_position = (self.bg.Width // 40) if not x_position else x_position
        self.y_position = (self.bg.Height // 2 - self.Height//2)if not y_position else y_position
        self.Velocity = 20 if not Velocity else Velocity
        self.jetImg = pygame.transform.scale(pygame.image.load('IMGS//JET.png'),(self.Width,self.Height))
        self.shoot = False

    def move(self,bullets):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y_position >= self.Velocity:
            self.y_position -= self.Velocity
        if keys[pygame.K_DOWN] and self.y_position < self.bg.Height - self.Height:
            self.y_position += self.Velocity
        if (keys[pygame.K_KP0] or keys[pygame.K_SPACE]) and bullets > 0:
            self.shoot = True
        
        
    def draw(self):
        self.bg.Window.blit(self.jetImg,(self.x_position,self.y_position))
        pygame.display.update()       

    def get_mask(self):
        return pygame.mask.from_surface(self.jetImg)