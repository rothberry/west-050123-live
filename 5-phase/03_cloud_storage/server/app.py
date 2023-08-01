from ipdb import set_trace
from dotenv import dotenv_values
from flask import Flask, request, make_response, abort, session, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
import cloudinary
import cloudinary.uploader
import cloudinary.api
from models import db, Picture

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

ENV = dotenv_values("../.env")

cloud_config = cloudinary.config(
    cloud_name=ENV["CLOUD_NAME"],
    api_key=ENV["CLOUD_API_KEY"],
    api_secret=ENV["CLOUD_SECRET"],
    secure=True
)
print("****1. Set up and configure the SDK:****\nCredentials: ",
      cloud_config.cloud_name, cloud_config.api_key, "\n")

migrate = Migrate(app, db)
db.init_app(app)

# * Create an upload route as a POST


@app.route("/upload", methods=["POST"])
def upload_file():
    app.logger.info("Upload Route")
    file_to_upload = request.files["file"]
    upload_result = cloudinary.uploader.upload(file_to_upload)
    app.logger.info(upload_result)
    return jsonify(upload_result)


# * Create a route to grab a Picture
@app.route("/pictures/<string:public_id>")
def get_picture(public_id):
    # test id: owakoo90yr4btu2xsdv8
    app.logger.info(f'Public Id: {public_id}')
    return "DONE..."

# * Create some restful routes for the Pictures in our DB

if __name__ == '__main__':
    app.run(port=5555, debug=True)
