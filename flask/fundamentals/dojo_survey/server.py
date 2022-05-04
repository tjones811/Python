from codecs import namereplace_errors
from flask import Flask, render_template, session, redirect,request
import random

app = Flask(__name__)
app.secret_key = 'ghuriha54839'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    print('Got post Info')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/goback')
def goback():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)