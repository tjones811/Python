from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo
from flask_app.models import dojo_model


@app.route('/ninja')
def new():

    dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html',dojos=dojos)

@app.route('/ninja/create', methods=['POST'])
def create():

    data = {
        'dojo_id' : request.form['dojo_id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }

    x = request.form['dojo_id']

    ninja = Ninja.create(data)
    print (ninja)

    return redirect(f'/dojos/show/{x}')


