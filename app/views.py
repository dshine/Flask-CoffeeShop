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
    slides = [
        {
            "src":"https://www.w3schools.com/bootstrap5/chicago.jpg",
            "city": "Chicago"
        },
        {
            "src":"https://www.w3schools.com/bootstrap5/la.jpg",
            "city": "LA" 
        },
        {
            "src":"https://www.w3schools.com/bootstrap5/ny.jpg",
            "city":"New York"
        }
    ]
    url = "https://randomuser.me/api/?results=4"
    response = requests.request("GET", url)
    data = response.json()
    return render_template('index.html', title=title, content=jumbotron, persons=data['results'], slides=slides)

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
    slides = [
        {
            "src":"https://images.unsplash.com/photo-1453614512568-c4024d13c247?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1032&q=80 ",
            "city": "Chicago"
        },
        {
            "src":"https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80 ",
            "city": "LA" 
        },
        {
            "src":"https://images.unsplash.com/photo-1513267048331-5611cad62e41?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80 ",
            "city":"New York"
        }
    ]
    url = "https://opensheet.vercel.app/17B5XfOn0S4LSFWUFmRMZvpodoqf2lDoJAyO4ZFnNieg/sheet1"
    response = requests.request("GET", url)
    data = response.json()
    return render_template('about.html', title=title, coffees=data, content=jumbotron,slides=slides)


@app.route("/randos")
@app.route("/randos/count/<count>")
@app.route("/randos/gender/<gender>")
@app.route("/randos/gender/<gender>/<count>")
def randomusers(count=50,gender="female"):
    count = count
    gender = gender
    jumbotron = {
        "title": "Our Staff",
        "body": "It's not easy having a good time! Even smiling makes my face ache!"
    }
    url = f"https://randomuser.me/api/?results={count}&gender={gender}"
    response = requests.request("GET", url)
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(response.json())
    data = response.json()
    return render_template('random.html', persons=data['results'], content=jumbotron)