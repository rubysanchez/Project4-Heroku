
import pandas as pd
import pickle 
from flask import Flask, render_template, request, redirect, jsonify, make_response

app = Flask(__name__)

prediction_model = pickle.load(open("resources/file.pkl","rb"))

@app.route("/")
def index():
    #home page for info and navigation
    return render_template("index.html")

@app.route("/data")
def data():
    #SQL lite
    return jsonify(data())

@app.route("/model/", method=["POST", "GET"])
def model():
    #model the prediction
    if request.method == "POST":
        input = request.form
    pred = prediction_model.predict(input)
    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run()
