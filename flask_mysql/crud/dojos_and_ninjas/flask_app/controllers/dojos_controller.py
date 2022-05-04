from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.dojo_model import Dojo



@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    
    dojos = Dojo.get_all_dojos()
    
    return render_template('dojos.html',dojos=dojos)

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }

    new_jojo = Dojo.create_dojo(data)

    return redirect('/')

@app.route('/dojos/show/<int:dojo_id>')
def dojo_show(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }

    dojo = Dojo.dojo_ninjas(data)

    return render_template('show_dojo.html',dojo=dojo)
