import pickle
import re
import json
import numpy as np
import config

class diabetes():
    def __init__ (self, Glucose,BloodPressure,SkinThickness, Insulin, BMI,
       DiabetesPedigreeFunction, Age):

        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
        
    def load_model (self):
        with open (config.PICKLE_FILE_PATH,"rb") as f:
            self.pkl = pickle.load(f)

        with open (config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    
    def get_diabetes_pred(self):
        self.load_model()

        test_array = np.zeros(len( self.json_data["columns"]))

        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age
          

        diabetes_status = self.pkl.predict([test_array])
        return diabetes_status


if __name__ == "__main__":

    Glucose = 148
    BloodPressure = 50
    SkinThickness =35
    Insulin = 0
    BMI =33.6
    DiabetesPedigreeFunction =0.627
    Age= 50

    diabetes_status_pred = diabetes(Glucose,BloodPressure,SkinThickness, Insulin, BMI,
       DiabetesPedigreeFunction, Age)
    diabetes_status_pred.get_diabetes_pred()