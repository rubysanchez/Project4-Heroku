
import pandas as pd
from flask import Flask, render_template, request, redirect, jsonify, make_response

def prediction(data):
    return data

app = Flask(__name__)

@app.route("/")
def index():
    #home page for info and navigation
    return render_template("index.html")

@app.route("/data")
def index():
    #SQL lite
    return ("#jsonified response")

@app.route("/model/", method=["POST", "GET"])
def index():
    #make the prediction
    if request.method == "POST":
        input = request.form
    pred = prediction(input)
    return render_template("index.html", pred = pred)

if __name__ == '__main__':
    app.run()
