import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(
        orders,
        how='left',
        left_on='id',
        right_on='customerId',
        suffixes=('', '_ord')
    )
    merged = merged[merged['id_ord'].isna()][['name']]
    return merged.rename(columns={'name': 'Customers'})
