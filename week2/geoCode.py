import httplib2
import json


google_geocode_id = "AIzaSyAvnFnZSiMNLeXX3eGh5kf9NEySf-zjkHY"

fsid = "P0ZAGLGKKXLD50RFY4AKJHWPPIL5NJWNVE1UHOJCGKZHLFUB"
fsSecret = "FLLJ2TP3SKNSJQYGBSVURTTXCXJQCLVBGH3NUOMRY20ZXBIE"

def getGeocodeLocation(inputString):
	locationString = inputString.replace(" ","+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(
		locationString, google_geocode_id))
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	return result['results'][0]['geometry']['location']


def findAResturant(mealType, location):
	geoloc = getGeocodeLocation(location)
	url = ("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20120609&ll=%s,%s&query=%s"%
		  (fsid, fsSecret,geoloc['lat'],geoloc['lng'],mealType))
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	return result

print json.dumps(findAResturant("pizza","Chaguanas"))