from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instans
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////blog.db'
db = SQLAlchemy(app) 

class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(12), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.String)

@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/<name>")
def coin(name): 
    return render_template ("index.html", name=name)
