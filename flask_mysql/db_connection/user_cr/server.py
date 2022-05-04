from flask import Flask, render_template, redirect, request, session
from user import User

app = Flask (__name__)


@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def user():
    users = User.get_all()
    
    return render_template("user.html",all_users = users)


@app.route('/user/new')
def new():
    return render_template('new_user.html')


@app.route('/create_user', methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect('/user')


if __name__ == "__main__":
    app.run(debug=True)