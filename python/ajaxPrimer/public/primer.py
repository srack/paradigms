# Sam Rack
# CSE30332
# Ajax Primer
# 4/1/2015

import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.TextBox import TextBox
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas.JSONService import loads
import pygwt

class cont:
	def onCompletion(self, text):
		data = loads(text)
		if data.has_key('title'):
			movieLabel.setText(data['title'])	
		else:
			movieLabel.setText("Error: Movie ID not found.")

	def onError(self, text, code):
		data = loads(text)
		movieLabel.setText('Error: HTTP Get Request')

def buttonHandler(self):
	mId = userText.getText()	
	try:
		x = int(mId)
		HTTPRequest().asyncGet("http://student00.cse.nd.edu:40001/movies/" + str(mId), cont(self))
	except:
		movieLabel.setText("Error: Enter an integer for the movie ID.")

if __name__ == '__main__':
	# give the base HTML file that the javascript will work on
	pyjd.setup("public/primer.html")

	instLabel = Label("Enter movie ID:", StyleName = 'teststyle')
	userText = TextBox("", StyleName = 'teststyle')
	clickButton = Button("Click Here", buttonHandler)
	movieLabel = Label()
	
	RootPanel().add(instLabel)
	RootPanel().add(userText)
	RootPanel().add(clickButton)
	RootPanel().add(movieLabel)
	pyjd.run()
