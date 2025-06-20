from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), '../model/churn_model.pkl')
model = joblib.load(model_path)

expected_columns = [ 
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 
    'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 
    'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Monthly_to_TotalRatio',
    'MultipleLines_binary', 'IsPaperlessBilling', 'PaymentMethodEncoded'
]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    
    df = pd.DataFrame([data])[expected_columns]

    
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return jsonify({
        "prediction": int(prediction),
        "probability": float(proba) 
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
