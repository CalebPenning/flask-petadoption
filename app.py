from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
import datetime
from models import Pet, connect_db, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ILOVEKITTYCATS420'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def render_homepage():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/edit/<int:p_id>', methods=['GET', 'POST'])
def edit_pet(p_id):
    """Show edit form for a pet instance and handle committing changes to db."""
    pet = Pet.query.get_or_404(p_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        
        flash(f"{pet.name}'s information was updated successfully.")
        return redirect('/')
    
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
    

