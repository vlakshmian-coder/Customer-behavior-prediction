# Vantara – Customer Behaviour Prediction

## Project Overview
Vantara is a customer intelligence and behaviour prediction project developed using the Online Retail II dataset. The project analyses customer purchasing behaviour, creates customer-level behavioural features, predicts churn risk using machine-learning models, compares model performance, and provides explainable AI visualisations using SHAP. The final results are presented through an interactive Streamlit dashboard.

## Objectives
- Clean and prepare retail transaction data.
- Create customer-level behavioural features.
- Identify customers at risk of churn.
- Train and compare machine-learning classification models.
- Evaluate model performance using standard classification metrics.
- Explain model predictions using SHAP.
- Present customer insights through an interactive dashboard.
- Deploy the dashboard using Streamlit Community Cloud.

## Key Features

### Customer Behaviour Analysis
Customer-level features include:
- Total Spend
- Total Orders
- Total Products
- Average Order Value
- Customer Tenure
- Tenure in Months
- Purchase Frequency per Month
- Average Spend per Product
- Average Quantity per Order
- Recency

### Churn Prediction
Customer churn was defined using customer recency, with customers having a recency greater than 90 days classified as churn-risk customers.

### Machine-Learning Models
The project compares:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Gradient Boosting
- K-Nearest Neighbours (KNN)
- Support Vector Machine (SVM)

Evaluation metrics include Accuracy, Precision, Recall, F1 Score, ROC-AUC and Confusion Matrix.

### Explainable AI
SHAP (SHapley Additive exPlanations) was used to make the churn model more interpretable. The dashboard includes SHAP feature-importance and summary/beeswarm visualisations.

## Streamlit Dashboard
The dashboard provides:
- Customer overview metrics
- Customer spending and purchasing analysis
- Model performance comparison
- Churn-related insights
- SHAP explainability visualisations

## Deployment
The final Streamlit application was deployed using Streamlit Community Cloud.

Live application:
https://customer-behavior-prediction-zwneyhdekzmzztkmwqbzm6.streamlit.app/

## Project Structure
```text
Vantara - Customer Behaviour Prediction/
├── frontend/
│   └── dashboard.py
├── data/
│   └── processed/
│       ├── customer_churn_features.csv
│       └── model_comparison.csv
├── models_artifacts/
│   └── churn_model.pkl
├── requirements.txt
├── README.md
└── PROJECT_DOCUMENTATION.docx
```

## Dataset
The project uses the Online Retail II dataset containing transaction information such as Invoice, Stock Code, Description, Quantity, Invoice Date, Price, Customer ID and Country.

The original large dataset is excluded from the final submission package because of its size.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- GitHub
- Streamlit Community Cloud

## Testing
The dashboard was tested locally and then deployed successfully. The deployed version was verified to display the latest dashboard, charts, model comparison and SHAP explainability visualisations.

## Project Status
**100% Completed for the implemented project scope.**

The core customer behaviour analysis, churn prediction, model comparison, explainability and interactive Streamlit dashboard have been completed and deployed.

## Future Enhancements
Possible future improvements include adding more dashboard tabs, additional customer segmentation visualisations, improved colour consistency, advanced interactive filtering and more detailed customer-level prediction explanations.

## Author
**Vijayalakshmi Narayanan**

Customer Behaviour Prediction – AI/ML Internship Project
