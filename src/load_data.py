from pathlib import Path
import pandas as pd

def load_data():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "processed" / "online_retail_cleaned.csv"

    df = pd.read_csv(file_path)

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    return df