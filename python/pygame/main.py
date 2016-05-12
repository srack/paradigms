# Sam Rack
# CSE 30332
# PyGame Primer

import sys
import os

import pygame
from pygame.locals import *

import math


#########
# Laser #
#########
class Laser(pygame.sprite.Sprite):
	### Laser(player) ###
	def __init__(self, player):
		pygame.sprite.Sprite.__init__(self)

		# save access to player that created it
		self.parent = player

		# rotate to the angle given by the player
		self.rotation = self.parent.rotation - self.parent.fudge

		self.image = pygame.image.load("media/laser.png")
		self.rect = self.image.get_rect()

		# assume radius of the death star ~= half the width of the original image
		rad = self.parent.origImage.get_rect().width / 2 * .8

		# determine the coordinates for the eye based on the rotation angle and parent characteristics
		xEye = self.parent.x + rad * math.cos(self.rotation / 180.0 * math.pi)
		yEye = self.parent.y - rad * math.sin(self.rotation / 180.0 * math.pi)	# subtracting because inverted y for screen
		self.rect = self.rect.move(xEye, yEye)

		# determine the direction in which the lasers should move
		moveAmount = 4
		self.dx = moveAmount * math.cos(self.rotation / 180.0 * math.pi)
		self.dy = -moveAmount * math.sin(self.rotation / 180.0 * math.pi)

		self.shouldRemove = False
		# this is only changed by earth, set to True after it has taken a health point from earth
		self.alreadyHit = False

	### .tick() ###
	def tick(self):
		# after a Laser is instantiated, it will follow the same trajectory at a constant velocity
		self.rect = self.rect.move(self.dx, self.dy)

		if self.rect.x < 0 or self.rect.x >= self.parent.gs.width or self.rect.y < 0 or self.rect.y >= self.parent.gs.height:
			self.shouldRemove = True


##########
# Player #
##########
class Player(pygame.sprite.Sprite):
	### Player(gs) ###
	def __init__(self, gs):
		pygame.sprite.Sprite.__init__(self)
		
		# save access to parent GameSpace
		self.gs = gs
		# information about the image for the player
		self.image = pygame.image.load("media/deathstar.png")
		self.rect = self.image.get_rect()

		self.x = self.rect.width/2
		self.y = self.rect.height/2 
		self.dx = self.dy = 1
		self.rotation = 0
		self.fudge = -45	# additional rotation so the eye is what is facing the mouse
		self.rect.center = (self.x, self.y)	

		# save copy of original image to limit resize errors -- always adjust this image?
		self.origImage = self.image
		
		# should the object be firing lasers now?
		self.toFire = False

		# sound to be played when the laser is being fired
		# this is started and stopped on key events, because those events indicate that
		#   the laser is beginning to or stopping fire and correspond with sound control 
		self.fireSound = pygame.mixer.Sound("media/screammachine.wav")

		# should the object be moving now?
		self.toMoveD = False
		self.toMoveU = False
		self.toMoveL = False
		self.toMoveR = False

		self.laserCounter = 0

	### .tick() ###
	def tick(self):
		# if firing lasers, the won't move update the rotation of the image or let the user move it
		if self.toFire == True:
			if self.laserCounter % 2 == 0:
				# to send a laser, just create a new one
				temp = Laser(self)
				self.gs.lasers.append(temp)
			self.laserCounter += 1
		
		# otherwise, move to face the mouse
		else:
			ex, ey = self.gs.earth.rect.topleft
		
			# update the sprite position, making sure it stays inside of the game window
			#  and not in the earth's area
			if self.toMoveD == True:
				self.y += self.dy
				if self.y > self.gs.height - self.rect.height/2:
					self.y -= self.dy
				if self.y + self.rect.height/2 > ey and self.x + self.rect.width/2 > ex:
					self.y -= 2*self.dy
			if self.toMoveU == True:
				self.y -= self.dy
				if self.y < self.rect.height/2:
					self.y += self.dy
				if self.y + self.rect.height/2 > ey and self.x + self.rect.width/2 > ex:
					self.y += 2*self.dy
			if self.toMoveL == True:
				self.x -= self.dx
				if self.x < self.rect.width/2:
					self.x += self.dx
				if self.y + self.rect.height/2 > ey and self.x + self.rect.width/2 > ex:
					self.x += 2*self.dx
			if self.toMoveR == True:
				self.x += self.dx
				if self.x > self.gs.width - self.rect.width/2: 
					self.x -= self.dx
				if self.y + self.rect.height/2 > ey and self.x + self.rect.width/2 > ex:
					self.x -= 2*self.dx

			# get mouse position
			mx, my = pygame.mouse.get_pos()

			# get the angle between the direction player is facing and the mouse position
			self.rotation = math.atan2(-(my - self.y), mx - self.x) * 180 / math.pi
			self.rotation += self.fudge

			self.image = pygame.transform.rotate(self.origImage, self.rotation)
			
			self.rect = self.image.get_rect()

			# set the location
			self.rect.center = (self.x, self.y)	

	
	### .startKeyPress(key) ###
	def startKeyPress(self, key):
		if (key == K_SPACE):
			self.toFire = True
			self.fireSound.play(loops = -1)
		elif (key == K_DOWN):
			self.toMoveD = True
		elif (key == K_UP):
			self.toMoveU = True
		elif (key == K_LEFT):
			self.toMoveL = True
		elif (key == K_RIGHT):
			self.toMoveR = True

	### .stopKeyPress(key) ###
	def stopKeyPress(self, key):
		if (key == K_SPACE):
			self.toFire = False
			self.fireSound.stop()
		elif (key == K_DOWN):
			self.toMoveD = False
		elif (key == K_UP):
			self.toMoveU = False
		elif (key == K_LEFT):
			self.toMoveL = False
		elif (key == K_RIGHT):
			self.toMoveR = False	

