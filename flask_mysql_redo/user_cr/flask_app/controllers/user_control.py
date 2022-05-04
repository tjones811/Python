from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.faction import Faction

@app.route('/')
def index():

    users = User.get_all()
    
    factions = Faction.get_all_factions()

    return render_template('index.html', all_users=users, all_factions= factions)


@app.route('/create_user')
def create_user():
    factions = Faction.get_all_factions()
    return render_template('create_user.html',all_factions = factions)


@app.route('/add_user', methods=['POST'])
def add_user():
    if not User.validate_user(request.form):
        return redirect('/create_user')
    
    
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        'faction_id': request.form['faction_id']
    }

    user =User.save(data) 
    print(user)
    return redirect(f'/user/show/{user}')


@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }

    user= User.get_user_with_faction(data)

    return render_template('show.html',one_user = user)

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }

    user= User.get_one(data)

    return render_template('edit.html',one_user= user)


@app.route('/user/update' , methods = ['POST'])
def update():

    data = {
        "id": request.form['id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    User.update(data)
    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete(id):

    data = {
        'id': id
    }

    User.delete(data)

    return redirect('/')