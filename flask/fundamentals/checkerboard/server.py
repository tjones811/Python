from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def one():
    return render_template("index.html", col = 8, row = 8,color1= 'red', color2 = 'blue')

@app.route('/<int:col>')
def two(col):
    return render_template("index.html", col=col, row=8, color1= 'red', color2 = 'blue')

@app.route('/<int:row>/<int:col>')
def three(row, col):
    return render_template("index.html", col=col, row=row, color1='red', color2='blue')
    

@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def four(row, col,color1,color2):
    return render_template("index.html", col=col, row=row, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)