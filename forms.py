from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, RadioField, SelectField, TextAreaField

from wtforms.validators import InputRequired, Optional, URL, Length

class AddPetForm(FlaskForm):
    """Form for putting up pets for adoption :("""
    
    name = StringField("Pet Name", validators=[InputRequired(message="Must provide a name for the animal.")])
    
    species = SelectField("Species", validators=[InputRequired('Must select a pet species.')], choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Rabbit', 'Rabbit'), ('Snake', 'Snake'), ('Lizard', 'Lizard')])
    
    age = IntegerField('Pet Age')
    
    photo_url = StringField('Pet Photo Url', validators=[Optional(), URL()])
    
    notes = TextAreaField(
        "Pet Notes",
        validators=[Optional(), Length(min=10)]
    )
    
    available = BooleanField('Are They Available?', validators=[InputRequired('Please choose an availability for the pet.')])
    
    
class EditPetForm(FlaskForm):
    """Form for editing existing pet info. Forms should default to the current value, then update the db with any attributes that are changed, such as if a pet goes from 'available' to 'not available' :) """
    
    photo_url = StringField(
        "Pet Photo Url",
        validators=[Optional(), URL()]
    )
    
    notes = TextAreaField(
        "Pet Notes",
        validators=[Optional(), Length(min=10)]
    )
    
    available = BooleanField('Are they available?', validators=[InputRequired('Please choose an availability for the pet.')])
    
    