import time

def stringFromWeatherData(summary, temp, wind_speed)->(str):
	"""
	Returns formatted string of weather data for output to terminal.
	"""
	
	return "Currently " + str(summary) + "\n" + \
			str(temp) + "˚F Outside\n" + \
			str(wind_speed) + "MPH Wind\n"