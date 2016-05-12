from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os
import sys
import requests
import json

################
class MoviesQT(QMainWindow):
	def __init__(self):
		# intitialize QMainWindow parent
		super(MoviesQT, self).__init__()
		
		# self.central holds MoviesCentral object that contains a GridLayout 
		#	with one grid containing a label
		self.central = MoviesCentral(parent = self)
		# calls inherited function (from QMainWindow) to set the central widget - this is
		#	the main object in the middle (ie. for Paint it is a canvass)
		self.setCentralWidget(self.central)

		# create a QAction object that will be added to the user menu
		# an action is something that can be chosen from a particular menu
		userAction = QAction("View Profile", self)
		# puts the handler in the table for the userAction specified in the line
		#	above when it gets the SIGNAL triggered(), self.view_profile is the 
		#	event handler the hidden dispatcher will give the event to
		# for SIGNAL("<funcName>(x)"), x is a parameter passed to the handler 
		self.connect(userAction, SIGNAL("triggered()"), self.view_profile)

		# menu bar is initially empty, but the inherited menuBar().addMenu("<menuName>")
		#	allows to add one or more menus
		self.user_menu = self.menuBar().addMenu("User")
		# this line adds the action defined above to the menu - an action is an option
		#	that will do something when a certain menu is selected
		self.user_menu.addAction(userAction)
		
		
	# handler function for triggered() signal of "View Profile" action
	def view_profile(self):
		msgbox = QMessageBox()
		# QMessageBox function that allows the text to be set
		msgbox.setText("garfield is a cat")
		# if we call msgbox.show here, it will be given to the main event loop, will show 
		#	up and very quickly disappear
		# msgbox.exec_() creates a new event loop for the message box, the other window will
		#	freeze because its event loop won't be used
		msgbox.exec_()
################
		
################
class MoviesCentral(QWidget):
	def __init__(self, parent=None):
		# if we have a parent, then it is the class that created us
		# look in MoviesQT, we see that MoivesCentral is created as the central widget
		# 	of the class; that object created will know MoviesCentral created it
		
		#super initializes the QWidget class from which this class inherits
		super(MoviesCentral, self).__init__(parent)
	
		# QLabel is another widget that can be put on the GUI
		self.titlelbl = QLabel("garfield")


		self.l1 = QLabel("hello")
		self.l2 = QLabel("hi")

		##
		# commonly done in python classes - not used with this application
		# doing this, we can communicate with/access our parent in other routines
		self.parent = parent
		##
		
		# QGridLayout is a widget to which we can add other widgets - for this example
		#	it only includes one grid section
		layout = QGridLayout()
		# add the titlelbl object we created to the QGridLayout widget so it is attached
		layout.addWidget(self.titlelbl, 2, 1)
		layout.addWidget(self.l1, 1, 2)	
		layout.addWidget(self.l2, 3, 3)


		# calls the inherited function setLayout (from QWidget) to attach the QGridLayout
		#	to the QWidget (which is attached to the QMainWindow in MoviesQT)
		self.setLayout(layout)
################
		
#############################
# MAIN CONCEPTS TO REMEMBER #
#############################
# creates the event queue		
app = QApplication(sys.argv)
# instantiates object of MoviesQt (inheriting from QMainWindow - the main portion of the
#	GUI that encapsulates the GUI (menu and status bar are sub-widgets of QMainWindow)
gui = MoviesQT()
# adds to the event queue an event to show the gui object
gui.show()
# starts the event loop (while(1))
app.exec_()

