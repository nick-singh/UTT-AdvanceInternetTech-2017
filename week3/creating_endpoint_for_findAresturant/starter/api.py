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



engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
  if request.method == 'GET':
    pass
  	# RETURN ALL RESTAURANTS IN DATABASE  	

  elif request.method == 'POST':
  	# MAKE A NEW RESTAURANT AND STORE IT IN DATABASE
    pass


    
@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
  
  if request.method == 'GET':
  	#RETURN A SPECIFIC RESTAURANT
  	pass
  elif request.method == 'PUT':
  	#UPDATE A SPECIFIC RESTAURANT
  	pass

  elif request.method == 'DELETE':
  	#DELETE A SPECFIC RESTAURANT
  	pass



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)