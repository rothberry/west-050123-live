#!/usr/bin/env python3
# 📚 Review With Students:
    # Authentication vs Authorization
    # Cookies vs Sessions
    # How Flask Encrypts Sessions

# Set up:
    # cd into server and run the following in the Terminal:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5000
        # flask db init
        # flask db revision --autogenerate -m'Create tables' 
        # flask db upgrade 
        # python seed.py
        # cd into client and run `npm i`

# Running React together 
     # In Terminal cd into the root directory, run:
        # `honcho start -f Procfile.dev`

""" 
    Both of the Auths

    Authentication:
    - Validating a user to be who they claim
    - Ex: Getting your hand stamped at a bar/club

    Session:
    - Active time while the user is logged into the app
    - a series of activities that the user does
    - Potentinally Encrpyted Object that holds data

    Cookie:
    - Piece of data stored within the browser
    - Mostly used for (and for this lectures purposes) credentials and keeping a user signed in


 """
from ipdb import set_trace
from dotenv import dotenv_values
from flask import Flask, request, make_response, abort, session, jsonify
from flask_migrate import Migrate

from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound, Unauthorized

from flask_cors import CORS

from models import db, Production, CastMember, User

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Set up:
    # generate a secrete key `python -c 'import os; print(os.urandom(16))'`
# load_env()
# ENV = dotenv_values()
ENV = dotenv_values("../.env")
app.secret_key = ENV["SECRET_KEY"]

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Productions(Resource):
    def get(self):
        production_list = [p.to_dict() for p in Production.query.all()]
        response = make_response(
            production_list,
            200,
        )

        return response

    def post(self):
        form_json = request.get_json()
        try:
            new_production = Production(
                title=form_json['title'],
                genre=form_json['genre'],
                budget=int(form_json['budget']),
                image=form_json['image'],
                director=form_json['director'],
                description=form_json['description']
            )
        except ValueError as e:
            abort(422,e.args[0])

        db.session.add(new_production)
        db.session.commit()

        response_dict = new_production.to_dict()

        response = make_response(
            response_dict,
            201,
        )
        return response
api.add_resource(Productions, '/productions')


class ProductionByID(Resource):
    def get(self,id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, 'The Production you were looking for was not found')
        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )
        
        return response

    def patch(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, 'The Production you were trying to update for was not found')

        for attr in request.form:
            setattr(production, attr, request.form[attr])

        production.ongoing = bool(request.form['ongoing'])
        production.budget = int(request.form['budget'])

        db.session.add(production)
        db.session.commit()

        production_dict = production.to_dict()
        
        response = make_response(
            production_dict,
            200
        )
        return response

    def delete(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, 'The Production you were trying to delete was not found')
        db.session.delete(production)
        db.session.commit()

        response = make_response('', 204)
        
        return response
api.add_resource(ProductionByID, '/productions/<int:id>')

# What are the REST(ish)ful routes for User
# GET       /users      INDEX
#   EX: Newsletter app, Social Media
# GET       /users/:id  SHOW
# POST      /users      SIGNUP/REGISTER
# GET       /authorized CURRENT_USER
# POST      /login      LOGIN
# DELETE    /logout     LOGOUT

# 1.✅ User
    # A user model was added to "models.py" along with an Authentication component in client/src/components/Authentication.sj
    # 1.1 Create a User POST route by creating a class Users that inherits from Resource
    # 1.2 Add the route '/users' with api.add_resource()
    # 1.3 Create a POST method
        # 1.3.1 use .get_json() to convert the request json 
        # 1.3.2 create a new user with the request data
        # 1.3.3 add and commit the new user
        # 1.3.4 Save the new users id to the session hash
        # 1.3.5 Make a response and send it back to the client
class Users(Resource):

    def post(self):
        form_json = request.get_json()
        new_user = User(
            name=form_json["name"],
            email=form_json["email"]
        )
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        return make_response(new_user.to_dict(), 201)


api.add_resource(Users, "/users")
# 2.✅ Test this route in the client/src/components/Authentication.sj 

# 3.✅ Create a Login route
    # 3.1 Create a login class that inherits from Resource
    # 3.2 Use api.add_resource to add the '/login' path
    # 3.3 Build out the post method
        # 3.3.1 convert the request from json and select the user name sent form the client. 
        # 3.3.2 Use the name to query the user with a .filter
        # 3.3.3 If found set the user_id to the session hash
        # 3.3.4 convert the user to_dict and send a response back to the client 
    #3.4 Toggle the signup form to login and test the login route

class Login(Resource):

    def post(self):
        current_user = User.query.filter_by(name=request.get_json()["name"]).first()
        if current_user:
            session["user_id"] = current_user.id
            return make_response(current_user.to_dict(), 200)
        else:
            return make_response({"errors": "Username not found"}, 404)

api.add_resource(Login, "/login")

# 4.✅ Create an AuthorizedSession class that inherits from Resource
    # 4.1 use api.add_resource to add an authorized route
    # 4.2 Create a get method
        # 4.2.1 Access the user_id from session with session.get
        # 4.2.2 Use the user id to query the user with a .filter
        # 4.2.3 If the user id is in sessions and found make a response to send to the client. else raise the Unauthorized exception (Note- Unauthorized is being imported from werkzeug.exceptions)

class CurrentUser(Resource):

    def get(self):
        print(session)
        current_user = User.query.filter_by(id = session.get("user_id")).first()

        if current_user:
            return make_response(current_user.to_dict(), 200)
        else:
            return make_response({"error": "Unauthorized..."}, 401)

api.add_resource(CurrentUser, "/authorized")
# 5.✅ Head back to client/src/App.js to restrict access to our app!

# 6.✅ Logout 
    # 6.1 Create a class Logout that inherits from Resource 
    # 6.2 Create a method called delete
    # 6.3 Clear the user id in session by setting the key to None
    # 6.4 create a 204 no content response to send back to the client

class Logout(Resource):
    def delete(self):
        session["user_id"] = None
        return make_response({}, 204)
    
api.add_resource(Logout, "/logout")


# 7.✅ Navigate to client/src/components/Navigation.js to build the logout button!

# 8 (or 1).✅ We will be using sessions in the application, so let's build out a quick cookie example
    # Creating a non RESTful route for /dark_mode
        # 8.1 Use the @app.route decorator and pass it the path '/dark_mode' and the 'methods=['GET']'
        # 8.2 Create a method called dark mode. 
        # 8.3 Create a response with make_response and pass it a dict that will list all of our cookies jsonify
        # 8.4 Set the cookies in the response with set_cookie and pass it a key 'mode' and a value 'dark'
        # 8.5 return the response, run the server and check the response in the browser.
        # Note: Now is a great time to view the cookies and talk about security concerns


@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )

    return response


if __name__ == '__main__':
    app.run(port=5000, debug=True)