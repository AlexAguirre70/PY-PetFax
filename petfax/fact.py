from flask import (Blueprint, render_template,request,redirect)
from . import models

bp=Blueprint('fact',__name__,url_prefix='/facts')

#index get and post route
@bp.route('/', methods=["GET","POST"])
def index():
    if request.method =="POST":
        newFact = request.form['fact']
        newSubmitter= request.form['submitter']

        new_fact = models.Fact(submitter=newSubmitter, fact=newFact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    #query the database to get all the rows in facts table
    results= models.Fact.query.all()
    
    return render_template('facts/index.html',facts=results)

#new fact form route
@bp.route('/new')
def new_fact():
    print (request)
    return render_template('facts/new.html')
