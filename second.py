from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/quizz'
db = SQLAlchemy(app)


class Names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    genre = db.Column(db.String(15))


@app.route("/index", method=['GET', 'POST'])
def ak():
    if(request.method=='POST'):
        name = request.form.get('name')

        entry = Names(name=name)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')


@app.route("/a")
def ak1():
    name = "Akash"
    return render_template('mov.html', namer=name)


app.run(debug=True)
