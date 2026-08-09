import streamlit as st
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"

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

# Display the polished model comparison charts already generated
# and saved in the reports folder.

col1, col2 = st.columns(2)

with col1:
    st.image(
        "reports/model_performance_comparison_all_metrics.png",
        caption="Model Performance Comparison — All Metrics",
        use_container_width=True
    )

with col2:
    st.image(
        "reports/model_comparison_roc_auc.png",
        caption="Model Comparison — ROC-AUC",
        use_container_width=True
    )

# Detailed performance table
st.dataframe(
    model_df,
    width="stretch"
)

st.divider()

# ==========================================================
# SHAP MODEL EXPLAINABILITY
# ==========================================================

st.subheader("🔍 Model Explainability — SHAP")

st.markdown(
    "SHAP (SHapley Additive exPlanations) helps explain "
    "which features contribute to the model's churn predictions."
)

col1, col2 = st.columns(2)

with col1:
    st.image(
        REPORTS_DIR / "shap_feature_importance_bar.png",
        caption="SHAP Feature Importance",
        use_container_width=True
    )

with col2:
    st.image(
        REPORTS_DIR / "shap_feature_importance.png",
        caption="SHAP Feature Importance — Detailed",
        use_container_width=True
    )

st.image(
     REPORTS_DIR / "shap_summary_beeswarm.png",
     caption="SHAP Beeswarm Summary",
     use_container_width=True
    )