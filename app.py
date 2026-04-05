from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Air Quality Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    pm25 = data['pm25']
    pm10 = data['pm10']
    no2 = data['no2']
    co1=data['co1']
    prediction = model.predict([[pm25, pm10, no2,co1]])[0]

    # Control suggestion logic
    if prediction > 200:
        suggestion = "Hazardous! Avoid outdoor activity."
    elif prediction > 100:
        suggestion = "Moderate. Wear mask."
    else:
        suggestion = "Air quality is good."

    return jsonify({
        "AQI": round(prediction, 2),
        "suggestion": suggestion
    })

if __name__ == "__main__":
    app.run(debug=True)


from flask_cors import CORS
CORS(app)