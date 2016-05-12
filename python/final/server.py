# Adrian Gerbaud and Sam Rack
# CSE 30332
# Final Project - Pong
# server.py

from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

import json
import time

from pong_new import *


portNum = 9233

# tickClients() #
# looping call will be done on this
	# this is the main place where we integrate event based with clock tick!
def tickClients(clientList):
	if len(clientList) == 0:
		return

	# first tick the game -- NOTE: .game is the same reference for both clients 
	clientList[0].game.tick()

	# getSendDict extracts game data needed to be sent and puts it in an understandable dictionary
	#	then we use json to convert into a string that can be sent across the network
	toSend = json.dumps(clientList[0].game.getSendDict())

	# then send out the update to both clients -- simply write it over the connection
	for client in clientList:
		client.transport.write(toSend)


# class: GameFullProtocol
# simple protocol that is created only to tell the client that the game is full
# deletes itself after performing this task
class GameFullProtocol(Protocol):
	# connectionMade() #
	def connectionMade(self):
		self.transport.write("Sorry, game is full.")
		del self


# class: GameProtocol
# two of these created to handle the two client connections for player 1 and 2 (actually 0 and 1)
# both protocols maintain the same reference to game, and are able to access the protocol for the
#	other client via players
class GameProtocol(Protocol):
	# construtor #
	def __init__(self, players, index, game, lc):
		self.players = players
		self.game = game
		self.pNum = index
		self.state = "WAITING"	# client is not quite ready
		self.lc = lc

	# connectionMade() #
	def connectionMade(self):
		# both clients are told to wait and are given their player number
		# clients will send back "ok" on receiving this, so the protocol will know they are ready	
		self.transport.write("WAIT " + str(self.pNum))	

	# dataReceived() #
	def dataReceived(self, data):
		## CONFIRMATION RECEIVED FROM CLIENT
		if self.state == "WAITING":
			# means we received "ok" from our client -- event driven, we won't know when the client will be ready
			self.state = "CONFIRMED"

			# if the other client has also said "ok", then we are ready to play
			if len(self.players) == 2 and self.players[(self.pNum + 1) % 2].state == "CONFIRMED":
				# send to all players in the game, to get ready
				for connection in self.players:
					# both protocols will be in the PLAYING state, which means the game has started
					connection.state = "PLAYING"
					# READY sent to the clients indicates that the game is beginning
					connection.transport.write("READY " + str(self.pNum))
				time.sleep(1)
				# event driven way to call tick 40 times/second, this looping call is set up in the factory
				# see tickClients() function for more information				
				self.lc.start(.025)
		
		## GAME EVENTS RECEIVED FROM CLIENT		
		elif self.state == "PLAYING":
			# this will happen 40 times/second because it is a response from the client after the client's game state
			# 	has been updated -- see the client file dataReceived function for more information
			self.game.handleEvents(json.loads(data))

		#else: #not necessary -- was just for debugging
			# should not be getting data, print error
			#print "ERROR: unexpected data received: " + data

	# connectionLost() #
	def connectionLost(self, msg):
		# the client that has not yet disconnected will handle the connectionLost by informing the user of game over
		# this is event driven because, again, we don't know when a user will exit
		os._exit(0)

# class: GameFactory
# factory class for producing game protocols that handle client connections
# also keeps track of these protocols with the list, self.players
# will only allow 2 players to join, then it will call a new protocol, dismissing the request (see GameFullProtocol class)	
class GameFactory(Factory):
	# constructor #
	def __init__(self):
		# keeps track of the two players  participating
		self.players = []
		# serverGS is a class 
		self.pong = serverGS()
		self.lc = LoopingCall(tickClients, self.players)

	# buildProtocol() #
	def buildProtocol(self, addr):
		if len(self.players) < 2:
			# send self.lc so one of the two protocols will be able to start the looping call when both clients are connected
			newPlayer = GameProtocol(self.players, len(self.players), self.pong, self.lc)
			self.players.append(newPlayer)
			return newPlayer
		else:
			return GameFullProtocol()



# main
if __name__ == "__main__":
	# will listen for two players for the game
	reactor.listenTCP(portNum, GameFactory())

	# start the event loop!
	reactor.run()
	
