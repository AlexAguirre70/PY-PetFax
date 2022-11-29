from flask import (Blueprint, render_template)
import json
pets_data= json.load(open('pets.json'))
#print(pets)

bp=Blueprint('pet',__name__,url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('index.html',pets=pets_data)

@bp.route('/<int:index>')
def show(index):
    pet_data= pets_data[int(index)-1]
    return render_template('show.html',pet=pet_data)

@bp.route('/<int:index>/new')
def new(index):
    pet_data= pets_data[int(index)-1]
    return render_template('new.html',pet=pet_data)