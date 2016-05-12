import unittest
import requests
import json

class TestRecommendations(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	SITE_URL = 'http://student01.cse.nd.edu:40063'
	RECOMMENDATIONS_URL = SITE_URL + '/recommendations/'
	RATINGS_URL = SITE_URL + '/ratings/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		m['apikey'] = 'cOBfTz6ZZG'
		r = requests.put(self.RESET_URL, json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_recommendations_get(self):
		self.reset_data()
		user_id = 149
		r = requests.get(self.RECOMMENDATIONS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['movie_id'], 989)

	def test_recommendations_put(self):
		self.reset_data()
		user_id = 199
		movie_id = 32
		rating = 5

		m = {}
		m['movie_id'] = movie_id
		m['rating'] = rating
		m['apikey'] = 'cOBfTz6ZZG'
		r = requests.put(self.RECOMMENDATIONS_URL + str(user_id), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['result'], 'success')

		r = requests.get(self.RATINGS_URL + str(movie_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['rating'], 3.947054930509596) #3.945731303772336)

if __name__ == "__main__":
	unittest.main()

