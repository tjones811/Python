from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'ghfgjkfhgjkd'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/destroy')
def reset_counter():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)