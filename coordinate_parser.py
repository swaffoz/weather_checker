default_coordinates = (38.87182454344979, -99.33700315795494)

def parseCoordinatesFromString(string)->(float, float):
	"""
	Takes a string and parses out a tuple of two floats.
	Both floats must be valid GPS coordinates.
	"""
	if string is None: return default_coordinates
	
	try:
		floats = [float(x) for x in string.split()]
	except ValueError as e:
		e.args = (string + " couldn't be parsed to latitude and longitude coordinates.", )
		raise e
	else:
		return coordinateTupleFromFloatArray(floats)

def coordinateTupleFromFloatArray(arr)->(float, float):
	"""
	Takes an array of 2 floats and creats a tuple of latitude and longitude coordinates.
	Extraneous elements in the input array will be ignored.
	Invalid coordinates will raise a CoordinateOutOfBoundsException	
	"""
	if arr[0] < -90 or arr[0] > 90:
		raise CoordinateOutOfBoundsException(str(arr[0]) + " isn't a valid latitude.")
	elif arr[1] < -180 or arr[1] > 180:
		raise CoordinateOutOfBoundsException(str(arr[1]) + " isn't a valid longitude.")
	return (arr[0], arr[1])

class CoordinateOutOfBoundsException(Exception):
	"""
	Raised if a coordinate tuple contains a latitude outside the bounds -90 to 90
	or a longtitude outside the bounds of -180 to 180.
	"""
	def __init__(self, *args):
		super().__init__(self, "Latitude can be -90˚ to 90˚, " +
								"Longitude may be -180˚ to 180˚.")
