import os
import json
from flask import (
    Flask, render_template, request, flash, session, url_for, redirect)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_paginate import Pagination, get_page_args
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


# All routes
@app.route("/")
@app.route("/home")
def home():
    # coins & users are for welcome screen for users that are not log in
    coins = list(mongo.db.coins.find())
    users = list(mongo.db.users.find())
    return render_template("home.html", coins_list=coins, user_list=users)


# Search route
@app.route("/search", methods=["GET", "POST"])
def search():
    # query & coins are for search
    query = request.form.get("query")
    coins = list(mongo.db.coins.find({"$text": {"$search": query}}))
    # coins_list & users are for welcome screen for users that are not log in
    coins_list = list(mongo.db.coins.find())
    users = list(mongo.db.users.find())
    # check for search results
    if len(coins) == 0:
        flash("No results, Please try again!")
        return redirect(url_for("home"))
    return render_template(
        "home.html", coins=coins, coins_list=coins_list, user_list=users)


"""
Register, Login, Profile, Logout functionality
"""


# Register route
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
        # add user into database
        mongo.db.users.insert_one(newuser)
        # put the new user into 'session' cookie
        session["user_email"] = request.form.get("email").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", user_email=session["user_email"]))
    return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for existing email
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user_email"] = request.form.get("email").lower()
                # return first name and surname
                flash("Welcome, {0} {1}".format(
                    existing_user["first_name"].capitalize(),
                    existing_user["last_name"].capitalize()))
                return redirect(url_for(
                    "profile", user_email=session["user_email"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


# Profile route
@app.route("/profile/<user_email>", methods=["GET", "POST"])
def profile(user_email):
    if 'user_email' in session:
        # grab all users list & the session user's email from database
        coins = list(mongo.db.coins.find())
        users = list(mongo.db.users.find())
        email = mongo.db.users.find_one(
            {"email": session["user_email"]})["email"]
        return render_template(
                "profile.html", user_email=email, users=users, coins=coins)
    return redirect(url_for("home"))


# Logout route
@app.route("/logout")
def logout():
    # remove user from session cookie and redirect to login
    if 'user_email' in session:
        flash("You have been logged out")
        session.pop("user_email")
        return redirect(url_for("home"))
    return render_template('errorpage.html')


"""
Email functionality
"""


# Email route
@app.route("/email")
def email():
    if 'user_email' in session:
        # grab all users list & the session user's email from database
        users = list(mongo.db.users.find())
        email = mongo.db.users.find_one(
            {"email": session["user_email"]})["email"]
        return render_template("email.html", users=users, user_email=email)
    return render_template("email.html")


"""
Catalog, New Coin, Edit Coin, Delete Coin functionality
"""


# Catalog route
@app.route("/catalog")
def catalog():
    coins = list(mongo.db.coins.find())
    # pagination for 10 items on the page

    def get_coins(offset=0, per_page=10):
        return coins[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # check for total length in a coins table
    total = len(coins)
    # return up to 10 items per page to catalog page
    pagination_coins = get_coins(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("catalog.html", coins=pagination_coins, page=page,
                           per_page=per_page, pagination=pagination,)


# New Coin route
@app.route("/new_coin", methods=["GET", "POST"])
def new_coin():
    if 'user_email' in session:
        # get data from html form
        if request.method == "POST":
            coin = {
                "name": request.form.get("name"),
                "type": request.form.get("type"),
                "weight": request.form.get("weight"),
                "weightunit": request.form.get("weightunit"),
                "mint": request.form.get("mint"),
                "country": request.form.get("country"),
                "purity": request.form.get("purity"),
                "year": request.form.get("year"),
                "description": request.form.get("description"),
                "image": request.form.get("image"),
                "timestamp": datetime.now(),
                "created_by": session["user_email"]
            }
            # insert new coin in to database
            mongo.db.coins.insert_one(coin)
            email = session['user_email']
            flash("New coin added into database")
            return redirect(url_for("profile", user_email=email))
        # read type data from database and sort ascending
        type = mongo.db.coin_type.find().sort("type", 1)
        # load country list from json file
        json_countries = open('static/json/countries.json')
        cl = json.load(json_countries)
        return render_template("new_coin.html", type=type, list=cl)
    return redirect(url_for("home"))


# Edit Coin route
@app.route("/edit_coin/<id>", methods=["GET", "POST"])
def edit_coin(id):
    if 'user_email' in session:
        # get data from html form
        if request.method == "POST":
            coin_edit = {
                "name": request.form.get("name"),
                "type": request.form.get("type"),
                "weight": request.form.get("weight"),
                "weightunit": request.form.get("weightunit"),
                "mint": request.form.get("mint"),
                "country": request.form.get("country"),
                "purity": request.form.get("purity"),
                "year": request.form.get("year"),
                "description": request.form.get("description"),
                "image": request.form.get("image"),
                "timestamp": datetime.now(),
                "created_by": session["user_email"]
            }
            # update coin in to database
            mongo.db.coins.update({"_id": ObjectId(id)}, coin_edit)
            email = session['user_email']
            flash("Coin details updated")
            return redirect(url_for("profile", user_email=email))
        coin = mongo.db.coins.find_one({"_id": ObjectId(id)})
        # read type data from database and sort ascending
        type = mongo.db.coin_type.find().sort("type", 1)
        # load country list from json file
        json_countries = open('static/json/countries.json')
        cl = json.load(json_countries)
        return render_template("edit_coin.html", coin=coin, type=type, list=cl)
    return redirect(url_for("home"))


# Delete Coin route
@app.route("/delete_coin/<id>")
def delete_coin(id):
    # if user is logged in remove user record from database
    if 'user_email' in session:
        mongo.db.coins.remove({"_id": ObjectId(id)})
        flash("Coin deleted")
        # if administrator redirect to catalog
        if session['user_email'] == "admin@coinscatalog.info":
            return redirect(url_for("catalog"))
        # if user redirect to users profile
        else:
            return redirect(url_for(
                "profile", user_email=session["user_email"]))


"""
Types, Add Type, Edit Type, Delete Type functionality
"""


# Types route
@app.route("/types")
def types():
    if 'user_email' in session:
        # check for admin email address
        if session['user_email'] == "admin@coinscatalog.info":
            # read type data from database and sort ascending
            types = list(mongo.db.coin_type.find().sort("type", 1))
            return render_template("types.html", types=types)
    return redirect(url_for("home"))


# Add Type route
@app.route("/new_type", methods=["GET", "POST"])
def new_type():
    if 'user_email' in session:
        # check for admin email address
        if session['user_email'] == "admin@coinscatalog.info":
            if request.method == "POST":
                type = {
                    "type": request.form.get("type")
                }
                # insert new type into database
                mongo.db.coin_type.insert_one(type)
                flash("New type added")
                return redirect(url_for("types"))
            return render_template("new_type.html")
    return redirect(url_for("home"))


# Edit Type route
@app.route("/edit_type/<id>", methods=["GET", "POST"])
def edit_type(id):
    if 'user_email' in session:
        # check for admin email address
        if session['user_email'] == "admin@coinscatalog.info":
            if request.method == "POST":
                type_edit = {
                    "type": request.form.get("type")
                    }
                # update type into database
                mongo.db.coin_type.update({"_id": ObjectId(id)}, type_edit)
                flash("Type details updated")
                return redirect(url_for("types"))
            # read type data from database
            type = mongo.db.coin_type.find_one({"_id": ObjectId(id)})
            return render_template("edit_type.html", type=type)
    return redirect(url_for("home"))


# Delete Type route
@app.route("/delete_type/<id>")
def delete_type(id):
    mongo.db.coin_type.remove({"_id": ObjectId(id)})
    flash("Coin type deleted")
    return redirect(url_for("types"))


# Redirect 404 error to home page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errorpage.html'), 404


# Redirect 500 error to home page
@app.errorhandler(500)
def internal_error(e):
    return render_template('errorpage.html'), 500


# Environment variables
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
