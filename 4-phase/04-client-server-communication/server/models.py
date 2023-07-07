# 📚 Review With Students:
    # Validations and Invalid Data

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# 1.✅ Import validates from sqlalchemy.orm

db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)

# 2.✅ Add Constraints to the Columns     

    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add the relationship between our Production -> CrewMember
        
    serialize_rules = ('-crew_members.production',)


# 3.✅ Use the "validates" decorator to create a validations
  
# 4.✅ navigate to app.py
    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'

# Add CrewMember model for the has_many association
    # name: string
    # role: string
    # production_id: int, foriegn_key
    # timestamps

class CrewMember(db.Model, SerializerMixin):
    __tablename__ = 'crew_members'

    id = db.Column(db.Integer, primary_key=True)
    

    def __repr__(self):
        return f'<CrewMember Name:{self.name}, Role:{self.role}'
        # return f'<CrewMember Name:{self.name}, Role:{self.role}, ProductionTitle: {self.production.title}'

