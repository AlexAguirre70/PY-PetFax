#configuration
from flask import Flask
app =Flask(__name__)

#index route
@app.route('/')
def index():
    return 'Hello, this is Petfax'

#pets route
@app.route('/pets')
def pets():
    return ('Check out our pets available for adoption')

#about route
@app.route('/about')
def about():
    return ('About PetFax page')
