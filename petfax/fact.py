from flask import (Blueprint, render_template,request)


bp=Blueprint('fact',__name__,url_prefix='/facts')

#new fact form route
@bp.route('/new')
def index():
    print (request)
    return render_template('facts/new.html')
