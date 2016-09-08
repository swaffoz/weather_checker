#!/usr/bin/python3

import sys
import coordinate_parser
import api_request
import api_response_parser
import weather_formatter
from urllib.request import urlopen

def checkWeather(*argv)->(str):
	"""
	Main function of script.
	"""
	
	input = None
	
	if (len(argv) == 2 or
		"-h" in argv or
		"--help" in argv):
		return " Usage: \n\t$weather_checker.py LATITUDE LONGITUDE"
	elif len(argv) > 2:
		input = " ".join([str(argv[1]), str(argv[2])])

	coords = coordinate_parser.parseCoordinatesFromString(input)
	req = api_request.createAPIRequestWithCoordinates(coords[0], coords[1])

	with urlopen(req) as response:
		response_text = response.read().decode('utf-8')
		weather_data = api_response_parser.parseAPIResponseToDictionary(response_text)
		return weather_formatter.stringFromWeatherData(weather_data['summary'], 
														 weather_data['temperature'], 
														 weather_data['wind_speed'])


def run_script(name):
	"""
	Act like a script if we were invoked like a script.
	This appeases coverage.py
	"""
	if name == '__main__':
		print(checkWeather(*sys.argv))

run_script(__name__)