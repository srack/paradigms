# Sam Rack
# CSE30332
# Ajax Pyjamas Interface
# 4/7/2015

import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Image import Image
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas.JSONService import loads
from pyjamas.JSONService import dumps
import pygwt


#######################
# MAIN SITE INTERFACE #
#######################

class movieInterface(Grid):
	def __init__(self):
		super(movieInterface, self).__init__(rows = 4, columns = 3)

		# identifiers from movie db or needed to access it
		self.uId = 3
		self.mId = 1 
		self.API_KEY = 'cOBfTz6ZZG'
		self.SERVER_SITE = 'http://student00.cse.nd.edu:40001'

		self.mTitle = "<title>"
		self.mRating = "<rating>"
		self.mPoster = ""
		self.eMessage = ""
		self.imgIndex = "http://www.cse.nd.edu/~cmc/teaching/cse30332_sp15/images/"

		# create all interface objects
		self.mTitleL = Label()
		self.mRatingL = Label()
		self.upVoteB = Button("UP", self.upPressed)
		self.mPosterI = Image()
		self.downVoteB = Button("DOWN", self.downPressed)
		# error message displayed in case of an error received from server
		self.eMessageL = Label()
		
		# add each of the objects to the grid in the appropriate location
		self.setWidget(0, 1, self.mTitleL)
		self.setWidget(1, 0, self.upVoteB)
		self.setWidget(1, 1, self.mPosterI)
		self.setWidget(1, 2, self.downVoteB)
		self.setWidget(2, 1, self.mRatingL)
		self.setWidget(3, 1, self.eMessageL)

		self.getNewMovieRec()

	# will call this from (1) the constructor to get the first recommendation, and 
	#	(2) on return of success for PUT recommendation after up/down pressed
	def getNewMovieRec(self):
		# reset the error message member
		self.eMessage = ""
		# make request for the new recommendation
		HTTPRequest().asyncGet(self.SERVER_SITE + "/recommendations/"+ str(self.uId), recControllerGET(self))

	# will call this after requests are received back from recommendations, movies, 
	#	and ratings (called from ratings controller) 
	def update(self):
		self.mTitleL.setText(self.mTitle)
		self.mRatingL.setText(self.mRating)
		self.mPosterI.setUrl(self.imgIndex + self.mPoster)
		self.eMessageL.setText(self.eMessage)

	# button pressed handler for UP button
	def upPressed(self):
		# set up dictionary to send
		data = {}
		data['apikey'] = self.API_KEY
		data['movie_id'] = self.mId
		data['rating'] = '5'
		text = dumps(data)
		# make the request
		HTTPRequest().asyncPut(self.SERVER_SITE + "/recommendations/" + str(self.uId), text, recControllerPUT(self))
	
	# button pressed handler for DOWN button
	def downPressed(self):
		# set up dictionary to send
		data = {}
		data['apikey'] = self.API_KEY
		data['movie_id'] = self.mId
		data['rating'] = '5'
		text = dumps(data)
		# make the request
		HTTPRequest().asyncPut(self.SERVER_SITE + "/recommendations/" + str(self.uId), text, recControllerPUT(self))


###############
# CONTROLLERS #
###############

class recControllerGET:
	def __init__(self, interface):
		self.main = interface
	
	def onCompletion(self, text):
		data = loads(text)
		# update movie id in main interface class
		self.main.mId = int(data['movie_id'])	
	
		# make request for the movie data
		HTTPRequest().asyncGet(self.main.SERVER_SITE + "/movies/" + str(self.main.mId), moviesControllerGET(self.main))

	def onError(self, text, code):
		self.main.eMessage = "Error received from server. Unable to update movie."
		self.main.update() 

class recControllerPUT:
	def __init__(self, interface):
		self.main = interface

	def onCompletion(self, text):
		data = loads(text)

		self.main.getNewMovieRec()

	def onError(self, text, code):
		self.main.eMessage = "Error received from server. Unable to update movie."
		self.main.update() 

class moviesControllerGET:
	def __init__(self, interface):
		self.main = interface
	
	def onCompletion(self, text):
		data = loads(text)
		self.main.mTitle = data['title']
		self.main.mPoster = data['img']

		# make requst for the rating data of the movie
		HTTPRequest().asyncGet(self.main.SERVER_SITE + "/ratings/" + str(self.main.mId), ratingsControllerGET(self.main))
		
	def onError(self, text, code):
		self.main.eMessage = "Error received from server. Unable to update movie."
		self.main.update()

class ratingsControllerGET:
	def __init__(self, interface):
		self.main = interface

	def onCompletion(self, text):
		data = loads(text)
		self.main.mRating = data['rating']

		# update main grid interface based on new movie information
		self.main.update()

	def onError(self, text, code):
		self.main.eMessage = "Error received from server. Unable to update movie."
		self.main.update()


########
# MAIN #
########

if __name__ == '__main__':
	# give the base HTML file that the javascript will work on
	pyjd.setup("public/movies.html")

	site = movieInterface()
	RootPanel().add(site)
	
	pyjd.run()
