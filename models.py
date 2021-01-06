"""Pet Adoption Agency Model"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Cute fuzzy friends!!!!"""
    
    __tablename__ = 'pets'
    
    def __repr__(self):
        s = self
        return f"""
        <Pet id = {s.id}, Pet name = {s.name}, 
        Pet species = {s.species}, Pet photo_url = {s.photo_url}, 
        Pet age = {s.age}, 
        notes: {s.notes}, 
        available: {s.available}>"""
        
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(30),
                     unique=False,
                     nullable=False)
    
    species = db.Column(db.String(20),
                        nullable=False,
                        unique=False)
    
    age = db.Column(db.Integer,
                    nullable=False,
                    unique=False)
    
    photo_url = db.Column(db.String,
                          default="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/No_image_available_400_x_600.svg/512px-No_image_available_400_x_600.svg.png",
                          nullable=False,
                          unique=False)
    
    notes = db.Column(db.String,
                      unique=False,
                      nullable=False)
    
    available = db.Column(db.Boolean,
                          unique=False,
                          nullable=False,
                          default=True)
    
    @property
    def get_info(self):
        p = self
        return f"""
        Meet {p.name}! {p.name} is a {p.age} year old {p.species}.
        """
