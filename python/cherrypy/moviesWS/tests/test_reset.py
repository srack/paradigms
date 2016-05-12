import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://student01.cse.nd.edu:40063'
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		m = {}
		m['apikey'] = 'cOBfTz6ZZG'
		r = requests.put(self.RESET_URL, data = json.dumps(m))

if __name__ == "__main__":
	unittest.main()

