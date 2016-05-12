## Sam Rack
## PyQt Assignment
## moviesGui.pyw
## 16 March 2015

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os
import sys
import requests
import json

###############
## MoviesGui ##
###############
class MoviesGui(QMainWindow):
	# constructor #
	def __init__(self):
		super(MoviesGui, self).__init__()

		# intialize values for accessing the web service
		self.API_KEY = 'cOBfTz6ZZG'
		self.SITE_URL = 'http://student00.cse.nd.edu:40001'

		# initially set userId to 1 as a default
		self.userId = 5

		# set the central widget of the window
		self.central = MoviesCentral(self)
		self.setFixedHeight(600)
		self.setFixedWidth(600)
		self.setCentralWidget(self.central)
		
		## set up actions to be placed in the menu items ##
		a_fExit = QAction("Exit", self)			# file -> exit action
		self.connect(a_fExit, SIGNAL("triggered()"), QCoreApplication.instance().quit)
		
		a_uViewProfile = QAction("View Profile", self)		# user -> view profile action
		self.connect(a_uViewProfile, SIGNAL("triggered()"), self.viewProfile)

		a_uSetUser = QAction("Set User", self)		# user -> set user action
		self.connect(a_uSetUser, SIGNAL("triggered()"), self.setUser)
	
		## set up the menu items and add the actions ##
		self.fileMenu = self.menuBar().addMenu("File")		# file menu setup
		self.fileMenu.addAction(a_fExit)
	
		self.userMenu = self.menuBar().addMenu("User")		# user menu setup
		self.userMenu.addAction(a_uViewProfile)
		self.userMenu.addAction(a_uSetUser)


	# viewProfile #
	def viewProfile(self):
		form = QMessageBox()

		# get user information
		r = requests.get(self.SITE_URL + '/users/' + str(self.userId))
		userData = json.loads(r.content)

		# set up the label to display the information		
		text = "Profile\nGender: " + userData['gender'] + "\nZipcode: " + str(userData['zipcode']) + "\nAge: " + str(userData['age'])
		form.setText(text)

		# start the event loop -- NOTE: this pauses the main application's event window
		form.exec_()


	# setUser #
	def setUser(self):
		# create a dialog box into which the user can enter a new user id
		form = QInputDialog()
		form.setLabelText("User ID:")

		# connect handler to the Okay button clicked with a new value entered
		form.textValueSelected.connect(self.userSet)
		# start the event loop
		form.exec_()
	

	# userSet #
	def userSet(self, value):
		try:
			intVal = int(value)
			# check that the value is in the range of valid user ids
			if intVal < 1 or intVal > 6040:
				self.userSetErr()
			else:
				self.userId = intVal
				self.central.newRec()
		except:
			self.userSetErr()


	# userSetErr #
	def userSetErr(self):
		# create a dialog box that tells the user that the userId he/she entered is invalid		
		form = QMessageBox()
		form.setText("Invalid UserId. \nEnter a value in the range 1-6040.")
		form.exec_()
		self.setUser()


###################
## MoviesCentral ##
###################
class MoviesCentral(QWidget):
	# constructor #
	def __init__(self, parent):
		super(MoviesCentral, self).__init__(parent)
		self.parent = parent

		# grid layout will contain all other widgets
		layout = QGridLayout()

		## add buttons ## 
		self.upButton = QPushButton("UP") 
		self.connect(self.upButton, SIGNAL("clicked()"), self.upVote)

		self.downButton = QPushButton("DOWN")
		self.connect(self.downButton, SIGNAL("clicked()"), self.downVote)		

		# add them to the layout
		layout.addWidget(self.upButton, 2, 1)
		layout.addWidget(self.downButton, 2, 3)


		## initialize movie information and get first reccomendation ##
		self.mId = 0
		self.mTitle = "TITLE"
		self.mGenre = "GENRE"
		self.mRating = 0.00
		self.mImage = "img.jpg"

		self.l_mTitle = QLabel(self.mTitle)
		self.l_mTitle.setAlignment(Qt.AlignCenter)
		self.l_mGenRat = QLabel(self.mGenre + "\n\n" + str(self.mRating))
		self.l_mGenRat.setAlignment(Qt.AlignCenter)
		# TO DO - IMAGE
		pm = QPixmap(self.mImage)

		self.l_mImage = QLabel()
		self.l_mImage.setAlignment(Qt.AlignCenter)
		self.l_mImage.setPixmap(pm)	

		self.newRec()

		# add the widgets to grid
		layout.addWidget(self.l_mTitle, 1, 2)
		layout.addWidget(self.l_mGenRat, 3, 2)
		layout.addWidget(self.l_mImage, 2, 2) 
		
		# set the layout for the widget object
		self.setLayout(layout)


	# upVote #
	def upVote(self):
		# put the rating of 5 into a dictionary to be converted by json
		ratDict = {}
		ratDict["movie_id"] = str(self.mId)
		ratDict["rating"] = "5"
		ratDict["apikey"] = self.parent.API_KEY		

		# send the rating to the user to update the database
		r = requests.put(self.parent.SITE_URL + '/recommendations/' + str(self.parent.userId), data = json.dumps(ratDict))

		# get a new recommendation for the user
		self.newRec()


	# downVote #
	def downVote(self):
 		# put the rating of 1 into a dictionary to be converted by json
		ratDict = {}
		ratDict["movie_id"] = str(self.mId)
		ratDict["rating"] = "1"
		ratDict["apikey"] = self.parent.API_KEY		

		# send the rating to the user to update the database
		r = requests.put(self.parent.SITE_URL + '/recommendations/' + str(self.parent.userId), data = json.dumps(ratDict))

		self.newRec()


	# newRec #
	def newRec(self):
		# get the movie id from the recommendations resource
		r = requests.get(self.parent.SITE_URL + '/recommendations/' + str(self.parent.userId))
		resp = json.loads(r.content)
		self.mId = resp['movie_id']
	
		# get the movie information corresponding to the movie id obtained
		r2 = requests.get(self.parent.SITE_URL + '/movies/' + str(self.mId))
		movieInfo = json.loads(r2.content)
		self.mTitle = movieInfo['title']
		self.l_mTitle.setText(self.mTitle)
		self.mGenre = movieInfo['genres']
		imgDir = "/afs/nd.edu/user37/cmc/Public/cse332_sp15/cherrypy/data/images/"
		self.mImage = imgDir + movieInfo['img']
		pm = QPixmap(self.mImage)
		self.l_mImage.setPixmap(pm)

		# get the rating
		r3 = requests.get(self.parent.SITE_URL + '/ratings/' + str(self.mId))
		rating = json.loads(r3.content)
		self.mRating = rating['rating']  
		self.l_mGenRat.setText(self.mGenre + "\n\n" + str(self.mRating))


##########
## MAIN ##
##########
if __name__ == "__main__":
	# create event queue for the gui
	app = QApplication(sys.argv)
	# instantiate the GUI object
	gui = MoviesGui()
	# add show event to the event queue
	gui.show()
	# start the event loop
	app.exec_()	
