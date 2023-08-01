from ipdb import set_trace
from dotenv import dotenv_values
from flask import Flask, request, make_response, abort, session, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Picture

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

ENV = dotenv_values("../.env")

migrate = Migrate(app, db)
db.init_app(app)

# * Create an upload route as a POST

# * Create a route to grab a Picture

# * Create some restful routes for the Pictures in our DB


if __name__ == '__main__':
	app.run(port=5555, debug=True)