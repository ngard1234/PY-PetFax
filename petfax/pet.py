#  Blueprint organize related routes and views together- similar to controller in express.
from flask import (Blueprint, render_template) 
import json 

pets = json.load(open('pets.json')) #to open files and to decode JSON. The base json package will have to be imported.

print(pets) #print in the console to see if it is loaded corectly.

# create an instance of the Bluprint class. 'pet' is the bluprint name, __name__: tells where in the project it's defined.
bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/') # defining the route- same as defining the routes directly on the app.
def index(): 
    return render_template('pets/index.html', pets=pets) # pass the loaded variable pets to the argument pets in index.html.

@bp.route('/<int:pet_id>')
def show_pets(pet_id): 
    pet = pets[pet_id]
    return render_template('pets/show_pets.html', pet=pet)