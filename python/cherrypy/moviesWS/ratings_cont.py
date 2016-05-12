# Sam Rack
# CSE 30332 CherryPy Web Service
# ratings_cont.py

from _movie_database import _movie_database

import cherrypy
import json
import re

class RatingsController: 
	def __init__(self, mDB):
		self.mdb = mDB
		return

	def GET_mId(self, mId):
		resp = {'result': 'success'}
		mId = int(mId)
		
		try:
			resp['movie_id'] = mId
			resp['rating'] = self.mdb.get_rating(mId)

		except KeyError:
			resp['result'] = 'error'
			resp['message'] = 'Key not found.'
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)
		
		return json.dumps(resp, encoding = "latin-1")
