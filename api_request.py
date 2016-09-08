from urllib import request

api_key = '2cd43dc590108cebeb3e910c567b5699'
base_url = 'https://api.forecast.io/forecast'

def createAPIRequestWithCoordinates(lat, lon)->(request.Request):
	"""
	Returns a Request object pointing to the server with specified latitude and longitude. 
	"""
	return request.Request(base_url + '/' + api_key + '/' + str(lat) + ',' + str(lon))
