
import pandas as pd
from src.data_collection.data_collection import create_connection, load_sales_data, load_stock_levels, load_temperature_data



def preprocess_data(df_sales, df_stock_levels, df_temperature):
    """
    Preprocess the data by converting the timestamp to datetime and modifying it to hourly basis.
    Aggregate the data on timestamp_hourly and product_id, merge the data, and replace null values with 0.
    Add more time features to the table and drop unnecessary columns.

    Parameters:
    df_sales (pd.DataFrame): The sales data.
    df_stock_levels (pd.DataFrame): The stock levels data.
    df_temperature (pd.DataFrame): The temperature data.

    Returns:
    pd.DataFrame: The preprocessed data.
    """
    
    dataframes = [df_sales, df_stock_levels, df_temperature]
    for i in dataframes:
        i['timestamp'] = pd.to_datetime(i['timestamp'])

    # Modify timestamp column to hourly basis
    df_sales['timestamp_hourly'] = df_sales['timestamp'].dt.to_period(freq = 'h')
    df_stock_levels['timestamp_hourly'] = df_stock_levels['timestamp'].dt.to_period(freq = 'h')
    df_temperature['timestamp_hourly'] = df_temperature['timestamp'].dt.to_period(freq = 'h')

    # Aggregate data on timestamp_hourly and product_id
    df_sales_agg = df_sales.groupby(['timestamp_hourly', 'product_id']).agg({'quantity': 'sum'}).reset_index()
    df_stock_levels_agg = df_stock_levels.groupby(['timestamp_hourly', 'product_id']).agg({'estimated_stock_pct': 'mean'}).reset_index()
    df_temperature_agg = df_temperature.groupby('timestamp_hourly').agg({'temperature': 'mean'}).reset_index()

    # Merge data
    merged_df = df_stock_levels_agg.merge(df_sales_agg, on=['timestamp_hourly', 'product_id'], how='left')
    merged_df = merged_df.merge(df_temperature_agg, on=['timestamp_hourly'], how='left')

    # Replace null values with 0
    merged_df['quantity'] = merged_df['quantity'].fillna(0)

    # Add more features to the table
    product_categories = df_sales[['product_id', 'category']].drop_duplicates()
    product_price = df_sales[['product_id', 'unit_price']].drop_duplicates()

    # Merge these features on merged_df
    merged_df = merged_df.merge(product_categories, on='product_id', how='left')
    merged_df = merged_df.merge(product_price, on='product_id', how='left')

    # Drop product_id
    merged_df.drop('product_id', axis=1, inplace=True)

    # Add day_of_month and hour features
    merged_df['day_of_month'] = merged_df['timestamp_hourly'].dt.day
    merged_df['hour'] = merged_df['timestamp_hourly'].dt.hour

    # Drop timestamp_hourly
    merged_df.drop('timestamp_hourly', axis=1, inplace=True)

    return merged_df

# if __name__ == "__main__":
#     connection_engine = create_connection()
#     df_sales = load_sales_data(connection_engine)
#     df_stock_levels = load_stock_levels(connection_engine)
#     df_temperature = load_temperature_data(connection_engine)
#     print(preprocess_data(df_sales, df_stock_levels, df_temperature))