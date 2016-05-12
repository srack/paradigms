# Sam Rack
# CSE 30332 CherryPy Web Service
# reset_cont.py

from _movie_database import _movie_database

import cherrypy
import json
import re

class ResetController:
	def __init__(self, mDB):
		self.mdb = mDB
		return

	def PUT_all(self):
		resp = {'result': 'success'}

		try:
			# reload database from .dat files
			self.mdb.load_movies("ml-1m/movies.dat")
			self.mdb.load_users("ml-1m/users.dat")
			self.mdb.load_ratings("ml-1m/ratings.dat")
			self.mdb.load_posters("images.dat")

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")

	def PUT_mId(self, mId):
		resp = {'result': 'success'}

		try:
			self.mdb.load_movie("ml-1m/movies.dat", mId)

		except KeyError:
			resp['result'] = 'error'
			resp['message'] = 'Key not found.'
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")
