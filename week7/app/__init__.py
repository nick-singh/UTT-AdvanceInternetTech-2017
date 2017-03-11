from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)



engine = create_engine('sqlite:///restaurant.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)



@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
	if request.method == 'GET':
		restaurants = session.query(Restaurant).all()
		return jsonify(restaurants = [i.serialize for i in restaurants])
	elif request.method == 'POST':
		location = request.json['location']
		mealType = request.json['mealType']    
		restaurant_info = findARestaurant(mealType, location)
		if restaurant_info != 'No Restaurants Found':
			# for restaurant in restaurant_info:
				# print restaurant['name'],restaurant['address'],restaurant['image'],restaurant['venue_id']
				# rest = Restaurant(restaurant_name = unicode(restaurant['name']), restaurant_address = unicode(restaurant['address']), restaurant_image = restaurant['image'], venue_id=restaurant['venue_id'])
				# session.add(restaurant)
				# session.commit()
			return jsonify(restaurants = restaurant_info)
		else:
			return jsonify({"error": restaurant_info})



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



