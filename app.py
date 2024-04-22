#!/usr/bin/env python3

import os
import sys
import subprocess
import datetime
from flask import Flask, render_template, request, redirect, url_for, make_response
from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

app = Flask(__name__)
app.config['DEBUG'] = os.getenv("FLASK_ENV", "development") == "development"

# Setup MongoDB connection from environment variables
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_dbname = os.getenv("MONGO_DBNAME", "mydatabase")

try:
    client = MongoClient(mongo_uri)
    db = client[mongo_dbname]
    print(" * Connected to MongoDB!")
except errors.ConnectionFailure as e:
    print(" * MongoDB connection error:", e)
    sys.exit(1)

@app.route('/')
def home():
    posts = db.posts.find().sort("created_at", -1)
    posts = list(posts)
    return render_template('base.html', posts=posts)

@app.route("/post/<post_id>")
def post(post_id):
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("post.html", post=post)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {
            "title": title,
            "content": content,
            "created_at": datetime.datetime.utcnow()
        }
        result = db.posts.insert_one(post)
        print("Inserted post with ID:", result.inserted_id)
        return redirect(url_for("home"))
    return render_template("create.html")


@app.route("/edit/<post_id>", methods=['GET', 'POST'])
def edit(post_id):
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db.posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$set": {"title": title, "content": content, "created_at": datetime.datetime.utcnow()}}
        )
        return redirect(url_for("post", post_id=post_id))
    return render_template("edit.html", post=post)

@app.route("/delete/<post_id>")
def delete(post_id):
    db.posts.delete_one({"_id": ObjectId(post_id)})
    return redirect(url_for("home"))

@app.errorhandler(Exception)
def handle_error(e):
    return render_template("error.html", error=e)

if __name__ == "__main__":
    app.run()
