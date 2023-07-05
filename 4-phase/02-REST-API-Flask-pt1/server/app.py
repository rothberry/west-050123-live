#!/usr/bin/env python3

# 📚 Review With Students:
    # API Fundamentals
    # MVC Architecture and Patterns / Best Practices
    # RESTful Routing
    # | HTTP Verb 	|       Path       	| Description        	|
    # |-----------	|:----------------:	|--------------------	|
    # |            	|   /path   	|    	|

# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5000
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

# 1. ✅ Import `Api` and `Resource` from `flask_restful`
    # ❓ What do these two classes do at a higher level? 

from models import db, Production

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# 2. ✅ Initialize the Api
    # `api = Api(app)`

# 3. ✅ Create a Production class that inherits from Resource

# 4. ✅ Create a GET (All) Route
  
# 5. ✅ Serialization ?

# 10. ✅ Use our serializer to format our response to be cleaner

# 11. ✅ Create a POST Route

   
# 12. ✅ Add the new route to our api with `api.add_resource`

# 13. ✅ Create a GET (One) route

# 14. ✅ Add the new route to our api with `api.add_resource`