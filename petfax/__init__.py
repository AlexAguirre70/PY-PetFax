from flask import (Flask, redirect)
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    #add SQLAlchemy config
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://petfax_user:petfax$123@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    # import the database models
    from . import models
    models.db.init_app(app)

    #instantiate Migrate
    migrate= Migrate(app,models.db)
    @app.route('/')
    def hello ():
        return redirect('/pets')

    from . import pet
    app.register_blueprint(pet.bp) 
   
    from . import fact
    app.register_blueprint(fact.bp) 
   
    return app