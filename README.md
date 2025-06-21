# 📞 Telecom Customer Churn Prediction

This project predicts whether a telecom customer will churn (leave) or not using machine learning.  
It covers preprocessing, training, API deployment with Flask, and a Streamlit interface — all containerized using Docker.

---

## Features

-  Data cleaning & feature engineering  
-  Random Forest classifier with hyperparameter tuning  
-  Flask REST API for prediction  
-  Interactive UI with Streamlit  
-  Docker & Docker Compose for easy deployment

---

##  Dataset

Used dataset: [Telco Customer Churn – Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn)

Includes:
- Customer demographics  
- Subscribed services  
- Account details  
- Churn label

---

## 🛠️ Technologies

- Python 3.10  
- scikit-learn  
- pandas, numpy  
- Flask  
- Streamlit  
- Docker, Docker Compose  

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/churn-prediction-project.git
cd churn-prediction-project
```

### 2. Make sure Docker Desktop is installed and running

```bash
docker-compose up --build
```

* Flask API: [http://localhost:5000](http://localhost:5000)
* Streamlit app: [http://localhost:8501](http://localhost:8501)

---

### 3. Test the API

You can test predictions via Postman or `curl`.

**POST** to `http://localhost:5000/predict` with a sample JSON body like:

```json
{
  "gender": 1,
  "SeniorCitizen": 0,
  "Partner": 1,
  "Dependents": 0,
  "tenure": 12,
  "PhoneService": 1,
  "MultipleLines": 1,
  "InternetService": 0,
  "OnlineSecurity": 1,
  "OnlineBackup": 0,
  "DeviceProtection": 0,
  "TechSupport": 0,
  "StreamingTV": 0,
  "StreamingMovies": 0,
  "Contract": 0,
  "PaperlessBilling": 1,
  "PaymentMethod": 2,
  "MonthlyCharges": 70.0,
  "TotalCharges": 1000.0,
  "Monthly_to_TotalRatio": 0.07,
  "MultipleLines_binary": 1,
  "IsPaperlessBilling": 1,
  "PaymentMethodEncoded": 2
}
```

---

## 📌 Notes

* The model was trained using **scikit-learn 1.6.1**; if you're using a newer version (e.g. 1.7.0), warnings may appear.
* For production, replace Flask’s development server with a WSGI server like **Gunicorn**.
* The Streamlit UI is simple — feel free to improve the design and user experience.
