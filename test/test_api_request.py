import unittest
from weather_checker import api_request
from urllib import request

class APIRequestTestCase(unittest.TestCase):
	
	def test_valid_coordinates_returns_request(self):
		"""
		Verifies that the correct request type is returned for use with urlopen()
		The value returned should be an instance of urllib.request.Request
		"""
		lat = 0
		lon = 0
		self.assertIsInstance(api_request.createAPIRequestWithCoordinates(lat, lon), request.Request)
	
	def test_request_returns_200_OK(self):
		"""
		Verifies that the request returned can be used to get information from the server.
		The server should return a 200 OK HTTP status with the request.
		"""
		lat = 0
		lon = 0
		r = api_request.createAPIRequestWithCoordinates(lat, lon)
		url = request.urlopen(r)
		self.assertEqual(url.getcode(), 200)
