import numpy as np
import pandas as pd
import pickle
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
    
    factors = [input_age,input_race, input_income, input_gender, input_stage, input_site, input_type]

    #load resources 
    prediction_data = pd.read_csv('resources/Blank_Form.csv')
    prediction_model = pickle.load(open("resources/model.pkl","rb"))

    #model the prediction
    prediction_data['Age'] = int(factors[0])
    prediction_data[f'Race_{factors[1]}']=1
    prediction_data[f'Median_Household_Income_{factors[2]}']=1
    prediction_data[f'Gender_{factors[3]}']=1
    prediction_data[f'Cancer_Stage_{factors[4]}']=1
    prediction_data[f'Cancer_Site_{factors[5]}']=1
    prediction_data[f'Cancer_Type_{factors[6]}']=1
    model.predict(np.reshape(np.array(prediction_data.values.tolist()),(1,198)))
    
    #make the prediction
    pred = prediction_model.predict(prediction_data)

    #return the prediction
    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run()
