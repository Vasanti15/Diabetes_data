from flask import Flask, render_template,jsonify, render_template_string, request
import config
from dataset.utils import diabetes

app = Flask(__name__)

@app.route('/')  

def hello_flask():

    print("Welcome to Data science")
    return 'vasanti'


@app.route('/diabetes_status')

def diabetes_status():
    Glucose = 148
    BloodPressure = 50
    SkinThickness =35
    Insulin = 0
    BMI =33.6
    DiabetesPedigreeFunction =0.627
    Age= 50


    diabetes_status_prediction = diabetes( Glucose,BloodPressure,SkinThickness, Insulin, BMI,
       DiabetesPedigreeFunction, Age)
   
    diabetes_status_prediction.get_diabetes_pred()


    return jsonify({"Result": f"diabetes status is:{diabetes_status_prediction}"})

if __name__ == "__main__":
 app.run()