import unittest
import time
from weather_checker import weather_formatter

class WeatherFormatterTestCase(unittest.TestCase):

	def test_summary_formatting(self):
		"""
		Validates that the summary format is presented as Currently {summary}
		"""
		summary = "summary"
		formatted_string = weather_formatter.stringFromWeatherData(summary, 
																	1, 
																	2)
		formatted_summary = formatted_string.split('\n')[0]
		expected_formatted_summary = "Currently " + str(summary)
		self.assertEqual(formatted_summary, expected_formatted_summary)
	
	def test_temperature_formatting(self):
		"""
		Validates that the temperature format is presented as {temp}˚F Outside
		"""
		temp = 1
		formatted_string = weather_formatter.stringFromWeatherData("summary", 
																	temp, 
																	2)
		formatted_temp = formatted_string.split('\n')[1]
		expected_formatted_temp = str(temp) + "˚F Outside"
		self.assertEqual(formatted_temp, expected_formatted_temp)
	
	def test_wind_speed_formatting(self):
		"""
		Validates that the wind speed format is presented as {wind}MPH Wind
		"""
		wind_speed = 2
		formatted_string = weather_formatter.stringFromWeatherData("summary", 
																	1, 
																	wind_speed)
		formatted_wind_speed = formatted_string.split('\n')[2]
		expected_formatted_wind_speed = str(wind_speed) + "MPH Wind"
		self.assertEqual(formatted_wind_speed, expected_formatted_wind_speed)

