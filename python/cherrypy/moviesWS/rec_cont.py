# Sam Rack
# CSE 30332 CherryPy Web Service
# rec_cont.py

from _movie_database import _movie_database
from api_check import ApiKeyCheck

import cherrypy
import json
import re

class RecommendationsController:
	def __init__(self, mDB, akc):
		self.mdb = mDB
		self.keyCheck = akc
		return

	def DELETE_all(self):
		resp = {'result': 'success'}
	
		try:
			# API key check
			data = cherrypy.request.body.fp.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				self.mdb.delete_all_ratings()
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1") 

	def GET_uId(self, uId):
		resp = {'result': 'success'}
		uId = int(uId)
		
		if self.mdb.get_user(uId) == None:
			resp['result'] = 'error'
			resp['message'] = 'Key not found.'
		else:
			resp['movie_id'] = self.mdb.get_highest_rated_unvoted_movie(uId)

		return json.dumps(resp, encoding = "latin-1")

	def PUT_uId(self, uId):
		resp = {'result': 'success'}
		uId = int(uId)

		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)
			if self.keyCheck.check(pData['apikey']):
				if self.mdb.get_user(uId) == None:
					resp['result'] = 'error'
					resp['message'] = 'Key not found.'
				else:
					self.mdb.set_user_movie_rating(uId, pData['movie_id'], pData['rating'])
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)
		
		return json.dumps(resp, encoding = "latin-1")
