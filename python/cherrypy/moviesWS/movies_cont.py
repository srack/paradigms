# Sam Rack
# CSE 30332 CherryPy Web Service
# movies_cont.py

from _movie_database import _movie_database
from api_check import ApiKeyCheck

import cherrypy
import json
import re

class MoviesController:
	def __init__(self, mDB, akc): 
		self.mdb = mDB
		self.keyCheck = akc
		return

	## GET_all ##
	def GET_all(self):
		resp = {'result': 'success'}		

		moviesL = []
		for movie in self.mdb.get_movies():
			moviesL.append(self.GET_mId(movie, useJson = 0))
		resp['movies'] = moviesL

		return json.dumps(resp, encoding = "latin-1")

	## POST ##
	def POST(self):
		resp = {'result': 'success'}		
		
		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				resp['id'] = self.mdb.add_movie((pData['title'], pData['genres']))
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")

	## DELETE_all ##
	def DELETE_all(self):
		resp = {'result': 'success'}		

		try:
			# for the API key
			data = cherrypy.request.body.fp.read()
			pData = json.loads(data)
			
			if self.keyCheck.check(pData['apikey']):
				self.mdb.delete_movies()
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")



	## GET_mId ##
	def GET_mId(self, mId, useJson = 1):
		# initialize response
		resp = {'result': 'success'}		

		# ensure mId is an int
		mId = int(mId)

		try:
			# get the title and genres
			l = self.mdb.get_movie(mId)
			if l == None:
				resp['result'] = 'error'
				resp['message'] = 'Key not found.'
			else:
				# fill in 'id' field
				resp['id'] = mId
				(resp['title'], resp['genres']) = l
				# get the image file name
				resp['img'] = self.mdb.get_poster_by_mid(mId)
				print resp['image'] + "\n" + "\n"
		except KeyError:
			resp['result'] = 'error'
			resp['message'] = 'Key not found.'	
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		if useJson == 1:
			return json.dumps(resp, encoding = "latin-1")
		else:
			return resp

	## PUT_mId ##
	def PUT_mId(self, mId):
		resp = {'result': 'success'}
		mId = int(mId)

		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)
		
			
			if self.keyCheck.check(pData['apikey']):
				if self.mdb.get_movie(mId) == None:
					self.mdb.add_movie((pData['title'], pData['genres']), mId)
				else:
					l = (pData['title'], pData['genres'])
					self.mdb.set_movie(mId, l)
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'
	
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")
			
	## DELETE_mId ##
	def DELETE_mId(self, mId):
		resp = {'result': 'success'}
		mId = int(mId)

		try:
			# for the API key  
			data = cherrypy.request.body.fp.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				# delete the movie
				self.mdb.delete_movie(mId)
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except KeyError:
			resp['result'] = 'error'
			resp['message'] = 'Key not found.'	
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")

			
