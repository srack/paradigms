import requests
import json

class _webservice_primer:
	## constructor ##
	def __init__(self, apikey):
		self.API_KEY = apikey
		self.SITE_URL = 'http://student00.cse.nd.edu:40001'
		self.MOVIES_URL = self.SITE_URL + '/movies/'
		self.RESET_URL = self.SITE_URL + '/reset/'

	## get_movie ##
	def get_movie(self, mid):
		r = requests.get(self.MOVIES_URL + str(mid))
		resp = json.loads(r.content)
		return resp

	## set_movie_title ##
	def set_movie_title(self, mid, newTitle):
		movie = self.get_movie(mid)
		movie['title'] = newTitle
		movie['apikey'] = self.API_KEY
		r = requests.put(self.MOVIES_URL + str(mid), data = json.dumps(movie))

	## delete_movie ##
	def delete_movie(self, mid):
		movie = self.get_movie(mid)
		movie['apikey'] = self.API_KEY
		r = requests.delete(self.MOVIES_URL + str(mid), data = json.dumps(movie))

	## reset_movie ##
	def reset_movie(self, mid):
		mydata = {}
		mydata['apikey'] = self.API_KEY
		r = requests.put(self.RESET_URL + str(mid), data = json.dumps(mydata))
		resp = json.loads(r.content)
		return resp


if __name__ == "__main__":
	MID = 66
	API_KEY = 'cOBfTz6ZZG'
	ws = _webservice_primer(API_KEY)

	ws.delete_movie(MID)

	movie = ws.get_movie(MID)
	if movie['result'] == 'success':
		print "Title:\t%s" % movie['title']
	else:
		print "Error:\t%s" % movie['message']
