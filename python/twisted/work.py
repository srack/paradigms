# Sam Rack
# CSE 30332
# Twisted Primer
# work.py

from twisted.internet.protocol import Factory
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

from twisted.internet.defer import DeferredQueue
from twisted.internet.defer import Deferred

cmdPort = 32001
servicePort = 22
dataPort = 9002

host = "student02.cse.nd.edu"

class ServiceConn(Protocol):
	def __init__(self, dataProt):
		self.dataProt = dataProt
		self.dataProt.serviceProt = self
		self.state = "WAIT_SERVICE"

	def connectionMade(self):
		# empty what has been queued on the data connection	
		while not self.dataProt.dqSize == 0:
			d = self.dataProt.dQueue.get()
			d.addCallback(self.sendData)
			self.dataProt.dqSize -= 1

		self.state = "CONNECTED_SERVICE"
		return

	def dataReceived(self, data):
		self.dataProt.sendData(data)

	def sendData(self, data):
		self.transport.write(data)

class ServiceConnFactory(ClientFactory):
	def __init__(self, dataProt):
		self.prot = None
		self.dataProt = dataProt

	def buildProtocol(self, addr):
		# only allow one protocol to be built
		if self.prot == None:
			self.prot = ServiceConn(self.dataProt)
			return self.prot

class DataConn(Protocol):
	def __init__(self):
		self.serviceProt = None
		self.state = "WAIT_DATA"
		self.dQueue = DeferredQueue()
		self.dqSize = 0	

	def connectionMade(self):
		self.state = "CONNECTED_DATA"
		
		# create the service connection -- only need queue in one direction
		reactor.connectTCP(host, servicePort, ServiceConnFactory(self))
		return

	def dataReceived(self, data):
		# queue the data if the service connection isn't yet ready
		if self.serviceProt == None or not self.serviceProt.state == "CONNECTED_SERVICE":
			self.dQueue.put(data)
			self.dqSize += 1
		else:
			self.serviceProt.sendData(data)
	
	def sendData(self, data):
		self.transport.write(data)

class DataConnFactory(ClientFactory):
	def __init__(self):
		self.prot = None

	def buildProtocol(self, addr):
		if self.prot == None:
			self.prot = DataConn()
			return self.prot

class CmdConn(Protocol):
	def dataReceived(self, data):
		if data == "start data connection":
			dataFact = DataConnFactory()
			reactor.connectTCP(host, dataPort, dataFact)

class CmdConnFactory(ClientFactory):
	def __init__(self):
		self.prot = None

	def buildProtocol(self, addr):
		if self.prot == None:
			self.prot = CmdConn()
			return self.prot

if __name__ == "__main__":
	reactor.connectTCP("student02.cse.nd.edu", cmdPort, CmdConnFactory())
	reactor.run()
