import json
from contextlib import suppress

def parseAPIResponseToDictionary(api_response)->(dict):
	"""
	Parses a response string from urllib.response.read() and returns a dict of weather data.
	The weather data includes: temperature, wind speed, summary, sunsetTime, sunriseTime.
	"""
	try:
		data = json.loads(api_response)
		weather_data = { 
						'summary': data['currently']['summary'],
						'temperature': data['currently']['temperature'], 
						'wind_speed': data['currently']['windSpeed'] 
						}
	except json.decoder.JSONDecodeError as e:
		e.args = ('Response from server was not valid JSON.',)
		raise
	except KeyError as e:
		suppress(e)
		raise WeatherDataNotFoundException((e.args[0] + ' was not found.',))
	else:
		return weather_data
	
class WeatherDataNotFoundException(Exception):
	"""
	Raised when weather data was expected but not provided.
	"""
	def __init__(self, *args):
		super().__init__(self, ('Check that request is valid and returns valid data',) + 
								args)