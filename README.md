
# End-to-End-Customer-Churn-Prediction

## Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project uses Machine Learning to predict whether a customer is likely to churn based on their service usage, contract type, support interactions, and billing information.

The project includes data preprocessing, model training, evaluation, business insights, and deployment through a Streamlit web application.

---

## Problem Statement

The objective of this project is to predict customer churn and identify the factors that contribute most to customer retention and customer loss.

By accurately identifying customers at risk of churning, businesses can take proactive measures to improve customer satisfaction and retention.

---

## Dataset Features

The model uses the following customer information:

* Tenure
* Monthly Charges
* Total Charges
* Support Calls
* Internet Service
* Online Security
* Tech Support
* Contract Type
* Payment Method

### Target Variable

* **Churn**

  * Yes = Customer leaves the company
  * No = Customer stays with the company

---

## Project Workflow

1. Data Cleaning and Preprocessing
2. Train-Test Split
3. Feature Scaling using StandardScaler
4. One-Hot Encoding for Categorical Features
5. Pipeline Creation using Scikit-Learn
6. Model Training using Logistic Regression
7. Model Evaluation
8. Model Interpretation
9. Streamlit App Development

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Jupyter Notebook

---

## Model Performance

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

These metrics help assess the model's ability to correctly identify customers who are likely to churn.

---

## Project Results

* Total Customers Analyzed: 20,000
* Customers Churned: 6,843
* Churn Rate: 34.22%
* Model Accuracy: 79.05%

The model successfully identified key patterns associated with customer churn, enabling businesses to proactively target at-risk customers and improve retention strategies.

---

## Business Questions Answered

### 1. How many customers are leaving?

Analysis revealed that **6,843 out of 20,000 customers churned**, resulting in a **churn rate of 34.22%**.

### 2. Why are customers leaving?

The primary drivers of churn were:

* Month-to-month contracts
* High monthly charges
* Unsolved issues
* Lack of technical support

### 3. What can the business do to reduce churn?

* Encourage long-term contracts
* Improve customer support quality
* Promote tech support and online security services
* Offer retention incentives to high-value customers

---

## Key Business Insights

The Logistic Regression model identified several important churn drivers:

### Factors Increasing Churn

* Month-to-Month Contract
* High Monthly Charges
* Unsolved issues
* No Tech Support Subscription

### Factors Reducing Churn

* Long Customer Tenure
* One-Year Contract
* Two-Year Contract
* Tech Support Subscription
* Online Security Service

### Business Recommendations

* Encourage customers to switch to long-term contracts.
* Improve customer support quality.
* Promote tech support and online security services.
* Offer retention incentives to customers with high monthly charges.

---

## Streamlit Application

The project includes an interactive Streamlit application where users can:

* Enter customer information
* Predict churn probability
* View churn predictions instantly

---

## Future Improvements

* Implement Random Forest and XGBoost models
* Perform Hyperparameter Tuning
* Add SHAP Explainability
* Deploy the application on Streamlit Cloud
* Compare multiple classification algorithms

---

## Author

**Husna Khanam**

Aspiring Data Scientist passionate about Machine Learning, Data Analysis, and building real-world AI solutions.
