# Adrian Gerbaud and Sam Rack
# CSE 30332
# Final Project - Pong
# client.py

import os
import sys
import time

from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory
from twisted.internet import reactor

import json

from pong_new import *

host = "student02.cse.nd.edu"
portNum = 9233

class ClientGameProtocol(Protocol):
	# constructor #
	def __init__(self):
		self.state = "INIT"
		self.pNum = -1
		self.game = None
		
	# dataReceived() #
	def dataReceived(self, data):
		## JUST CONNECTING
		if self.state == "INIT":
			# will receive either "WAIT <pNum>"
			dataC = data.split(" ")
			# this is sent if there are already two clients connected to the server, no more room in the game
			if dataC[0] == "Sorry,":
				print data
				os._exit(0)

			# extract the player number - specified by the order in which connection happens
			self.pNum = int(dataC[1])	
			
			# create the game, given player number
			self.game = clientGS(self.pNum)
			# show the inital game state
			self.game.updateScreen(waiting=True)

			if dataC[0] == "WAIT":
				self.state = "WAITING"
				self.transport.write("OK")
			else:
				# this shouldn't happen
				print "ERROR: unexpected data received, state"

		## WAITING FOR THE OTHER USER TO CONNECT
			# this is event driven -- don't know when the other client will connect and be ready
			# 	to play
		elif self.state == "WAITING":
			#print data
			# will receive "READY <pNum>"
			if data.split(" ")[0] == "READY":
				self.state ="PLAYING"

		## GAME STATE UPDATE -- this will happen every clock tick (as determined by the server)
			# the server uses a LoopingCall to send the updated game state every 1/40th of a second
			# this is received by each client and used to update the game object and then the screen
			# technically event driven, but the event is controlled by a clock
		elif self.state == "PLAYING":
			# update the necessary game pieces, given the json data receieved from the server
			self.game.updateSelf(json.loads(data))

			# update the screen for the user
			self.game.updateScreen()

			# send event updates back to server 
				# though the event check happens AFTER the update (opposite the typical steps for the game,
				#	this will not cause any noticable issues because the game is updated every 1/40th of a 
				# 	second -- the user will not see it any differently and this made implementation much easier
			events = self.game.processEvents()
			self.transport.write(json.dumps(events))
			# if one of the events detected is QUIT, then exit the game, connectionLost on the other client and server
			# 	will handle this client exiting 
			if len(events) > 0 and events[0] == "QUIT":
				self.game.gameOverScreen()
				time.sleep(1)
				os._exit(0)

	# connectionLost() #
	def connectionLost(self, msg):
		# display the game over screen for 5 seconds, then exit
		self.game.gameOverScreen()
		time.sleep(3)
		os._exit(0)

# ClientGameFactory
class ClientGameFactory(ClientFactory):
	# buildProtocol() #
	def buildProtocol(self, addr):
		return ClientGameProtocol()



# main
if __name__ == "__main__":
	reactor.connectTCP(host, portNum, ClientGameFactory()) 

	# start game loop
	reactor.run()
