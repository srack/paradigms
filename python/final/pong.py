import sys
import os
import math
import pygame
from pygame.locals import *

player = 0

class score(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.font = pygame.font.SysFont("calibri",40)
        self.xpos = x
        self.ypos = y

    def tick(self,score):
        self.score = self.font.render(str(score), True,(255,255,255))

class bar(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        self.bar = pygame.Surface((10,60))
        self.bar = self.bar.convert()
        self.bar.fill(color)
        
        self.rect = self.bar.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score = 0
   
    def tick(self):
        return

    def move(self, keycode):
        if keycode == K_UP:
            self.rect = self.rect.move(0, -9)
        if keycode == K_DOWN:
            self.rect = self.rect.move(0, 9)
        return

class ball(pygame.sprite.Sprite):
    def __init__(self):
        self.circ_sur = pygame.Surface((15,15))
        self.circ = pygame.draw.circle(self.circ_sur,(0,255,0),(15/2,15/2),15/2)
        self.circle = self.circ_sur.convert()
        self.circle.set_colorkey((0,0,0))
        
        self.rect = self.circle.get_rect()
        self.rect.x = 640/2
        self.rect.y = 480/2
        
        self.x_speed = -3.0
        self.y_speed = 3.0
    
    def tick(self,bar0,bar1):
        # Walls
        if self.rect.y > 480:
            self.y_speed = -self.y_speed
        
        elif self.rect.y < 0:
            self.y_speed = -self.y_speed
        
        ## collision with bars
        # left bar
        if self.rect.colliderect(bar0.rect) == True:
            self.x_speed = -self.x_speed
        
        # right bar
        elif self.rect.colliderect(bar1.rect) == True:
            self.x_speed = -self.x_speed
        
        if self.rect.x < 0:
            self.rect.x = 640/2
            self.rect.y = 480/2
            bar1.score += 1
                   
        if self.rect.x > 640:
            self.rect.x = 640/2
            self.rect.y = 480/2
            bar0.score += 1
                   
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed
        
class GameSpace:
    def main(self):
        # 1) basic init
        pygame.init()
        
        self.size = self.width, self.height = 640, 480
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        pygame.key.set_repeat(1, 50)
        
        
        # 2) set up game objects
        self.clock = pygame.time.Clock()
        self.bar0 = bar((255,0,0),10,215)
        self.bar1 = bar((0,0,255),620,215)
        self.ball = ball()
        self.score0 = score(250,10)
        self.score1 = score(380,10)

        # 3) start game loop
        while 1:
            # 4) regulate tick speed
            self.clock.tick(60)

            # 5) handle user input events

            for event in pygame.event.get():
                if player == 0:
                    if event.type == KEYDOWN:
                        self.bar0.move(event.key)
                
                    if event.type == KEYUP:
                        self.bar0.move(event.key)
                
                if player == 1:
                    if event.type == KEYDOWN:
                        self.bar1.move(event.key)
                
                    if event.type == KEYUP:
                        self.bar1.move(event.key)
                        
                if event.type == pygame.QUIT:
                    sys.exit()

    
            # 6) ongoing behavior
            self.bar0.tick()
            self.bar1.tick()
            self.ball.tick(self.bar0,self.bar1)
            self.score0.tick(self.bar0.score)
            self.score1.tick(self.bar1.score)
            
            # 7) animation
            self.screen.fill(self.black)
            self.screen.blit(self.bar0.bar,self.bar0.rect)
            self.screen.blit(self.bar1.bar,self.bar1.rect)
            self.screen.blit(self.ball.circle,self.ball.rect)
            self.screen.blit(self.score0.score,(self.score0.xpos, self.score0.ypos))
            self.screen.blit(self.score1.score,(self.score1.xpos, self.score1.ypos))



            pygame.display.flip()

gs = GameSpace()
gs.main()
