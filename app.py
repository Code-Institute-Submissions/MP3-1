import os
from flask import (
    Flask, render_template, request, flash, session, url_for, redirect)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


# initialize application
app = Flask(__name__)


# Connect with mongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# initialize mongo as a global variable
mongo = PyMongo(app)


# All routes (home as temporary)
@app.route("/")
@app.route("/home")
def home():
    users = list(mongo.db.users.find())
    return render_template("profile.html", users=users)


# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check for existing email
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Email already exists")
            return redirect(url_for("register"))
        # create new user
        newuser = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "timestamp": datetime.now(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # add user into db
        mongo.db.users.insert_one(newuser)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful!")
    return render_template("register.html")


# Environment variables
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")))
