import unittest
from weather_checker import coordinate_parser

class CoordinateParserTestCase(unittest.TestCase):
	
	def test_empty_input_is_allowed(self):
		"""
		Verifies that a user can omit latitude and longitude from input.
		The parser should return the default coordinate.
		"""
		self.assertEqual(coordinate_parser.parseCoordinatesFromString(None), 
							coordinate_parser.default_coordinates)
		
	def test_no_coordinates_found_raises_error(self):
		"""
		Verifies that input that is not two floats is rejected.
		The parser should raise an error.
		"""
		with self.assertRaises(ValueError):
			coordinate_parser.parseCoordinatesFromString("abcd efgh")
	
	def test_impossible_coordinates_raises_error(self):
		"""
		Verifies that impossible coordinates are not returned.
		The parser should raise an error.
		"""
		with self.assertRaises(coordinate_parser.CoordinateOutOfBoundsException):
			coordinate_parser.parseCoordinatesFromString("91 -180")
		with self.assertRaises(coordinate_parser.CoordinateOutOfBoundsException):
			coordinate_parser.parseCoordinatesFromString("-90 181")
	
	def test_valid_input_is_parsed(self):
		"""
		Verifies that valid input is parsed correctly.
		The parser should return a coordinate as a tuple.
		"""
		input_string = "10 -20"
		coordinates = (10, -20)
		self.assertEqual(coordinate_parser.parseCoordinatesFromString(input_string), 			
							coordinates)
