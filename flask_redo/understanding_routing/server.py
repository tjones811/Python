from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def say(name):
    

    
    return 'Hi ' + name

@app.route('/repeat/<int:num>/<word>')
def repeat(num,word):

    return word * num

if __name__ == "__main__":
    app.run(debug=True)