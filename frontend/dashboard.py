import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Vantara - Customer Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("Vantara")
st.markdown("### Customer Behavior Prediction")
st.caption(
    "Customer intelligence dashboard for analyzing spending, "
    "purchasing behaviour, and churn risk."
)

st.divider()

# Load processed customer data
customer_df = pd.read_csv(
    "data/processed/customer_churn_features.csv"
)

st.subheader("Customer Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", len(customer_df))

with col2:
    st.metric("Total Spend", f"£{customer_df['TotalSpend'].sum():,.2f}")

with col3:
    st.metric("Average Order Value", f"£{customer_df['AverageOrderValue'].mean():,.2f}")

with col4:
    churn_rate = customer_df["Churn"].mean() * 100
    st.metric("Churn Rate", f"{churn_rate:.1f}%")

st.subheader("Customer Data")

st.dataframe(
    customer_df,
    use_container_width=True
)
st.subheader("Customer Spending Analysis")

st.bar_chart(
    customer_df.set_index("Customer ID")["TotalSpend"].head(20)
)

st.subheader("Spend vs Orders")

st.scatter_chart(
    customer_df,
    x="TotalOrders",
    y="TotalSpend"
)

st.subheader("Model Performance Comparison")

model_df = pd.read_csv(
    "data/processed/model_comparison.csv"
)

# Model performance chart
performance_chart = model_df.set_index("Model")[
    ["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]
]

st.bar_chart(performance_chart)

# Detailed performance table
st.dataframe(
    model_df,
    width="stretch"
)