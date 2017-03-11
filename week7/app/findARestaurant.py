# -*- coding: utf-8 -*-
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "P0ZAGLGKKXLD50RFY4AKJHWPPIL5NJWNVE1UHOJCGKZHLFUB"
foursquare_client_secret = "FLLJ2TP3SKNSJQYGBSVURTTXCXJQCLVBGH3NUOMRY20ZXBIE"
google_api_key = "AIzaSyAt-lQkLsGUVO1BnRQW03N-pgNJGne63Sk"

def getGeocodeLocation(inputString):
    #Replace Spaces with '+' in URL
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    #print response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)


def get_venue_menu(venue_id):
    h = httplib2.Http()
    #default image url
    imageURL = "http://runawayapricot.com/wp-content/uploads/2014/09/placeholder.jpg"
    url = ('https://api.foursquare.com/v2/venues/%s/menu?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
    result = json.loads(h.request(url,'GET')[1])
    print result

def get_venue_image(venue_id):
    h = httplib2.Http()
    #default image url
    imageURL = "http://runawayapricot.com/wp-content/uploads/2014/09/placeholder.jpg"
    #Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
    print url
    result = json.loads(h.request(url,'GET')[1])
    #Grab the first image
    #if no image available, insert default image url
    if result['response']['photos']['items']:
        firstpic = result['response']['photos']['items'][0]
        prefix = firstpic['prefix']
        suffix = firstpic['suffix']
        imageURL = prefix + "300x300" + suffix
    return imageURL
        

#This function takes in a string representation of a location and cuisine type, geocodes the location, and then pass in the latitude and longitude coordinates to the Foursquare API
def findARestaurant(mealType, location):
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    # if we have a valid response
    if result['response']['venues']:
        rest = []
        # for all restaurants that were returned
        for restaurant in result['response']['venues']:
            # get the restaurant id
            venue_id = restaurant['id'] 
            # get the restaurant name
            restaurant_name = restaurant['name']
            #  get the restaurant address
            restaurant_address = restaurant['location']['formattedAddress']
            #Format the Restaurant Address into one string
            address = ""
            for i in restaurant_address:
                address += i + " "
            restaurant_address = address
            imageURL = get_venue_image(venue_id)
            restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL, 'venue_id':venue_id}
            rest.append(restaurantInfo)            
        return rest
    else:
        #print "No Restaurants Found for %s" % location
        return {"message":"No Restaurants Found"}
