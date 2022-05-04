from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():

    users = User.get_all()
    print (users)

    return render_template('index.html', all_users=users)


@app.route('/create_user')
def create_user():
    return render_template('create_user.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    user =User.save(data) 
    print(user)
    return redirect(f'/user/show/{user}')


@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }

    user= User.get_one(data)

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