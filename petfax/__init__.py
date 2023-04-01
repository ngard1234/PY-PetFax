
# The __init__.py file is where we want to initially configure Flask and write the function that will create the instance of our app.
from flask import Flask 

def create_app(): # application factory create an instance of app from Flask.
    app = Flask(__name__)

    @app.route('/') 
    def hello(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact_page blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app
