from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "ffju48rf94u"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['post'])
def create_user():
    print ('Got post information')
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']


    print(request.form)

    return redirect ('/show')

@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    
    return render_template('show.html',name_on_template = session['username'],
    email_on_template = session['useremail'])

if __name__ == '__main__':
    app.run(debug=True)