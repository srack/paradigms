# Sam Rack
# CSE 30332 CherryPy Web Service
# main.py
# 3/29/15

import cherrypy
from _movie_database import _movie_database
from movies_cont import MoviesController
from reset_cont import ResetController
from users_cont import UsersController
from ratings_cont import RatingsController
from rec_cont import RecommendationsController
from api_check import ApiKeyCheck


def startService():
	mdb = _movie_database()
	akc = ApiKeyCheck('cOBfTz6ZZG')	

	disp = cherrypy.dispatch.RoutesDispatcher()

	moviesCont = MoviesController(mdb, akc)
	resetCont = ResetController(mdb)
	usersCont = UsersController(mdb, akc)
	ratingsCont = RatingsController(mdb)
	recCont = RecommendationsController(mdb, akc)

	# /movies/ resource request handlers
	disp.connect('moviesGetAll', '/movies/', controller = moviesCont, action = 'GET_all', 
		conditions = dict(method = ['GET']))
	disp.connect('moviesPost', '/movies/', controller = moviesCont, action = 'POST',
		conditions = dict(method = ['POST']))
	disp.connect('moviesDeleteAll', '/movies/', controller = moviesCont, action = 'DELETE_all',
		conditions = dict(method = ['DELETE']))

	# /movies/:movie_id resource request handlers
	disp.connect('moviesGetMid', '/movies/:mId', controller = moviesCont, action = 'GET_mId', 
		conditions = dict(method = ['GET']))
	disp.connect('moviesPutMid', '/movies/:mId', controller = moviesCont, action = 'PUT_mId',
		conditions = dict(method = ['PUT']))
	disp.connect('moviesDeleteMid', '/movies/:mId', controller = moviesCont, action = 'DELETE_mId', 
		conditions = dict(method = ['DELETE']))

	# /users/ resource request handlers
	disp.connect('usersGetAll', '/users/', controller = usersCont, action = 'GET_all', 
		conditions = dict(method = ['GET']))
	disp.connect('usersPost', '/users/', controller = usersCont, action = 'POST',
		conditions = dict(method = ['POST']))
	disp.connect('usersDeleteAll', '/users/', controller = usersCont, action = 'DELETE_all',
		conditions = dict(method = ['DELETE']))

	# /users/:user_id resource request handlers
	disp.connect('usersGetUid', '/users/:uId', controller = usersCont, action = 'GET_uId',
		conditions = dict(method = ['GET']))
	disp.connect('usersPutUid', '/users/:uId', controller = usersCont, action = 'PUT_uId',
		conditions = dict(method = ['PUT']))
	disp.connect('usersDeleteUid', '/users/:uId', controller = usersCont, action = 'DELETE_uId',
		conditions = dict(method = ['DELETE']))
		
	# /ratings/:movie_id resource request handler
	disp.connect('ratingsGetMid', '/ratings/:mId', controller = ratingsCont, action = 'GET_mId', 
		conditions = dict(method = ['GET']))

	# /recommendations/ resource request handler
	disp.connect('recDeleteAll', '/recommendations/', controller = recCont, action = 'DELETE_all',
		conditions = dict(method = ['DELETE']))

	# /recommendations/:user_id resource request handler
	disp.connect('recGetUid', '/recommendations/:uId', controller = recCont, action = 'GET_uId', 
		conditions = dict(method = ['GET']))
	disp.connect('recPutUid', '/recommendations/:uId', controller = recCont, action = 'PUT_uId',
		conditions = dict(method = ['PUT']))

	# /reset/ resource request handlers
	disp.connect('resetPutAll', '/reset/', controller = resetCont, action = 'PUT_all', 
		conditions = dict(method = ['PUT']));

	# define the configuration of the server
	conf = {'global' : {'server.socket_host':'student01.cse.nd.edu', 'server.socket_port':40063}, '/' : {'request.dispatch':disp} }
	cherrypy.config.update(conf)


	mdb.load_movies("ml-1m/movies.dat")
	mdb.load_users("ml-1m/users.dat")
	mdb.load_ratings("ml-1m/ratings.dat")
	mdb.load_posters("images.dat")
	print "Done initializing movies db"	


	# set up the event queue
	app = cherrypy.tree.mount(None, config = conf)
	# start the event loop
	cherrypy.quickstart(app)

if __name__ == '__main__':
	startService()
