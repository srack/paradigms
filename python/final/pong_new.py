# Adrian Gerbaud and Sam Rack
# CSE 30332
# Final Project - Pong
# pong_new.py

import sys
import os
import random
import math
import pygame
from pygame.locals import *


screenW = 640
screenH = 480

barW = 10
barH = 90

# class: score
# for client use
class score(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.font = pygame.font.SysFont("calibri",40)
		self.xpos = x
		self.ypos = y
		self.score = self.font.render(str(0), True,(255,255,255))
	
	def tick(self,score):
		self.score = self.font.render(str(score), True,(255,255,255))

# class: gameOver
# for client use
class gameOver(pygame.sprite.Sprite):
	def __init__(self):
		self.font = pygame.font.SysFont("calibri", 60)
		self.xpos = screenW / 2 - 120
		self.ypos = screenH / 2 - 50
		self.score = self.font.render("GAME OVER", True, (100, 0, 255))
		

# class: bar
# for client use
class bar(pygame.sprite.Sprite):
	def __init__(self,color,x,y,width,height):
		self.bar = pygame.Surface((width,height))
		self.bar = self.bar.convert()
		self.bar.fill(color)
    
		self.rect = self.bar.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.score = 0
 
# class: sBar
# for server use, don't need the pygame attributes
class sBar:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.score = 0
	
	def tick(self):
		return

	def move(self, keycode):
		if keycode == str(K_UP):
			self.y -= 11
		elif keycode == str(K_DOWN):
			self.y += 11

# class: ball
# for client use, objects will be updated by clientGS class
class ball(pygame.sprite.Sprite):
	def __init__(self):     
		self.circ_sur = pygame.Surface((15,15))
		self.circ = pygame.draw.circle(self.circ_sur,(0,255,0),(15/2,15/2),15/2)
		self.circle = self.circ_sur.convert()
		self.circle.set_colorkey((0,0,0))
      
		self.rect = self.circle.get_rect()
		self.rect.x = screenW/2
		self.rect.y = screenH/2
      
		self.x_speed = -3.0
		self.y_speed = 3.0

# class: sBall
# for server use, used to actually update the location of the ball in tick()
class sBall:
	def __init__(self):
		self.x = screenW/2
		self.y = screenH/2

		self.x_speed = -5.0
		self.y_speed = 5.0

	def tick(self,bar0,bar1):
		## wall
		if self.y > screenH:
			self.y = screenH
			self.y_speed = -self.y_speed
		
		elif self.y < 0:
			self.y = 0
			self.y_speed = -self.y_speed
		
		## collision with bars 
		# random y direction
		# left bar
		if self.x >= bar0.x and self.x <= (bar0.x + bar0.width) and self.y >= bar0.y and self.y <= (bar0.y + bar0.height):   
			self.x_speed = -self.x_speed
			
			multiplier = 1
			if random.randint(0, 1) == 1:
				multiplier = -1 
			self.y_speed *= multiplier

			self.x += 2*self.x_speed
		
		# right bar
		elif self.x >= bar1.x and self.x <= (bar1.x + bar1.width) and self.y >= bar1.y and self.y <= (bar1.y + bar1.height):
			self.x_speed = -self.x_speed

			multiplier = 1
			if random.randint(0, 1) == 1:
				multiplier = -1 
			self.y_speed *= multiplier

			self.x += 2*self.x_speed
		
		## score updates
		if self.x < 0:
			bar1.score += 1
			# reset ball
			self.x = screenW/2
			self.y = screenH/2

		if self.x > screenW:
			bar0.score += 1
			# reset ball
			self.x = screenW/2
			self.y = screenH/2

		## finally, update ball location		           
		self.x += self.x_speed
		self.y += self.y_speed


# class: clientGS
# this is the game space class used on both clients, includes pygame sprites and will actually 
#	display things (as opposed to the server with just representations)
class clientGS:
	# constructor #
	def __init__(self, player):
		pygame.init()
		self.size = self.width, self.height = screenW, screenH
		self.screen = pygame.display.set_mode(self.size)

		self.black = 0, 0, 0
		pygame.key.set_repeat(1, 50)

		self.bar0 = bar((255,0,0), barW, screenH/2 - barH/2, barW, barH)
		self.bar1 = bar((0,0,255), screenW - 2*barW, screenH/2 - barH/2, barW, barH)
		self.ball = ball()
		self.score0 = score(250,10)
		self.score1 = score(380,10)
	
		self.player = player

	# updateSelf() #
	def updateSelf(self, posDict):
		# called on reception of json game data from the server at each tick
		self.bar0.rect.x = posDict['bar0'][0]
		self.bar0.rect.y = posDict['bar0'][1]

		self.bar1.rect.x = posDict['bar1'][0]
		self.bar1.rect.y = posDict['bar1'][1]
    
		self.ball.rect.x = posDict['ball'][0]
		self.ball.rect.y = posDict['ball'][1]

		self.bar0.score = posDict['score'][0]
		self.bar1.score = posDict['score'][1]
		self.score0.score = self.score0.font.render(str(posDict['score'][0]), True,(255,255,255))
		self.score1.score = self.score0.font.render(str(posDict['score'][1]), True,(255,255,255))

	# updateScreen() #
	def updateScreen(self, waiting=False):
		# called after updateSelf() to blit everything to the screen 
		self.screen.fill(self.black)
		
		if waiting == True:
			font = pygame.font.SysFont("calibri", 50)
			xpos = screenW / 2 - 200
			ypos = screenH / 2 - 50
			msg = font.render("WAITING FOR PLAYER " + str((self.player + 1) % 2 + 1), True, (100, 0, 255))
			self.screen.blit(msg, (xpos, ypos))
			
		self.screen.blit(self.bar0.bar,self.bar0.rect)
		self.screen.blit(self.bar1.bar,self.bar1.rect)
		self.screen.blit(self.ball.circle,self.ball.rect)
		self.screen.blit(self.score0.score,(self.score0.xpos, self.score0.ypos))
		self.screen.blit(self.score1.score,(self.score1.xpos, self.score1.ypos))
		
		pygame.display.flip()

	# processEvents() #
	def processEvents(self):
		# called after updateScreen(), sends back events by user the the server as a list
		toSend = []
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				toSend.append(str(self.player) + "," + str(event.key) + ",down")

			elif event.type == KEYUP:
				toSend.append(str(self.player) + "," + str(event.key) + ",up")

			elif event.type == pygame.QUIT:
				toSend = []
				# indicates to server that this user is quitting
				toSend.append("QUIT")
				return toSend			
		return toSend

	def gameOverScreen(self):
		self.screen.fill(self.black)
		go = gameOver()
		self.screen.blit(self.score0.score,(self.score0.xpos, self.score0.ypos))
		self.screen.blit(self.score1.score,(self.score1.xpos, self.score1.ypos))
		self.screen.blit(go.score, (go.xpos, go.ypos))		

		pygame.display.flip()


# class: serverGS
# one instantiated on the server, updated with tick to reflect the next tick in the game, then
#	data from it is sent to each client so they can update their game state   
class serverGS:
	def __init__(self):
		self.size = self.width, self.height = screenW, screenH

		self.bar0 = sBar(barW, self.height/2 - barH/2, barW, barH)
		self.bar1 = sBar(self.width - 2*barW, self.height/2 - barH/2, barW, barH)

		self.ball = sBall()

	# handleEvents() #
	def handleEvents(self, eList):
		# called on reception of events list from clients
		if len(eList) == 1:
			if eList[0] == "QUIT":
				print "SOMEONE QUIT!"
				return
 
		for event in eList:
			eComp = event.split(",")
			pNum = int(eComp[0])
			key = eComp[1]
			if pNum == 0:
				if eComp[2] == "down":
					self.bar0.move(key)
				
				elif eComp[2] == "up":
					self.bar0.move(key)

			elif pNum == 1:
				if eComp[2] == "down":
					self.bar1.move(key)

				elif eComp[2] == "up":
					self.bar1.move(key)

	# tick() #
	def tick(self):
		# at each tick this is called to update the game
		self.bar0.tick()
		self.bar1.tick()
		self.ball.tick(self.bar0, self.bar1)


	# getSendDict() #
	def getSendDict(self):
		# called after tick to get the dictionary that will be sent to the clients as a json
		sendDict = {}
		sendDict['bar0'] = [self.bar0.x, self.bar0.y, self.bar0.width, self.bar0.height]
		sendDict['bar1'] = [self.bar1.x, self.bar1.y, self.bar1.width, self.bar1.height]
		sendDict['ball'] = [self.ball.x, self.ball.y]
		sendDict['score'] = [self.bar0.score, self.bar1.score]
	

		return sendDict
	


