import pandas as pd

def load_catalog(csv_path: str):
    df = pd.read_csv(csv_path)

    # Clean up column names just in case there are trailing whitespaces
    df.columns = df.columns.str.strip()

    # Create a set of product names for O(1) lookup
    product_name_set = set(df["Product_Name"].str.lower().str.strip())  # lowercased for fuzzy matching

    # Map product names to product info
    product_info = {
        row["Product_Name"].strip().lower(): {
            "sku": row["Product_Code"],
            "price": row["Price"],
            "moq": row["Min_Order_Quantity"],
            "stock": row["Available_in_Stock"],
            "description": row["Description"]
        }
        for _, row in df.iterrows()
    }

    return product_name_set, product_info
