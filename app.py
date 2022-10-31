from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app) 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))
    tag = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.String(500), nullable=False)

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/<name>")
def blog(name): 
    return render_template ("index.html", name=name)
