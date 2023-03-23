from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Image URL of Pet", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes on Pet")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Image URL of Pet", validators=[Optional(), URL()])
    notes = StringField("Notes on Pet")
    available = BooleanField("Pet Available?")
