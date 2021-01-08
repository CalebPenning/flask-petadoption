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

@app.route('/edit-pet/<int:p_id>', methods=['GET', 'POST'])
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
    

@app.route('/delete-pet/<int:p_id>')
def ask_permission(p_id):
    pet = Pet.query.get_or_404(p_id)
    return render_template('permissions.html', pet=pet)

@app.route('/delete-pet/<int:p_id>', methods=['POST'])
def remove_pet(p_id):
    if Pet.query.get(p_id):
        Pet.query.filter_by(id=p_id).delete()
        db.session.commit()
        
        flash("Listing deleted successfully")
        return redirect('/')
    
@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data 
        notes = form.notes.data
        available = form.available.data
        
        flash(f"New listing for pet: {name}, {age} year old {species} added successfully")
        
        pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        
        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/details/<int:p_id>')
def show_pet_details(p_id):
    pet = Pet.query.get_or_404(p_id)
    return render_template('details.html', pet=pet)