from ipdb import set_trace
from dotenv import dotenv_values
from flask import Flask, request, make_response, abort, session, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Picture
from os import system
import cloudinary
import cloudinary.uploader  # the POST request to the cloudinary API endpoint
import cloudinary.api

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

print(
    f"*** CLOUD_NAME: {cloud_config.cloud_name}\n*** CLOUD KEY: {cloud_config.api_key}")


migrate = Migrate(app, db)
db.init_app(app)

# * Create an upload route as a POST


@app.route("/upload", methods=["POST"])
def upload():
    app.logger.info("Upload Route")
    set_trace()
    file_to_upload = request.files["file"]
    # can send more than one file, if we code it dynamically
    public_id = file_to_upload.filename.split(".")[0]
    upload_result = cloudinary.uploader.upload(
        file_to_upload, public_id=public_id)
    app.logger.info(upload_result)
    return make_response(upload_result)


# * Create a route to grab a Picture
@app.route('/pictures/<string:public_id>')
def get_picture(public_id):
    print(f'Public id: {public_id}')
    image_info = cloudinary.api.resource(public_id)
    print(image_info)
    return make_response(image_info)

# * Create some restful routes for the Pictures in our DB


@app.route("/")
def home():
    return make_response({"message": "Hi"})


if __name__ == '__main__':

    app.run(port=5555, debug=True)
