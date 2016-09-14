import unittest
from weather_checker import api_response_parser
from json import decoder

class APIResponseParserTestCase(unittest.TestCase):

	def test_parses_weather_data(self):
		"""
		Validate that the parser will parse weather data.
		The method should parse correctly and return a dict with weather data.
		"""
		fake_response = ('{"currently":{"summary":"rainy","temperature":6,"windSpeed":7}}')
		
		parsed_dict = api_response_parser.parseAPIResponseToDictionary(fake_response)
		actual_dict = { 
						'summary': 'rainy',
						'temperature': 6, 
						'wind_speed': 7 
						}
		self.assertEqual(parsed_dict, actual_dict)
	
	def test_missing_weather_data_raises_error(self):
		"""
		Validate that the parser will require temperature, wind speed, summary, 
		sunsetTime, sunriseTime. in the response.
		The method should return a WeatherDataNotFoundException.
		"""
		fake_response = '{"currently":{"cats":0, "frogs":-5, "dogs":"yes"}}'
		with self.assertRaises(api_response_parser.WeatherDataNotFoundException):
			api_response_parser.parseAPIResponseToDictionary(fake_response)
	
	def test_invalid_json_data_raises_error(self):
		"""
		Validate that the parser will require valid JSON data to parse.
		The method should return a JSONDecodeError.
		"""
		fake_response = "this is not JSON."
		with self.assertRaises(decoder.JSONDecodeError):
			api_response_parser.parseAPIResponseToDictionary(fake_response)

	def test_allows_unnecessary_fields(self):
		"""
		Validate that the parser will ignore fields unrealted to weather data.
		The method should parse correctly and return a dict with weather data.
		"""
		fake_response = ('{"currently":{"cats":0, "summary":"rainy", '
						 				'"frogs":-1, "temperature":6, ' 
						 				'"windSpeed":7, "dogs":"yes"}}')
						 				
		parsed_dict = api_response_parser.parseAPIResponseToDictionary(fake_response)
		actual_dict = { 
						'summary': 'rainy',
						'temperature': 6, 
						'wind_speed': 7 
						}
		self.assertEqual(parsed_dict, actual_dict)
