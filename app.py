from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Movies-app!'

@app.route("/movies.json")
def index():
    return db.movies_all()