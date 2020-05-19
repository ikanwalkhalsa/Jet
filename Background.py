import pygame

class Background:

    def __init__(self, Width = None, Height = None):
        self.x_pos = 0
        self.Width = 700 if not Width else Width
        self.Height = 450 if not Height else Height
        self.Window = pygame.display.set_mode((self.Width, self.Height))
        pygame.display.set_caption("HelliCarrier")
        self.bgImg = pygame.transform.scale(pygame.image.load('IMGS//bg7.jpg'),(self.Width,self.Height))
        self.Window.blit(self.bgImg,(0,0))
    
    def drawBg(self,b,score,Speed = None):
        self.Speed = 10 if Speed == None else Speed
        self.Window.blit(self.bgImg,(self.x_pos,0))
        self.Window.blit(self.bgImg,(self.x_pos+self.Width,0))
        self.x_pos -= self.Speed
        if self.x_pos == -self.Width:
            self.x_pos = -self.Speed
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        textsurface = myfont.render(str(b.bulletCount), False, (255, 255, 255))
        Score = myfont.render("Score :"+str(score), False, (255, 255, 255))
        self.Window.blit(textsurface,(62,0))
        self.Window.blit(Score,(300,0))
        self.Window.blit(b.bulletImg,(0,0))
        self.Window.blit(b.bulletImg,(0,20))