#########
# Enemy #
#########
class Enemy(pygame.sprite.Sprite):
	### Enemy(gs) ###
	def __init__(self, gs):
		pygame.sprite.Sprite.__init__(self)
	
		# for the explosion sound
		self.explSound = pygame.mixer.Sound("media/explode.wav")

		# save access to parent GameSpace
		self.gs = gs
		# information about the image for the object
		self.image = pygame.image.load("media/globe.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width - self.rect.width/16, self.gs.height - self.rect.height/16)	

		self.initHealth = 50
		self.health = self.initHealth
		self.isAlive = True



	def tick(self):
		if self.isAlive == True:
			if self.health == self.initHealth/4:
				self.image = pygame.image.load("media/globe_red100.png")
				self.rect = self.image.get_rect()
				self.rect.center = (self.gs.width - self.rect.width/16, self.gs.height - self.rect.height/16)	
			
			elif self.health <= 0 and self.health/2 >= -9:
				# start explosion sound when the explosion animation begins
				if self.health == 0:	
					self.explSound.play()		
				self.image = pygame.image.load("media/explosion/frames00" + str(-(self.health/2) )+ "a.png")
				self.rect = self.image.get_rect()
				self.rect.center = (self.gs.width - self.rect.width/16, self.gs.height - self.rect.height/16)
				self.health -= 1	
			elif self.health/2 <= -10:
				self.image = pygame.image.load("media/explosion/frames0" + str(-(self.health/2)) + "a.png")
				self.rect = self.image.get_rect()
				self.rect.center = (self.gs.width - self.rect.width/16, self.gs.height - self.rect.height/16)
				if self.health/2 == -16: 
					self.isAlive = False
				self.health -= 1

			for laser in self.gs.lasers:
				# poll for this event because only want collision detected during the tick
				if self.rect.colliderect(laser.rect) and laser.alreadyHit == False and self.health > 0:
					self.health -= 1
					laser.alreadyHit = True



#############
# GameSpace #
#############
class GameSpace:
	### .main() ###
	def main(self):
		# --BASIC INITS-- #
		pygame.init()
		self.size = self.width, self.height = 640, 480
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)

		# --GAME OBJS AND CLOCK SETUP-- #
		self.clock = pygame.time.Clock()
		
		# ds = death star the user will control
		self.ds = Player(self)
		self.earth = Enemy(self)
		self.lasers = []

		# --START GAME LOOP-- # 
		while True:
			# --REGULATE TICK FREQUENCY-- #
			self.clock.tick(30) 	# will tick at most every 1/60th of a second

			# --HANDLE USER INPUT (EVENT LOOP)-- #
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					self.ds.startKeyPress(event.key)
				elif event.type == KEYUP:
					self.ds.stopKeyPress(event.key)

			# --TICK GAME OBJS-- #
			self.ds.tick()
			for laser in self.lasers:
				if laser.shouldRemove == True:
					self.lasers.remove(laser)
				else:
					laser.tick()		
			self.earth.tick()
	

			# --RESET SCREEN AND DISPLAY GAME OBJS-- # 
			# reset to black before adding objects
			self.screen.fill(self.black)
			
			# add the game objects
			for laser in self.lasers:
				self.screen.blit(laser.image, laser.rect)
			if (self.earth.isAlive):
				self.screen.blit(self.earth.image, self.earth.rect)
			self.screen.blit(self.ds.image, self.ds.rect)


			# flip the screen to get the updated screen
			pygame.display.flip() 



# call gs.main() to make all the magic happen
if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
