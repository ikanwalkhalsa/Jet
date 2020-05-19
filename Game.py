import pygame
from Jet import Jet
from Background import Background
from Enemy import Enemy
from Bullets import Bullet
import sys

class Main:

    def __init__(self):
        self.bg = Background()
        self.jet = Jet(self.bg)
        self.b = Bullet(self.bg,self.jet)
        self.Score = 0

    
    def playSound(self,Sound):
        pygame.mixer.init()
        pygame.mixer.music.load(Sound)
        pygame.mixer.music.play()

    def gameloop(self):
        Enemies = [Enemy(self.bg)]
        Bullets = []
        gameCounter = 1
        run =  True
        Dificulty = 2
        while run:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.b.bulletCount <= 10:
                if gameCounter % 50 == 0:
                    self.b.bulletCount += 1
            self.jet.move(self.b.bulletCount)
            if self.b.bulletCount >= 1 and self.jet.shoot:
                Bullets.append(Bullet(self.bg,self.jet))
                self.b.bulletCount -= 1
                self.jet.shoot = False
                self.playSound('Sounds\jet.mp3')
            self.bg.drawBg(self.b,self.Score)
            for bullet in Bullets:
                bullet.draw()
                if bullet.x_position > self.bg.Width:
                    Bullets.pop(Bullets.index(bullet))
            if len(Enemies) == 0:
                Enemies.append(Enemy(self.bg))
            for i,enemy in enumerate(Enemies):
                for bullet in Bullets:
                    if enemy.collide(bullet):
                        Enemies.pop(i)
                        Bullets.pop(Bullets.index(bullet))
                        self.Score += 100
                        self.playSound('Sounds\collision.mp3')
                if enemy.collide(self.jet):
                    self.playSound('Sounds\collision.mp3')
                    run = False
                    break
                if enemy.x_position <self.bg.Width - self.bg.Width//Dificulty and i == len(Enemies) - 1:
                    Enemies.append(Enemy(self.bg))
                if enemy.x_position < 0 - enemy.Width:
                    Enemies.pop(i)
                enemy.draw()
            if gameCounter % 100 == 0 :
                self.Score += 10
            self.jet.draw()
            gameCounter += 1

        run = True 
        while run:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    run = False
            self.bg.drawBg(self.b,self.Score,Speed=0)
            for enemy in Enemies:
                enemy.draw()
            pygame.font.init()
            myfont = pygame.font.SysFont('Comic Sans MS', 70)
            textsurface = myfont.render("YOU LOST", False, (255, 255, 255))
            self.bg.Window.blit(textsurface,(150,150))
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.gameloop()


if __name__ == "__main__":
    Main().gameloop()