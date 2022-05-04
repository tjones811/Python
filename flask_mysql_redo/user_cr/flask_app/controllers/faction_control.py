from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.faction import Faction
from flask_app.models.user import User




@app.route('/faction/new')
def new_faction():
    return render_template('add_faction.html')

@app.route('/faction/create', methods=['POST'])
def create_faction():
    data = {
        'name': request.form['name'],
        'level': request.form['level'],
        'date_created': request.form['date_created']
    }

    new_faction_id =Faction.create_new_faction(data)


    return redirect('/')


@app.route('/faction/<int:faction_id>')
def show_one_faction(faction_id):
    query_data = {
        'faction_id': faction_id
    }

    one_faction = Faction.get_faction_with_users(query_data)

    return render_template('show_one_faction.html',one_faction = one_faction)

