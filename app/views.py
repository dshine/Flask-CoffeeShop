from flask import Flask, render_template

from app import app

@app.route("/")
def home():
    title = "Home Page"
    return render_template('index.html', title=title)

@app.route("/about")
def about():
    title = "About Page"
    return render_template('about.html', title=title) 

@app.route("/menu")
def menu():
    title = "Tasty Treats"
    return render_template('about.html', title=title)