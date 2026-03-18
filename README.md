# 🏠 Singapore Resale Flat Prices Prediction

## 📌 Project Overview

This project focuses on building a **machine learning model** to predict the resale prices of flats in Singapore and deploying it as a **user-friendly web application**. The application helps users estimate flat prices based on various features such as location, flat type, and lease details.

---

## 🎯 Problem Statement

The Singapore resale flat market is highly dynamic and influenced by multiple factors. Accurately estimating resale prices is challenging for buyers and sellers.

This project aims to:

* Build a predictive model using historical resale transaction data
* Provide accurate price estimates based on user inputs
* Deploy the model as an interactive web application

---

## 🚀 Skills Gained

* Data Wrangling
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Building & Evaluation
* Model Deployment (Streamlit)

---

## 🏢 Domain

Real Estate

---

## 📊 Data Source

Dataset collected from:
https://beta.data.gov.sg/collections/189/view

---

## ⚙️ Project Workflow

### 1. Data Collection & Preprocessing

* Collected resale flat transaction data (1990 – Present)
* Cleaned missing values and handled inconsistencies
* Structured dataset for modeling

### 2. Feature Engineering

Key features used:

* Town
* Flat Type
* Storey Range
* Floor Area
* Flat Model
* Lease Commence Date

Additional transformations:

* Date feature extraction (year, month)
* Encoding categorical variables
* Log transformation (if applied)

### 3. Model Building

* Trained regression models:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor
* Selected best-performing model based on evaluation metrics

### 4. Model Evaluation

Metrics used:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score
* Adjusted R² Score

### 5. Web Application (Streamlit)

* Built an interactive UI for user inputs
* Inputs include:

  * Town
  * Flat Type
  * Storey Range
  * Floor Area
  * Lease Year
* Displays predicted resale price

---

## ▶️ How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/your-username/singapore-flat-price-prediction.git
cd singapore-flat-price-prediction
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Streamlit App

```
streamlit run app.py
```

---

## 📈 Results

* Built a robust regression model for price prediction
* Achieved good accuracy based on evaluation metrics
* Delivered an interactive web application for real-time predictions

---

## 💡 Impact

* Helps buyers make informed decisions
* Assists sellers in estimating property value
* Demonstrates real-world ML application in real estate

---

## 🙌 Conclusion

This project showcases the integration of **machine learning, data analysis, and web deployment** to solve a real-world problem in the housing sector.

---

## ⭐ Acknowledgment

Thanks to Singapore HDB for providing open access to resale flat data.
