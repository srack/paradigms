import unittest
import requests
import json

class TestUsers(unittest.TestCase):

	#@classmethod
	#def setUpClass(self):
	SITE_URL = 'http://student01.cse.nd.edu:40063'
	USERS_URL = SITE_URL + '/users/'
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

	def test_users_get(self):
		self.reset_data()
		user_id = 6029
		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['gender'], 'F')
		self.assertEquals(resp['zipcode'], '23185')

	def test_users_put(self):
		self.reset_data()
		user_id = 95

		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['gender'], 'M')
		self.assertEquals(resp['zipcode'], '98201')

		m = {}
		m['gender'] = 'M'
		m['zipcode'] = '19999'
		m['occupation'] = 3
		m['age'] = 99
		m['apikey'] = 'cOBfTz6ZZG'
		r = requests.put(self.USERS_URL + str(user_id), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['result'], 'success')

		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['gender'], m['gender'])
		self.assertEquals(resp['zipcode'], m['zipcode'])

	def test_users_delete(self):
		self.reset_data()
		user_id = 95

		m = {}
		m['apikey'] = 'cOBfTz6ZZG'
		r = requests.delete(self.USERS_URL + str(user_id), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['result'], 'success')

		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['result'], 'error')
		#self.assertEquals(resp['message'], 'user not found')

if __name__ == "__main__":
	unittest.main()

