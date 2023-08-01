from ipdb import set_trace
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Picture(db.Model):
    __tablename__ = "pictures"

    id = db.Column(db.Integer, primary_key=True)

    # add any columns that may be needed from the cloudinary

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
