from sqlalchemy import create_engine, inspect
import json

def query():
    data_dict = {}
    database_path ="resources/survivalprediction.sqllite"
    engine = create_engine(f"sqlite:///{database_path}")
    gender = engine.execute("Select distinct gender from prediction").fetchall()
    income = engine.execute("Select distinct Median_Household_Income from prediction").fetchall()
    type = engine.execute("Select distinct Cancer_Type from prediction").fetchall()
    stage = engine.execute("Select distinct Cancer_Stage from prediction").fetchall()
    site = engine.execute("Select distinct Cancer_Site from prediction").fetchall()
    race = engine.execute("Select distinct race from prediction").fetchall()
    data_dict = {"site":site, "type":type, "stage":stage, "gender":gender, "income":income, "race":race}
    return data_dict