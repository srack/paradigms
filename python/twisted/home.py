# Sam Rack
# CSE 30332
# Twisted Primer
# home.py

from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

from twisted.internet.defer import DeferredQueue
from twisted.internet.defer import Deferred

cmdPort = 32001
clientPort = 9001
dataPort = 9002


class DataConn(Protocol):
	def __init__(self, clientProt):
		self.state = "WAIT_DATA"
		clientProt.dataProt = self
		self.clientProt = clientProt

	def connectionMade(self):
		# empty the deferred queue of data from the client
		while not self.clientProt.dqSize == 0:
			d = self.clientProt.dQueue.get()
			self.clientProt.dqSize -= 1
			d.addCallback(self.writeData)

		self.state = "CONNECTED_DATA"

	def dataReceived(self, data):
		if self.clientProt.state == "CONNECTED_CLIENT":
			self.clientProt.writeData(data)
		# else case should not happen

	def writeData(self, data):
		if self.state == "CONNECTED_DATA":
			self.transport.write(data)
		# again, else case should not happen

class DataConnFactory(Factory):
	def __init__(self, clientProt):
		self.prot = None
		self.clientProt = clientProt

	def buildProtocol(self, addr):
		# only create one
		if self.prot == None:
			self.prot = DataConn(self.clientProt)
			return self.prot


class CmdConn(Protocol):
	def __init__(self):
		self.state = "WAIT_CMD"

	def connectionMade(self):
		self.state = "CONNECTED_CMD"

	def startDataConn(self, clientProt):
		if self.state == "CONNECTED_CMD":
			reactor.listenTCP(dataPort, DataConnFactory(clientProt))
			# will indicate that work should begin the data connection
			self.transport.write("start data connection")
		else:
			# should not happen
			print "Error"


class CmdConnFactory(Factory):
	def __init__(self):
		self.prot = None

	def buildProtocol(self, addr):
		# only allow one command connection
		if self.prot == None:
			self.prot = CmdConn()
			return self.prot


class ClientConn(Protocol):
	def __init__(self, cmdProt):
		self.state = "WAIT_CLIENT"
		self.cmdProt = cmdProt	
		self.dataProt = None

		self.dQueue = DeferredQueue()
		self.dqSize = 0

	def connectionMade(self):
		self.state = "CONNECTED_CLIENT"
		if not self.cmdProt == None:
			# start the data connection that will bridge it
			self.cmdProt.startDataConn(self)	

	def dataReceived(self, data):
		# if the data connection is not yet ready, buffer
		if self.dataProt == None or not self.dataProt.state == "CONNECTED_DATA":
			# buffer the data, and add to the count of items in the queue
			self.dQueue.put(data)
			self.dqSize += 1
			return
		else:
			self.dataProt.writeData(data)

	def writeData(self, data):
		self.transport.write(data)

class ClientConnFactory(Factory):
	def __init__(self, cmdFact):
		self.prot = None
		self.cmdFact = cmdFact
	
	def buildProtocol(self, addr):
		# only allow one client connection
		if self.prot == None:
			# initialize client conn with a reference to the protol so they can know the status of each other
			self.prot = ClientConn(cmdFact.prot)
			return self.prot

if __name__ == "__main__":
	# command connection factory
	cmdFact = CmdConnFactory()
	# client connection factory, gets a ref to cmdFactory so the connections can work with each other
	clientFact = ClientConnFactory(cmdFact)

	# put events on queue to wait for command and client connections
	reactor.listenTCP(cmdPort, cmdFact)
	reactor.listenTCP(clientPort, clientFact)

	# start the event loop
	reactor.run()
