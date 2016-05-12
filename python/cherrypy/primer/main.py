## Sam Rack
## CSE30332 CherryPy Primer
## main.py
## 03/20/15

import cherrypy
from dcont import DictionaryController

## startService ##
def startService():
	# dispatcher that will direct events to the corresponding handlers
	disp = cherrypy.dispatch.RoutesDispatcher()

	# initialize controller and tell the dispatcher about event handlers
	dictCont = DictionaryController()
	disp.connect('dictGetAll', '/dictionary/', controller = dictCont, action = 'GET_all', 
		conditions = dict(method = ['GET']))
	disp.connect('dictPost', '/dictionary/', controller = dictCont, action = 'POST',
		conditions = dict(method = ['POST']))
	disp.connect('dictDelAll', '/dictionary/', controller = dictCont, action = 'DELETE_all',
		conditions = dict(method = ['DELETE']))
	disp.connect('dictGetKey', '/dictionary/:key', controller = dictCont, action = 'GET_key', 
		conditions = dict(method = ['GET']))
	disp.connect('dictPut', '/dictionary/:key', controller = dictCont, action = 'PUT', 
		conditions = dict(method = ['PUT']))
	disp.connect('dictDelKey', '/dictionary/:key', controller = dictCont, action = 'DELETE_key',
		conditions = dict(method = ['DELETE']))


	# defines the configuration for the host and port number of the service
	conf = {'global' : {'server.socket_host':'student00.cse.nd.edu', 'server.socket_port': 40063},
		'/' : {'request.dispatch': disp} }
	cherrypy.config.update(conf)
	
	# sets up the event queue for the web service
	app = cherrypy.tree.mount(None, config = conf)
	# starts the event loop
	cherrypy.quickstart(app)



if __name__ == '__main__':
	startService()
