from flask import Flask, request
from flask_cors import CORS
import db


app = Flask(__name__)
CORS(app)

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
@app.route("/movies/<id>.json")
def show(id):
    return db.movies_find_by_id(id)

@app.route("/movies/<id>.json", methods=["PATCH"])
def update(id):
    title = request.form.get("title")
    director = request.form.get("director")
    genre = request.form.get("genre")
    runtime = request.form.get("runtime")
    rating = request.form.get("rating")
    return db.movies_update_by_id (id, title, director, genre, runtime, rating)

@app.route("/movies/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.movies_destroy_by_id(id)

@app.route("/users.json")
def index_user():
    return db.users_all()

@app.route("/users.json", methods=["POST"])
def create_user():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    return db.users_create(name, email, password)

@app.route("/users/<id>.json")
def show_user(id):
    return db.users_find_by_id(id)

@app.route("/users/<id>.json", methods=["PATCH"])
def update_user(id):
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    return db.users_update_by_id(id, name, email, password)

@app.route("/users/<id>.json", methods=["DELETE"])
def destroy_user(id):
    return db.users_destroy_by_id(id)


