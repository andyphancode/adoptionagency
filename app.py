from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm
from app import *

app = Flask(__name__) 
app.app_context().push() 
app.config['SECRET_KEY'] = 'idksecretkey' 
debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/", methods=["GET"])
def root():
    """Show homepage listing pets."""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Show pet form or add pet."""

    form = AddPetForm()

    if form.validate_on_submit():

        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes =  form.notes.data

        pet = Pet(name=pet_name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("add.html", form=form)

@app.route("/<pet_id>", methods=["GET","POST"])
def edit_pet(pet_id):
    """Show edit pet form or edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect("/")
    else:
        return render_template("edit.html", form=form, pet=pet)
        
