from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Movies-app!'

@app.route("/movies.json")
def index():
    return db.movies_all()

@app.route("/movies.json", methods=["POST"])
def create():
    title = request.form.get("title")
    director = request.form.get("director")
    genre = request.form.get("genre")
    runtime = request.form.get("runtime")
    rating = request.form.get("rating")
    return db.movies_create(title, director, genre, runtime, rating)
