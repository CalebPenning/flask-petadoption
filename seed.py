from app import app
from models import db, Pet

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add some pets to initially populate our table
owen = Pet(name="Owen", species="Cat", age=9, notes="Very sweet cat. Loves the outdoors but comes inside occasionally. Keep him inside during the cold months if you can help it, broke his hip when he was a young cat and it still bothers him. Loves wet food.", available=False)

honey_bear = Pet(name="Honey Bear", species="Cat", age=7, notes="Very sweet, very vocal. Goes outside but will not leave the perimeter of your place, and won't go outside at all right after adoption. Will sleep with you and hang with you indoors.", available=False)

sparky = Pet(name="Sparky", species="Hedgehog", age=2, notes="Wretched creature. Adopt at your own risk.", available=True)

# Add and commit our pets to the db
db.session.add_all([owen, honey_bear, sparky])
db.session.commit() 