import numpy as np
import pandas as pd
import pickle
import csv
import sql_data
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    #home page for info and navigation
    return render_template("index.html")

@app.route("/viz")
def viz():
    #home page for info and navigation
    return render_template("viz.html")

@app.route("/data")
def data():
    #SQL lite connection
    data = sql_data.query()
    return jsonify(data)

@app.route("/model/", methods=["POST", "GET"])
def model():
    #retrieve user inputs
    if request.method == "POST":
        input_age = request.form["age"]
        input_race = request.form["ethnicity"]
        input_income = request.form["income"]
        input_gender = request.form["gender"]
        input_stage = request.form["stage"]
        input_site = request.form["site"]
        input_type = request.form["type"]
    
    #load resources 
    features = []
    prediction_data = []
    with open('resources/Blank_Form.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    for row in data:
        features.append(row[0])
        prediction_data.append(int(row[1]))
        
    prediction_model = pickle.load(open("resources/model.pkl","rb"))

    #model the prediction
    prediction_data[features.index('Age')] = int(input_age)
    prediction_data[features.index(f'Race_{input_race}')] =1
    prediction_data[features.index(f'Median_Household_Income_{input_income}')] =1
    prediction_data[features.index(f'Gender_{input_gender}')]=1
    prediction_data[features.index(f'Cancer_Stage_{input_stage}')]=1
    prediction_data[features.index(f'Cancer_Site_{input_site}')]=1
    prediction_data[features.index(f'Cancer_Type_ {input_type}')]=1

    pred = prediction_model.predict(np.reshape(np.array(prediction_data),(1,198)))

    #return the prediction
    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run()
