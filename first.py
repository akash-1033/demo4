from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
#import mysql.connector

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/leaderboard'
db = SQLAlchemy(app)

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="leaderboard"
# )




class Ldb(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(15))
    name = db.Column(db.String(25), nullable=False)
    #points = db.Column(db.Integer)


# Array 1: Questions
questions = [
    "In the movie \"The Shining,\" what was the name of the hotel where the story takes place?",
    "Who directed the horror movie \"Psycho\" in 1960?",
    "Which horror movie features a villain named Freddy Krueger?",
    "In the movie \"Scream,\" what is the name of the killer who wears a Ghostface mask?",
    "Which 1973 horror movie was based on a novel by William Peter Blatty?",
    "Who played the lead role in the 1976 horror movie \"Carrie\"?",
    "What is the name of the clown in Stephen King's \"It\"?",
    "In the movie \"Halloween,\" what is the name of the main character who is stalked by Michael Myers?",
    "Which horror movie features a family that moves into a haunted house in Amityville, New York?",
    "Who directed the 2005 horror movie \"The Descent\"?"
]

# Array 2: Options
options = [
    ["Overlook Hotel","Bates Motel","Stanley Hotel"],
    ["John Carpenter","Alfred Hitchcock","Wes Craven"],
    ["Halloween","A Nightmare on Elm Street","Friday the 13th"],
    ["The Exorcist","Rosemary's Baby","The Omen"],
    ["Billy Loomis","Stu Macher","Both A and B"],
    ["Jamie Lee Curtis","Sissy Spacek","Linda Blair"],
    ["Pennywise","Jester","Twisty"],
    ["Laurie Strode","Nancy Thompson","Sidney Prescott"],
    ["The Conjuring","Poltergeist","The Amityville Horror"],
    ["James Wan","Neil Marshall","Rob Zombie"]
]

N= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



@app.route("/q", methods=['GET','POST'])
def func():
    return render_template('mov.html', n=N ,l=len(questions), ques=questions, option=options)



@app.route("/a" ,methods = ['GET', 'POST'] )
def movm():
    nam = "Abhinav"
    if (request.method == 'POST'):
        '''Add entry to the database'''
        name = request.form.get('name')

        entry =Ldb(name=name)
        db.session.add(entry)
        db.session.commit()

    return render_template('mov.html' , name=nam)

@app.route("/index")
def ind():
    cd ="option"
    return render_template('index.html', cd=cd )

app.run(debug=True)