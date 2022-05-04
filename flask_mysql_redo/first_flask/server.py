from flask import Flask, render_template,redirect,request,session
app = Flask(__name__)

from friend import Friend

@app.route('/')
def index():

    friends = Friend.get_all()
    print (friends)
    return render_template('index.html',all_friends = friends)

@app.route('/create_friend', methods = ['POST'])
def create_friend():

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "occupation": request.form['occupation']
    }

    Friend.save(data)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)