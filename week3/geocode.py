import httplib2
import json


google_geocode_id = "AIzaSyAvnFnZSiMNLeXX3eGh5kf9NEySf-zjkHY"
google_initial_url = """https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"""

def get_geocode_location(input_string):
	location_string = input_string.replace(" ", "+")
	url = google_initial_url%(location_string, google_geocode_id)
	
	http_request = httplib2.Http()
	response, content = http_request.request(url, 'GET')
	print response, content


get_geocode_location("utt pt lisas")