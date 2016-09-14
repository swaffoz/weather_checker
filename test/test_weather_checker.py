import unittest
import weather_checker
import sys
import os


class WeatherCheckerTestCase(unittest.TestCase):

	def test_help_argument_does_not_crash(self):
		"""
		Validates only that main script does not crash when given the help arguments.
		"""
		weather_checker.checkWeather('-h')
		weather_checker.checkWeather('--help')
	
	def test_no_arguments_does_not_crash(self):
		"""
		Validates only that main script does not crash when given no arguments.
		"""
		weather_checker.checkWeather()
	
	def test_one_argument_does_not_crash(self):
		"""
		Validates only that main script does not crash when given 1 argument.
		"""
		weather_checker.checkWeather(1)
	
	def test_two_arguments_does_not_crash(self):
		"""
		Validates only that main script does not crash when given 2 arguments.
		"""
		weather_checker.checkWeather(1, 2)
		
	def test_more_than_two_arguments_does_not_crash(self):
		"""
		Validates only that main script does not crash when given >2 arguments.
		"""
		weather_checker.checkWeather(1, 2, 3) 
	
	def test_does_not_crash_as_main(self):
		"""
		Validates only that the weather checker does not crash when run as __main__ 
		script. Ignores print out from script by sending stdout to devnull.
		"""
		sys.stdout = open(os.devnull, 'w')
		weather_checker.run_script('__main__')
