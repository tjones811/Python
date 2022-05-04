from crypt import methods
from flask import Flask, render_template, session, redirect,request
import random

app = Flask(__name__)
app.secret_key = 'ghuriha54839'


@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)