"""
rfm_pipeline.py

Performs RFM analysis and customer segmentation using KMeans clustering.

Author: Alireza
"""

def calculate_rfm(df):
    reference_date = df['order_date'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('customer_id').agg({
        'order_date': lambda x: (reference_date - x.max()).days,
        'order_id': 'nunique',
        'profit': 'sum'
    }).reset_index()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary_Profit']
    return rfm