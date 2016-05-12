# Sam Rack
# CSE 30332 CherryPy Web Service
# users_cont.py

from _movie_database import _movie_database
from api_check import ApiKeyCheck

import cherrypy
import json
import re

class UsersController:
	def __init__(self, mDB, akc):
		self.mdb = mDB
		self.keyCheck = akc
		return


	def GET_all(self):
		resp = {'result': 'success'}

		usersL = []
		for user in self.mdb.get_users():
			usersL.append(self.GET_uId(user, useJson = 0))
		resp['users'] = usersL

		return json.dumps(resp, encoding = "latin-1")


	def POST(self):
		resp = {'result': 'success'}

		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				resp['id'] = self.mdb.add_user((pData['gender'], pData['age'], pData['occupation'], pData['zipcode']))
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")


	def DELETE_all(self):
		resp = {'result': 'success'}

		try:
			# for the API key 
			data = cherrypy.request.body.fp.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				self.mdb.delete_users()
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)
		return json.dumps(resp, encoding = "latin-1")


	def GET_uId(self, uId, useJson = 1):
		resp = {'result': 'success'}

		uId = int(uId)

		try:
			# get the user data
			l = self.mdb.get_user(uId)
			if l == None:
				resp['result'] = 'error'
				resp['message'] = 'Key not found.'
			else:
				resp['id'] = uId
				(resp['gender'], resp['age'], resp['occupation'], resp['zipcode']) = l

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

		return json.dumps(resp, encoding = "latin-1")


	def PUT_uId(self, uId):
		resp = {'result': 'success'}
		uId = int(uId)

		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				if self.mdb.get_user(uId) == None:
					self.mdb.add_user((pData['gender'], pData['age'], pData['occupation'], pData['zipcode']), uId)
				else:
					l = (pData['gender'], pData['age'], pData['occupation'], pData['zipcode'])
					self.mdb.set_user(uId, l)
			else:
				resp['result'] = 'error'
				resp['message'] = 'Invalid API Key'	

		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp, encoding = "latin-1")


	def DELETE_uId(self, uId):
		resp = {'result': 'success'}
		uId = int(uId)

		try:
			# for the API key -- TO DO
			data = cherrypy.request.body.fp.read()
			pData = json.loads(data)

			if self.keyCheck.check(pData['apikey']):
				# delete the user
				self.mdb.delete_user(uId)
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


