from flask import Flask, render_template, request
from app import app

import requests, json

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
    url = "https://opensheet.vercel.app/17B5XfOn0S4LSFWUFmRMZvpodoqf2lDoJAyO4ZFnNieg/sheet1"
    response = requests.request("GET", url)
    data = response.json()
    return render_template('about.html', title=title, coffees=data)

@app.route("/randos")
def randomusers():
    url = "https://randomuser.me/api/?results=50"
    response = requests.request("GET", url)
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    # print(response.json())
    data = response.json()
    return render_template('random.html', persons=data['results'])