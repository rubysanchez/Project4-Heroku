
import pandas as pd
import pickle
from sqlalchemy import create_engine
from flask import Flask, render_template, request, redirect, jsonify, make_response

app = Flask(__name__)

prediction_model = pickle.load(open("resources/model.pkl","rb"))

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
    #SQL lite
    database_path ="resources/survivalprediction.sqllite"
    engine = create_engine(f"sqlite:///{database_path}")
    data = engine.execute("Select * from prediction")
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

    #model the prediction
    prediction_data = pd.DataFrame()
    prediction_data['Age'] = int(factors[0])
    prediction_data[f'Race_{factors[1]}']=1
    prediction_data[f'Median_Household_Income_{factors[2]}']=1
    prediction_data[f'Gender_{factors[3]}']=1
    prediction_data[f'Cancer_Stage_{factors[4]}']=1
    prediction_data[f'Cancer_Site_{factors[5]}']=1
    prediction_data[f'Cancer_Type_{factors[6]}']=1
    
    #make the prediction
    pred = prediction_model.predict(prediction_data)

    #return the prediction
    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run()
