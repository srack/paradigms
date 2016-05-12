import unittest
import requests
import json

class TestRatings(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	SITE_URL = 'http://student01.cse.nd.edu:40063'
	RATINGS_URL = SITE_URL + '/ratings/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		m['apikey'] = 'cOBfTz6ZZG'
		r = requests.put(self.RESET_URL, data = json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_ratings_get(self):
		self.reset_data()
		movie_id = 32

		r = requests.get(self.RATINGS_URL + str(movie_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['rating'], 3.945731303772336)
		self.assertEquals(resp['movie_id'], movie_id)

if __name__ == "__main__":
	unittest.main()

