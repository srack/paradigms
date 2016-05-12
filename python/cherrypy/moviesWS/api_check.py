# Sam Rack
# CSE 30332 CherryPy Web Service
# api_check.py

class ApiKeyCheck:
	def __init__(self, key = 'cOBfTz6ZZG'):
		self.apiKey = key

	def check(self, key):
		return (key == self.apiKey)
			
