## Sam Rack
## CSE30332 CherryPy Primer
## dcont.py
## 03/18/15

import cherrypy
import json
import re

class DictionaryController():
	def __init__(self):
		# all dictionary keys will be string
		self.dict = {}

	def GET_key(self, key):
		# initialize the response dictionary
		resp = {'result': 'success'}
		
		# ensure key is a string
		key = str(key)

		try:
			if not self.dict.has_key(key):
				resp['result'] = 'error'
				resp['message'] = 'Key not found.'
			else:	
				resp['value'] = self.dict[key]
				resp['key'] = key

		except Exception as ex:
			resp['result'] = 'failure'			
			resp['message'] = str(ex)

		return json.dumps(resp)

	def GET_all(self):
		# initialize the response dictionary
		resp = {'result': 'success'}
	
		# fill in a list with all key value pairs in the dictionary
		entriesList = []
		for key in self.dict.keys():
			entriesList.append({"key": key, "value": self.dict[key]})

		resp['entries'] = entriesList

		return json.dumps(resp)
		
	def POST(self):
		# initialize the response dictionary
		resp = {'result': 'success'}

		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)
			self.dict[str(pData['key'])] = str(pData['value'])
			
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp)

	def DELETE_all(self):
		# initialize the response dictionary
		resp = {'result': 'success'}

		self.dict.clear()
	
		return json.dumps(resp)

	def DELETE_key(self, key):
		resp = {'result': 'success'}
		key = str(key)	

		try:
			if not self.dict.has_key(key):
				resp['result'] = 'error'
				resp['message'] = 'Key not found.'
			else:
				del self.dict[key]
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp)

	def PUT(self, key):
		resp = {'result': 'success'}
		key = str(key)

		try:
			data = cherrypy.request.body.read()
			pData = json.loads(data)
			self.dict[key] = str(pData['value'])
		except Exception as ex:
			resp['result'] = 'failure'
			resp['message'] = str(ex)

		return json.dumps(resp)
