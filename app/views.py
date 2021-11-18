from flask import Flask, render_template, request
from app import app

import requests, json

@app.route("/")
def home():
    title = "Home Page"
    jumbotron = {
        "title": "My Cool Title",
        "body": "Using a series of utilities, you can create this jumbotron, just like the one in previous versions of Bootstrap. Check out the examples below for how you can remix and restyle it to your liking."
    }
    return render_template('index.html', title=title, content=jumbotron)

@app.route("/about")
def about():
    title = "About Page"
    jumbotron = {
        "title": "About Us",
        "body": "You can add a quick description to this section that will highlight some key features"
    }
    return render_template('about.html', title=title, content=jumbotron) 

@app.route("/menu")
def menu():
    title = "Tasty Treats"
    jumbotron = {
        "title": "Yummmmmmyyy!!!",
        "body": "Check out our selection of rich coffees, exotic teas and delicious treats"
    }
    url = "https://opensheet.vercel.app/17B5XfOn0S4LSFWUFmRMZvpodoqf2lDoJAyO4ZFnNieg/sheet1"
    response = requests.request("GET", url)
    data = response.json()
    return render_template('about.html', title=title, coffees=data, content=jumbotron)

@app.route("/randos")
def randomusers():
    jumbotron = {
        "title": "Our Staff",
        "body": "It's not easy having a good time! Even smiling makes my face ache!"
    }
    url = "https://randomuser.me/api/?results=50"
    response = requests.request("GET", url)
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(response.json())
    data = response.json()
    return render_template('random.html', persons=data['results'], content=jumbotron)